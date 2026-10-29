"""Arc-B d x d generalization of the cascade divisor theorem.

Results tested (algebra first, numerics adversarial):

 THM-1 (any d x d upper-triangular family): the divisor
   M = Gamma(T) Gamma(s)^{-1} is upper triangular with nonnegative
   diagonal, and per superdiagonal pair
     sign(M_{i,i+1}) = sign(r_i(T) - r_i(s)),
     r_i(t) = |U_{i,i+1}|^2 / |U_{ii}|^2
   (identical proof to 2x2: (A^{-1})_{i,i+1} = -A_{i,i+1}/(A_ii
   A_{i+1,i+1})).

 THM-2 (single Jordan block J_k, k >= 3): V(t) = |e^{-iJt}|^2 =
   f(t^2 N), f(x) = sum_m x^m/(m!)^2, N the nilpotent. Divisor
   = h(N), h = f(bx)/f(ax), a = s^2, b = T^2. Coefficients:
     c_1 = b - a                          (>= 0: THM-1, r = t^2)
     c_2 = b^2/4 - ab + 3a^2/4 = (b-a)(b-3a)/4
           NEGATIVE for 1 < b/a < 3  (i.e. s < T < sqrt(3) s)
     c_3 = b^3/36 - ab^2/4 + 3a^2 b/4 - 19a^3/36
           (measured POSITIVE on the whole tested range b/a in
           (1, 9]; an earlier hand-algebra claim of a negative
           window near b = 2a was an arithmetic slip, caught by
           check [3] -- the negativity of the k >= 3 cascade lives
           in the SECOND superdiagonal)
   Generator: L = V' V^{-1} = 2tN f'(t^2 N) f(t^2 N)^{-1}:
     L_{i,i+1} = 2t > 0,  L_{i,i+2} = -t^3 < 0.
   => the k >= 3 Jordan cascade is NOT M1-free: negativity lives in
   the second superdiagonal for every step ratio T/s < sqrt(3)
   (including all infinitesimal steps). "Pure conditional mass
   creation" is a strictly k = 2 phenomenon. (Paper 4 is scoped to
   the k=2 cell -- unaffected; paper 6 must state this.)

 THM-3 (detuned bidiagonal chain): the direction readout is
   PER BOND: bond i's first negativity onset is pi/delta_i,
   delta_i = w_i - w_{i+1} (each 2x2 sub-block carries the 2x2
   theorem independently).

ASCII only; numpy/scipy. Seconds.
"""

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(23)
TOL = 1e-9


def V_of(H, t):
    U = expm(-1j * H * t)
    return np.abs(U) ** 2


def divisor_raw(H, s, T):
    return V_of(H, T) @ np.linalg.inv(V_of(H, s))


def jordan(k, w=1.0):
    return w * np.eye(k) + np.diag(np.ones(k - 1), 1)


def main():
    print("=" * 72)
    print("Arc-B d x d: cascade divisor theorem, general dimension")
    print("=" * 72)

    # ---- [1] THM-1 adversarial ----------------------------------------
    print("\n[1] THM-1, random upper-triangular H, d = 3,4,5:")
    for d in (3, 4, 5):
        n, bad, worst_lower, worst_diag = 0, 0, 0.0, np.inf
        for _ in range(200):
            H = np.triu(rng.standard_normal((d, d))
                        + 1j * rng.standard_normal((d, d)))
            H -= 1j * np.diag(rng.uniform(0, 0.5, d))
            s, dt = rng.uniform(0.05, 4), rng.uniform(0.01, 0.8)
            Vs, VT = V_of(H, s), V_of(H, s + dt)
            if np.linalg.cond(Vs) > 1e8:
                continue
            M = VT @ np.linalg.inv(Vs)
            worst_lower = max(worst_lower,
                              np.abs(np.tril(M, -1)).max())
            worst_diag = min(worst_diag, np.diag(M).real.min())
            for i in range(d - 1):
                dr = VT[i, i + 1] / VT[i, i] - Vs[i, i + 1] / Vs[i, i]
                if abs(M[i, i + 1]) < TOL or abs(dr) < TOL:
                    continue
                n += 1
                bad += (np.sign(M[i, i + 1].real) != np.sign(dr))
        print("  d=%d : %d/%d sign matches; max lower-tri residual "
              "%.1e; min diagonal %+.1e" % (d, n - bad, n,
                                            worst_lower, worst_diag))

    # ---- [2] THM-2: c_2 window ----------------------------------------
    print("\n[2] THM-2, J_3: M_{1,3} vs c2 = (b-a)(b-3a)/4, s = 1:")
    H = jordan(3)
    errs, sgn_ok = [], True
    for T in (1.1, 1.3, np.sqrt(3) - 1e-3, np.sqrt(3) + 1e-3, 2.0, 2.5):
        a, b = 1.0, T ** 2
        c2 = (b - a) * (b - 3 * a) / 4
        m13 = divisor_raw(H, 1.0, T)[0, 2].real
        errs.append(abs(m13 - c2) / max(abs(c2), 1e-12))
        sgn_ok &= (np.sign(m13) == np.sign(c2)) or abs(c2) < 1e-6
        print("  T=%.4f : M_13 %+.6f   c2 %+.6f" % (T, m13, c2))
    print("  max reldiff %.1e ; window boundary sqrt(3) = 1.7320508: "
          "sign flips there: %s" % (max(errs), sgn_ok))
    # measured crossing
    Ts = np.arange(1.01, 2.2, 0.0005)
    m = [divisor_raw(H, 1.0, T)[0, 2].real for T in Ts]
    cross = Ts[np.argmax(np.array(m) > 0)]
    print("  measured sign crossing T = %.5f (sqrt(3) = %.5f)"
          % (cross, np.sqrt(3)))

    # ---- [3] c_3 for J_4 ------------------------------------------------
    print("\n[3] THM-2, J_4: M_{1,4} vs c3 closed form, s = 1:")
    H = jordan(4)
    err3 = 0.0
    for T in (1.05, 1.4, 1.8, 2.2, 3.0):
        a, b = 1.0, T ** 2
        c3 = b**3 / 36 - a * b**2 / 4 + 3 * a**2 * b / 4 \
            - 19 * a**3 / 36
        m14 = divisor_raw(H, 1.0, T)[0, 3].real
        err3 = max(err3, abs(m14 - c3) / max(abs(c3), 1e-12))
        print("  T=%.2f : M_14 %+.6f   c3 %+.6f" % (T, m14, c3))
    print("  max reldiff %.1e" % err3)

    # ---- [4] generator signs -------------------------------------------
    print("\n[4] generator L = V'V^{-1} at J_3 (finite difference, "
          "h=1e-6):")
    H = jordan(3)
    for t in (0.5, 1.0, 2.0):
        h = 1e-6
        L = (V_of(H, t + h) - V_of(H, t - h)) / (2 * h) \
            @ np.linalg.inv(V_of(H, t))
        print("  t=%.1f : L_12 = %+.6f (2t = %+.6f)   L_13 = %+.6f "
              "(-t^3 = %+.6f)" % (t, L[0, 1].real, 2 * t,
                                  L[0, 2].real, -t ** 3))

    # ---- [5] THM-3: per-bond onsets ------------------------------------
    print("\n[5] THM-3, detuned bidiagonal d=4 chain, per-bond "
          "pi/delta_i:")
    w = np.array([2.0, 1.4, 1.0, 0.2])   # delta = 0.6, 0.4, 0.8
    H = np.diag(w) + np.diag(np.ones(3), 1)
    dt = 0.02
    for i, D in enumerate(-np.diff(w)):
        onset = None
        for s in np.arange(0.05, 2.5 * np.pi / D, 0.01):
            Vs, VT = V_of(H, s), V_of(H, s + dt)
            q = VT[i, i + 1] * Vs[i, i] - VT[i, i] * Vs[i, i + 1]
            if q < -TOL * (abs(q) + 1):
                onset = s
                break
        print("  bond %d (delta=%.1f) : onset %.3f   pi/delta %.3f  "
              "ratio %.4f" % (i + 1, D, onset, np.pi / D,
                              onset / (np.pi / D)))

    print("\nconclusion: THM-1 (triangularity + per-bond sign law)")
    print("holds in all d; THM-2: pure mass creation is a k=2")
    print("phenomenon -- k>=3 Jordan cascades go negative in the")
    print("second superdiagonal for every step ratio T/s < sqrt(3)")
    print("(generator entry -t^3); THM-3: the unfolding-direction")
    print("readout is per bond.")
    print("done.")


if __name__ == "__main__":
    main()
