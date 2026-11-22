"""Complex LM restricted to shift-nu unknowns (111 unknowns for m=3) or unconstrained (1215). usage: restricted_complex.py m F which nstarts"""
import numpy as np, sys, time
from pkcore import *
from shifts import unknown_shifts
NU=[(2,-1,-1),(-1,2,-1),(-1,-1,2)]
def lmc(S,mask,x0,iters=150,tol=1e-12):
    idx=np.nonzero(mask)[0]; x=x0.copy(); lam=1e-2
    def full(x): e=np.zeros(S.nunk,dtype=complex); e[idx]=x; return e
    def res(x): return S.resid(S.B0+S.eps_to_B(full(x)))[:,S.keep].ravel()
    r=res(x); f=np.vdot(r,r).real
    for it in range(iters):
        J=S.jacobian(S.B0+S.eps_to_B(full(x)),mask=mask); g=J.conj().T@r; H=J.conj().T@J
        while True:
            d=np.linalg.solve(H+lam*np.eye(len(x)),-g); r2=res(x+d); f2=np.vdot(r2,r2).real
            if f2<f: x,r,f=x+d,r2,f2; lam=max(lam/3,1e-15); break
            lam*=4
            if lam>1e12: return full(x),np.sqrt(f)
        if np.sqrt(f)<tol: break
    return full(x),np.sqrt(f)
if __name__=="__main__":
    m=int(sys.argv[1]); name=sys.argv[2]; which=sys.argv[3]; ns=int(sys.argv[4])
    F=FS[name] if name in FS else hesse(float(name))
    S=Setup(m,F); sh=unknown_shifts(S)
    mask=np.array([s in NU for s in sh]) if which=='nu' else np.ones(S.nunk,bool)
    print(f"COMPLEX LM m={m} F={name} ansatz={which}: {mask.sum()} complex unknowns",flush=True)
    for s in range(ns):
        rng=np.random.default_rng(900+s); n=int(mask.sum())
        x0=(rng.normal(size=n)+1j*rng.normal(size=n))*10**rng.uniform(-0.5,1.5)
        t=time.time(); e,nr=lmc(S,mask,x0); print(f" start {s}: min |r|={nr:.6e}  |e|={np.linalg.norm(e):.4f}  max|Im e|={abs(e.imag).max():.2e} ({time.time()-t:.0f}s)",flush=True)
