# Test of the "indicial-jump" form of the refined RR conjecture (index_route_notes.md, Conj. I3) against the exact tables.
#   P_r(t) = chi(X) t^2 + [r in Z<=0] Delta(t) + [r in Z>=2] t^4 Delta(1/t),   Delta(t) = 1 + b1 t + (b1-1) t^2 = (1+t)(1+(b1-1)t).
# Data from cp2/sing_out.txt, cp2/p1p1_out.txt (exact linear algebra). Residue r = -m/k.
import re, sys
from fractions import Fraction
sys.path.insert(0,'.')
def parse(fn):
    blocks={};cur=None
    for line in open(fn):
        if line.startswith("=="): cur=line[2:].strip(); blocks[cur]={}; continue
        m=re.match(r"^(-?\d+) \[([\d, ]+)\]",line)
        if cur and m: blocks[cur][int(m.group(1))]=[int(x) for x in m.group(2).split(",")]
    return blocks
def conj(m,chiX,k,c,rank,mu):
    b1=c-rank
    r=Fraction(-m,k)
    P=[0,0,chiX,0,0]
    if r==1:                      # K_X, Hodge-Tate: all in degree 2
        return P
    D=[1,b1,b1-1]                 # Delta(t) coefficients (degrees 0,1,2)
    if r.denominator==1 and r<=0:
        for i,x in enumerate(D): P[i]+=x
    elif r.denominator==1 and r>=2:
        for i,x in enumerate(D): P[4-i]+=x
    return P
tests=[
 ("sing_out.txt","smooth(Fermat)",3,3,1,1,0,range(-15,16)),
 ("sing_out.txt","nodal y2z-x3-x2z",3,3,1,1,1,range(-15,16)),
 ("sing_out.txt","conic+secant x(yz-x2)",3,3,2,1,2,range(-15,16)),
 ("sing_out.txt","triangle xyz",3,3,3,1,3,range(-15,16)),
 ("p1p1_out.txt","smooth(random 2,2)",4,2,1,1,0,range(-9,9)),
 ("p1p1_out.txt","two (1,1) conics, transverse",4,2,2,1,2,range(-9,9)),
 ("p1p1_out.txt","four lines x0x1y0y1",4,2,4,2,4,range(-9,9)),
 ("p1p1_out.txt","(1,1)+(1,0)+(0,1)",4,2,3,2,3,range(-9,9)),
]
tot=bad=0
for fn,name,chiX,k,c,rank,mu,rng in tests:
    B=parse(fn)
    nb=0
    for m in rng:
        if m not in B.get(name,{}): continue
        d=B[name][m]; p=conj(m,chiX,k,c,rank,mu); tot+=1
        if d!=p: bad+=1; nb+=1; print("MISMATCH",name,m,d,p)
        assert sum((-1)**i*x for i,x in enumerate(d))==chiX
    b1=c-rank
    print(f"{name:34s} b1={b1} Delta=(1+t)(1+{b1-1}t) mismatches={nb}")
print("total",tot,"mismatches",bad)
