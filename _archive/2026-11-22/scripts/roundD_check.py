# Round D checks.
# (1) HRR-based Euler characteristic: sum_b (-1)^b chi(P^n, wedge^b T (x) O(m)) == (-1)^n * (n+1)   (rk E=1, chi(P^n)=n+1)
#     using chi(Omega^p(k)) recursion from the Euler sequence 0->Omega^p->wedge^p O(-1)^{n+1}->Omega^{p-1}->0.
# (2) Theorem T (toric, generic sigma, no r_i = 1):  P_HH = [rho in M and all r_i <= 0](1+t)^n + (#vertices) t^n,
#     compared with the closed weight criterion crit_poly (random large A mod 2^61-1), all fans in toric_crit.FANS with n=2 and n=4.
import sys, itertools
sys.path.insert(0, '.')
from math import comb
from fractions import Fraction as Fr

def chi_O(n, k):            # chi(P^n, O(k)) = C(k+n, n) as a polynomial in k
    num = 1
    for j in range(1, n + 1):
        num *= (k + j)
    den = 1
    for j in range(1, n + 1):
        den *= j
    return num // den

def chi_Omega(n, p, k):
    if p < 0: return 0
    if p == 0: return chi_O(n, k)
    return comb(n + 1, p) * chi_O(n, k - p) - chi_Omega(n, p - 1, k)

def euler_total(n, m):
    # wedge^b T = Omega^{n-b} (n+1)  (since K^{-1}=O(n+1))
    return sum((-1) ** b * chi_Omega(n, n - b, m + n + 1) for b in range(n + 1))

ok = True
for n in range(1, 7):
    for m in range(-12, 13):
        if euler_total(n, m) != (-1) ** n * (n + 1):
            ok = False; print("EULER FAIL", n, m, euler_total(n, m))
print("(1) total Euler characteristic == (-1)^n chi(P^n) for n=1..6, m=-12..12:", ok)

# products via multiplicativity of both sides: wedge^•T of product is the tensor product; chi multiplicative
# (verified implicitly: sum_b (-1)^b chi(wedge^b T (x) L) is multiplicative under products with L=L1 [x] L2).

# (2) Theorem T check
from toric_crit import FANS, crit_poly, weights, rk_of, randA
from toric_hh import P

def vertices(rays, a, box):
    n = len(rays[0]); return sum(1 for chi, C in weights(rays, a, box) if rk_of(C, n) == n)

def avec(name, ms):
    rays = FANS[name]; a = [0] * len(rays)
    if name == 'P2': a[2] = ms[0]
    if name == 'P1xP1': a[1] = ms[0]; a[3] = ms[1]
    if name == 'P4': a[4] = ms[0]
    if name == 'P2xP2': a[2] = ms[0]; a[5] = ms[1]
    if name == 'P1^4':
        for k in range(4): a[2 * k + 1] = ms[k]
    return a

tests = [('P2', (1,)), ('P2', (2,)), ('P2', (3,)), ('P1xP1', (1, 1)), ('P1xP1', (1, 2)), ('P1xP1', (2, 3)),
         ('P4', (1,)), ('P2xP2', (1, 1)), ('P1^4', (1, 1, 1, 1))]
tot = bad = 0
for name, ms in tests:
    rays = FANS[name]; n = len(rays[0]); a = avec(name, ms); box = max(a) + n + 3
    V = vertices(rays, a, box)
    for seed in (7, 8):
        A = randA(n, seed, 10 ** 9)
        grid = list(itertools.product(range(-2, 3), repeat=n)) if n == 2 else list(itertools.product(range(-1, 2), repeat=n))
        grid = [tuple(Fr(x) for x in g) for g in grid] + [tuple(Fr(1, 3) if i == 0 else Fr(0) for i in range(n))]
        for rho in grid:
            r = [sum(rho[j] * rays[i][j] for j in range(n)) - a[i] for i in range(len(rays))]
            if any(x == 1 for x in r):
                continue
            pred = [0] * (n + 1)
            if all(x.denominator == 1 for x in rho) and all(x <= 0 for x in r):
                pred = [comb(n, b) for b in range(n + 1)]
            pred[n] += V
            got = crit_poly(rays, a, A, rho, box)
            tot += 1
            if got != pred:
                bad += 1; print("MISMATCH", name, ms, rho, got, pred)
    print(name, ms, "V =", V, "running mismatches", bad, "of", tot, flush=True)
print("(2) Theorem T: mismatches", bad, "of", tot)
