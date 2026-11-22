"""LM restricted to unknowns of given shifts. usage: restricted.py m Fname shifts(nu|all-nu|nu+0) nstarts"""
import numpy as np, sys, time
from pkcore import *
from shifts import unknown_shifts
def solve_restricted(S,mask,e0,iters=200,tol=1e-13,verbose=False):
    mask=np.asarray(mask); idx=np.nonzero(mask)[0]; x=e0[idx].copy(); lam=1e-2
    def full(x): e=np.zeros(S.nunk); e[idx]=x; return e
    def res(x): return S.resid(S.B0+S.eps_to_B(full(x)))[:,S.keep].ravel()
    r=res(x); f=r@r
    for it in range(iters):
        J=S.jacobian(S.B0+S.eps_to_B(full(x)),mask=mask); g=J.T@r; H=J.T@J
        while True:
            d=np.linalg.solve(H+lam*np.eye(len(x)),-g); x2=x+d; r2=res(x2); f2=r2@r2
            if f2<f: x,r,f=x2,r2,f2; lam=max(lam/3,1e-15); break
            lam*=4
            if lam>1e12: return full(x),np.sqrt(f)
        if verbose: print(it,np.sqrt(f),flush=True)
        if np.sqrt(f)<tol: break
    return full(x),np.sqrt(f)
NU=[(2,-1,-1),(-1,2,-1),(-1,-1,2)]
if __name__=="__main__":
    m=int(sys.argv[1]); name=sys.argv[2]; which=sys.argv[3]; ns=int(sys.argv[4])
    F=FS[name] if name in FS else hesse(float(name))
    S=Setup(m,F); sh=unknown_shifts(S)
    if which=='nu': mask=np.array([s in NU for s in sh])
    elif which=='nu0': mask=np.array([s in NU or s==(0,0,0) for s in sh])
    elif which.startswith('nuk'): k=int(which[3:]); mask=np.array([s==NU[k] for s in sh])
    print(f"m={m} F={name} ansatz={which}: {mask.sum()} unknowns",flush=True)
    for s in range(ns):
        rng=np.random.default_rng(300+s); e0=rng.normal(size=S.nunk)*10**rng.uniform(-1,1.5)
        t=time.time(); e,nr=solve_restricted(S,mask,e0); print(f" start {s}: min |r|={nr:.6e} |e|={np.linalg.norm(e):.4f} ({time.time()-t:.0f}s)",flush=True)
