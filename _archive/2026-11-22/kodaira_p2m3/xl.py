"""Exact mod-p XL / truncated Macaulay linear algebra for small polynomial systems.
Equations: list of dict {monomial tuple (sorted var indices): coeff}. Computes the degree-D truncated ideal (multipliers of degree <= D-deg) and reports
- whether 1 is in the span (INCONSISTENT over algebraic closure of F_p => no solution),
- dimension of quotient (number of monomials of deg<=D minus rank), linear forms in span."""
import numpy as np, itertools, sys, time
from modla import rref
def eqs_from_system(J0,L,diag,Qt,rows,n):
    eqs=[]
    for r in rows:
        d={}
        if J0[r]: d[()]=int(round(J0[r]))
        for i in range(n):
            if L[r,i]: d[(i,)]=int(round(L[r,i]))
            if diag[r,i]: d[(i,i)]=int(round(diag[r,i]))
        for (i,j),v in Qt.items():
            if v[r]: d[(i,j)]=int(round(v[r]))
        eqs.append(d)
    return eqs
def macaulay(eqs,n,D,p,verbose=True):
    # all monomials of deg <= D
    mons=[()]
    for d in range(1,D+1): mons+=list(itertools.combinations_with_replacement(range(n),d))
    mid={m:i for i,m in enumerate(mons)}
    rows=[]
    mult=[()]
    maxdeg=max(max(len(m) for m in e) for e in eqs)
    for d in range(1,D-maxdeg+1): mult+=list(itertools.combinations_with_replacement(range(n),d))
    # order columns by decreasing degree so that elimination eliminates high-degree first (graded ordering)
    order=sorted(range(len(mons)),key=lambda i:(-len(mons[i]),mons[i])); pos={mons[i]:k for k,i in enumerate(order)}
    nrow=0; data=[]
    for e in eqs:
        de=max(len(m) for m in e)
        for mu in mult:
            if len(mu)+de>D: continue
            row={}
            for m,c in e.items():
                mm=tuple(sorted(m+mu)); row[pos[mm]]=(row.get(pos[mm],0)+c)%p
            data.append(row)
    A=np.zeros((len(data),len(mons)),dtype=np.uint32)
    for i,row in enumerate(data):
        for j,c in row.items(): A[i,j]=c
    if verbose: print(f"Macaulay matrix {A.shape}",flush=True)
    t=time.time(); Rm,piv=rref(A,p)
    if verbose: print(f"rank {len(piv)} ({time.time()-t:.0f}s)",flush=True)
    inconsistent = (len(mons)-1) in piv   # column of constant monomial (last in ordering)
    return Rm,piv,mons,order,pos,inconsistent
