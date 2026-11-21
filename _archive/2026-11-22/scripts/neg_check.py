# Independent check for m<=-4: hypercohomology of (wedge T(m), d_sigma) computed directly on
# H^2(P^2,O(k)) = span{x^a : all a_i<=-1, |a|=k} (Cech/local cohomology), no Serre duality used.
# H^2(T(m)) = H^2(O(m+1))^3 / E.H^2(O(m)) (Euler sequence; E.: injective for m<=-4).
import sys
from poisson import padd,pmul,pscale,eps,rank,P
from itertools import product
def neg_monos(d):  # all exponents <=-1, sum=d
    out=[]
    if d>-3: return out
    for a in range(-1,d+1,-1):
        for b in range(-1,d-a,-1):
            c=d-a-b
            if c<=-1: out.append((a,b,c))
    return out
def proj(p): return {k:v for k,v in p.items() if all(e<0 for e in k)}
def ldiff(p,i):  # derivative on Laurent polynomials
    r={}
    for k,v in p.items():
        if k[i]!=0:
            kk=list(k); kk[i]-=1; kk=tuple(kk); r[kk]=(r.get(kk,0)+v*k[i])%P
    return {k:v for k,v in r.items() if v}
def pm(p,q): return pmul(p,q)
def setup(F):
    dF=[]
    for i in range(3):
        r={}
        for k,v in F.items():
            if k[i]>0:
                kk=list(k); kk[i]-=1; r[tuple(kk)]=(r.get(tuple(kk),0)+v*k[i])%P
        dF.append(r)
    Pi=[[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                e=eps(i,j,k)
                if e: Pi[i][j]=padd(Pi[i][j],pscale(dF[k],e%P))
    return Pi
X=[{(1,0,0):1},{(0,1,0):1},{(0,0,1):1}]
def run(F,m):
    Pi=setup(F)
    V0=neg_monos(m); V1=neg_monos(m+1); V2=neg_monos(m+3)
    def d0(s):
        return [proj(__import__('functools').reduce(lambda a,b:padd(a,b),[pm(Pi[i][j],ldiff(s,j)) for j in range(3)],{})) for i in range(3)]
    def vapply(Xv,p):
        c={}
        for k in range(3): c=padd(c,pm(Xv[k],ldiff(p,k)))
        return c
    def d1(Xv):
        sc={}
        for i in range(3):
            for j in range(3):
                t=vapply(Xv,Pi[i][j])
                for k in range(3):
                    t=padd(t,pm(Pi[k][j],ldiff(Xv[i],k)),-1)
                    t=padd(t,pm(Pi[i][k],ldiff(Xv[j],k)),-1)
                for k in range(3):
                    e=eps(k,i,j)
                    if e: sc=padd(sc,pm(X[k],pscale(t,(e*pow(2,P-2,P))%P)))
        return proj(sc)
    def flat(v): return {(c,)+k:val for c in range(3) for k,val in v[c].items()}
    imgs=[d0({a:1}) for a in V0]
    Es=[[proj(pm(X[i],{a:1})) for i in range(3)] for a in V0]
    rE=rank([flat(e) for e in Es]); assert rE==len(V0),"Euler map not injective"
    rfull=rank([flat(v) for v in imgs]+[flat(e) for e in Es])
    r0=rfull-rE                       # rank of d0 into H^2(T(m))
    dimT=3*len(V1)-len(V0)            # dim H^2(T(m))
    rows=[]
    for c in range(3):
        for a in V1:
            Xv=[{},{},{}]; Xv[c]={a:1}; rows.append(d1(Xv))
    r1=rank(rows)                     # rank of d1 on 3*V1 (should kill E.V0)
    killsE=all(not d1(e) for e in Es)
    comp=all(not d1(v) for v in imgs)
    # H^2=ker d0, H^3=ker d1/im d0, H^4=coker d1  (total degrees 2,3,4)
    H2=len(V0)-r0; H3=dimT-r1-r0; H4=len(V2)-r1
    return dict(dims=(len(V0),dimT,len(V2)),r0=r0,r1=r1,d1_kills_E=killsE,d1d0=comp,H=[0,0,H2,H3,H4])
if __name__=="__main__":
    Ff={(3,0,0):1,(0,3,0):1,(0,0,3):1}
    Fh=dict(Ff); Fh[(1,1,1)]=5
    for name,F in (("Fermat",Ff),("Hesse5",Fh)):
        print(name)
        for m in range(-4,-16,-1):
            r=run(F,m); print(m,r)
