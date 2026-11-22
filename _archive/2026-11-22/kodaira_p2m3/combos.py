"""Restricted (shift-nu_k) ansatz for Fermat at m=3. For each k find all (rational) solutions of the single-monomial problem F=x_k^3,
check exactly, then test all combinations for the Fermat Jacobiator."""
import numpy as np, itertools, sys
from pkcore import *
from shifts import unknown_shifts
import v0_system
NU=v0_system.NU
mono={0:(3,0,0),1:(0,3,0),2:(0,0,3)}
Sf=Setup(3,FS['fermat']); shf=unknown_shifts(Sf)
allsols={}
for k in range(3):
    S,mask,idx,J0,L,diag,Qt=v0_system.build(3,{mono[k]:1},k)
    n=len(idx); Qi=np.array([q[0] for q in Qt]); Qj=np.array([q[1] for q in Qt]); Qv=np.array(list(Qt.values())).T
    res=lambda x: J0+L@x+Qv@(x[Qi]*x[Qj])
    def jac(x):
        J=L.astype(float).copy()
        for p,(i,j) in enumerate(zip(Qi,Qj)): J[:,i]+=Qv[:,p]*x[j]; J[:,j]+=Qv[:,p]*x[i]
        return J
    def lm(x):
        lam=1e-2; r=res(x); f=r@r
        for it in range(300):
            J=jac(x); g=J.T@r; H=J.T@J
            while True:
                d=np.linalg.lstsq(H+lam*np.eye(n),-g,rcond=None)[0]; r2=res(x+d); f2=r2@r2
                if f2<f: x=x+d; r=r2; f=f2; lam=max(lam/3,1e-14); break
                lam*=4
                if lam>1e10: return x,np.sqrt(f)
            if f<1e-26: break
        return x,np.sqrt(f)
    rng=np.random.default_rng(k); sols=[]
    for s in range(60):
        x,nr=lm(rng.normal(size=n)*10**rng.uniform(-0.5,1.5))
        if nr<1e-9:
            xr=np.rint(x*8)/8
            if np.abs(x-xr).max()<1e-6 and abs(res(xr)).max()==0:   # exact rational check (multiples of 1/8 are exact in float64)
                if not any(np.array_equal(xr,y) for y in sols): sols.append(xr)
            elif not any(np.linalg.norm(x-y)<1e-6 for y in sols): print("  non-1/8-rational real solution found?",k,np.round(x[:5],4)); sols.append(x)
    print(f"k={k} ({mono[k]}): {len(sols)} distinct real solutions in {60} starts; exact (1/8-rational) check: {[abs(res(s)).max()==0 for s in sols]}",flush=True)
    full=[]
    for x in sols:
        e=np.zeros(Sf.nunk); e[idx]=x; full.append(e)
    allsols[k]=full
np.save('combos_sols.npy',np.array([[s for s in allsols[k]] for k in range(3)],dtype=object),allow_pickle=True)
print("testing all combinations for the Fermat cubic (F=x^3+y^3+z^3) with the exact Jacobiator:")
best=None
for combo in itertools.product(*[range(len(allsols[k])) for k in range(3)]):
    e=sum(allsols[k][c] for k,c in enumerate(combo))
    R=Sf.resid(Sf.B0+Sf.eps_to_B(e))[:,Sf.keep]
    nz=int((np.abs(R)>0).sum()); nr=np.linalg.norm(R)
    print("  combo",combo,": exact residual norm %.4f, nonzero coords %d"%(nr,nz))
