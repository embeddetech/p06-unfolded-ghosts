"""Arc-B go/no-go gate (paper 6): 2x2 divisor-failure taxonomy.

For sub-stochastic families Gamma(t) = |e^{-iHt}/sigma_max(t)|^2 the
two-point divisor M = Gamma(s+dt) Gamma(s)^{-1} can fail
sub-stochasticity in exactly two elementary ways in 2x2:
  M1: some entry < 0                    (broken-dimer mechanism, paper 1)
  M2: entries >= 0 but a column sum > 1 (conditional mass creation, paper 4)

Scout conjecture (t4_threads_report.md item 3): M1 <-> complex-spectrum
(broken) dynamics, M2 <-> Jordan/cascade dynamics, exhaustive and
exclusive. Paper 4 already contains a counter-hint: the PT DIMER at its
own EP fails via M1 (neg entry by t ~ 0.7) while the PU Jordan cell
fails via M2 -- both are Jordan points. Refined conjecture tested here:

  (R1) M2 occurs iff |U(t)|^2 is triangular in the beable basis
       (one-way cascade alignment), which is non-generic;
  (R2) complex-spectrum (broken) families fail via M1;
  (R3) real-spectrum diagonalizable families: measured, no prediction;
  (R4) MIXED cells (M1 and M2 at the same (s,dt)) -- the scout's
       original conjecture was that these are absent in 2x2; the runs
       below REFUTE it (MIXED occurs in the dimer families and the
       random ensembles -- see the [1]-[2] printouts). Kept here as
       the recorded hypothesis; the paper does not rely on R1-R4,
       citing this script only for block [4].

Block [4] makes the sigma_max convention explicit (paper 6, Sec. 3
conventions paragraph): divisor entry SIGNS are invariant under every
positive scalar renormalization c(t) of the contraction normalization
(M1 is convention-free); divisor COLUMN SUMS scale by
c^2(s)/c^2(s+dt), so M2 -- onset and occurrence -- is stated relative
to the minimal convention c = sigma_max. Dichotomy for the unit cell
(coupling kappa): the raw |U|^2 divisor column sum is exactly
1 + kappa^2(T^2-s^2), so avoiding the crossing at ALL pairs requires
c^2(t) >= c^2(0) e^{kappa^2 t^2} (sufficient too: verified) --
divisibility is purchasable only at divergent conditioning overhead
c^2/sigma_max^2, i.e. only by discarding survival probability the
dynamics never loses.

Classes swept (each with random similarity conjugations where noted):
  DIMER-U   PT dimer gamma < kappa (unbroken, real spectrum, non-normal)
  DIMER-EP  PT dimer gamma = kappa (Jordan, symmetric beable mixing)
  DIMER-B   PT dimer gamma > kappa (broken, complex pair)
  PU-J2     pure Jordan cell [[w,1],[0,w]] (triangular cascade)
  J2-CONJ   random-S-conjugated Jordan cells (generic beable alignment)
  DIAG-R    random-S-conjugated real distinct spectrum
  DIAG-C    random-S-conjugated complex-conjugate pair

ASCII only; numpy. Fast (< 1 min).
"""

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(11)
TOL = 1e-10


def dimer(gam, kap=1.0):
    return np.array([[1j * gam, kap], [kap, -1j * gam]])


def jordan2(w=1.0):
    return np.array([[w, 1.0], [0.0, w]])


def rand_S():
    S = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    while np.linalg.cond(S) > 20:
        S = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    return S


def gamma_of(H, t):
    U = expm(-1j * H * t)
    return np.abs(U / np.linalg.svd(U, compute_uv=False)[0]) ** 2


def classify_family(H, ss, dts):
    """Sweep (s, dt); return set of failure modes seen + first onsets."""
    modes = set()
    onset = {}
    for dt in dts:
        for s in ss:
            G1, G2 = gamma_of(H, s), gamma_of(H, s + dt)
            if abs(np.linalg.det(G1)) < 1e-13:
                continue
            M = G2 @ np.linalg.inv(G1)
            neg = M.min() < -TOL
            col = M.sum(axis=0).max() > 1.0 + TOL
            if neg and col:
                modes.add("MIXED")
                onset.setdefault("MIXED", s)
            elif neg:
                modes.add("M1")
                onset.setdefault("M1", s)
            elif col:
                modes.add("M2")
                onset.setdefault("M2", s)
    return modes, onset


def is_triangular_cascade(H, ts):
    """|U(t)|^2 triangular (same corner) for all t?"""
    lo = all(np.abs(expm(-1j * H * t))[1, 0] ** 2 < 1e-12 for t in ts)
    up = all(np.abs(expm(-1j * H * t))[0, 1] ** 2 < 1e-12 for t in ts)
    return lo or up


def report(name, H, ss, dts, tri_ts):
    modes, onset = classify_family(H, ss, dts)
    tri = is_triangular_cascade(H, tri_ts)
    lab = "+".join(sorted(modes)) if modes else "DIVISIBLE(window)"
    ons = "  onsets: " + ", ".join(
        "%s@s=%.2f" % (m, s) for m, s in sorted(onset.items())) \
        if onset else ""
    print("  %-9s cascade=%-5s -> %s%s" % (name, tri, lab, ons))
    return modes, tri


def main():
    print("=" * 72)
    print("Arc-B gate: 2x2 divisor-failure taxonomy "
          "(M1 negativity vs M2 mass creation)")
    print("=" * 72)
    ss = np.linspace(0.05, 8.0, 240)
    dts = (0.02, 0.1, 0.5)
    tri_ts = np.linspace(0.1, 8.0, 40)

    print("\n[1] canonical members:")
    res = {}
    res["DIMER-U"] = report("DIMER-U", dimer(0.5), ss, dts, tri_ts)
    res["DIMER-EP"] = report("DIMER-EP", dimer(1.0), ss, dts, tri_ts)
    res["DIMER-B"] = report("DIMER-B", dimer(1.5), ss, dts, tri_ts)
    res["PU-J2"] = report("PU-J2", jordan2(), ss, dts, tri_ts)

    print("\n[2] random ensembles (n=40 each; union of modes; counts):")
    for name, make in (
        ("J2-CONJ", lambda: rand_S() @ jordan2() @
            np.linalg.inv(rand_S())),  # placeholder, fixed below
        ("DIAG-R", None), ("DIAG-C", None),
    ):
        counts = {}
        tri_n = 0
        for i in range(40):
            S = rand_S()
            Si = np.linalg.inv(S)
            if name == "J2-CONJ":
                H = S @ jordan2() @ Si
            elif name == "DIAG-R":
                e = np.sort(rng.uniform(0.2, 2.0, 2))
                H = S @ np.diag(e) @ Si
            else:
                a, b = rng.uniform(0.2, 2.0), rng.uniform(0.1, 1.0)
                H = S @ np.diag([a + 1j * b, a - 1j * b]) @ Si
            modes, _ = classify_family(H, ss[::4], dts)
            tri_n += is_triangular_cascade(H, tri_ts)
            key = "+".join(sorted(modes)) if modes else "DIV"
            counts[key] = counts.get(key, 0) + 1
        print("  %-9s cascades=%d/40  modes: %s" % (name, tri_n, counts))

    print("\n[3] verdict lines:")
    m_ep, _ = res["DIMER-EP"]
    m_j2, tri_j2 = res["PU-J2"]
    m_b, _ = res["DIMER-B"]
    print("  R1 (M2 <-> triangular cascade): PU-J2 tri=%s modes=%s; "
          "DIMER-EP tri=False modes=%s" % (tri_j2, sorted(m_j2),
                                           sorted(m_ep)))
    print("  R2 (broken -> M1): DIMER-B modes=%s" % sorted(m_b))
    print("  R4 (no MIXED cells): see MIXED occurrences above")

    print("\n[4] the sigma_max convention: invariance split + "
          "minimal-conditioning dichotomy")
    J = jordan2()
    kap = 1.0

    def smax_t(t):
        return np.linalg.svd(expm(-1j * J * t), compute_uv=False)[0]

    def divisor_c(cfun, s, tau):
        U1, U2 = expm(-1j * J * s), expm(-1j * J * (s + tau))
        G1 = np.abs(U1) ** 2 / cfun(s) ** 2
        G2 = np.abs(U2) ** 2 / cfun(s + tau) ** 2
        return G2 @ np.linalg.inv(G1)

    mism, on_min, on_over = 0, None, None
    for s in np.arange(0.05, 4.0, 0.01):
        Ma = divisor_c(smax_t, s, 0.02)
        Mb = divisor_c(lambda t: smax_t(t) * (1 + 0.5 * t), s, 0.02)
        if not np.array_equal(np.sign(np.round(Ma, 12)),
                              np.sign(np.round(Mb, 12))):
            mism += 1
        if on_min is None and Ma.sum(axis=0).max() > 1 + 1e-10:
            on_min = s
        if on_over is None and Mb.sum(axis=0).max() > 1 + 1e-10:
            on_over = s
    print("  M1 sign-pattern mismatches under renormalization: %d "
          "(convention-free)" % mism)
    print("  M2 onset: %.3f (minimal) vs %s (over-conditioned "
          "c = sigma_max(1+t/2)) -- convention-relative"
          % (on_min, ("%.3f" % on_over) if on_over else "none"))
    for s in (0.5, 2.0):
        U1 = expm(-1j * J * s)
        U2 = expm(-1j * J * (s + 1e-4))
        raw = (np.abs(U2) ** 2 @ np.linalg.inv(np.abs(U1) ** 2)
               ).sum(axis=0).max()
        print("  raw divisor col sum at s=%.1f: %.8f vs "
              "1+k^2(T^2-s^2) = %.8f" % (s, raw,
                                         1 + kap ** 2 *
                                         ((s + 1e-4) ** 2 - s ** 2)))
    cfree = lambda t: smax_t(t) * np.exp(0.5 * kap ** 2 * t ** 2)
    worst = -np.inf
    for s in np.arange(0.05, 5.0, 0.05):
        for tau2 in (0.01, 0.1, 0.5, 1.0, 2.0):
            M = divisor_c(cfree, s, tau2)
            worst = max(worst, M.sum(axis=0).max())
            assert M.min() >= -1e-12
    print("  crossing-free convention c^2 = sigma_max^2 e^{k^2 t^2}: "
          "max col sum %.6f (<= 1);" % worst)
    print("  overhead c^2/sigma_max^2 at t = 1/3/5: %.2f / %.1e / %.1e "
          "-- divergent" % tuple(np.exp(kap ** 2 * t ** 2)
                                 for t in (1.0, 3.0, 5.0)))
    # zero-step onset, emitted (the constant quoted as 0.486 in the
    # papers): under the minimal convention the divisor column sum
    # crosses one as tau -> 0 where d/dt[k^2 t^2] first exceeds
    # d/dt ln sigma_max^2, i.e. at the root of
    # 2 k^2 t sigma^2(t) = (sigma^2)'(t); for the unit cell
    # sigma^2 = 1 + t^2/2 + t sqrt(1 + t^2/4).
    from scipy.optimize import brentq
    s2 = lambda t: 1 + t ** 2 / 2 + t * np.sqrt(1 + t ** 2 / 4)
    h = 1e-7
    f = lambda t: 2 * kap ** 2 * t * s2(t) - (s2(t + h) - s2(t - h)) \
        / (2 * h)
    tc0 = brentq(f, 0.1, 1.0)
    print("  zero-step column-sum crossing (root of 2 k^2 t sigma^2 = "
          "(sigma^2)'): t_c = %.4f" % tc0)

    print("\ndone.")


if __name__ == "__main__":
    main()
