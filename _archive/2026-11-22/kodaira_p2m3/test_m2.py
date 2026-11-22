import numpy as np, time, sys
from pkcore import *
m=int(sys.argv[1]); name=sys.argv[2]
F=FS[name] if name in FS else hesse(int(name))
t=time.time(); S=Setup(m,F); print("N",S.N,"K",S.K,"T",S.T,"nI",S.nI,"nunk",S.nunk,"nkeep",S.nkeep,"setup %.1fs"%(time.time()-t))
R0=S.resid(S.B0); print("nonzero triples at B0:",int((abs(R0).sum(axis=1)>0).sum()),"classcheck",S.classcheck(R0))
# check consistency: resid(B0+eps) = J0 + L eps + J(eps)
rng=np.random.default_rng(0); e=rng.integers(-3,4,S.nunk).astype(float)
t=time.time(); L=S.jacobian(S.B0); print("jac time %.1fs"%(time.time()-t), L.shape)
lhs=S.resid(S.B0+S.eps_to_B(e))[:,S.keep].ravel()
rhs=S.resid(S.B0)[:,S.keep].ravel()+L@e+S.resid(S.eps_to_B(e))[:,S.keep].ravel()
print("polarization check max err",abs(lhs-rhs).max())
