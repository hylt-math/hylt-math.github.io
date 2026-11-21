# Round K: checks of the refined Riemann-Roch statements (roundK_notes.md)
#  (K1) chi(X; DR_log(L)) = int c_n(T(-log D)) = chi(U) for every L (Chern-class/HRR check on P^2 with smooth degree-d curve, all twists a)
#  (K2) Theorem K:  P_HH(t) = chi(X) t^n + sum_{k<n} h^k(U;L_U) (t^k - (-1)^k t^n)   (n even, U affine, Theorem R hypotheses, no r_i in Z>=1)
#       (a) surface tables (sing_out.txt, p1p1_out.txt), r<=0 or r not integer; r>=2 via Serre-duality r<->2-r;
#       (b) toric n=2,4 (exact weight criterion).
import re, sys, itertools
from fractions import Fraction as Fr
from math import comb
sys.path.insert(0,'.')

# ---------- (K1)
def chiO(k): return (k+1)*(k+2)//2          # chi(P^2,O(k))
def chiOm1(k): return 3*chiO(k-1)-chiO(k)  # Euler sequence
bad=0;tot=0
for d in range(1,8):
    for a in range(-12,13):
        chiD=chiO(a)-chiO(a-d)
        S=chiO(a)-(chiOm1(a)+chiD)+chiO(a+d-3)   # Omega^2(log D)=K(D)=O(d-3)
        c2=3-3*d+d*d                              # c_2(T(-log D)) from c(T)/(1+dH)
        chiU=3-(3*d-d*d)                          # chi(P^2) - chi(smooth plane curve)
        tot+=1
        if not(S==c2==chiU): bad+=1; print("K1 MISMATCH",d,a,S,c2,chiU)
print("(K1) chi(X;DR_log(O(a))) = c_2(T(-log D)) = chi(U): mismatches",bad,"of",tot)

# ---------- (K2a) surfaces
def parse(fn):
    blocks={};cur=None
    for line in open(fn):
        if line.startswith("=="): cur=line[2:].strip(); blocks[cur]={}; continue
        m=re.match(r"^(-?\d+) \[([\d, ]+)\]",line)
        if cur and m: blocks[cur][int(m.group(1))]=[int(x) for x in m.group(2).split(",")]
    return blocks
def thmK(n,chiX,h):            # h = [h^0..h^{n-1}] of H^k(U;L_U)
    P=[0]*(n+1); P[n]+=chiX
    for k,hk in enumerate(h):
        P[k]+=hk; P[n]-=(-1)**k*hk
    return P
def pred_surface(m,chiX,k,c,rank):
    b1=c-rank; r=Fr(-m,k)
    if r==1: return None
    if r>=2 and r.denominator==1:                      # Serre duality P_{2-r}(t)=t^4 P_r(1/t)
        Q=thmK(2,chiX,[1,b1])+[0,0]; return Q[::-1]
    if r.denominator==1: return thmK(2,chiX,[1,b1])+[0,0]    # r<=0: L_U trivial, h^0=1, h^1=b1(U)
    return thmK(2,chiX,[0,0])+[0,0]                          # r non integer: L_U nontrivial, h^0=h^1=0 (data-consistent)
tests=[
 ("sing_out.txt","smooth(Fermat)",3,3,1,1,range(-15,16)),
 ("sing_out.txt","nodal y2z-x3-x2z",3,3,1,1,range(-15,16)),
 ("sing_out.txt","conic+secant x(yz-x2)",3,3,2,1,range(-15,16)),
 ("sing_out.txt","triangle xyz",3,3,3,1,range(-15,16)),
 ("p1p1_out.txt","smooth(random 2,2)",4,2,1,1,range(-9,9)),
 ("p1p1_out.txt","two (1,1) conics, transverse",4,2,2,1,range(-9,9)),
 ("p1p1_out.txt","four lines x0x1y0y1",4,2,4,2,range(-9,9)),
 ("p1p1_out.txt","(1,1)+(1,0)+(0,1)",4,2,3,2,range(-9,9)),
]
tot=bad=0
for fn,name,chiX,k,c,rank,rng in tests:
    B=parse(fn); nb=0
    for m in rng:
        if m not in B.get(name,{}): continue
        p=pred_surface(m,chiX,k,c,rank)
        if p is None: continue
        tot+=1
        if B[name][m]!=p: bad+=1;nb+=1;print("MISMATCH",name,m,B[name][m],p)
    print(f"{name:34s} mismatches={nb}")
print("(K2a) Theorem K on surface tables:",bad,"mismatches of",tot)

# ---------- (K2b) toric
from toric_crit import FANS, crit_poly, weights, rk_of, randA
def vertices(rays,a,box):
    n=len(rays[0]); return sum(1 for chi,C in weights(rays,a,box) if rk_of(C,n)==n)
def avec(name,ms):
    rays=FANS[name]; a=[0]*len(rays)
    if name=='P2': a[2]=ms[0]
    if name=='P1xP1': a[1]=ms[0]; a[3]=ms[1]
    if name=='P4': a[4]=ms[0]
    if name=='P2xP2': a[2]=ms[0]; a[5]=ms[1]
    if name=='P1^4':
        for k in range(4): a[2*k+1]=ms[k]
    return a
tt=[('P2',(1,)),('P2',(3,)),('P1xP1',(1,1)),('P1xP1',(2,3)),('P4',(1,)),('P2xP2',(1,1)),('P1^4',(1,1,1,1))]
tot=bad=0
for name,ms in tt:
    rays=FANS[name]; n=len(rays[0]); a=avec(name,ms); box=max(a)+n+3
    V=vertices(rays,a,box)           # = chi(X)
    A=randA(n,7,10**9)
    grid=list(itertools.product(range(-2,3),repeat=n)) if n==2 else list(itertools.product(range(-1,2),repeat=n))
    grid=[tuple(Fr(x) for x in g) for g in grid]+[tuple(Fr(1,3) if i==0 else Fr(0) for i in range(n))]
    for rho in grid:
        r=[sum(rho[j]*rays[i][j] for j in range(n))-a[i] for i in range(len(rays))]
        if any(x.denominator==1 and x>=1 for x in r): continue     # excludes Z>=1 residues (Theorem R hypothesis (i))
        triv=all(x.denominator==1 for x in rho)
        h=[comb(n,k) for k in range(n)] if triv else [0]*n         # H^k((C*)^n;L_U)
        pred=thmK(n,V,h)
        got=crit_poly(rays,a,A,rho,box); tot+=1
        if got!=pred: bad+=1; print("MISMATCH",name,ms,rho,got,pred)
    print(name,ms,"chi(X)=",V,"running mismatches",bad,"of",tot,flush=True)
print("(K2b) Theorem K, toric n=2,4:",bad,"mismatches of",tot)
