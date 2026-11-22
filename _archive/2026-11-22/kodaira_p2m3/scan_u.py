"""Continuation in u: F_u=(1-u)*xyz+u*(x^3+y^3+z^3) (Hesse pencil, u=0 toric, u=1 Fermat). Warm-started LM at each u.
usage: scan_u.py m"""
import numpy as np, sys, time
from pkcore import *
from lm import solve
m=int(sys.argv[1]); us=[float(x) for x in sys.argv[2].split(',')]
rng=np.random.default_rng(5)
e=None
for u in us:
    F={(3,0,0):u,(0,3,0):u,(0,0,3):u,(1,1,1):1-u}
    S=Setup(m,F)
    if e is None: e=rng.normal(size=S.nunk)
    t=time.time(); e,nr=solve(S,e,iters=60,verbose=False,tol=1e-11)
    print(f"m={m} u={u}: min |r|={nr:.4e} |e|={np.linalg.norm(e):.3f} ({time.time()-t:.0f}s)",flush=True)
    np.save(f"scan_m{m}_u{u}.npy",e)
