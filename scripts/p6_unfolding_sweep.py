"""Arc-A: mode-level direction-resolved unfolding sweep (paper 6).

The equal-frequency PU / conformal-gravity mode pair is a k=2 Jordan
point. Two inequivalent unfolding kinds, each with a phase phi:

 FAMILY direction (physical parameters: mass term, width): detune
   omega_2^2 = omega^2 + Delta, Delta = |Delta| e^{i phi}. Split is
   LINEAR (non-generic unfolding; paper 4's cond = 2.00/delta lives
   here). Mode-pair normal form: H = [[w1, 1],[0, w2]] (triangular
   -- the cascade of the divisor theorems!), w2 = sqrt(w^2+Delta).
   Growth rate = |Im w2| ~ |Delta| sin(phi) / (2w).
     phi = 0 (Stelle m^2): zero growth, oscillatory; secular window
       t < 1/delta; dictionary cost cond ~ 2/delta.
     phi = arctan(gamma/m^2) (Merlin width): growth gamma/(2w) per
       pair -- Arc-E's time-dilated width, recovered.

 GENERIC direction (regulators, NON-SYMPLECTIC lattice, machine noise;
   a *symplectic* lattice discretization is the STRUCTURED case (open
   oscillatory band, handled in the paper body, not here): perturb the
   block entry: H = [[w, 1],[eps e^{i phi}, w]]. Puiseux: eigenvalues
   w +- sqrt(eps) e^{i phi/2}; growth = sqrt(eps) |sin(phi/2)|.
     phi = 0: real split (oscillatory); ANY other phase: growth.
     Random-phase noise: growing with probability 1 -- "the pure
     theory is the boundary."

 OMEGA -> 0 CORNER (Ilhan-Kovner, k=0 conformal cosmology): the
   family direction becomes Puiseux itself (w2 = sqrt(Delta)):
   growth = sqrt(|Delta|) |sin(phi/2)|. IK's induced
   omega_eff^2 = -(3/4) gamma_b^2 is phi = pi, |Delta| = (3/4)
   gamma_b^2 => growth = (sqrt(3)/2) gamma_b: the agent's
   frozen-mode formula, with no free parameters.

Physics-facing map printed at the end. 4x4 PU companion matrix used
as the faithfulness check on the 2x2 normal forms.

ASCII only; numpy. Seconds.
"""

import numpy as np
from scipy.integrate import solve_ivp

rng = np.random.default_rng(5)


def pu_companion(w1sq, w2sq):
    """x'''' = -(w1^2+w2^2) x'' - w1^2 w2^2 x, first-order 4x4."""
    A = np.zeros((4, 4), dtype=complex)
    A[0, 1] = A[1, 2] = A[2, 3] = 1.0
    A[3, 2] = -(w1sq + w2sq)
    A[3, 0] = -(w1sq * w2sq)
    return A


def growth_of(A):
    return np.linalg.eigvals(A).real.max()


def main():
    print("=" * 72)
    print("Arc-A: mode-level unfolding sweep (direction -> dynamics)")
    print("=" * 72)
    w = 1.0

    # ---- [1] family direction at finite omega -------------------------
    print("\n[1] FAMILY direction, omega=1: growth vs "
          "|Delta| sin(phi)/(2 omega):")
    worst = 0.0
    for phi in (0.0, np.pi / 6, np.pi / 2, np.pi * 5 / 6, np.pi):
        for d in (1e-3, 1e-2, 1e-1):
            A = pu_companion(w ** 2, w ** 2 + d * np.exp(1j * phi))
            gr = growth_of(A)
            pred = d * abs(np.sin(phi)) / (2 * w)
            err = abs(gr - pred) / max(pred, 1e-12)
            # exclude phi = 0, pi explicitly (float sin(pi) ~ 1e-16
            # would otherwise admit a roundoff-dominated junk term
            # into the worst statistic, contradicting the label)
            if abs(np.sin(phi)) > 1e-6:
                worst = max(worst, err)
            if d == 1e-2:
                print("  phi=%5.2f : growth %.6e   |D|sin(phi)/2w "
                      "%.6e" % (phi, gr, pred))
    print("  worst reldiff over grid (phi != 0, pi): %.1e" % worst)
    # phi = 0 control: secular window + cond = 2/delta
    print("  [ctrl] phi=0 (Stelle): growth at |D|=1e-2: %.1e "
          "(oscillatory)" % growth_of(pu_companion(1.0, 1.0 + 1e-2)))
    for d in (1e-2, 1e-3):
        A = pu_companion(1.0, 1.0 + d)
        _, V = np.linalg.eig(A)
        delta = d / 2  # frequency detuning ~ Delta/(2 w^2) * w
        print("  [ctrl] cond(S) = %.1f vs 2/delta = %.1f  (ratio "
              "%.3f)" % (np.linalg.cond(V), 2 / delta,
                         np.linalg.cond(V) * delta / 2))

    # ---- [2] generic direction at finite omega -------------------------
    print("\n[2] GENERIC direction, omega=1: growth vs "
          "sqrt(eps)|sin(phi/2)|:")
    worst = 0.0
    for phi in (0.0, np.pi / 3, np.pi / 2, np.pi):
        for eps in (1e-6, 1e-4, 1e-2):
            H = np.array([[w, 1.0],
                          [eps * np.exp(1j * phi), w]])
            gr = np.max((-1j * np.linalg.eigvals(H)).real)
            pred = np.sqrt(eps) * abs(np.sin(phi / 2))
            if pred > 0:
                worst = max(worst, abs(gr - pred) / pred)
        if phi > 0:
            print("  phi=%5.2f : growth(eps=1e-4) %.6e   pred %.6e"
                  % (phi, np.max((-1j * np.linalg.eigvals(
                      np.array([[w, 1.0],
                                [1e-4 * np.exp(1j * phi), w]])
                  )).real), np.sqrt(1e-4) * abs(np.sin(phi / 2))))
    print("  worst reldiff (phi != 0): %.1e" % worst)
    print("  Puiseux exponent check (phi=pi): growth ~ eps^p, "
          "p = %.4f (expect 0.5000)"
          % np.polyfit(np.log([1e-6, 1e-4, 1e-2]),
                       np.log([np.max((-1j * np.linalg.eigvals(
                           np.array([[w, 1.0], [-e, w]]))).real)
                           for e in (1e-6, 1e-4, 1e-2)]), 1)[0])
    # random-phase noise: growing with probability 1
    grs = []
    for _ in range(500):
        phi = rng.uniform(0, 2 * np.pi)
        H = np.array([[w, 1.0], [1e-8 * np.exp(1j * phi), w]])
        grs.append(np.max((-1j * np.linalg.eigvals(H)).real))
    ngrow = int(np.sum(np.array(grs) > 1e-12))
    print("  random-phase eps=1e-8 (500 draws): growing %d/%d "
          "(fraction %.3f), median rate %.1e (~sqrt(eps)=1e-4)"
          % (ngrow, len(grs), ngrow / len(grs), np.median(grs)))

    # ---- [3] the omega -> 0 corner (Ilhan-Kovner) ----------------------
    print("\n[3] omega -> 0 corner: growth = sqrt|Delta| |sin(phi/2)|;"
          " IK check:")
    worst = 0.0
    for phi in (0.0, np.pi / 2, np.pi):
        for d in (1e-4, 1e-2, 1.0):
            A = pu_companion(0.0, d * np.exp(1j * phi))
            gr = growth_of(A)
            pred = np.sqrt(d) * abs(np.sin(phi / 2))
            if pred > 0:
                worst = max(worst, abs(gr - pred) / pred)
    print("  worst reldiff (phi != 0): %.1e" % worst)
    for gb in (0.5, 1.0, 2.0):
        A = pu_companion(0.0, -0.75 * gb ** 2)   # IK: phi=pi
        print("  IK gamma_b=%.1f : frozen-mode growth %.6f   "
              "(sqrt(3)/2) gamma_b = %.6f" % (gb, growth_of(A),
                                              np.sqrt(3) / 2 * gb))
    # [3b] independent NONLINEAR check: integrate Ilhan-Kovner's
    # actual EOM gamma'' = (1/4) gamma (gamma.gamma) on the E=0
    # branch and reproduce their exact solution Eq.(58),
    # gamma_r(t) = gamma_0/(1 - gamma_0 t/2^{3/2}), and the
    # singularity time t_c = 2^{3/2}/gamma_0. (The frozen-mode rates
    # above are the map's own algebra; THIS is the independent
    # support from the nonlinear dynamics.)
    print("  [3b] nonlinear IK reproduction (solve_ivp, rtol 1e-12):")
    for g0 in (0.5, 1.0, 2.0):
        tc = 2 ** 1.5 / g0

        def rhs(t, y):
            g1, g2, p1, p2 = y
            r2 = g1 * g1 + g2 * g2
            return [p1, p2, 0.25 * g1 * r2, 0.25 * g2 * r2]

        ev = lambda t, y: np.hypot(y[0], y[1]) - 1e6
        ev.terminal = True
        sol = solve_ivp(rhs, [0, 1.2 * tc],
                        [g0, 0.0, g0 ** 2 / 2 ** 1.5, 0.0],
                        rtol=1e-12, atol=1e-13, events=ev,
                        dense_output=True)
        tb = sol.t_events[0][0]
        rel = max(abs(np.hypot(*sol.sol(t)[:2])
                      - g0 / (1 - g0 * t / 2 ** 1.5))
                  / (g0 / (1 - g0 * t / 2 ** 1.5))
                  for t in np.linspace(0.05 * tc, 0.9 * tc, 30))
        print("    gamma_0=%.1f : blowup t = %.6f vs t_c = %.6f ; "
              "max reldiff vs Eq.(58) %.1e" % (g0, tb, tc, rel))

    # ---- [4] the physics-facing map ------------------------------------
    print("\n[4] THE MAP (mode level, verified above):")
    print("  deformation          kind     phase        dynamics")
    print("  Einstein/Stelle m^2  family   phi=0        oscillatory;"
          " cost 2/delta")
    print("  Merlin width i*gam   family   arctan(g/m2) growth "
          "gamma/2w (Arc-E)")
    print("  IK self-interaction  corner   phi=pi       blowup, "
          "rate (sqrt3/2)gamma_b")
    print("  non-sympl.lat/mach   generic  random       growing "
          "w.p. 1; rate sqrt(eps)")
    print("  => the conformal point is the phase boundary; the")
    print("     oscillatory set is the family real axis, PUNCTURED")
    print("     at Delta = 0 (while omega_2^2 > 0), plus the generic")
    print("     positive-real ray only. Divisor image (THMs 1-4):")
    print("     real side, M1 recurs at pi/delta per bond; imaginary")
    print("     rays + EP, M1-free k=2 cascade, pure M2; mixed")
    print("     complex splits in the UPPER half-plane, M1 windows")
    print("     recur INDEFINITELY, paced by Re delta (the envelope")
    print("     sqrt(a^2+b^2) exceeds the decaying b*exp(-b t) for")
    print("     all t); only the LOWER-half wedges go transient")
    print("     and then silent.")
    print("done.")


if __name__ == "__main__":
    main()
