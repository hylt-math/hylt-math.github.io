import numpy as np
from v0_complex import *
rng=np.random.default_rng(7); out=[]
import time; t=time.time()
for s in range(40):
    x,nr=lm(rng.normal(size=n)*10**rng.uniform(-0.5,1.5)+0j)
    if nr<1e-9:
        J=jac(x); sv=np.linalg.svd(J,compute_uv=False); rk=int((sv>1e-7*sv[0]).sum())
        out.append((np.linalg.norm(x),rk,abs(x.imag).max(),x.real.copy()))
        print(f"start {s}: |x|={np.linalg.norm(x):.4f}  rank J={rk} (dim {n-rk}), max|Im|={abs(x.imag).max():.1e}, sigma_min/sigma_max={sv[-1]/sv[0]:.1e}",flush=True)
    if time.time()-t>100: break
