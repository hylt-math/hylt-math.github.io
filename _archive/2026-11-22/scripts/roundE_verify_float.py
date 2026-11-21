"""Independent float verification of the numerically found quadratic Poisson structure on C^6 (Veronese m=2, Fermat):
(1) Jacobi identity {a,{b,c}}+cyc=0 on random points via explicit finite differences of the bivector; (2) restriction to the Veronese cone equals Pi_F."""
import numpy as np, itertools, sys
from roundE_veronese_poisson import run, p
fn=sys.argv[1]; m=2
e=np.load(f"roundE_sol_{fn}_{m}.npy")
from collections import defaultdict
Q0,J0,n1,mons,idx,jac,yadd,brg,ymul = run(m,fn)
def sym(v): return v if v<=p//2 else v-p
bysum=defaultdict(list)
for i in range(n1):
    for j in range(i,n1):
        mu=tuple(mons[i][t]+mons[j][t] for t in range(3)); bysum[mu].append((i,j))
I2=[]
for mu,prs in bysum.items():
    for q in prs[1:]: I2.append({prs[0]:1.0,q:-1.0})
pairs=list(itertools.combinations(range(n1),2))
cols=[(a,b,r) for (a,b) in pairs for r in range(len(I2))]
# float bracket table: B[(a,b)] = dict monomial->float
B={k:{kk:float(sym(v)) for kk,v in d.items()} for k,d in Q0.items()}
for c,co in enumerate(e):
    a,b,r=cols[c]
    for kk,v in I2[r].items():
        B[(a,b)][kk]=B[(a,b)].get(kk,0)+co*v; B[(b,a)][kk]=B[(b,a)].get(kk,0)-co*v
def Pi(y):
    P=np.zeros((n1,n1))
    for (a,b),d in B.items():
        P[a,b]=sum(v*y[i]*y[j] for (i,j),v in d.items())
    return P
def jacobi(y,h=1e-5):
    # {y_a,{y_b,y_c}} = sum_d Pi_ad d_d Pi_bc ; cyclic
    P=Pi(y); dP=np.zeros((n1,n1,n1))
    for d in range(n1):
        yp=y.copy(); yp[d]+=h; ym=y.copy(); ym[d]-=h
        dP[d]=(Pi(yp)-Pi(ym))/(2*h)
    J=np.zeros((n1,n1,n1))
    for a,b,c in itertools.product(range(n1),repeat=3):
        J[a,b,c]=sum(P[a,d]*dP[d,b,c]+P[b,d]*dP[d,c,a]+P[c,d]*dP[d,a,b] for d in range(n1))
    return np.abs(J).max()
rng=np.random.default_rng(0)
for t in range(3):
    y=rng.normal(size=n1); print("max |Jacobiator| at random point (|y|~1):",jacobi(y))
# restriction to cone: y=nu(x)
def nu(x): return np.array([np.prod([x[i]**mm[i] for i in range(3)]) for mm in mons])
x=rng.normal(size=3); y=nu(x); P=Pi(y)
F={'fermat':lambda x:(3*x[0]**2,3*x[1]**2,3*x[2]**2),'xyz':lambda x:(x[1]*x[2],x[0]*x[2],x[0]*x[1])}.get(fn)
if F:
    g=np.array(F(x)); Pix=np.array([[0,g[2],-g[1]],[-g[2],0,g[0]],[g[1],-g[0],0]])
    # Jacobian of nu
    Jn=np.zeros((n1,3))
    for k in range(3):
        xp=x.copy(); xp[k]+=1e-6; xm=x.copy(); xm[k]-=1e-6; Jn[:,k]=(nu(xp)-nu(xm))/2e-6
    print("restriction error |Pi(nu(x)) - Dnu Pi_F Dnu^T| =",np.abs(P-Jn@Pix@Jn.T).max())
