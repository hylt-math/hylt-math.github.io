from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
# ---- multivariate polynomials in N variables, truncated at total degree D ----
class P:
    def __init__(s, d=None, N=4, D=4):
        s.N=N; s.D=D; s.d={k:v for k,v in (d or {}).items() if v!=0 and sum(k)<=D}
    @staticmethod
    def const(c,N=4,D=4): return P({(0,)*N:F(c)},N,D)
    @staticmethod
    def var(i,N=4,D=4):
        e=[0]*N; e[i]=1; return P({tuple(e):F(1)},N,D)
    def __add__(a,b):
        if not isinstance(b,P): b=P.const(b,a.N,a.D)
        r=dict(a.d)
        for k,v in b.d.items(): r[k]=r.get(k,0)+v
        return P(r,a.N,a.D)
    __radd__=__add__
    def __neg__(a): return P({k:-v for k,v in a.d.items()},a.N,a.D)
    def __sub__(a,b): return a+(-b if isinstance(b,P) else -F(b))
    def __rsub__(a,b): return (-a)+b
    def __mul__(a,b):
        if not isinstance(b,P): return P({k:v*F(b) for k,v in a.d.items()},a.N,a.D)
        r={}
        for k1,v1 in a.d.items():
            for k2,v2 in b.d.items():
                k=tuple(x+y for x,y in zip(k1,k2))
                if sum(k)<=a.D: r[k]=r.get(k,0)+v1*v2
        return P(r,a.N,a.D)
    __rmul__=__mul__
    def __pow__(a,n):
        r=P.const(1,a.N,a.D)
        for _ in range(n): r=r*a
        return r
    def deg(a,k): return P({m:v for m,v in a.d.items() if sum(m)==k},a.N,a.D)
    def iszero(a): return not a.d
def series_sub(coeffs, x, N=4, D=4):
    """sum coeffs[k] x^k, x a P with no constant term"""
    r=P.const(0,N,D); xp=P.const(1,N,D)
    for k,c in enumerate(coeffs):
        if k>D: break
        r=r+xp*c; xp=xp*x
    return r
def expser(D): return [F(1,factorial(k)) for k in range(D+1)]
def todd_coeffs(D):
    # x/(1-e^{-x}) = 1/(sum_{k>=0} (-1)^k x^k/(k+1)!)
    den=[F((-1)**k, factorial(k+1)) for k in range(D+1)]
    inv=[F(0)]*(D+1); inv[0]=F(1)
    for n in range(1,D+1):
        inv[n]=-sum(den[k]*inv[n-k] for k in range(1,n+1))
    return inv
def to_elem(p, N=4):
    """express symmetric P in elementary symmetric e1..eN; returns dict exps->coef"""
    p=P(dict(p.d),p.N,p.D); out={}
    es=[None]+[elem(i,N,p.D) for i in range(1,N+1)]
    while p.d:
        m=max(p.d.keys()); c=p.d[m]
        assert all(m[i]>=m[i+1] for i in range(N-1)), "not symmetric?"
        ex=tuple(m[i]-(m[i+1] if i+1<N else 0) for i in range(N))
        out[ex]=c
        t=P.const(1,N,p.D)
        for i,e in enumerate(ex): t=t*(es[i+1]**e)
        p=p-t*c
    return out
def elem(k,N=4,D=4):
    r=P.const(0,N,D)
    for S in combinations(range(N),k):
        t=P.const(1,N,D)
        for i in S: t=t*P.var(i,N,D)
        r=r+t
    return r
def show(d):
    names=['c1','c2','c3','c4']
    terms=[]
    for ex,c in sorted(d.items()):
        s='*'.join(f"{names[i]}^{e}" if e>1 else names[i] for i,e in enumerate(ex) if e)
        terms.append(f"({c})*{s}" if s else f"({c})")
    return ' + '.join(terms)
# ---- truncated one-variable series in H (H^{n+1}=0), coefficients Fractions ----
def smul(a,b,n):
    r=[F(0)]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n: r[i+j]+=x*y
    return r
def spow(a,k,n):
    r=[F(1)]+[F(0)]*n
    for _ in range(k): r=smul(r,a,n)
    return r
def sinv(a,n):
    r=[F(0)]*(n+1); r[0]=1/a[0]
    for m in range(1,n+1):
        r[m]=-sum(a[k]*r[m-k] for k in range(1,m+1))/a[0]
    return r
def sexp(c,n): # exp(c H)
    return [F(c)**k/factorial(k) for k in range(n+1)]
def stodd(n):  # Q(H)
    t=todd_coeffs(n); return t[:n+1]
