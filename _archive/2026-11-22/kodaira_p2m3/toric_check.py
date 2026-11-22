"""Exact check of Theorem PK-toric inside our pipeline: F=xyz, diagonal quadratic Poisson structure {y_a,y_b}=omega(a,b) y_a y_b
(omega(e0,e1)=omega(e1,e2)=omega(e2,e0)=1) is Poisson (Jacobiator = 0 exactly) and induces the same bracket as Pi_F on the Veronese ring
(difference B_tor - B0 has zero class-sums, i.e. lies in I_2).  Integer arithmetic, m=2,3,4."""
import numpy as np, sys
from pkcore import *
for m in (2,3,4):
    S=Setup(m,FS['xyz'])
    om=np.zeros((3,3)); om[0,1]=om[1,2]=om[2,0]=1; om=om-om.T
    Bt=np.zeros((S.N,S.N,S.K))
    for a in range(S.N):
        for b in range(S.N):
            if a!=b:
                w=sum(om[i,j]*S.mons[a][i]*S.mons[b][j] for i in range(3) for j in range(3))
                Bt[a,b,S.pid[tuple(sorted((a,b)))]]=w
    D=Bt-S.B0
    cs=max(abs(D[a,b,ks].sum()) for a in range(S.N) for b in range(S.N) for ks in S.byc.values())
    R=S.resid(Bt)
    print(f"m={m}: N={S.N}; max class-sum of (B_tor - B0) = {cs} (0 => B_tor-B0 in I_2, same induced bracket on R); max |Jacobiator(B_tor)| = {abs(R).max()} (all {len(S.triples)} triples, all cubic monomials)")
