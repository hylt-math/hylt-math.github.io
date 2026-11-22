"""Multi-start LM for Jacobiator(B0+eps)=0.  usage: multistart.py m name nstarts"""
import numpy as np, sys, time
from pkcore import *
from lm import solve
m=int(sys.argv[1]); name=sys.argv[2]; ns=int(sys.argv[3]); seed0=int(sys.argv[4]) if len(sys.argv)>4 else 100
F=FS[name] if name in FS else hesse(float(name))
S=Setup(m,F)
print("F=",name,"m=",m,"nunk",S.nunk,flush=True)
for s in range(ns):
    rng=np.random.default_rng(seed0+s); sc=10**rng.uniform(-1.5,1.7)
    e0=rng.normal(size=S.nunk)*sc
    t=time.time(); e,nr=solve(S,e0,iters=80,verbose=False,tol=1e-12)
    print(f"start {s} scale {sc:.2f}: final |r|={nr:.6e} |e|={np.linalg.norm(e):.3f} ({time.time()-t:.0f}s)",flush=True)
    np.save(f"ms_m{m}_{name}_{seed0+s}.npy",e)
