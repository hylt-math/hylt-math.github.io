# Compare the Theorem (surface case, nodal D, equal residues r = -m/k) with the exact-linear-algebra tables computed earlier
#   (cp2/sing_out.txt for P^2, cp2/p1p1_out.txt for P^1xP^1).
# Inputs per example: X (chi, rank of the classes [D_i] spans), c = #components (smooth or nodal-irreducible ok),
#   mu = #nodes (self-nodes count), k = -K_X / O(1)-ratio (m -> r = -m/k)
# Theorem: for r != 1:
#   m in kZ, m>=0  (r in Z_{<=0}) : H^*(U;C)            + mu[2] = [1,b1,b2,0,0]+mu e_2
#   m in kZ, m<=-2k (r in Z_{>=2}): H^*_c(U;C)          + mu[2] = [0,0,b2,b1,1]+mu e_2
#   m not in kZ (r not in Z)       : H^*(U;L)=H^*_c    + mu[2] = [0,0,chi(U),0,0]+mu e_2   (assuming H^1(U;L)=0)
#   m = -k (r = 1), L=K_X, X of Hodge-Tate type: [0,0,chi(X),0,0]
# with  chi(D)=mu, chi(U)=chi(X)-mu, b1(U)=c-rank<[D_i]>, b2=chi(U)-1+b1, b3=b4=0 (U affine since D ample).
import re,sys
def parse(fn):
    blocks={};cur=None
    for line in open(fn):
        if line.startswith("=="): cur=line[2:].strip(); blocks[cur]={}; continue
        m=re.match(r"^(-?\d+) \[([\d, ]+)\]",line)
        if cur and m: blocks[cur][int(m.group(1))]=[int(x) for x in m.group(2).split(",")]
    return blocks
def pred(m,chiX,k,c,rank,mu):
    chiU=chiX-mu; b1=c-rank; b2=chiU-1+b1
    if m==-k: return [0,0,chiX,0,0]
    if m%k==0 and m>=0: return [1,b1,b2+mu,0,0]
    if m%k==0: return [0,0,b2+mu,b1,1]
    return [0,0,chiU+mu,0,0]
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
    if name not in B: print("missing",name,list(B)); continue
    nb=0
    for m in rng:
        if m not in B[name]: continue
        d=B[name][m]; p=pred(m,chiX,k,c,rank,mu); tot+=1
        if d!=p: bad+=1; nb+=1; print("MISMATCH",name,m,d,p)
    print(f"{name:35s} compared, mismatches={nb}")
print("total compared",tot,"mismatches",bad)
