"""F=x^3 (m=3): exact rational solution of the single-monomial problem (unknowns of shift nu_0). Entries are multiples of 1/8, hence exactly representable
in float64; all products/sums below are exact, so a zero residual is an exact statement."""
import numpy as np
from pkcore import *
import v0_system
from restricted import solve_restricted
S=Setup(3,FS['x3']); from shifts import unknown_shifts
sh=unknown_shifts(S); mask=np.array([s==v0_system.NU[0] for s in sh])
rng=np.random.default_rng(1); e,nr=solve_restricted(S,mask,rng.normal(size=S.nunk)*3)
print("float LM residual",nr,"|e|",np.linalg.norm(e))
er=np.rint(e*8)/8; print("max |e - round(8e)/8| =",abs(e-er).max(),"; distinct nonzero values (x8):",sorted(set(np.rint(er[er!=0]*8).astype(int)))[:20])
R=S.resid(S.B0+S.eps_to_B(er))
print("EXACT Jacobiator of (B0+eps) with eps rounded to multiples of 1/8: max |coeff| =",abs(R).max(),"(over all 120 triples x 220 cubic monomials)")
np.save('x3_exact_eps.npy',er)
