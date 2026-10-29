"""Arc-B theorem numerics: the divisor sees the unfolding direction.

THEOREM CANDIDATE (2x2 cascade divisor dichotomy). Let H be upper
triangular, H = [[w1, c],[0, w2]], c != 0, U(t) = e^{-iHt},
Gamma(t) = |U(t)/sigma_max(t)|^2, divisor M = Gamma(s+dt) Gamma(s)^-1.
Then:
 (i)  M is upper triangular with nonnegative diagonal -- always.
 (ii) sign(M_12) = sign(r(s+dt) - r(s)) where r(t) = |U12|^2/|U11|^2
      (the cascade ratio; normalization-independent).
 (iii) real frequency split delta = w1 - w2 (real direction):
      r(t) = |c|^2 (2 - 2 cos(delta t))/delta^2 oscillates =>
      negativity (M1) recurs; FIRST onset at s* = pi/|delta| (where r
      peaks and turns down). EP limit delta -> 0: r -> |c|^2 t^2
      monotone => M1-free (paper 4's PU cell).
 (iv) imaginary split (decay direction), w1 = w - i g1, w2 = w - i g2:
      r(t) = |c|^2 (1 - e^{(g1-g2)t})^2/(g1-g2)^2 monotone => M1-free
      at all times; indivisibility enters purely via M2.
So within cascade families the divisor failure mode is the image of
the unfolding direction: real split => M1 returns (period pi/delta);
EP or purely imaginary split => pure conditional mass creation
(mixed complex splits are NOT M1-free -- see block [6]). Corrects the
morning gate's coarser "cascade => M1-free."

Checks: [1] identity (ii) machine-precision over random triangular H
(complex c, mixed w) at random (s,dt); [2] first-M1 onset vs
pi/delta across a delta sweep; [3] imaginary-split M1-freeness over
long windows + M2 presence; [4] EP: M1-free, M2 onset ~ 0.48
(zero-step 0.486; paper-4 cross-check); [5] closed-form r(t) vs numerics.

ASCII only; numpy/scipy. Seconds.
"""

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(7)
TOL = 1e-9


def tri(w1, w2, c):
    return np.array([[w1, c], [0.0, w2]], dtype=complex)


def U_of(H, t):
    return expm(-1j * H * t)


def gamma_of(H, t):
    U = U_of(H, t)
    return np.abs(U / np.linalg.svd(U, compute_uv=False)[0]) ** 2


def divisor(H, s, dt):
    return gamma_of(H, s + dt) @ np.linalg.inv(gamma_of(H, s))


def r_of(H, t):
    U = U_of(H, t)
    return np.abs(U[0, 1]) ** 2 / np.abs(U[0, 0]) ** 2


def main():
    print("=" * 72)
    print("Arc-B theorem numerics: divisor failure mode vs unfolding "
          "direction")
    print("=" * 72)

    # ---- [1] sign identity, adversarial --------------------------------
    print("\n[1] identity sign(M_12) = sign(r(s+dt)-r(s)), random "
          "triangular H:")
    bad, n = 0, 0
    worst_margin = np.inf
    for _ in range(400):
        w1 = rng.uniform(-2, 2) - 1j * rng.uniform(0, 1) * (rng.random() < .5)
        w2 = rng.uniform(-2, 2) - 1j * rng.uniform(0, 1) * (rng.random() < .5)
        c = (rng.standard_normal() + 1j * rng.standard_normal())
        H = tri(w1, w2, c)
        s, dt = rng.uniform(0.05, 6), rng.uniform(0.01, 1.0)
        M = divisor(H, s, dt)
        dr = r_of(H, s + dt) - r_of(H, s)
        if abs(M[0, 1]) < TOL or abs(dr) < TOL:
            continue
        n += 1
        if np.sign(M[0, 1].real) != np.sign(dr):
            bad += 1
        worst_margin = min(worst_margin, abs(M[1, 0]))
        # (i): lower-left exactly zero, diagonal nonnegative
        assert abs(M[1, 0]) < 1e-10 and M[0, 0].real > -1e-12 \
            and M[1, 1].real > -1e-12
    print("  %d/%d sign matches (0 expected failures); max |M_21| "
          "residual < 1e-10: OK" % (n - bad, n))

    # ---- [2] first-M1 onset vs pi/delta (real split) -------------------
    print("\n[2] real split: first-M1 onset vs pi/delta "
          "(dt=0.02 scan):")
    dt = 0.02
    for D in (0.4, 0.8, 1.2, 2.0):
        H = tri(1.0 + D / 2, 1.0 - D / 2, 1.0)
        onset = None
        for s in np.arange(0.05, 2.5 * np.pi / D, 0.01):
            if divisor(H, s, dt)[0, 1].real < -TOL:
                onset = s
                break
        pred = np.pi / D
        print("  delta=%.1f : onset %.3f   pi/delta = %.3f   "
              "ratio %.4f" % (D, onset, pred, onset / pred))

    # ---- [3] imaginary split: M1-free, M2 present ----------------------
    print("\n[3] imaginary (decay) split, w = 1 - i*g, long window "
          "t <= 40:")
    # M1 check via the inversion-free identity: sign(M_12) =
    # sign(b(T)a(s) - a(T)b(s)) with unnormalized |U|^2 entries --
    # the naive divisor inverse loses ~19 digits at gamma*t ~ 40
    # (first run of this script printed -9.1e18 there; kept in git
    # history as the cautionary artifact).
    for dg in (0.2, 0.6, 1.0):
        H = tri(1.0, 1.0 - 1j * dg, 1.0)
        worst_q, m2_onset = 0.0, None
        for s in np.arange(0.05, 40, 0.05):
            Us, UT = U_of(H, s), U_of(H, s + 0.1)
            aT, bT = np.abs(UT[0, 0])**2, np.abs(UT[0, 1])**2
            a_s, b_s = np.abs(Us[0, 0])**2, np.abs(Us[0, 1])**2
            q = (bT * a_s - aT * b_s) / (bT * a_s + aT * b_s)
            worst_q = min(worst_q, q)
            if m2_onset is None and s < 20:  # divisor OK at small s
                M = divisor(H, s, 0.1)
                if (M.real.sum(axis=0).max() - 1.0) > TOL:
                    m2_onset = s
        print("  dgamma=%.1f : worst normalized sign-quantity %+.1e "
              "(M1-free iff >= 0)   M2 onset s=%.2f"
              % (dg, worst_q, m2_onset))

    # ---- [4] EP cross-check --------------------------------------------
    print("\n[4] EP (delta=0) cross-check vs paper 4:")
    H = tri(1.0, 1.0, 1.0)
    worst_neg, m2_onset = 0.0, None
    for s in np.arange(0.05, 20, 0.01):
        M = divisor(H, s, 0.05)
        worst_neg = min(worst_neg, M.min().real)
        if m2_onset is None and (M.real.sum(axis=0).max() - 1.0) > TOL:
            m2_onset = s
    print("  worst entry %+.1e (provably 0)   M2 onset s=%.2f "
          "(paper 4: t_c ~ 0.50)" % (worst_neg, m2_onset))

    # ---- [5] closed forms ----------------------------------------------
    print("\n[5] closed-form r(t) vs numerics (max reldiff over "
          "t in [0.1, 6]):")
    ts = np.linspace(0.1, 6, 60)
    D = 0.9
    H = tri(1.0 + D / 2, 1.0 - D / 2, 1.3)
    err1 = max(abs(r_of(H, t) - 1.3 ** 2 * (2 - 2 * np.cos(D * t))
                   / D ** 2) / r_of(H, t) for t in ts)
    g = 0.7
    H = tri(1.0, 1.0 - 1j * g, 1.3)
    err2 = max(abs(r_of(H, t) - 1.3 ** 2 * (1 - np.exp(-g * t)) ** 2
                   / g ** 2) / r_of(H, t) for t in ts)
    H = tri(1.0, 1.0, 1.3)
    err3 = max(abs(r_of(H, t) - 1.3 ** 2 * t ** 2) / r_of(H, t)
               for t in ts)
    print("  real split: %.1e   imag split: %.1e   EP (|c|t)^2: %.1e"
          % (err1, err2, err3))

    # ---- [6] mixed complex splits: monotone ONLY at pure imaginary ----
    # (audit pass 1 caught the false converse "complex split =>
    # M1-free"; the correct statement: r(t) = |c|^2 |e^{i delta t}-1|^2
    # / |delta|^2 is monotone iff Re(delta) = 0.)
    print("\n[6] mixed splits delta = |d| e^{i phase}: count of "
          "decreasing r-intervals, t <= 40 (FULL circle -- audit "
          "pass 2 caught an upper-half-plane-only scan being "
          "generalized):")
    for deg in (0, 30, 60, 90, 120, 150, 180, 181, 185, 188, 190,
                193, 210, 240, 270, 300, 330):
        ph = np.deg2rad(deg)
        delta = 0.6 * np.exp(1j * ph)
        w2 = 1.0 - delta            # w1 = 1.0; split = delta
        H = tri(1.0, w2, 1.0)
        ts = np.arange(0.05, 40, 0.02)
        rs = np.array([r_of(H, t) for t in ts])
        dd = np.diff(rs)
        dec = dd < -1e-12
        ndec = int(np.sum(dec))
        # strict count (< 0): tolerance-robust in the flattened tail;
        # the -1e-12 count differs by a few near-threshold steps at
        # 60/120 deg (1049 vs strict 1050) -- both printed so the
        # paper's strict value is reproducible from this artifact.
        nstrict = int(np.sum(dd < 0.0))
        # windows = maximal contiguous runs of decrease
        nwin = int(np.sum(dec[1:] & ~dec[:-1]) + (1 if dec[0] else 0))
        print("  phase %3d deg : decreasing intervals %5d (strict "
              "%5d) in %3d window(s)  %s"
              % (deg, ndec, nstrict, nwin,
                 "(monotone: M1-free)" if ndec == 0 else ""))
    # cone boundary by bisection: r monotone iff
    # phi(t) = b cos(at) + a sin(at) - b e^{-bt} >= 0 for all t > 0
    # (scale-invariant in |delta|); boundary angles in the lower
    # half-plane, symmetric about 270 deg.
    ts = np.linspace(1e-4, 400, 400000)

    def monotone(deg):
        ph = np.deg2rad(deg)
        a, b = np.cos(ph), np.sin(ph)
        return np.min(b * np.cos(a * ts) + a * np.sin(a * ts)
                      - b * np.exp(-b * ts)) > -1e-12

    lo, hi = 180.0, 270.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if monotone(mid):
            hi = mid
        else:
            lo = mid
    print("  lower-cone boundary: %.3f deg (i.e. %.3f deg from the "
          "real axis; mirror at %.3f deg)"
          % (hi, hi - 180.0, 540.0 - hi))

    print("\nconclusion: within cascade families the divisor failure")
    print("mode reads out the unfolding direction -- real split: M1")
    print("returns at s = pi/delta; EP and decay split: M1-free, pure")
    print("conditional mass creation (M2).")
    print("done.")


if __name__ == "__main__":
    main()
