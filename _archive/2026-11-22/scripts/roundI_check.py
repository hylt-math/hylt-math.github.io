# Round I check: intrinsic obstruction criterion for extra (non-generic) classes in the toric weight formula.
# For a subset S of rays (independent, 0<|S|<n) call S "solvable" if there is x in C^n and y in C^S with
#     <x,u_i> = r_i - 1 (i in S),   A x = sum_{i in S} y_i u_i       (i.e. A x in W_S).
# Claim tested (necessary direction): if NO S is solvable, then HH Poincare polynomial == generic prediction
# (vertex classes + weight -rho).  Also report 'false alarms' (S solvable but no change) and 'hits'.
import sys, random, itertools
sys.path.insert(0, '.')
from toric_hh import P, modfrac, rank
from toric_crit import FANS, crit_poly, generic_pred, rk_of, randA
from fractions import Fraction as Fr

def solvable(rays, a, A, rho, S):
    n = len(rays[0]); s = len(S)
    # unknowns: x_1..x_n, y_1..y_s  (n+s unknowns); equations: n + s
    rows = []; rhs = []
    for k in range(n):
        row = [A[k][j] % P for j in range(n)] + [(-rays[S[t]][k]) % P for t in range(s)]
        rows.append(row); rhs.append(0)
    for t in range(s):
        u = rays[S[t]]
        r_i = sum(Fr(u[j]) * Fr(rho[j]) for j in range(n)) - a[S[t]]
        row = [u[j] % P for j in range(n)] + [0] * s
        rows.append(row); rhs.append(modfrac(r_i - 1))
    M = rows; Mb = [rows[i] + [rhs[i]] for i in range(len(rows))]
    return rank(M, n + s) == rank(Mb, n + s + 1)

def flag(rays, a, A, rho):
    n = len(rays[0]); bad = []
    for s in range(1, n):
        for S in itertools.combinations(range(len(rays)), s):
            if rk_of([rays[i] for i in S], n) != s: continue
            if solvable(rays, a, A, rho, list(S)): bad.append(S)
    return bad

def block_A(n, blocks, seed, big=10**9):
    r = random.Random(seed); A = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(b):
            for j in range(i + 1, b):
                x = r.randint(1, big); A[off + i][off + j] = x; A[off + j][off + i] = -x
        off += b
    return A

if __name__ == "__main__":
    rnd = random.Random(5)
    stats = dict(nosolv_ok=0, nosolv_bad=0, solv_diff=0, solv_same=0)
    setups = [('P2xP2', [2, 2], 1), ('P1^4', None, 1), ('P4', None, 1), ('P2', None, 2), ('P1xP1', None, 1)]
    for name, blocks, m in setups:
        rays = FANS[name]; n = len(rays[0]); a = [0] * len(rays)
        if name == 'P2': a[2] = m
        if name == 'P1xP1': a[1] = m; a[3] = m
        if name == 'P4': a[4] = m
        if name == 'P2xP2': a[2] = m; a[5] = m
        if name == 'P1^4': a[1] = m; a[3] = m; a[5] = m; a[7] = m
        box = max(a) + n + 2 if n == 4 else max(a) + n + 4
        cases = []
        for t in range(6):
            cases.append(('generic', randA(n, rnd.randint(0, 10**6), 10**9)))
        if name == 'P2xP2': cases.append(('block22', block_A(4, [2, 2], 3)))
        if name == 'P1^4':
            cases.append(('block2+2', block_A(4, [2, 2], 4)))
        if name in ('P4',): cases.append(('smallint', randA(n, 7, 2)))
        for tag, A in cases:
            if rk_of(A, n) != n: continue
            for rho in [[Fr(0)] * n, [Fr(-1)] * n, [Fr(1, 3)] * n, [Fr(-1), Fr(-1)] + [Fr(0)] * (n - 2),
                        [Fr(1), Fr(0)] + [Fr(0)] * (n - 2)]:
                act = crit_poly(rays, a, A, rho, box); gen = generic_pred(rays, a, rho, box)
                fl = flag(rays, a, A, rho)
                if not fl:
                    if act == gen: stats['nosolv_ok'] += 1
                    else: stats['nosolv_bad'] += 1; print('VIOLATION', name, tag, rho, act, gen)
                else:
                    if act != gen: stats['solv_diff'] += 1; print('hit', name, tag, [float(x) for x in rho], 'S=', fl[:3], 'act', act, 'gen', gen)
                    else: stats['solv_same'] += 1
    print(stats)
