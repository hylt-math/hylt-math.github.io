"""All complex solutions of the 37-unknown system for F=x^3, shift nu_0 (m=3) by complex Gauss-Newton/LM multistart."""
import numpy as np, sys
from v0_system import build
S,mask,idx,J0,L,diag,Qt=build(3,None,0); n=len(idx)
Qi=np.array([k[0] for k in Qt]); Qj=np.array([k[1] for k in Qt]); Qv=np.array(list(Qt.values())).T   # (rows, npairs)
def res(x): return J0+L@x+Qv@(x[Qi]*x[Qj])
def jac(x):
    J=L.astype(complex).copy()
    # d/dx_i of sum_p Qv[:,p] x_i x_j
    for p,(i,j) in enumerate(zip(Qi,Qj)): J[:,i]+=Qv[:,p]*x[j]; J[:,j]+=Qv[:,p]*x[i]
    return J
def lm(x,iters=400):
    lam=1e-2; r=res(x); f=np.vdot(r,r).real
    for it in range(iters):
        J=jac(x); g=J.conj().T@r; H=J.conj().T@J
        while True:
            d=np.linalg.solve(H+lam*np.eye(n),-g); r2=res(x+d); f2=np.vdot(r2,r2).real
            if f2<f: x=x+d; r=r2; f=f2; lam=max(lam/3,1e-14); break
            lam*=4
            if lam>1e10: return x,np.sqrt(f)
        if f<1e-26: break
    return x,np.sqrt(f)
if __name__=="__main__":
    ns=int(sys.argv[1]); rng=np.random.default_rng(int(sys.argv[2]))
    sols=[]; fails=0
    for s in range(ns):
        x0=(rng.normal(size=n)+1j*rng.normal(size=n))*10**rng.uniform(-0.5,1.5)
        x,nr=lm(x0)
        if nr<1e-8:
            if not any(np.linalg.norm(x-y)<1e-5*(1+np.linalg.norm(y)) for y in sols): sols.append(x); print(f"new solution #{len(sols)} after {s+1} starts: |x|={np.linalg.norm(x):.5f}, max|Im|={abs(x.imag).max():.2e}",flush=True)
        else: fails+=1
    print("starts",ns,"converged to residual<1e-8:",ns-fails,"distinct complex solutions:",len(sols))
    np.save('V0_complex_sols.npy',np.array(sols))
