"""Float Levenberg-Marquardt for Jacobiator(B0+eps)=0 (numerical existence only)."""
import numpy as np, time, sys
from pkcore import *
def solve(S,e0,iters=300,verbose=True,tol=1e-13):
    e=e0.copy(); lam=1e-2
    def res(e): return S.resid(S.B0+S.eps_to_B(e))[:,S.keep].ravel()
    r=res(e); f=r@r
    for it in range(iters):
        J=S.jacobian(S.B0+S.eps_to_B(e))
        g=J.T@r; H=J.T@J
        while True:
            try: d=np.linalg.solve(H+lam*np.eye(len(e)),-g)
            except np.linalg.LinAlgError: lam*=10; continue
            e2=e+d; r2=res(e2); f2=r2@r2
            if f2<f: e,r,f=e2,r2,f2; lam=max(lam/3,1e-15); break
            lam*=4
            if lam>1e12: return e,np.sqrt(f)
        if verbose: print(it,"|r|=%.3e lam=%.1e |e|=%.2f"%(np.sqrt(f),lam,np.linalg.norm(e)),flush=True)
        if np.sqrt(f)<tol: break
    return e,np.sqrt(f)
if __name__=="__main__":
    m=int(sys.argv[1]); name=sys.argv[2]; seed=int(sys.argv[3]) if len(sys.argv)>3 else 0
    F=FS[name] if name in FS else hesse(float(name))
    S=Setup(m,F); rng=np.random.default_rng(seed)
    e0=rng.normal(size=S.nunk)*float(sys.argv[4]) if len(sys.argv)>4 else rng.normal(size=S.nunk)
    t=time.time(); e,nr=solve(S,e0); print("final |r|",nr,"time %.0fs"%(time.time()-t))
    np.save(f"sol_m{m}_{name}_s{seed}.npy",e)
