# Checks for serre_rr_statements.md  (run: python3 serre_rr_check.py from cp2/)
# (1) Theorem A1 (E_1 vanishing for a>0, effective Serre threshold m0) via Bott/Kunneth on P^2 and P^1xP^1,
#     and consistency with the exact tables (degrees >=3 vanish for m>=m0, surfaces).
# (2) Periodicity for m>=1 of the tables; (3) Poincare polynomial closed form in the residue r.
from math import comb
import re
def h_O_P1(d):  # (h0,h1) of O(d) on P^1
    return (d+1,0) if d>=0 else (0,-d-1)
def h_O_P2(d):  # (h0,h1,h2)
    if d>=0: return (comb(d+2,2),0,0)
    return (0,0,comb(-d-1,2))
def h_O_P1P1(a,b):
    A=h_O_P1(a);B=h_O_P1(b)
    return [sum(A[i]*B[k-i] for i in range(2) if 0<=k-i<2) for k in range(3)]
def h_Omega1_P2(j): # Bott
    # h^0(Omega^1(j)) = j^2-1 choose.. formula: C(j+1,j)*C(j-1,1) = (j+1)(j-1) for j>1 ; h^1=1 if j==0 ; h^2(Omega^1(j))=h^0(Omega^1(-j)) (Serre duality, K=O(-3): h^2(Omega^1(j)) = h^0(T(-j-3)) = h^0(Omega^1(-j))
    def h0(j): return (j+1)*(j-1) if j>=2 else 0
    return (h0(j), 1 if j==0 else 0, h0(-j))
def E1_P2(m):
    # wedge^0=O(m), wedge^1=T(m)=Omega^1(m+3), wedge^2=O(m+3)
    return {0:h_O_P2(m),1:h_Omega1_P2(m+3),2:h_O_P2(m+3)}
def E1_P1P1(m):
    return {0:h_O_P1P1(m,m),
            1:[x+y for x,y in zip(h_O_P1P1(m+2,m),h_O_P1P1(m,m+2))],
            2:h_O_P1P1(m+2,m+2)}
def vanishing_threshold(E1,lo=-20,hi=20):
    bad=[m for m in range(lo,hi) if any(E1(m)[b][a]!=0 for b in range(3) for a in (1,2))]
    return max(bad)+1 if bad else lo, bad
for name,E in (("P2",E1_P2),("P1xP1",E1_P1P1)):
    m0,bad=vanishing_threshold(E)
    print(name,"E_1^{a>0,b}=0 for all m >=",m0,"; non-vanishing m in [-20,20):",bad)
# tables
def parse(fn):
    blocks={};cur=None
    for line in open(fn):
        if line.startswith("=="): cur=line[2:].strip(); blocks[cur]={}; continue
        mm=re.match(r"^(-?\d+) \[([\d, ]+)\]",line)
        if cur and mm: blocks[cur][int(mm.group(1))]=[int(x) for x in mm.group(2).split(",")]
    return blocks
S=parse("sing_out.txt"); P=parse("p1p1_out.txt")
def check(B,name,m0,k,hi):
    ok=all(B[name][m][3]==0 and B[name][m][4]==0 for m in range(m0,hi) if m in B[name])
    per=all(B[name][m]==B[name][m+k] for m in range(1,hi-k) if m in B[name] and m+k in B[name])
    print(f"{name:32s} degrees>=3 vanish for m>={m0}: {ok};  period {k} for m>=1: {per}")
for n in ["smooth(Fermat)","nodal y2z-x3-x2z","conic+secant x(yz-x2)","triangle xyz"]: check(S,n,-2,3,16)
for n in ["smooth(random 2,2)","two (1,1) conics, transverse","four lines x0x1y0y1","(1,1)+(1,0)+(0,1)"]: check(P,n,-1,2,9)
# (3) Poincare polynomial in the residue r  (all equal residues, nodal D, Theorem 2); returns [h0..h4]
def poincare(r,chiX,c,rank,mu):
    # r rational; Zr: r integer
    chiU=chiX-mu; b1=c-rank; b2=chiU-1+b1
    from fractions import Fraction
    r=Fraction(r)
    if r==1: return [0,0,chiX,0,0]
    if r.denominator==1 and r<=0: return [1,b1,b2+mu,0,0]
    if r.denominator==1 and r>=2: return [0,0,b2+mu,b1,1]
    return [0,0,chiX,0,0]
from fractions import Fraction
ex=[("P2 smooth cubic",S,"smooth(Fermat)",3,3,1,1,0,range(-15,16)),
    ("P2 triangle",S,"triangle xyz",3,3,3,1,3,range(-15,16)),
    ("P1xP1 four lines",P,"four lines x0x1y0y1",4,2,4,2,4,range(-9,9))]
tot=bad=0
for lab,B,n,chiX,k,c,rk,mu,rng in ex:
    for m in rng:
        if m in B[n]:
            tot+=1
            if poincare(Fraction(-m,k),chiX,c,rk,mu)!=B[n][m]: bad+=1
print("Poincare polynomial formula in r=-m/k:",tot,"values,",bad,"mismatches")
# duality r <-> 2-r, k <-> 4-k
d=0
for r in [Fraction(a,6) for a in range(-30,43)]:
    p=poincare(r,3,3,1,3); q=poincare(2-r,3,3,1,3)
    if r!=1 and p!=q[::-1]: d+=1
print("duality symmetry P_r(k)=P_{2-r}(4-k) violations:",d)
