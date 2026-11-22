"""Exact mod-p linear data: L (first-order Jacobi operator at B0), J0, ranks, first-order obstruction J0 in im L ?"""
import numpy as np, time, sys
from pkcore import *
from modla import *
m=int(sys.argv[1]); name=sys.argv[2]; p=int(sys.argv[3])
F=FS[name] if name in FS else hesse(int(name))
S=Setup(m,F)
B0=np.mod(S.B0,p)
t=time.time(); L=S.jacobian(B0,mod=p); J0=S.resid(B0,mod=p)[:,S.keep].ravel()
print(f"m={m} F={name} p={p}: L {L.shape}, jac %.0fs"%(time.time()-t),flush=True)
nzr=np.where((np.abs(L).sum(1)+np.abs(J0))>0)[0]; L=L[nzr]; J0=J0[nzr]
print("nonzero rows",len(nzr),"J0 nonzero entries",int((J0%p!=0).sum()))
t=time.time()
A=np.concatenate([L,J0[:,None]],axis=1).astype(np.int64)
Rm,piv=rref(A,p)
rankAug=len(piv); rankL=len([c for c in piv if c<S.nunk])
print("rank L =",rankL,"; rank [L|J0] =",rankAug,"; nunk",S.nunk,"; dim ker L =",S.nunk-rankL,"(%.0fs)"%(time.time()-t))
print("FIRST-ORDER OBSTRUCTION J0 notin im L" if rankAug>rankL else "first-order obstruction vanishes (J0 in im L)")
