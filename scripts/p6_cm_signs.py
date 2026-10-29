"""Arc-B: the general c_m sign pattern of the Jordan-cascade divisor.

Objects. V(t) = |e^{-iJ_k t}|^2 = f(t^2 N), f(x) = sum x^m/(m!)^2
= I_0(2 sqrt(x)). Divisor D = V(T)V(s)^{-1} = h(N),
h(x) = f(rho x)/f(x) after scaling, rho = T^2/s^2 >= 1.
c_m(rho) = m-th Taylor coefficient of h = the m-th superdiagonal of
the divisor (in units of s^{2m}).

RESULT 1 (PROVEN -- generator alternation). I_0(2 sqrt(x)) is entire
of order 1/2 with all zeros on the negative axis at x_n =
-j_{0,n}^2/4 (j_{0,n} = zeros of J_0). Hadamard:
f(x) = prod_n (1 + 4x/j_n^2), so
  f'/f (x) = sum_n 1/(x + j_n^2/4),
each term a simple pole with weight 1 on the negative axis. Taylor
coefficients: [f'/f]_m = (-1)^m 4^{m+1} sigma_{m+1}, sigma_p =
sum_n j_n^{-2p} (the classical RAYLEIGH SUMS -- exact rationals:
sigma_1 = 1/4, sigma_2 = 1/32, sigma_3 = 1/192, sigma_4 = 11/12288,
...). Hence the divisor generator L = V'V^{-1} = 2tN f'/f(t^2 N)
has entries
  L_{i, i+1+m} = 2 (-1)^m 4^{m+1} sigma_{m+1} t^{2m+1}:
STRICTLY ALTERNATING SIGNS at every depth, for every t. Negativity
at even depths (2nd, 4th, ... superdiagonal) is unavoidable for
k >= 3: mass-creation purity is k = 2 only, now with the exact
coefficient law. Checks [3]: exact series coefficients vs numerical
Rayleigh sums from scipy jn_zeros.

RESULT 2 (dominant-pole sign law, verified numerically). h(x) has
poles only at x_n = -j_n^2/4 (independent of rho); the residue at
x_1 carries the factor J_0(j_1 sqrt(rho)). For large m,
  c_m(rho) ~ (-1)^m J_0(j_1 sqrt(rho)) * [j_1/(2 J_1(j_1))]
             * (4/j_1^2)^{m+1},
so   sign(c_m) -> (-1)^m sign(J_0(j_1 sqrt(rho)))   and
     c_{m+1}/c_m -> -4/j_1^2 = -0.691660...
The finite-m negative windows converge to the FOURIER-BESSEL BANDS:
even m: J_0(j_1 sqrt(rho)) < 0 <=> rho in (1, (j_2/j_1)^2) union
((j_3/j_1)^2, (j_4/j_1)^2) ... = (1, 5.269) u (12.949, 24.042) ...;
odd m: the complementary bands. (Consistent with the measured
windows: c_2 in (1,3), c_4 in (1,4.78) -- marching toward 5.269;
c_3 none, c_5 in (5.406, 7.240) inside the odd band.)
Checks [4],[5].

All series arithmetic in exact rationals (Fractions); floats only
for roots, expm cross-checks, and Bessel sums.
"""

from fractions import Fraction
import math

import numpy as np
from scipy.linalg import expm
from scipy.special import jn_zeros, j0

M_MAX = 12


def series():
    f = [Fraction(1, math.factorial(m) ** 2) for m in range(M_MAX + 2)]
    fp = [Fraction(1, math.factorial(m) * math.factorial(m + 1))
          for m in range(M_MAX + 2)]
    g = [Fraction(1)]
    for n in range(1, M_MAX + 2):
        g.append(-sum(f[k] * g[n - k] for k in range(1, n + 1)))
    return f, fp, g


def c_poly(m, f, g):
    """Exact coefficients (in rho^j) of c_m(rho)."""
    return [f[j] * g[m - j] for j in range(m + 1)]


def main():
    f, fp, g = series()
    print("=" * 72)
    print("Arc-B: general c_m sign pattern (exact rationals + "
          "adversarial floats)")
    print("=" * 72)

    # ---- [1] exact polynomials, negative windows on rho > 1 ----------
    print("\n[1] negative windows of c_m(rho), rho > 1 (exact "
          "coefficients, numpy roots):")
    windows = {}
    for m in range(2, M_MAX + 1):
        coef = c_poly(m, f, g)
        # numpy wants highest power first
        r = np.roots([float(c) for c in coef[::-1]])
        rr = sorted(x.real for x in r
                    if abs(x.imag) < 1e-8 and x.real > 1 + 1e-9)
        # sample signs between the roots to identify windows
        pts = [1.0] + rr + [max(rr, default=1.0) * 1.5 + 2]
        neg = []
        for lo, hi in zip(pts[:-1], pts[1:]):
            mid = (lo + hi) / 2
            val = sum(float(coef[j]) * mid ** j for j in range(m + 1))
            if val < 0:
                neg.append((lo, hi))
        windows[m] = neg
        print("  m=%2d : %s" % (m, "  ".join("(%.3f, %.3f)" % w
                                             for w in neg) or "none"))

    # ---- [2] cross-check vs direct expm divisor ----------------------
    print("\n[2] c_m(rho) vs expm divisor of J_13 (s=1, worst "
          "reldiff over m=1..12):")
    k = M_MAX + 1
    J = np.eye(k) + np.diag(np.ones(k - 1), 1)
    for rho in (2.0, 6.0, 14.0):
        T = np.sqrt(rho)
        V1 = np.abs(expm(-1j * J * 1.0)) ** 2
        VT = np.abs(expm(-1j * J * T)) ** 2
        D = VT @ np.linalg.inv(V1)
        worst = 0.0
        for m in range(1, M_MAX + 1):
            exact = sum(float(x) * rho ** jj
                        for jj, x in enumerate(c_poly(m, f, g)))
            worst = max(worst, abs(D[0, m].real - exact)
                        / max(abs(exact), 1e-12))
        print("  rho=%.0f : worst reldiff %.1e" % (rho, worst))

    # ---- [3] generator = alternating Rayleigh sums (PROVEN) -----------
    print("\n[3] generator law l_m = (-1)^m 4^(m+1) sigma_(m+1), "
          "sigma_p = sum j_n^(-2p):")
    l = [sum(fp[j] * g[m - j] for j in range(m + 1))
         for m in range(M_MAX + 1)]
    zs = jn_zeros(0, 200000)
    ok = True
    for m in range(0, 8):
        sig = np.sum(zs ** (-2.0 * (m + 1)))
        if m == 0:   # sigma_1: slow tail, add integral correction
            sig += 1.0 / (np.pi ** 2 * (len(zs) - 0.25))
        pred = (-1) ** m * 4 ** (m + 1) * sig
        ok &= abs(float(l[m]) - pred) / abs(pred) < 1e-6
        print("  m=%d : exact %-12s  Rayleigh %.10f  (reldiff %.1e)"
              % (m, str(l[m]), pred,
                 abs(float(l[m]) - pred) / abs(pred)))
    print("  strict alternation (proven via Hadamard/Stieltjes): %s"
          % all((-1) ** m * float(l[m]) > 0 for m in range(M_MAX + 1)))

    # ---- [4] dominant-pole asymptotics --------------------------------
    print("\n[4] dominant-pole law, ratio c_(m+1)/c_m -> -4/j_1^2 = "
          "%.6f:" % (-4 / jn_zeros(0, 1)[0] ** 2))
    j1 = jn_zeros(0, 1)[0]
    for rho in (2.0, 6.0, 14.0):
        cs = [sum(float(x) * rho ** jj
                  for jj, x in enumerate(c_poly(m, f, g)))
              for m in range(M_MAX + 1)]
        ratios = [cs[m + 1] / cs[m] for m in (9, 10, 11)]
        sgn_pred = np.sign(j0(j1 * np.sqrt(rho)))
        sgn_ok = all(np.sign(cs[m]) == (-1) ** m * sgn_pred
                     for m in (10, 11, 12))
        print("  rho=%4.0f : ratios %.4f %.4f %.4f ; sign law at "
              "m=10..12: %s (J0(j1 sqrt(rho)) = %+.3f)"
              % (rho, *ratios, sgn_ok, j0(j1 * np.sqrt(rho))))

    # ---- [5] window edges -> Fourier-Bessel bands ---------------------
    print("\n[5] window edges vs Bessel bands (j_n/j_1)^2 = "
          "%.3f, %.3f, %.3f:" % tuple((jn_zeros(0, 4)[1:] / j1) ** 2))
    for m in (2, 4, 6, 8, 10, 12):
        e = windows[m][0][1] if windows[m] else float("nan")
        print("  even m=%2d : first window right edge %.4f "
              "(-> 5.269)" % (m, e))
    for m in (3, 5, 7, 9, 11):
        w = windows[m]
        print("  odd  m=%2d : windows %s (-> (5.269, 12.949))"
              % (m, "  ".join("(%.3f, %.3f)" % x for x in w)
                 or "none"))

    print("\nconclusion: the deep-cascade divisor's sign structure is")
    print("Bessel-zero arithmetic -- generator: exact alternating")
    print("Rayleigh law (proven); finite steps: Fourier-Bessel bands")
    print("with edges -> (j_n/j_1)^2. Negativity is unavoidable at")
    print("depth >= 2; mass-creation purity is k = 2 only.")
    print("done.")


if __name__ == "__main__":
    main()
