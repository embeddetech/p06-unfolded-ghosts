"""Arc-C: devices D4 (dimer at its EP) and D5 (unidirectional cascade)
for the photonic proposal -- design + measurement-chain Monte Carlo.

PHYSICS CORRECTION to the threads-scout concept: a reciprocal coupler
at its EP is the DIMER-EP (Jordan vector (1,-i)/sqrt2, |U|^2 full in
the guide basis) -- it fails divisibility by NEGATIVITY (t_c ->
1/(kappa sqrt2), the EP limit of the existing t_c formula). The
triangular PU cell in the GUIDE basis needs UNIDIRECTIONAL coupling:
coherent coupling J with synthetic phase pi/2 plus dissipative
coupling Gamma_d through a lossy bus gives H_12 = i(J - Gamma_d),
H_21 = -i(J + Gamma_d): fully one-way at J = Gamma_d (Hatano-Nelson
asymmetry). That device (D5) realizes conditional-mass-creation
indivisibility: divisor M1-free, column-sum crossing 1 at
z_c = 0.486/(2J) in the zero-step limit (generator crossing
0.4859; finite-step values are protocol-dependent).

Estimator theory points (verified in [1]):
 - det of a triangular divisor = product of positive diagonal ratios:
   the T2 det-based estimator is BLIND to the cascade onset; the
   column-sum observable is REQUIRED for D5.
 - detuning the D5 resonators by delta keeps H triangular and turns
   on the 2x2 theorem: first divisor negativity at z* = pi/delta --
   direction spectroscopy (delta >= ~0.5 /cm to fit a 10 cm chip).
 - [1c] sigma_max(z) is INTENSITY-ACCESSIBLE for the triangular
   device: for lower-triangular U the Gram matrix U^dag U has
   diagonal = the measured column intensity sums and off-diagonal
   modulus sqrt(Ghat_21 Ghat_22), so sigma_max^2 = its largest
   eigenvalue -- a function of the measured Ghat entries alone (no
   phase-resolved characterization needed). Under asymmetry
   imperfection eta the reconstruction error is Weyl-bounded by the
   measured residual entry: |Delta sigma_max^2| <= sqrt(Ghat_11
   Ghat_12), with Ghat_12 at the dark floor for a certified device.

MC ([2],[3]): T2 error model -- 2% fabrication disorder (J, Gamma_d,
kappa, gamma), 3% per-launch calibration, Poisson shot noise at 1e4
photons/launch, 1e-4 dark floor, imperfect asymmetry eta = J-Gamma_d
at 3% of J, 400 realizations.

ESTIMATOR NOTE (audit-driven correction): the original LSQ model fit
did NOT resolve J, Gamma_d, eta on the balanced device -- its
outputs stayed pinned at initialization (corr(param_hat, param)
~ 0.05), so its quoted spreads were echoes of the injected priors.
The balanced-device estimators are now CLOSED-FORM and calibration-
free: Gamma_d from the log-slope of the dark-subtracted Ghat_11
ladder (per-launch calibration enters only the intercept), and
J + Gamma_d from mean sqrt(Ghat_21/Ghat_11)/z (the calibration
cancels exactly in the ratio). The MC prints recovery correlations
as controls. eta at the 3% design level is NOT resolvable from this
intensity data (its Ghat_12 signal peaks at the dark floor at 1e4
photons; the non-recovery control is printed): eta is CERTIFIED,
not fitted, and the certification is two-channel because
negativity reads only eta > 0 (real split): window cleanliness
bounds eta/J on its positive side below the ~13% boundary ([1b]),
the z* re-entry length measures positive eta above a few % of J, and
the eta < 0 (imaginary-split) side is negativity-silent at any
magnitude -- it is bounded instead by the sign-blind [1c] Weyl
residual sqrt(Ghat_11 Ghat_12) from the same data. The LSQ fit is retained only for the detuned
(spectroscopy) device, where the detuning delta is genuinely recovered.

ASCII only; numpy/scipy.
"""

import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

rng = np.random.default_rng(12)

ZS = np.arange(0.5, 10.01, 0.5)          # chip-length ladder [cm]
NPH = 1e4                                # photons per launch
DARK = 1e-4
DZ = 0.25                                # divisor step [cm]


def H_d5(J, Gd, eta, Delta):
    """Unidirectional pair: synthetic phase pi/2 + dissipative bus."""
    return np.array([[-Delta / 2 - 1j * Gd, 1j * eta],
                     [-1j * (J + Gd), Delta / 2 - 1j * Gd]])


def gam_phys(H, z):
    return np.abs(expm(-1j * H * z)) ** 2


def norm_divisor(H, z1, z2):
    """sigma_max-normalized divisor (theory convention)."""
    U1, U2 = expm(-1j * H * z1), expm(-1j * H * z2)
    G1 = np.abs(U1 / np.linalg.svd(U1, compute_uv=False)[0]) ** 2
    G2 = np.abs(U2 / np.linalg.svd(U2, compute_uv=False)[0]) ** 2
    return G2 @ np.linalg.inv(G1)


def zc_colsum(H, zmax=12.0):
    for z in np.arange(0.05, zmax, 0.01):
        if norm_divisor(H, z, z + DZ).real.sum(axis=0).max() > 1 + 1e-9:
            return z
    return np.nan


def zstar_neg(H, zmax=12.0):
    for z in np.arange(0.05, zmax, 0.01):
        if norm_divisor(H, z, z + DZ).real.min() < -1e-9:
            return z
    return np.nan


def min_entry(H, zmax=6.0):
    """Min divisor entry over the measurement window, skipping
    ill-conditioned base points (cond > 1e8) whose inverses amplify
    roundoff into fake negativity."""
    out = 0.0
    for z in np.arange(0.1, zmax, 0.1):
        U1 = expm(-1j * H * z)
        G1 = np.abs(U1 / np.linalg.svd(U1, compute_uv=False)[0]) ** 2
        if np.linalg.cond(G1) > 1e8:
            continue
        out = min(out, norm_divisor(H, z, z + DZ).real.min())
    return out


def measure(H, cal, nph=NPH):
    """Noisy intensity ladder: per-launch calibration + shot + dark."""
    out = []
    for z in ZS:
        G = gam_phys(H, z)
        Ghat = np.empty((2, 2))
        for j in range(2):
            lam = nph * (cal[j] * G[:, j] + DARK)
            Ghat[:, j] = rng.poisson(lam) / nph
        out.append(Ghat)
    return np.array(out)


def fit_model(data, x0):
    """LSQ fit of (J, Gd, eta, Delta, cal1, cal2) to the ladder."""
    def resid(p):
        J, Gd, eta, Delta, c1, c2 = p
        H = H_d5(J, Gd, eta, Delta)
        r = []
        for z, Ghat in zip(ZS, data):
            G = gam_phys(H, z)
            G = G * np.array([c1, c2])[None, :]
            r.extend((Ghat - G).ravel())
        return r
    return least_squares(resid, x0, method="lm").x


def main():
    print("=" * 72)
    print("Arc-C: D4 (dimer at EP) + D5 (unidirectional cascade) "
          "design & MC")
    print("=" * 72)

    J0, Gd0 = 0.25, 0.25                 # D5 nominal [1/cm]; 2J = 0.5
    kap4 = 0.30                          # D4: gamma = 2 kappa = 0.60

    # ---- [1] design facts ---------------------------------------------
    print("\n[1] design facts (noiseless model):")
    H5 = H_d5(J0, Gd0, 0.0, 0.0)
    U = expm(-1j * H5 * 3.0)
    print("  D5 one-way check: |U_12|^2/|U_11|^2 at z=3: %.1e "
          "(triangular)" % (np.abs(U[0, 1]) ** 2 / np.abs(U[0, 0]) ** 2))
    zc = zc_colsum(H5)
    # honest comparator: the pure Jordan cell with the SAME coupling
    # and the SAME physical divisor step (the onset is
    # step-convention dependent; 0.486/(2J) is the dt -> 0
    # unit-cell value -- 0.50 is what a coarse 0.05 base grid
    # detects -- and neither is this protocol's)
    Hcell = np.array([[1.0, 2 * J0], [0.0, 1.0]])
    print("  D5 mass-creation onset z_c = %.3f cm  (pure cell, same "
          "step: %.3f; dt->0 limit 0.486/(2J) = %.3f)"
          % (zc, zc_colsum(Hcell), 0.486 / (2 * J0)))
    print("  D5 divisor min entry over ladder: %+.1e (M1-free)"
          % min_entry(H5))
    dets = [np.linalg.det(norm_divisor(H5, z, z + DZ)).real
            for z in np.arange(0.5, 10, 0.5)]
    print("  D5 det of divisor: min %.4f > 0 -- det estimator BLIND;"
          " column-sum required" % min(dets))
    for D in (0.5, 0.8):
        H = H_d5(J0, Gd0, 0.0, D)
        print("  D5 spectroscopy delta=%.1f: first negativity z* = "
              "%.3f cm (pi/delta = %.3f)" % (D, zstar_neg(H),
                                             np.pi / D))
    a = kap4                              # at EP: a = gamma/2 = kappa
    H4 = np.array([[1j * a, kap4], [kap4, -1j * a]])
    print("  D4 (kappa=%.2f, gamma=%.2f): M1 onset z = %.3f cm "
          "(1/(kappa sqrt2) = %.3f)" % (kap4, 2 * kap4,
                                        zstar_neg(H4),
                                        1 / (kap4 * np.sqrt(2))))

    # ---- [1b] imperfection tolerance curve ------------------------------
    print("\n[1b] D5 tolerance: divisor min entry vs asymmetry "
          "imperfection eta/J:")
    for frac in (0.01, 0.03, 0.10, 0.12, 0.13, 0.14,
                 -0.03, -0.14, -0.30, -0.50, -1.00):
        H = H_d5(J0, Gd0, frac * J0, 0.0)
        me = min_entry(H)
        zst = zstar_neg(H, 30.0)
        # eta > 0: real-direction split 2 sqrt(eta(J+Gd)) -> M1
        # returns at pi/split (2x2 theorem, mixed family: approx);
        # eta < 0: complex direction -> M1-free
        print("  eta/J = %+4.0f%% : window min entry %+.2e ; first "
              "negativity z* = %s cm" % (100 * frac, me,
                                         ("%.1f" % zst)
                                         if np.isfinite(zst)
                                         else ">30"))

    # ---- [1c] intensity-only sigma_max for the triangular device -------
    print("\n[1c] sigma_max(z) from intensities alone (triangular "
          "device):")

    def smax_from_intensities(G):
        # lower-triangular corner (u12 = 0): U^dag U diagonal =
        # measured column sums (exact even at eta != 0); off-diagonal
        # modulus = sqrt(G21 G22) at exact triangularity
        A = np.array([[G[0, 0] + G[1, 0],
                       np.sqrt(G[1, 0] * G[1, 1])],
                      [np.sqrt(G[1, 0] * G[1, 1]),
                       G[0, 1] + G[1, 1]]])
        return np.linalg.eigvalsh(A)[-1]

    worst0 = 0.0
    for z in np.arange(0.1, 6.01, 0.1):
        U = expm(-1j * H5 * z)
        G = np.abs(U) ** 2
        s2 = np.linalg.svd(U, compute_uv=False)[0] ** 2
        worst0 = max(worst0, abs(smax_from_intensities(G) - s2) / s2)
    print("  eta = 0: worst relative error of the reconstruction "
          "over z in (0,6]: %.1e" % worst0)
    Heta = H_d5(J0, Gd0, 0.03 * J0, 0.0)
    werr, wbound, wrel, viol = 0.0, 0.0, 0.0, 0
    for z in np.arange(0.05, 6.01, 0.05):
        U = expm(-1j * Heta * z)
        G = np.abs(U) ** 2
        s2 = np.linalg.svd(U, compute_uv=False)[0] ** 2
        err = abs(smax_from_intensities(G) - s2)
        bound = np.sqrt(G[0, 0] * G[0, 1])   # Weyl: unknown term
        if err > werr:
            werr, wbound, wrel = err, bound, err / s2
        if err > bound + 1e-12:
            viol += 1
    print("  eta = 3%% J: worst |Delta sigma^2| = %.2e (relative "
          "%.1e), Weyl bound sqrt(G11 G12) = %.2e," % (werr, wrel,
                                                       wbound))
    print("  bound violations over the ladder: %d -- the column-sum "
          "observable is intensity-only," % viol)
    print("  with a data-driven systematic bound from the residual "
          "entry itself.")

    # ---- [2] D5 Monte Carlo ---------------------------------------------
    print("\n[2] D5 measurement-chain MC (400 realizations, 1e4 "
          "photons/launch):")

    def ratio_fit(data):
        """Closed-form calibration-free balanced-device estimators
        (see ESTIMATOR NOTE in the docstring)."""
        g11 = data[:, 0, 0] - DARK
        m = g11 > 10 * DARK
        Gd = -np.polyfit(ZS[m], np.log(g11[m]), 1)[0] / 2
        g21 = np.clip(data[:, 1, 0] - DARK, 1e-12, None)
        JG = np.mean(np.sqrt(g21[m] / g11[m]) / ZS[m])
        return JG - Gd, Gd

    zcs, zs05, dJ = [], [], []
    Js, Jh, etas, etah = [], [], [], []
    Dts, Dhs = [], []
    for _ in range(400):
        J = J0 * (1 + 0.02 * rng.standard_normal())
        Gd = Gd0 * (1 + 0.02 * rng.standard_normal())
        eta = 0.03 * J0 * rng.standard_normal()
        cal = 1 + 0.03 * rng.standard_normal(2)
        # balanced device: closed-form ratio estimators
        data = measure(H_d5(J, Gd, eta, 0.0), cal)
        Jhat, Gdhat = ratio_fit(data)
        Js.append(J)
        Jh.append(Jhat)
        dJ.append((Jhat - J) / J)
        zcs.append(zc_colsum(H_d5(Jhat, Gdhat, 0.0, 0.0)) - zc_colsum(
            H_d5(J, Gd, eta, 0.0)))        # estimator error, per device
        # eta NON-recovery control: the old LSQ fit, kept only as a
        # printed diagnostic of what the intensity fit cannot do
        p = fit_model(data, [J0, Gd0, 0.0, 0.0, 1.0, 1.0])
        etas.append(eta)
        etah.append(p[2])
        # detuned device (spectroscopy row), delta = 0.5: LSQ fit
        # retained (the detuning delta is genuinely recovered here -- and the
        # recovery correlation is printed as a control, per the
        # same rule that caught the balanced-device prior echo)
        Dtrue = 0.5 * (1 + 0.02 * rng.standard_normal())
        data = measure(H_d5(J, Gd, eta, Dtrue), cal)
        p = fit_model(data, [J0, Gd0, 0.0, 0.5, 1.0, 1.0])
        Dts.append(Dtrue)
        Dhs.append(p[3])
        zs05.append(zstar_neg(H_d5(*p[:4])) - np.pi / Dtrue)
    zcs, zs05, dJ = map(np.array, (zcs, zs05, dJ))
    Js, Jh, etas, etah = map(np.array, (Js, Jh, etas, etah))
    Dts, Dhs = np.array(Dts), np.array(Dhs)
    cJ = np.corrcoef(Jh, Js)[0, 1]
    ce = np.corrcoef(etah, etas)[0, 1]
    cD = np.corrcoef(Dhs, Dts)[0, 1]
    print("  J recovery (ratio estimator): (Jhat-J)/J = %+.4f +- "
          "%.4f ; corr(Jhat, J) = %.2f" % (dJ.mean(), dJ.std(), cJ))
    print("  z_c estimator error (vs each device's own truth): "
          "%+.4f +- %.4f cm" % (np.nanmean(zcs), np.nanstd(zcs)))
    print("  eta NON-recovery control (LSQ fit): corr(etahat, eta) = "
          "%.2f -- the intensity fit" % ce)
    print("  does NOT resolve eta at the 3% design level (Ghat_12 "
          "signal at the dark floor);")
    print("  eta is certified by window cleanliness ([1b]) + the "
          "[1c] Weyl residual instead.")
    print("  z* error vs pi/delta_true: %+.3f +- %.3f cm ; "
          "corr(deltahat, delta) = %.2f (genuine recovery control)"
          % (np.nanmean(zs05), np.nanstd(zs05), cD))

    # ---- [3] D4 negativity depth for contrast ---------------------------
    print("\n[3] D4 contrast: divisor min entry over the window:")
    print("  D4 model: min entry %.3f (O(1) negative) vs D5 "
          "balanced ~0 (mechanism contrast is the headline "
          "observable)" % min_entry(H4, 4.0))
    # D4's det channel, printed (the fingerprint's other half):
    # the dimer's divisor det leaves 1 and goes negative, unlike the
    # cascade's positive-definite diagonal-ratio det
    det_min, det_cross = 1.0, None
    for z in np.arange(0.1, 4.0, 0.01):
        U1 = expm(-1j * H4 * z)
        G1 = np.abs(U1 / np.linalg.svd(U1, compute_uv=False)[0]) ** 2
        if np.linalg.cond(G1) > 1e8:
            continue
        dv = np.linalg.det(norm_divisor(H4, z, z + DZ)).real
        det_min = min(det_min, dv)
        if det_cross is None and dv < 0:
            det_cross = z
    print("  D4 divisor det: first negative at z = %s cm, min %.1f "
          "-- det-crossing + negativity" %
          (("%.2f" % det_cross) if det_cross else ">4", det_min))
    print("  is the dimer's fingerprint; det-silent + column-sum-loud "
          "is the cascade's.")

    print("\ndone.")


if __name__ == "__main__":
    main()
