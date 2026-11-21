"""Round E (part 3): numerical test of the full quadratic Jacobi system J0 + L e + J(e) = 0 over R (integer data lifted
from mod-p arithmetic; valid because coefficients are small).  Many random starts, Levenberg-Marquardt.
Not a proof of non-existence when residual>0; a numerical existence certificate otherwise (can be polished)."""
import sys, itertools, random, numpy as np
from collections import defaultdict
from scipy.optimize import least_squares
from roundE_veronese_poisson import run, p
m=int(sys.argv[1]); fn=sys.argv[2]; nstart=int(sys.argv[3]) if len(sys.argv)>3 else 40
Q0,J0,n1,mons,idx,jac,yadd,brg,ymul = run(m,fn)
def sym(v): return v if v<=p//2 else v-p
bysum=defaultdict(list)
for i in range(n1):
    for j in range(i,n1):
        mu=tuple(mons[i][t]+mons[j][t] for t in range(3)); bysum[mu].append((i,j))
I2=[]
for mu,prs in bysum.items():
    for q in prs[1:]: I2.append({prs[0]:1,q:p-1})
pairs=list(itertools.combinations(range(n1),2))
cols=[(a,b,r) for (a,b) in pairs for r in range(len(I2))]; nc=len(cols)
def tab(es):  # es: list of (col idx, coef)
    B=dict(Q0)
    for c,co in es:
        a,b,r=cols[c]; poly={k:(v*co)%p for k,v in I2[r].items()}
        B[(a,b)]=yadd(B[(a,b)],poly); B[(b,a)]=yadd(B[(b,a)],poly,p-1)
    return B
def jv(J):
    d={}
    for t,poly in J.items():
        for k,v in poly.items(): d[(t,k)]=sym(v)
    return d
def etab(es):  # eps-only table
    B={}
    for c,co in es:
        a,b,r=cols[c]; poly={k:(v*co)%p for k,v in I2[r].items()}
        B[(a,b)]=yadd(B.get((a,b),{}),poly); B[(b,a)]=yadd(B.get((b,a),{}),poly,p-1)
    return B
J0v=jv(J0)
Je1=[jv(jac(etab([(c,1)]))) for c in range(nc)]
Lc=[]
for c in range(nc):
    Jc=jv(jac(tab([(c,1)])))
    d={}
    for k in set(Jc)|set(J0v)|set(Je1[c]):
        v=Jc.get(k,0)-J0v.get(k,0)-Je1[c].get(k,0)
        if v: d[k]=v
    Lc.append(d)
# quadratic tensor via polarization (only pairs c<d)
Qt=defaultdict(dict)  # (c,d)->{rowkey:val}, for J(e)=sum_{c<=d} e_c e_d Qt
for c in range(nc):
    Qt[(c,c)]=Je1[c]
for c in range(nc):
    for d in range(c+1,nc):
        a1,b1,_=cols[c]; a2,b2,_=cols[d]
        # J is a trilinear expression in table entries; entries only interact if brackets share an index; do full eval
        Jcd=jv(jac(etab([(c,1),(d,1)])))
        dd={}
        for k in set(Jcd)|set(Je1[c])|set(Je1[d]):
            v=Jcd.get(k,0)-Je1[c].get(k,0)-Je1[d].get(k,0)
            if v: dd[k]=v
        if dd: Qt[(c,d)]=dd
rowkeys=sorted(set(k for d in Lc for k in d)|set(J0v)|set(k for d in Qt.values() for k in d))
rid={k:i for i,k in enumerate(rowkeys)}; nr=len(rowkeys)
print("rows",nr,"cols",nc,"quadratic pairs",len(Qt))
L=np.zeros((nr,nc)); 
for c,d in enumerate(Lc):
    for k,v in d.items(): L[rid[k],c]=v
j0=np.zeros(nr)
for k,v in J0v.items(): j0[rid[k]]=v
qi=[];qj=[];qr=[];qv=[]
for (c,d),dd in Qt.items():
    for k,v in dd.items(): qi.append(c);qj.append(d);qr.append(rid[k]);qv.append(v)
qi=np.array(qi);qj=np.array(qj);qr=np.array(qr);qv=np.array(qv,float)
def res(e):
    r=j0+L@e
    np.add.at(r,qr,qv*e[qi]*e[qj])
    return r
def jac_(e):
    Jm=L.copy()
    np.add.at(Jm,(qr,qi),qv*e[qj]); np.add.at(Jm,(qr,qj),qv*e[qi])
    return Jm
print("initial |J0| =",np.linalg.norm(j0))
# linear-part least squares minimum
e_lin,*_=np.linalg.lstsq(L,-j0,rcond=None); print("linear-part-only residual:",np.linalg.norm(j0+L@e_lin))
best=1e99
rng=np.random.default_rng(1)
for s in range(nstart):
    e0=rng.normal(size=nc)*(10**rng.uniform(-1,1.5))
    sol=least_squares(res,e0,jac=jac_,method='lm',xtol=1e-14,ftol=1e-14,gtol=1e-14,max_nfev=2000)
    nrm=np.linalg.norm(sol.fun)
    best=min(best,nrm)
    if nrm<1e-9: print("start",s,": SOLUTION residual",nrm,"|e|=",np.linalg.norm(sol.x)); np.save(f"roundE_sol_{fn}_{m}.npy",sol.x); break
print("best residual over",s+1,"starts:",best)
