"""Exact (integer arithmetic) verification that the rounded float solution at m=2 (Fermat) satisfies Jacobiator(B0+eps)=0 over Z."""
import numpy as np
from pkcore import *
S=Setup(2,FS['fermat'])
e=np.load('ms_m2_fermat_100.npy'); ei=np.rint(e)
print("max rounding error of float solution:",abs(e-ei).max(),"; nonzero entries:",int((ei!=0).sum()),"values:",sorted(set(ei[ei!=0])))
B=np.rint(S.B0+S.eps_to_B(ei)).astype(np.int64)
assert abs(S.B0+S.eps_to_B(ei)-B).max()==0
# exact integer Jacobiator via int64 einsum (entries small -> no overflow)
G=np.zeros((S.N,S.K,S.T),dtype=np.int64)
for a in range(S.N):
    for k,(c,d) in enumerate(S.pairs):
        for kp in range(S.K):
            for (x,y) in ((c,d),(d,c)):
                coef=B[a,x,kp]
                if coef: G[a,k,S.tid[tuple(sorted(S.pairs[kp]+(y,)))]]+=coef
X=np.einsum('bck,akt->abct',B,G)
Y=X+np.transpose(X,(2,0,1,3))+np.transpose(X,(1,2,0,3))
print("exact integer Jacobiator: max |coeff| over ALL (a,b,c,monomial) =",abs(Y).max())
# check Poisson ideal & the quotient bracket: {y_a,y_b} equals lifted x-bracket mod I
