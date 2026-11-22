# Round J2: Poisson-Kodaira for P1xP1 (Segre m=1): classical Sklyanin quadratic Poisson structure on C^4 (Feigin-Odesskii q_{4,1}(E)).
# Check numerically (finite precision, exact rational arithmetic via Fractions): Jacobi; Casimirs Q1=sum x_i^2, Q2=sum J_i x_i^2 (to be tested);
# then each quadric Q1 - lam*Q2 is Poisson subvariety (a symplectic leaf closure) = Segre P1xP1; degeneracy locus = Q1=Q2=0 (elliptic quartic).
import itertools, random
from fractions import Fraction as Fr
J=[Fr(2),Fr(3),Fr(7)]          # J1,J2,J3 generic
def Jab(a,b,c): return (J[a]-J[b])   # corrected: coefficient J_j-J_k (no division); Jacobi verified below
# structure constants: {x_i,x_j}=sum c[i][j][(k,l)] x_k x_l
def build(sign):
    br={}
    def put(i,j,coef,k,l):
        br.setdefault((i,j),{}); br[(i,j)][(k,l)]=br[(i,j)].get((k,l),0)+coef
        br.setdefault((j,i),{}); br[(j,i)][(k,l)]=br[(j,i)].get((k,l),0)-coef
    # indices 0..3 = x0,x1,x2,x3
    put(0,1,sign*Jab(1,2,0),2,3)   # {x0,x1}=J23 x2x3 with J23=(J2-J3)/J1
    put(0,2,sign*Jab(2,0,1),3,1)
    put(0,3,sign*Jab(0,1,2),1,2)
    put(2,3,1,0,1); put(3,1,1,0,2); put(1,2,1,0,3)
    return br
def pmul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=tuple(sorted(k1+k2)); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def padd(a,b,c=1):
    r=dict(a)
    for k,v in b.items(): r[k]=r.get(k,0)+c*v
    return {k:v for k,v in r.items() if v!=0}
def pd(a,i):
    r={}
    for k,v in a.items():
        if i in k:
            l=list(k); l.remove(i); kk=tuple(l); r[kk]=r.get(kk,0)+v*k.count(i)
    return {k:v for k,v in r.items() if v!=0}
def bracket(br,f,g):
    r={}
    for i in range(4):
        fi=pd(f,i)
        if not fi: continue
        for j in range(4):
            gj=pd(g,j)
            if not gj: continue
            c=br.get((i,j),{})
            if not c: continue
            cp={tuple(sorted(k)):v for k,v in c.items()}
            r=padd(r,pmul(pmul(fi,gj),cp))
    return r

X=[{(i,):Fr(1)} for i in range(4)]
br=build(1)
bad=0
for i,j,k in itertools.combinations(range(4),3):
    t=padd(padd(bracket(br,X[i],bracket(br,X[j],X[k])),bracket(br,X[j],bracket(br,X[k],X[i]))),bracket(br,X[k],bracket(br,X[i],X[j])))
    if t: bad+=1
print("Jacobi violations (of 4 triples):",bad)
# quadratic Casimirs: Q=sum_{a<=b} q_ab x_a x_b ; solve {Q,x_i}=0 by linear algebra (Fractions)
mons=[(a,b) for a in range(4) for b in range(a,4)]
cols=[]
for m in mons:
    Q={m:Fr(1)}
    cols.append([bracket(br,Q,X[i]) for i in range(4)])
keys=sorted({(i,k) for c in cols for i in range(4) for k in c[i]})
rows=[[c[i].get(k,Fr(0)) for c in cols] for (i,k) in keys]
# nullspace
def nullspace(M,n):
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(n):
        pr=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]; iv=1/M[r][c]; M[r]=[x*iv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        v=[Fr(0)]*n; v[f]=Fr(1)
        for row,pc in zip(M,piv): v[pc]=-row[f]
        out.append(v)
    return out
ns=nullspace(rows,len(mons))
print("dim of space of quadratic Casimirs:",len(ns))
for v in ns: print({m:str(c) for m,c in zip(mons,v) if c!=0})
# rank of pi at random rational point and on cone Q1=0 (if Q1=sum x_i^2 is Casimir)
import random
random.seed(1)
def pimat(x):
    M=[[Fr(0)]*4 for _ in range(4)]
    for (i,j),c in br.items():
        M[i][j]=sum(v*x[k]*x[l] for (k,l),v in c.items())
    return M
def rank(M):
    M=[r[:] for r in M]; r=0
    for c in range(4):
        pr=next((i for i in range(r,4) if M[i][c]!=0),None)
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]
        for i in range(r+1,4):
            f=M[i][c]/M[r][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        r+=1
    return r
x=[Fr(random.randint(1,9)) for _ in range(4)]
print("generic rank of pi:",rank(pimat(x)))
