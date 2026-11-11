"""Recompute every numeric answer printed in the guide. Run: python scripts/verify.py
Prints PASS/FAIL per question id and exits 1 if anything fails."""
import math
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp
from scipy.stats import norm

results = []


def check(qid, got, expected, tol=2e-3, note=""):
    if isinstance(got, np.ndarray):
        got = list(got)
    if isinstance(got, (list, tuple)):
        ok = all(abs(float(g) - float(e)) <= tol * max(1, abs(float(e))) for g, e in zip(got, expected)) and len(got) == len(expected)
    else:
        ok = abs(float(got) - float(expected)) <= tol * max(1, abs(float(expected)))
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {qid:<14} got={got} expected={expected} {note}")


Q = norm.sf

# ---------------- U1 Bayes ----------------
pd_ = .4 * .02 + .35 * .04 + .25 * .05
check("jun26-1b", [pd_, .35 * .04 / pd_], [0.0345, 0.4058])
pb = (18 * .15 + 22 * .10 + 15 * .34) / 55
check("apr25-1a", [pb, 2.2 / 10], [0.1818, 0.22])
check("nov22-1a", .75 * .65 + .4 * .35, 0.6275)
check("apr24-1b", .0005 * .99 / (.0005 * .99 + .9995 * .01), 0.0472)
check("oct21-1a", .018 * .95 / (.018 * .95 + .982 * .03), 0.367)
check("apr24-1a", (math.exp(-.4) - math.exp(-.6)) / math.exp(-.4), 0.1813)
check("jan22-1a", .85 * .25 / (.8 * .75 + .85 * .25), 0.2615)
pa = .3 * .85 + .45 * .92 + .25 * .6
check("jan20-2", [pa, .15 / pa], [0.819, 0.1832])

# ---------------- U2 joint pdf ----------------
x, y, c, th, lam = sp.symbols("x y c theta lam", positive=True)
tri = sp.integrate(sp.integrate(c * x + 1, (x, 0, 1 - y)), (y, 0, 1))
check("apr25-1c", sp.solve(sp.Eq(tri, 1), c)[0], 3)
check("jun26-1c", sp.integrate(6 * x ** 2 * y, (y, 0, 1)).subs(x, .5), 3 * .5 ** 2, note="p_X(0.5)=3x^2")
check("apr24-1c", sp.integrate(2, (x, y, 1)).subs(y, .25), 2 * (1 - .25), note="p_Y(0.25)=2(1-y)")
check("nov22-1b", [F(1, 6) + F(1, 4) + F(1, 8), F(1, 8) + F(1, 6) + F(1, 6)], [13 / 24, 11 / 24])

# ---------------- U3 ----------------
check("oct21-1d", math.comb(8, 6) * .8 ** 6 * .2 ** 2, 0.2936)
u = sp.symbols("u")
check("apr24-1d", sp.integrate(sp.cos(1 + u) / (2 * sp.pi), (u, 0, 2 * sp.pi)), 0, note="mean of cos(t+U) at t=1")
xs = [1, 1, 1, 0]; ys = [1, 3, 3, 5]
rxy = {tau: sum(xs[n] * ys[n - tau] for n in range(4) if 0 <= n - tau < 4) / 4 for tau in range(-3, 3)}
check("nov19-1a", [rxy[t] for t in range(-3, 3)], [5 / 4, 8 / 4, 11 / 4, 7 / 4, 1, 1 / 4])

# ---------------- U4 factorisation ----------------
def factor(alpha, beta):
    """alpha + beta cos(theta) = C(1+a^2) + C a (z+1/z) with |a|<1 ; returns (a, C)"""
    b = abs(beta) / 2
    roots = np.roots([b, -alpha, b])
    a = min(roots, key=abs)
    return float(a), float(b / a)
a, C = factor(61, 60); check("apr25-1e", [a, 1 / C], [5 / 6, 1 / 36])
a, C = factor(25, -24); check("apr24-1e", [a, 7 / C], [3 / 4, 7 / 16])
a, C = factor(5 / 3, -1); check("nov22-1d", [a, 1 / C], [1 / 3, 2 / 3])
# jan22-1d check the printed factorisation reproduces the (corrected) PSD at theta=0 and pi
for t_, lab in [(0, "0"), (math.pi, "pi")]:
    lhs = (17 / 8 - math.cos(t_)) / (25 / 16 + 1.5 * math.cos(t_))
    rhs = 2 * abs(1 - .25 * np.exp(-1j * t_)) ** 2 / abs(1 + .75 * np.exp(-1j * t_)) ** 2
    check(f"jan22-1d@{lab}", rhs, lhs)

# ---------------- U5 MLE ----------------
k, n, S = sp.symbols("k n S", positive=True)
theta = sp.symbols("theta", positive=True)
ell = -S / theta - n * k * sp.log(theta)
check("jun26-2b", sp.solve(sp.diff(ell, theta), theta)[0].subs({S: 10, n: 5, k: 2}), 10 / (5 * 2), note="theta=S/(nk)")
xv = 3.0; th_hat = -math.log(4 * xv / 7 - 1)
lamf = lambda t: 1 / (1 + math.exp(-t))
d = lambda t: (1 - lamf(t)) * (1 - 4 / 7 * lamf(t) * xv)
check("apr25-2c", d(th_hat), 0, tol=1e-6, note="derivative zero at -ln(4x/7-1), x=3")
T = sp.symbols("T", positive=True)
ell = -n * sp.log(theta) - T / (2 * theta)
check("apr24-2c", sp.solve(sp.diff(ell, theta), theta)[0].subs({T: 10, n: 4}), 10 / 8, note="theta=T/(2N)")
ell = -2 * n * sp.log(theta) - T / (2 * theta ** 2)
check("nov19-3a", sp.solve(sp.diff(ell, theta), theta)[0].subs({T: 8, n: 4}), math.sqrt(8 / 8), note="sqrt(T/2N)")
check("jan19-2a", sp.solve(sp.diff(n * sp.log(lam) - lam * S, lam), lam)[0].subs({n: 2, S: 6}), 1 / 3)
x1, x2 = 1.0, 2.0
check("nov22-2d", math.atan2(x2, x1), math.atan(x2 / x1))

# ---------------- U6 MAP ----------------
check("jun26-2c", [sum([3, 5, 4, 6, 4]), 11 / 25, 10 / 22, 2 * 4 * 3 * 5 * 3], [22, 0.44, 0.4545, 360])
check("jun26-2d", [sum([2, 4, 3, 5, 2, 4]), 22 / 8, 20 / 6, math.prod(math.factorial(v) for v in [2, 4, 3, 5, 2, 4])], [20, 2.75, 3.3333, 1658880])
xv = 5.0; th_hat = -math.log(xv / 2 - 1)
d = lambda t: (1 - lamf(t)) * (1 - xv * lamf(t) / 2)
check("apr24-2d", d(th_hat), 0, tol=1e-6, note="derivative zero at -ln(x/2-1), x=5")
post = (x + 2) ** 2 * theta * sp.exp(-(x + 2) * theta)
check("nov22-2g", sp.solve(sp.diff(sp.log(post), theta), theta)[0].subs(x, 3), 1 / 5, note="1/(x+a), x=3,a=2")
yv, s2 = 0.7, 1.3
check("jan22-2h", math.exp(-(yv - 1) ** 2 / (2 * s2)) / math.exp(-(yv + 1) ** 2 / (2 * s2)), math.exp(2 * yv / s2), note="posterior ratio = e^{2y/s2}")

# ---------------- U7 MMSE ----------------
check("nov22-2f", sp.integrate(theta * post, (theta, 0, sp.oo)).subs(x, 3), 2 / 5, note="2/(x+a)")
check("jan22-2g", math.tanh(yv / s2), (math.exp(2 * yv / s2) - 1) / (math.exp(2 * yv / s2) + 1))
num = sp.integrate(lam ** 2 * sp.exp(-lam * x), (lam, 0, 2)); den = sp.integrate(lam * sp.exp(-lam * x), (lam, 0, 2))
mine = (2 - (4 * x ** 2 + 4 * x + 2) * sp.exp(-2 * x)) / (x * (1 - (2 * x + 1) * sp.exp(-2 * x)))
check("jan19-2b", (num / den).subs(x, 1.5), mine.subs(x, 1.5))
check("deck-2f", 0.75 * 1 + 0.25 * (-1), 0.5, note="x(2c-1) at x=1, c=3/4")

# ---------------- U8 CRLB ----------------
lp = sp.log(x) - 2 * sp.log(theta) - x ** 2 / (2 * theta ** 2)
d2 = sp.diff(lp, theta, 2)
Ex2 = sp.integrate(x ** 2 * x / theta ** 2 * sp.exp(-x ** 2 / (2 * theta ** 2)), (x, 0, sp.oo))
info = sp.simplify(-d2.subs(x ** 2, Ex2))
check("nov19-3b", (1 / (4 * info)).subs(theta, 2), 2 ** 2 / (4 * 4), note="CRLB theta^2/(4N), N=4")
check("nov22-2e", 2.0 ** 2 / 0.5, 8.0, note="A^2/sigma^2 with A=2, sigma^2=0.5")

# ---------------- U9 LS ----------------
pts = [(0, 3), (2, 4), (3, 3)]
H = np.array([[p[0], 1] for p in pts], float); yy = np.array([p[1] for p in pts], float)
ab = np.linalg.lstsq(H, yy, rcond=None)[0]
check("apr25-2b", ab, [1 / 14, 45 / 14])

# ---------------- U11 correlogram ----------------
corr = lambda r: (lambda t: r[0] + 2 * sum(r[k] * np.cos(k * t) for k in range(1, len(r))))
check("jun26-3c", [corr([3, 2, 1])(0), corr([3, 2, 1])(np.pi / 2), corr([3, 2, 1])(np.pi)], [9, 1, 1])
check("apr25-3d", [corr([2, -.25, -3 / 16])(0), corr([2, -.25, -3 / 16])(np.pi)], [1.125, 2.125])
check("apr24-3d", [corr([25 / 16, -.75, .5, -.5])(0), corr([25 / 16, -.75, .5, -.5])(np.pi)], [0.0625, 5.0625])
check("jan22-3c", [corr([13 / 8, -15 / 16, .25])(0), corr([13 / 8, -15 / 16, .25])(np.pi)], [13 / 8 - 15 / 8 + .5, 13 / 8 + 15 / 8 + .5])
check("nov19-2a", [corr([1, .7, .5, .3])(0), corr([1, .7, .5, .3])(np.pi)], [4, 0])
check("jan20-3a", [corr([1 / 21, 2 / 105])(0), corr([1 / 21, 2 / 105])(np.pi)], [9 / 105, 1 / 105])
check("oct21-3c", [corr([28 / 27, -4 / 27])(0)], [20 / 27])

# ---------------- U12 AR ----------------
def yw(r, p):
    R = np.array([[r[abs(i - j)] for j in range(p)] for i in range(p)], float)
    a = np.linalg.solve(R, -np.array(r[1:p + 1], float))
    s2 = r[0] + sum(a[i] * r[i + 1] for i in range(p))
    return list(a), s2
a, s2 = yw([3, 2, 1], 2); check("jun26-3d", a + [s2], [-0.8, 0.2, 1.6])
den = lambda a: (1 + sum(v ** 2 for v in a), 2 * (a[0] + a[0] * a[1]) if len(a) > 1 else 2 * a[0], 2 * a[1] if len(a) > 1 else 0)
check("jun26-3d-den", den([-0.8, 0.2]), [1.68, -1.92, 0.4])
a, s2 = yw([2, -.25, -3 / 16], 1); check("apr25-3e", a + [s2, 126 / 65, 126 / 49], [1 / 8, 63 / 32, 1.9385, 2.5714])
a, s2 = yw([25 / 16, -.75, .5], 2); check("apr24-3e", a + [s2], [204 / 481, -56 / 481, 9129 / 7696])
a, s2 = yw([1, -1 / 8], 1); check("nov22-3f", a + [s2], [1 / 8, 63 / 64])
a, s2 = yw([13 / 8, -15 / 16], 1); check("jan22-3d", a + [s2], [15 / 26, 451 / 416])
check("jan22-3d-psd", 5863 / (7208 + 6240), (451 / 416) / (901 / 676 + 15 / 13))
a, s2 = yw([1, .7, .5], 2); check("nov19-2b", a + [s2], [-0.6863, -0.0196, 0.5098])
a, s2 = yw([28 / 27, -4 / 27], 1); check("oct21-3b", a + [s2, 224 / 225], [1 / 7, 64 / 63, (64 / 63) / (50 / 49)])

# ---------------- U13 MA ----------------
def ma1(r0, r1):
    rho = r1 / r0
    b = min(np.roots([rho, -1, rho]), key=abs).real
    return b, r1 / b
b, s2 = ma1(2, -.25); check("apr25-3f", [b, s2, s2 * (1 + b ** 2)], [-4 + math.sqrt(15), 1.968, 2.0])
b, s2 = ma1(1, -1 / 8); check("nov22-3g", [b, s2], [-0.127, 0.984])
b, s2 = ma1(1 / 21, 2 / 105); check("jan20-3b", [b, s2], [0.5, 4 / 105])
bb = F(1, 4); aa = F(-15, 16) / (1 + bb); check("jan22-3b", [aa, bb, 1 + aa ** 2 + bb ** 2], [-0.75, 0.25, 13 / 8])

# ---------------- U14 model autocorrelation ----------------
bco = [1, -.5, .25, -.5]
r = [sum(bco[m] * bco[m + k] for m in range(len(bco) - k)) for k in range(4)]
check("apr24-3c", r, [25 / 16, -.75, .5, -.5])
# nov22-3e: ARMA(1,1) x = i - i1 + 3/4 x1, s2 = 7/8 : solve r0, r1
r0, r1 = sp.symbols("r0 r1")
s2v = sp.Rational(7, 8); a1 = sp.Rational(3, 4)
sol = sp.solve([sp.Eq(r0, 2 * s2v + a1 ** 2 * r0 - 2 * a1 * s2v), sp.Eq(r1, -s2v + a1 * r0)], [r0, r1])
check("nov22-3e", [sol[r0], sol[r1]], [1, -1 / 8])
check("nov22-3d", [28 * (1 - 1) / (25 - 24), 28 * 2 / 49], [0, 1.1429])
s2v = 1; a1 = sp.Rational(1, 2); b1 = sp.Rational(-2, 3)
sol = sp.solve([sp.Eq(r0, s2v * (1 + b1 ** 2) + a1 ** 2 * r0 + 2 * a1 * b1 * s2v), sp.Eq(r1, b1 * s2v + a1 * r0)], [r0, r1])
check("oct21-3a", [sol[r0], sol[r1]], [28 / 27, -4 / 27])

# ---------------- U15 ----------------
check("jun26-3b", [(1000 - 200) / 100 + 1, 1 / 9], [9, 0.1111])
check("apr25-3a", [1 / (1 - math.exp(-2))], [1.1565])
tt = sp.symbols("t", positive=True); Tb = sp.symbols("Tb", positive=True); A, w = sp.symbols("A w", positive=True)
P = sp.limit(sp.integrate((A * sp.sin(w * tt)) ** 2, (tt, -Tb / 2, Tb / 2)) / Tb, Tb, sp.oo)
check("apr25-3a-P", P.subs(A, 3), 9 / 2, note="A^2/2")
check("deck-energy", [float(sp.integrate(sp.exp(-2 * tt), (tt, 0, sp.oo))), 100, 25 / 2, 1 / 4], [0.5, 100, 12.5, 0.25])
check("apr25-3g", [corr([2, -.25, -3 / 16])(0), 126 / 81, 1.5], [1.125, 1.556, 1.5], note="values at 0 -> plot D")

# ---------------- U16 LRT ----------------
check("apr25-4a", 0.1 ** (1 / 6), 0.6813)
check("deck-4d", math.sqrt(8 / 3 * math.log(4)), 1.923)
check("nov22-4c", 3 * math.log(2) - math.log(1.5), 3 * math.log(2) - math.log(1.5), note="gamma' = N ln2 - ln gamma (symbolic)")
s0, s1 = 1.0, 2.0; eta = 1.0
L = lambda xx: (s0 ** 2 / s1 ** 2) * math.exp(xx ** 2 / 2 * (1 / s0 ** 2 - 1 / s1 ** 2))
gp = math.sqrt(2 * s0 ** 2 * s1 ** 2 / (s1 ** 2 - s0 ** 2) * math.log(eta * s1 ** 2 / s0 ** 2))
check("jun26-4b", L(gp), eta, tol=1e-6, note="L(gamma')=eta for s0=1,s1=2")

# ---------------- U17 PFA/PD ----------------
cq = math.log(4 / math.sqrt(2 * math.pi)); yth = (1 + math.sqrt(1 + 8 * cq)) / 2
check("apr24-4b", [yth, Q(yth), .5 * math.exp(-yth / 2), 2 * Q(yth), math.exp(-yth / 2)], [1.5884, 0.0561, 0.226, 0.1118, 0.4519])
check("jan22-4c", [2 * 0.0559, math.exp(-1.5884 / 2)], [0.1118, 0.4519])
check("nov22-4e", [-math.log(.9), 1 - .81], [0.1054, 0.19])
check("nov22-4e-pd", 1 - math.exp(-2 * -math.log(.9)), 0.19)
xth = math.log(20) / 1.9
check("jan20-5a", [xth, 1 - math.exp(-2 * xth), 1 - math.exp(-.1 * xth)], [1.5767, 0.957, 0.146])
xth_b = -math.log(.9) / .1; l1 = -math.log(.1) / xth_b
check("jan20-5b", [xth_b, l1], [1.0536, 2.1855])
check("jan20-5c", [1 - math.exp(-l1 * math.log(2) / .1), 1 - math.exp(-l1 * math.log(10) / .1)], [1.0, 1.0])
check("nov19-4b", [2 * (.5 - .341 - .136 - .021), 2 * (.5 - .341)], [0.004, 0.318])
erf = {-3: -.997, -2: -.954, -1: -.683, 0: 0, 1: .683, 2: .954, 3: .997}
tab = [(-1, 1), (-1, 2), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
pd_list = [.5 * (1 - erf[t - m]) for t, m in tab]; pfa_list = [.5 * (1 - erf[t]) for t, m in tab]
check("oct21-4a-pd", pd_list, [.977, .9985, .8415, .977, .5, .8415, .1585, .5, .023, .1585])
check("oct21-4a-pfa", pfa_list, [.8415, .8415, .5, .5, .1585, .1585, .023, .023, .0015, .0015])
check("jan19-3b", [.5 * (1 - erf[0]), .5 * (1 - erf[-2]), .5 * (1 - erf[-1]), .5 * (1 - erf[-1]), .5 * (1 - erf[1]), .5 * (1 - erf[2])],
      [.5, .977, .8415, .8415, .1585, .023])
check("u17-tiny", [1 - math.exp(-1), 1 - math.exp(-2), 1 - math.exp(-.5)], [0.6321, 0.8647, 0.3935])

# ---------------- U18 Bayesian detector ----------------
check("nov22-4f", math.log(3), 1.0986)
check("nov22-4g", [1 - 1 / 3, 1 / 9, .4 * 2 / 3 + .6 / 9], [2 / 3, 1 / 9, 1 / 3])
check("apr25-4c", [1 / 100, 5 >= 0.01], [0.01, 1])
check("jun26-4c", .9 / .1, 9)
check("u18-tiny", [math.log(3), math.log(2)], [1.0986, 0.6931])

# ---------------- maths page ----------------
check("M4", 1 / (1 - .25), 4 / 3)
check("M9", [2 / 3, 1 / 9], [float(sp.integrate(sp.exp(-y), (y, 0, sp.log(3)))), float(sp.integrate(2 * sp.exp(-2 * y), (y, sp.log(3), sp.oo)))])
check("M8", sorted(np.roots([30, -61, 30])), [5 / 6, 1.2])

n_fail = results.count(False)
print(f"\n{len(results) - n_fail}/{len(results)} PASS")
sys.exit(1 if n_fail else 0)
