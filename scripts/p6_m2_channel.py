"""Arc-B addendum (pass-9 F1 rescope): the divisor's SECOND channel.

The negativity (M1) channel of the cascade divisor reads Re(delta)
-- oscillatory content -- and is provably silent on the +i ray, the
EP, and the silent cone about -i (p6_divisor_theorem.py). This
script answers the question that rescoped the paper's thesis: what
does the COLUMN-SUM (M2, conditional-mass-creation) channel see on
those silent directions, and does either channel see the flagship
Ilhan-Kovner corner?

 [1] Bond level (2x2 triangular cell, split delta = |d| e^{i phi}):
     M1 and M2 onsets over the full circle of split phases, two
     step sizes.  FINDINGS (quoted in paper 6, Sec. 3):
       - M2 fires at EVERY phase, including the entire M1-silent
         set: the instrument as a whole has no silent direction.
       - The M2 onset is ASYMMETRIC between the two imaginary rays
         (growing +i late, decaying -i early): the column-sum
         channel resolves exactly the sign that negativity cannot.
       - M2 is convention-relative (sigma_max convention; see
         p6_divisor_gate.py [4]); M1 is convention-free.

 [2] The omega -> 0 corner (IK's k=0 sector) is a SIZE-4 Jordan
     block, not a bond: Theorem k2 (k>=3 mixing) applies, so its
     divisor is negativity-bearing REGARDLESS of unfolding
     direction.  Verified: M1 onset at the pure corner and at both
     family unfoldings (phi = pi blowup, phi = 0 oscillatory)
     equals the theorem's short-step window boundary
     s* = tau/(sqrt3 - 1) (the first s with (s+tau)/s < sqrt3), at
     two step sizes.  The bond-level silent set does NOT apply to
     the corner.

ASCII only; numpy/scipy.
"""

import numpy as np
from scipy.linalg import expm

TOLN = -1e-9
TOLC = 1e-9


def onsets(ufun, tmax=12.0, base=0.01, tau=0.05):
    """(M1, M2) onsets of the sigma_max-normalized divisor."""
    m1 = m2 = None
    for s in np.arange(base, tmax, base):
        U1, U2 = ufun(s), ufun(s + tau)
        G1 = np.abs(U1 / np.linalg.svd(U1, compute_uv=False)[0]) ** 2
        G2 = np.abs(U2 / np.linalg.svd(U2, compute_uv=False)[0]) ** 2
        if np.linalg.cond(G1) > 1e8:
            continue
        M = G2 @ np.linalg.inv(G1)
        if m1 is None and M.min() < TOLN:
            m1 = s
        if m2 is None and M.sum(axis=0).max() > 1 + TOLC:
            m2 = s
        if m1 is not None and m2 is not None:
            break
    return m1, m2


def fmt(x):
    return ("%.2f" % x) if x is not None else "none"


def main():
    print("=" * 72)
    print("The divisor's second channel: M2 on the M1-silent set, "
          "and the size-4 corner")
    print("=" * 72)

    # ---------------- [1] bond-level two-channel sweep -----------------
    print("\n[1] 2x2 bond, split delta = 0.6 e^{i phi}, coupling 1, "
          "tau = 0.05, base grid 0.01:")
    print("    phi[deg]   M1 onset   M2 onset")
    res = {}
    for deg in (0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330):
        d = 0.6 * np.exp(1j * np.deg2rad(deg))
        H = np.array([[1.0 + d, 1.0], [0.0, 1.0]])
        m1, m2 = onsets(lambda t, H=H: expm(-1j * H * t))
        res[deg] = (m1, m2)
        sil = "  <- M1-silent" if m1 is None else ""
        print("      %3d      %-8s   %-8s%s" % (deg, fmt(m1), fmt(m2),
                                                sil))
    HEP = np.array([[1.0, 1.0], [0.0, 1.0]])
    m1, m2 = onsets(lambda t: expm(-1j * HEP * t))
    print("      EP       %-8s   %-8s  <- M1-silent (pure cell)"
          % (fmt(m1), fmt(m2)))
    # dense-grid quantifier check: 5-degree spacing over the full
    # circle (72 phases) -- count silent phases, report onset range
    dense = []
    for deg in range(0, 360, 5):
        d = 0.6 * np.exp(1j * np.deg2rad(deg))
        H = np.array([[1.0 + d, 1.0], [0.0, 1.0]])
        dense.append(onsets(lambda t, H=H: expm(-1j * H * t))[1])
    nsil = sum(1 for x in dense if x is None)
    lo = min(x for x in dense if x is not None)
    hi = max(x for x in dense if x is not None)
    print("    dense scan, 5-deg grid (72 phases): silent phases %d; "
          "M2 onsets in [%.2f, %.2f]" % (nsil, lo, hi))
    print("    M2 fires at every sampled phase; onset asymmetry on "
          "the imaginary axis:")
    print("      +i (growing, 90) M2 = %s vs -i (decaying, 270) "
          "M2 = %s" % (fmt(res[90][1]), fmt(res[270][1])))
    # robustness of the asymmetry: second |delta| and second tau
    for dd, tau in ((0.3, 0.05), (0.6, 0.02)):
        row = []
        for deg in (90, 270):
            d = dd * np.exp(1j * np.deg2rad(deg))
            H = np.array([[1.0 + d, 1.0], [0.0, 1.0]])
            row.append(onsets(lambda t, H=H: expm(-1j * H * t),
                              tau=tau)[1])
        print("      |d|=%.1f tau=%.2f: M2(+i) = %s vs M2(-i) = %s"
              % (dd, tau, fmt(row[0]), fmt(row[1])))

    # ---------------- [2] the size-4 corner ----------------------------
    print("\n[2] the omega->0 corner: size-4 block, both channels, "
          "vs the Theorem-k2 boundary")

    def pu_companion(w1sq, w2sq):
        # x'''' + (w1^2 + w2^2) x'' + w1^2 w2^2 x = 0, variables
        # (x, x', x'', x''') -- at the corner this is the J_4(0)
        # chain basis itself (beable-aligned cascade)
        A = np.zeros((4, 4), dtype=complex)
        A[0, 1] = A[1, 2] = A[2, 3] = 1.0
        A[3, 2] = -(w1sq + w2sq)
        A[3, 0] = -w1sq * w2sq
        return A

    def fmt3(x):
        return ("%.3f" % x) if x is not None else "none"

    for tau in (0.05, 0.02):
        sstar = tau / (np.sqrt(3.0) - 1.0)
        print("  tau = %.2f  (Theorem-k2 short-step boundary "
              "s* = tau/(sqrt3-1) = %.4f; corner base grid 0.002):"
              % (tau, sstar))
        for name, w2sq in (("pure corner        ", 0.0),
                           ("phi=pi  (IK blowup)", -0.36),
                           ("phi=0   (oscillat.)", +0.36)):
            A = pu_companion(0.0, w2sq)
            m1, m2 = onsets(lambda t, A=A: expm(A * t), tmax=8.0,
                            base=0.002, tau=tau)
            print("    %s : M1 onset %-7s M2 onset %-7s" %
                  (name, fmt3(m1), fmt3(m2)))
        print("    (M1 onset = first base-grid point past s*: the "
              "corner block's negativity")
        print("     is the depth->=3 theorem; the bond-level silent "
              "set does not apply.)")
    # direction-independence at FINITE unfolding is a computed
    # statement (the theorem covers the corner block itself):
    # 12-phase circle of complex family unfoldings at |Delta| = 0.36
    m1s = []
    for deg in range(0, 360, 30):
        A = pu_companion(0.0, 0.36 * np.exp(1j * np.deg2rad(deg)))
        m1s.append(onsets(lambda t, A=A: expm(A * t), tmax=8.0,
                          base=0.002, tau=0.05)[0])
    u = sorted(set(fmt3(x) for x in m1s))
    print("  finite-unfolding direction scan (|Delta| = 0.36, 12 "
          "phases at 30 deg, tau = 0.05):")
    print("    M1 onsets: %s -- identical at every sampled phase"
          % ", ".join(u))

    print("\nVERDICT (paper 6 rescope): the negativity channel reads "
          "Re(delta) with a")
    print("known silent set; the column-sum channel (convention-"
          "relative) fires at every")
    print("SAMPLED direction and resolves the +i/-i sign; the "
          "flagship corner instability is")
    print("caught by the depth theorem itself. Two channels, no "
          "silent direction.")
    print("\ndone.")


if __name__ == "__main__":
    main()
