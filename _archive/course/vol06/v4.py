from lib import *
from itertools import combinations
from v2 import ci, binom_gen
def chiP_universal(n):
    N=n;D=n
    x=[P.var(i,N,D) for i in range(N)]
    Q=todd_coeffs(D)
    td=P.const(1,N,D)
    for xi in x: td=td*series_sub(Q,xi,N,D)
    res=[]
    em=[series_sub([F((-1)**k,factorial(k)) for k in range(D+1)],xi,N,D) for xi in x]  # e^{-x_i}
    for p in range(n+1):
        chp=P.const(0,N,D)
        for S in combinations(range(N),p):
            t=P.const(1,N,D)
            for i in S: t=t*em[i]
            chp=chp+t
        top=(chp*td).deg(n)
        res.append(to_elem(top,N))
    return res
def show2(d,names):
    terms=[]
    for ex,c in sorted(d.items()):
        s='*'.join(f"{names[i]}^{e}" if e>1 else names[i] for i,e in enumerate(ex) if e)
        terms.append(f"({c})*{s}")
    return ' + '.join(terms)
for n in (2,3):
    print("n=",n)
    for p,r in enumerate(chiP_universal(n)): print("  chi(Omega^%d) ="%p, show2(r,['c1','c2','c3']))
# CY3 numbers
c,deg=ci(4,[5],3)
c3=c[3]*deg
print("quintic chi(Omega^1)= -c3/2 =",-c3/2)
# Euler theorem: sum_b (-1)^b chi(wedge^b T ⊗ E) on a variety given by c_i in H (single variable); E = O(m)
def euler_total(c,deg,n,m,dual=False):
    # roots formal: compute ch(wedge^b T) via universal formulas in elementary symmetric -> evaluate
    N=n;D=n
    x=[P.var(i,N,D) for i in range(N)]
    Q=todd_coeffs(D)
    td=P.const(1,N,D)
    for xi in x: td=td*series_sub(Q,xi,N,D)
    ex=[series_sub(expser(D),xi,N,D) for xi in x]
    tot=P.const(0,N,D)
    for b in range(n+1):
        chb=P.const(0,N,D)
        for S in combinations(range(N),b):
            t=P.const(1,N,D)
            for i in S: t=t*ex[i]
            chb=chb+t
        tot=tot+chb*((-1)**b)
    top=(tot*td).deg(n)     # sum_b (-1)^b ch(wedge^b T) Td, degree n part  (as poly in roots)
    # full: need degree n part of ch(E)*tot*td; tot*td has components in degrees >=n only? compute whole
    full=(tot*td)
    ch_m=sexp(m,n)  # in H
    # evaluate: replace e_k(x) by c[k] H^k
    el={}
    total=F(0)
    for deg_k in range(0,n+1):
        part=full.deg(deg_k)
        d=to_elem(part,N) if part.d else {}
        val=F(0)
        for exps,cf in d.items():
            t=cf
            dd=0
            for i,e in enumerate(exps):
                t*=c[i+1]**e; dd+=(i+1)*e
            assert dd==deg_k
            val+=t
        # multiply by ch_{n-deg_k}(O(m)) = m^{n-k}/(n-k)!
        total+=val*F(m)**(n-deg_k)/factorial(n-deg_k)
    return total*deg
for nam,degs in [(2,[]),(3,[]),(3,[4]),(3,[3]),(4,[5]),(4,[3]),(5,[2,4])]:
    n=nam-len(degs); c,deg=ci(nam,degs,n)
    vals=[euler_total(c,deg,n,m) for m in range(-6,7)]
    e=c[n]*deg
    print(nam,degs,"n=",n,"set",set(vals),"expected",(-1)**n*e)
    assert set(vals)=={(-1)**n*e}
# rank 3 E? check with E=O(a)+O(b) : additive -> ok
