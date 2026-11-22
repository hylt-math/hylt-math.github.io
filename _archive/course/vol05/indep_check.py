from fractions import Fraction as F
from math import comb
import itertools
def C(a,k):
    # binomial for a>=0 else 0 (a<k->0)
    return comb(a,k) if a>=k and a>=0 else 0
def h(n,m,q):
    if q==0: return C(m+n,n) if m>=0 else 0
    if q==n: return C(-m-1,n) if m<=-n-1 else 0
    return 0
# 1 Serre duality & chi polynomial
for n in range(1,5):
    for m in range(-14,14):
        for q in range(n+1):
            assert h(n,m,q)==h(n,-m-n-1,n-q)
        chi=sum((-1)**q*h(n,m,q) for q in range(n+1))
        p=F(1)
        for i in range(1,n+1): p*=F(m+i,i)
        assert chi==p,(n,m)
print("1 ok")
# monomial-level H^2(P^2,O(m)) basis count check against formula
def monos(m):  # all a_i<=-1, sum=m, n=2
    return [(a0,a1,m-a0-a1) for a0 in range(-1,m-1,-1) for a1 in range(-1,m-a0,-1) if m-a0-a1<=-1] if m<=-3 else []
for m in range(-9,3): assert len(monos(m))==h(2,m,2),m
# 2 T_P2(m)
res={}
for m in range(-12,8):
    B=monos(m); Bt=monos(m+1)
    idx={a:i for i,a in enumerate(Bt)}
    # map x^a -> (x_i x^a)_i
    import numpy as np
    M=np.zeros((3*len(Bt),len(B)))
    for j,a in enumerate(B):
        for i in range(3):
            b=list(a); b[i]+=1; b=tuple(b)
            if b in idx: M[i*len(Bt)+idx[b],j]=1
    rk=np.linalg.matrix_rank(M) if M.size else 0
    h1=len(B)-rk; h2=3*len(Bt)-rk
    h0=3*h(2,m+1,0)-h(2,m,0)
    chi=3*sum((-1)**q*h(2,m+1,q) for q in range(3))-sum((-1)**q*h(2,m,q) for q in range(3))
    assert h0-h1+h2==chi,(m,h0,h1,h2,chi)
    res[m]=(h0,h1,h2)
print("2 TP2 nonvanishing q>0:",[(m,v[1],v[2]) for m,v in res.items() if v[1] or v[2]])
# 3 Chern: series in H
def series_mul(a,b,N):
    r=[F(0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N: r[i+j]+=x*y
    return r
def cX(Npn,d,dim):
    num=[F(comb(Npn+1,k)) for k in range(Npn+2)]
    den=[F((-d)**k) for k in range(dim+1)]
    s=series_mul(num,den,dim)
    return s
for d in range(1,7):
    s=cX(4,d,3); e=s[3]*d   # int_X H^3 = d
    print(" e(X_%d in P4)="%d,e,end=";")
print()
s=cX(3,4,2); print("K3: c1,c2:",s[1],s[2]*4)
s=cX(3,3,2); print("cubic surface c2*3=",s[2]*3)
# chi(T) surfaces
for name,c1,c2 in [("P2",9,3),("F_a",8,4),("K3",0,24),("cubic",3,9)]:
    print(name,F(7*c1-5*c2,6)) if name!="cubic" else None
# 4 Hodge/prim
b=[1,0,1,204,1,0,1]; print("quintic prim",[b[k]-(b[k-2] if k>=2 else 0) for k in range(4)])
# 5 unified chi
f=lambda k:F((k+1)*(k+2),2)
print("unified P2:",{m:f(m)-(3*f(m+1)-f(m))+f(m+3) for m in range(-8,8)}.values().__iter__().__next__(), set({m:f(m)-(3*f(m+1)-f(m))+f(m+3) for m in range(-8,8)}.values()))
# 6 P1xP1 table
def h1d(m,q): return h(1,m,q)
def hP(a,b):
    out=[0,0,0]
    for q1 in (0,1):
        for q2 in (0,1): out[q1+q2]+=h1d(a,q1)*h1d(b,q2)
    return tuple(out)
for a in (-1,0,1,2,3):
    print(a,[hP(a-2,b-2) for b in (-1,0,1,2,3)])
# 7 SerreFail (b)
print([hP(m,-2) for m in range(0,4)])
# 8 hyper
def hX(d,k,q):
    if q==0: return C(k+3,3)-C(k-d+3,3)
    if q==1: return 0
    return h(3,k-d,3)-h(3,k,3)
for d in range(1,8):
    for k in range(-10,13):
        assert hX(d,k,2)==hX(d,d-4-k,0),(d,k)
print("pg",[hX(d,0,2) for d in range(1,7)])
# 9 quartic moduli
print("quartic moduli",comb(7,3)-1-15)
# torus Pfaffian
E=np.zeros((4,4)); E[0,1]=-1;E[1,0]=1;E[2,3]=-1;E[3,2]=1
print("Pf",E[0,1]*E[2,3]-E[0,2]*E[1,3]+E[0,3]*E[1,2])
