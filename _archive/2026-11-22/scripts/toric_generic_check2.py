# generic-sigma prediction (refined) vs closed criterion, dim 4 fans. Precomputes weight lists.
import sys,itertools; sys.path.insert(0,'.')
from toric_crit import *
def avec(name,ms):
    rays=FANS[name]; a=[0]*len(rays)
    if name=='P4': a[4]=ms[0]
    if name=='P2xP2': a[2]=ms[0];a[5]=ms[1]
    if name=='P1^4':
        for k in range(4): a[2*k+1]=ms[k]
    if name=='P1xP3': a[1]=ms[0]; a[5]=ms[1]
    if name=='P1xP1xP2': a[1]=ms[0];a[3]=ms[1];a[6]=ms[2]
    return a
def prep(rays,a,box):
    n=len(rays[0]); L=[]
    for chi,C in weights(rays,a,box):
        L.append((chi,C,rk_of(C,n)))
    return L
def crit_fast(L,A,rho,n):
    rhoP=[modfrac(x) for x in rho]; poly=[0]*(n+1)
    for chi,C,s in L:
        v=[(sum(A[i][j]*((chi[j]%P)+rhoP[j]) for j in range(n)))%P for i in range(n)]
        if rk_of(C+[v],n)==s:
            for b in range(s,n+1): poly[b]+=comb(n-s,b-s)
    return poly
def gen_fast(L,rays,a,rho,n):
    lam=set()
    for chi,C,s in L:
        if s==n: lam.add(chi)
        elif s==n-1:
            x=[chi[j]+Fr(rho[j]) for j in range(n)]
            if all(sum(x[j]*u[j] for j in range(n))==0 for u in C): lam.add(chi)
    if all(Fr(x).denominator==1 for x in rho):
        chi=tuple(-int(x) for x in rho)
        d={c:(C,s) for c,C,s in L}
        if chi in d: lam.add(chi)
    d={c:(C,s) for c,C,s in L}
    poly=[0]*(n+1)
    for chi in lam:
        C,s=d[chi]
        for b in range(s,n+1): poly[b]+=comb(n-s,b-s)
    return poly
if __name__=="__main__":
    tests=[('P4',(1,)),('P4',(2,)),('P2xP2',(1,2)),('P1^4',(1,1,1,1)),('P1^4',(1,2,1,3)),('P1xP3',(1,1)),('P1xP1xP2',(1,1,1))]
    tot=bad=0
    for name,ms in tests:
        rays=FANS[name]; n=4; a=avec(name,ms); box=max(a)+n+3
        L=prep(rays,a,box)
        for seed in [101,102]:
            A=randA(n,seed,10**9)
            rhos=list(itertools.product(range(-2,2),repeat=4))+[(Fr(1,2),0,0,0),(Fr(1,3),Fr(1,2),0,0),(0,0,Fr(2,5),-1)]
            for rho in rhos:
                p1=crit_fast(L,A,rho,n); p2=gen_fast(L,rays,a,rho,n); tot+=1
                if p1!=p2: bad+=1; print("MISMATCH",name,ms,rho,p1,p2,flush=True)
        print(name,ms,"done; running mismatches",bad,"of",tot,flush=True)
    print("TOTAL mismatches",bad,"of",tot)
