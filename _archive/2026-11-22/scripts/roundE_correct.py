"""Round E (part 2): solve for eps in Hom(Lambda^2 S_1, I_2) s.t. Pi0+eps is Poisson (Jacobi), Veronese m.
Linear part J0 + L(eps) = 0 first (mod p), then the quadratic residual on the affine solution space."""
import sys, itertools, random
from roundE_veronese_poisson import run, p, inv
m=int(sys.argv[1]); fn=sys.argv[2]
Q0,J0,n1,mons,idx,jac,yadd,brg,ymul = run(m,fn)
# I_2 basis
from collections import defaultdict
bysum=defaultdict(list)
for i in range(n1):
    for j in range(i,n1):
        mu=tuple(mons[i][t]+mons[j][t] for t in range(3)); bysum[mu].append((i,j))
I2=[]
for mu,pairs in bysum.items():
    base=pairs[0]
    for q in pairs[1:]:
        I2.append({base:1,q:p-1})
print("dim I_2 =",len(I2),"dim S_2 =",n1*(n1+1)//2)
pairs=list(itertools.combinations(range(n1),2))
cols=[(a,b,r) for (a,b) in pairs for r in range(len(I2))]
print("unknowns:",len(cols))
def table_with(e):  # e: dict (a,b,r)->coef  (only a<b)
    B=dict(Q0)
    for (a,b,r),c in e.items():
        poly={k:(v*c)%p for k,v in I2[r].items()}
        B[(a,b)]=yadd(B[(a,b)],poly); B[(b,a)]=yadd(B[(b,a)],poly,p-1)
    return B
def jvec(J):
    d={}
    for t,poly in J.items():
        for k,v in poly.items(): d[(t,k)]=v
    return d
J0v=jvec(J0)
# columns of L
Lcols=[]
for c in cols:
    B=table_with({c:1}); Jc=jvec(jac(B)); Jq=jvec(jac({k:v for k,v in table_with({c:1}).items()} if False else {}))  # placeholder
    # J(Pi0+e)=J0+L e+J(e); J(e) for e-only table:
    Be=defaultdict(dict)
    a,b,r=c
    Be[(a,b)]=I2[r]; Be[(b,a)]={k:(-v)%p for k,v in I2[r].items()}
    Je=jvec(jac(dict(Be)))
    col={}
    keys=set(Jc)|set(J0v)|set(Je)
    for k in keys:
        v=(Jc.get(k,0)-J0v.get(k,0)-Je.get(k,0))%p
        if v: col[k]=v
    Lcols.append(col)
# linear system L e = -J0
rowkeys=sorted(set(k for col in Lcols for k in col)|set(J0v))
rid={k:i for i,k in enumerate(rowkeys)}
nr=len(rowkeys); nc=len(cols)
print("rows:",nr,"cols:",nc)
# Gaussian elimination on augmented columns (dense, mod p) using lists of row dicts
rows=[dict() for _ in range(nr)]
for j,col in enumerate(Lcols):
    for k,v in col.items(): rows[rid[k]][j]=v
for k,v in J0v.items(): rows[rid[k]][nc]=(-v)%p
piv={}
order=[]
for r in rows:
    r=dict(r)
    for c0,pr in piv.items():
        if c0 in r:
            f=r[c0]
            for k,v in pr.items():
                r[k]=(r.get(k,0)-f*v)%p
                if r[k]==0: del r[k]
    cs=[k for k in r if k<nc]
    if not cs:
        if r.get(nc,0)!=0:
            print("LINEAR PART INCONSISTENT: no eps with J0+L eps=0 ->", "(this does not by itself exclude quadratic solutions)")
            sys.exit(0)
        continue
    c0=min(cs); f=inv(r[c0]); r={k:(v*f)%p for k,v in r.items()}
    for c1,pr in list(piv.items()):
        if c0 in pr:
            g=pr[c0]
            for k,v in r.items():
                pr[k]=(pr.get(k,0)-g*v)%p
                if pr[k]==0: del pr[k]
    piv[c0]=r
rank=len(piv)
print("rank of L (augmented consistent):",rank,"; kernel dim =",nc-rank)
# particular solution (free vars = 0)
e0={}
for c0,pr in piv.items():
    v=pr.get(nc,0)
    if v: e0[cols[c0]]=v
B=table_with(e0); Jr=jvec(jac(B))
print("residual Jacobi (quadratic part) for particular linear solution: nonzero terms =",len(Jr))
if not Jr: print("==> POISSON EXTENSION FOUND (quadratic Poisson structure on P^N extending sigma) mod",p)
else:
    # try random points of the affine solution space to see if any kills residual (heuristic only)
    free=[c for c in range(nc) if c not in piv]
    best=len(Jr)
    for t in range(30):
        e=dict(e0); 
        for c in free:
            val=random.randrange(p)
            # adjust pivots: x_piv = rhs - sum pr[c]*x_c
            e[cols[c]]=(e.get(cols[c],0)+val)%p
            for c0,pr in piv.items():
                if c in pr: e[cols[c0]]=(e.get(cols[c0],0)-pr[c]*val)%p
        e={k:v for k,v in e.items() if v}
        nzr=len(jvec(jac(table_with(e))))
        best=min(best,nzr)
    print("random affine samples: min #nonzero Jacobi terms =",best,"(not a proof of non-existence)")
