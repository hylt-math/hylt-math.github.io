"""Exact polynomial system for F=x^3, unknowns = shift nu_0 components (37). Returns (J0 vector, L matrix, Q tensor) as integers."""
import numpy as np
from pkcore import *
from shifts import unknown_shifts
NU=[(2,-1,-1),(-1,2,-1),(-1,-1,2)]
def build(m=3,F=None,which=0):
    F=F or FS['x3']; S=Setup(m,F); sh=unknown_shifts(S)
    mask=np.array([s==NU[which] for s in sh]) if which is not None else np.ones(S.nunk,bool)
    n=int(mask.sum()); idx=np.nonzero(mask)[0]
    def R(x):
        e=np.zeros(S.nunk); e[idx]=x
        return S.resid(S.B0+S.eps_to_B(e))[:,S.keep].ravel(), S.resid(S.eps_to_B(e))[:,S.keep].ravel()
    z=np.zeros(n); J0=R(z)[0]
    L=np.array([R(np.eye(n)[i])[0]-J0-R(np.eye(n)[i])[1] for i in range(n)]).T
    diag=np.array([R(np.eye(n)[i])[1] for i in range(n)]).T          # Q(e_i)
    Qt={}
    for i in range(n):
        for j in range(i+1,n):
            v=R(np.eye(n)[i]+np.eye(n)[j])[1]-diag[:,i]-diag[:,j]
            if np.abs(v).max()>0: Qt[(i,j)]=v
    return S,mask,idx,J0,L,diag,Qt
if __name__=="__main__":
    S,mask,idx,J0,L,diag,Qt=build()
    n=len(idx); rows=np.nonzero((np.abs(J0)+np.abs(L).sum(1)+np.abs(diag).sum(1)+sum((np.abs(v) for v in Qt.values()),0))>0)[0]
    print("unknowns",n,"nonzero equations",len(rows))
    print("all integer data?",np.allclose(J0,np.rint(J0)) and np.allclose(L,np.rint(L)) and np.allclose(diag,np.rint(diag)))
    quad=[r for r in rows if np.abs(diag[r]).sum()+sum(abs(v[r]) for v in Qt.values())>0]
    print("equations with quadratic terms:",len(quad),"purely linear/constant:",len(rows)-len(quad))
    print("pure quadratic-term count (i<=j pairs):",(np.abs(diag).sum(0)>0).sum(),"diag;",len(Qt),"offdiag")
