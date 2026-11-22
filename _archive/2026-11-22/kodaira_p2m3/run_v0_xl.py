import numpy as np, sys
from v0_system import build
from xl import *
p=int(sys.argv[1]); D=int(sys.argv[2]); which=int(sys.argv[3]) if len(sys.argv)>3 else 0
S,mask,idx,J0,L,diag,Qt=build(3,None,which)
n=len(idx); rows=np.nonzero((np.abs(J0)+np.abs(L).sum(1)+np.abs(diag).sum(1)+sum((np.abs(v) for v in Qt.values()),0))>0)[0]
eqs=eqs_from_system(J0,L,diag,Qt,rows,n)
Rm,piv,mons,order,pos,inc=macaulay(eqs,n,D,p)
print("p=",p,"D=",D,"inconsistent (1 in ideal):",inc)
ncol=len(mons); nmon=ncol
# quotient dimension: number of non-pivot columns
print("non-pivot monomials (quotient dim at degree D):",ncol-len(piv))
# linear polynomials (variables determined): rows of RREF whose support is within degree<=1 monomials
lin=[]
for r in range(Rm.shape[0]):
    nzc=np.nonzero(Rm[r])[0]
    degs=[len(mons[order[c]]) for c in nzc]
    if max(degs)<=1: lin.append(r)
print("rows with support in degree<=1:",len(lin))
