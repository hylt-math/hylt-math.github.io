"""Round L checks: regular-type (type 1) examples M -> X with symplectic fibres.
(1) invariant-form model of the L_0-complex  Lambda(F^* + N)  for flat symplectic T^2-bundles over a
    complex torus (Kodaira-Thurston: monodromy shear; Bieberbach: monodromy -1), compared with the
    Leray prediction  P(t) = (1+t) * sum_j t^j * sum_a t^a h^a(X, V^j (x) G).
(2) graded Riemann-Roch polynomials for X=P^1, Y=T^2 or S^2 and the Euler-characteristic identity.
Everything exact (sympy rationals)."""
import itertools
from fractions import Fraction as R

def frank(M):
    M=[row[:] for row in M]; r=0
    if not M: return 0
    rows,cols=len(M),len(M[0])
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i][c]!=0: piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        for i in range(rows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]/M[r][c]
                M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        r+=1
        if r==rows: break
    return r

class P:
    # tiny polynomial class: dict exponent->coeff
    def __init__(s,d): s.d={k:v for k,v in d.items() if v!=0}
    def __add__(s,o):
        d=dict(s.d)
        for k,v in o.d.items(): d[k]=d.get(k,0)+v
        return P(d)
    def __mul__(s,o):
        if not isinstance(o,P): o=P({0:o})
        d={}
        for a,x in s.d.items():
            for b,y in o.d.items(): d[a+b]=d.get(a+b,0)+x*y
        return P(d)
    __rmul__=__mul__
    def ev(s,x): return sum(v*x**k for k,v in s.d.items())
    def __eq__(s,o): return s.d==o.d
    def __repr__(s): return ' + '.join(f"{v}t^{k}" for k,v in sorted(s.d.items())) or '0'
T=P({1:1}); ONE=P({0:1})
def lie_algebra_cohomology(n, brackets, extra_free=0):
    """Chevalley-Eilenberg complex of a Lie algebra with basis e_0..e_{n-1}, brackets {(i,j):{k:c}}
    ([e_i,e_j]=sum c e_k), tensored with an exterior algebra on `extra_free` abelian generators
    (the N-part, with trivial differential). Returns list of Betti numbers (complex, dims over Q)."""
    N = n + extra_free
    # d on dual basis: d e^k = - sum_{i<j} c_{ij}^k e^i e^j ; extra generators closed
    dgen = {k: {} for k in range(N)}
    for (i, j), v in brackets.items():
        for k, c in v.items():
            dgen[k][(i, j)] = dgen[k].get((i, j), 0) - c
    subsets = {p: list(itertools.combinations(range(N), p)) for p in range(N + 1)}
    idx = {p: {s: a for a, s in enumerate(subsets[p])} for p in subsets}
    def wedge_sorted(lst):
        # sign and sorted tuple of a list of generators (zero if repeat)
        if len(set(lst)) < len(lst): return 0, None
        sign = 1; l = list(lst)
        for a in range(len(l)):
            for b in range(len(l) - 1 - a):
                if l[b] > l[b + 1]:
                    l[b], l[b + 1] = l[b + 1], l[b]; sign = -sign
        return sign, tuple(l)
    mats = {}
    for p in range(N):
        M = [[R(0)]*len(subsets[p]) for _ in range(len(subsets[p + 1]))]
        for col, s in enumerate(subsets[p]):
            # d(e^{s0}...e^{s_{p-1}}) = sum_a (-1)^a e^{s0}..d(e^{s_a})..
            for a, g in enumerate(s):
                for (i, j), c in dgen[g].items():
                    lst = list(s[:a]) + [i, j] + list(s[a + 1:])
                    sg, t = wedge_sorted(lst)
                    if sg == 0: continue
                    M[idx[p + 1][t]][col] += (-1) ** a * sg * c
        mats[p] = M
    ranks = {p: frank(mats[p]) for p in range(N)}
    ranks[-1] = 0; ranks[N] = 0
    return [len(subsets[p]) - ranks[p] - ranks[p - 1] for p in range(N + 1)]

def poly(b): return P({k:c for k,c in enumerate(b)})

t = T
print("== (1a) Kodaira-Thurston type-1 GC structure: F = <X1,X2,W>, [X2,W] = -1/2 X1 ; N = <d_z> (abelian, trivial action)")
b = lie_algebra_cohomology(3, {(1, 2): {0: R(-1, 2)}}, extra_free=1)
print("invariant-model Betti numbers:", b, " P(t)=", poly(b))
# Leray/E_2 prediction: X elliptic, G=O, V^0=V^2=O, V^1 = Atiyah bundle F_2 (h^0=h^1=1)
h = {0: (1, 1), 1: (1, 1), 2: (1, 1)}   # (h^0,h^1) of V^j (x) O
pred = (ONE + t) * sum((P({j:1}) * (P({0:h[j][0]}) + P({1:h[j][1]})) for j in range(3)), P({}))
print("Leray E_2 prediction:", pred, "-> match:", pred == poly(b))

print("== (1b) Bieberbach type: (T^2 x E)/Z_2, (y,x)->(-y,x+tau/2); V^1 = L_{-1}+L_{-1}, acyclic when G=O")
# invariants of abelian algebra <dy1,dy2,dzbar,dz-part> under y -> -y  (even number of dy's)
gens = ['y1', 'y2', 'zb', 'zN']
cnt = {}
for r in range(5):
    for s in itertools.combinations(range(4), r):
        if sum(1 for g in s if g in (0, 1)) % 2 == 0:
            cnt[r] = cnt.get(r, 0) + 1
b2 = [cnt.get(r, 0) for r in range(5)]
pred2 = (ONE + t) * sum((P({j:1}) * (P({0:h2[0]}) + P({1:h2[1]})) for j, h2 in {0: (1, 1), 1: (0, 0), 2: (1, 1)}.items()), P({}))
print("invariant Betti numbers:", b2, " Leray prediction:", pred2, "match:", pred2 == poly(b2))

print("== (2) graded Riemann-Roch (m >= m0): X=P^1, G=O(m); T_X = O(2); P(t) = P_Y(t) * ((m+1) + (m+3) t)")
PY = {'T2': P({0:1,1:2,2:1}), 'S2': P({0:1,2:1})}
for name, py in PY.items():
    for m in (0, 1, 2, 5):
        Pm = py * (P({0:m+1}) + P({1:m+3}))
        chi = Pm.ev(-1); chiY = py.ev(-1)
        print(name, "m=", m, "P=", Pm, " P(-1)=", chi, " = -2*chi(Y)?", chi == -2 * chiY)
print("== (2b) X elliptic (T_X = O), deg G = d>0, V^1 flat rank 2, T^2 fibres: P = d(1+t)^3 :", [ (ONE+T)*(P({0:dd,1:2*dd,2:dd})) == P({0:dd,1:3*dd,2:3*dd,3:dd}) for dd in (1,2,5)])
