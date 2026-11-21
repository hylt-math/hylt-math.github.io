# Closed weight criterion: HH Poincare polynomial = sum over weights chi in Lambda of t^s (1+t)^(n-s),
#  Lambda = {chi in M : c_i(chi) >= -1 for all i, A(chi+rho) in span(u_i : c_i(chi) = -1)}, s = rank span(u_i : c_i = -1).
# Valid when E_1^{a>0}=0.  crit_poly implements it directly; generic_pred is the prediction for 'generic' (irrational) A.
import sys,itertools,random; sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
from math import comb
def weights(rays,a,box):
    n=len(rays[0])
    for chi in itertools.product(range(-box,box+1),repeat=n):
        C=[];ok=True
        for u,ai in zip(rays,a):
            c=sum(x*y for x,y in zip(chi,u))+ai
            if c<-1: ok=False;break
            if c==-1: C.append(u)
        if ok: yield chi,C
def rk_of(vecs,n): 
    return rank([[x%P for x in v] for v in vecs],n) if vecs else 0
def crit_poly(rays,a,A,rho,box):
    n=len(rays[0]); rhoP=[modfrac(x) for x in rho]; poly=[0]*(n+1)
    for chi,C in weights(rays,a,box):
        s=rk_of(C,n)
        v=[(sum(A[i][j]*((chi[j]%P)+rhoP[j]) for j in range(n)))%P for i in range(n)]
        if rk_of(C+[v],n)==s:       # v in span(C)
            for b in range(s,n+1): poly[b]+=comb(n-s,b-s)
    return poly
def generic_pred(rays,a,rho,box):
    n=len(rays[0]); poly=[0]*(n+1)
    # vertex weights
    verts=set()
    for chi,C in weights(rays,a,box):
        if rk_of(C,n)==n: verts.add(chi)
    poly[n]+=len(verts)
    # weight -rho
    if all(Fr(x).denominator==1 for x in rho):
        chi=tuple(-int(x) for x in rho)
        if chi not in verts:
            C=[];ok=True
            for u,ai in zip(rays,a):
                c=sum(x*y for x,y in zip(chi,u))+ai
                if c<-1: ok=False;break
                if c==-1: C.append(u)
            if ok:
                s=rk_of(C,n)
                for b in range(s,n+1): poly[b]+=comb(n-s,b-s)
    return poly
def randA(n,seed,big):
    r=random.Random(seed)
    while True:
        A=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                x=r.randint(-big,big); A[i][j]=x; A[j][i]=-x
        # nondegenerate mod P check
        if rk_of([row for row in A],n)==n: return A
FANS={
 'P2':[(1,0),(0,1),(-1,-1)],
 'P1xP1':[(1,0),(-1,0),(0,1),(0,-1)],
 'P4':[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)],
 'P2xP2':[(1,0,0,0),(0,1,0,0),(-1,-1,0,0),(0,0,1,0),(0,0,0,1),(0,0,-1,-1)],
 'P1^4':[(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)],
 'P1xP3':[(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,-1,-1,-1)],
 'P1xP1xP2':[(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1),(0,0,-1,-1)][:0] or [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1),(0,0,-1,-1)],
}
if __name__=="__main__":
    # 1. validate crit_poly == hh (linear algebra) for small A
    rnd=random.Random(0); bad=0; tot=0
    for name,m in [('P2',2),('P1xP1',1),('P4',1),('P2xP2',1),('P1^4',1)]:
        rays=FANS[name]; n=len(rays[0])
        a=[0]*len(rays)
        if name=='P2': a[2]=m
        if name=='P1xP1': a[1]=m;a[3]=m
        if name=='P4': a[4]=m
        if name=='P2xP2': a[2]=m;a[5]=m
        if name=='P1^4': a[1]=m;a[3]=m;a[5]=m;a[7]=m
        for t in range(12):
            A=randA(n,rnd.randint(0,10**6),3)
            rho=[rnd.choice([Fr(0),Fr(-1),Fr(1),Fr(-2),Fr(1,2),Fr(-1,3)]) for _ in range(n)]
            p1=hh(rays,a,A,rho,box=max(a)+n+3); p2=crit_poly(rays,a,A,rho,max(a)+n+3)
            tot+=1
            if p1!=p2: bad+=1; print("MISMATCH",name,A,rho,p1,p2)
    print("crit vs linear algebra: mismatches",bad,"of",tot)
