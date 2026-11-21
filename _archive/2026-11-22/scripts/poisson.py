import itertools, sys
from math import comb
P=32003
def monos(d):
    return [(a,b,d-a-b) for a in range(d+1) for b in range(d-a+1)] if d>=0 else []
# polynomials: dict {(a,b,c):coef mod P}
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        r[k]=(r.get(k,0)+s*v)%P
    return {k:v for k,v in r.items() if v}
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=(k1[0]+k2[0],k1[1]+k2[1],k1[2]+k2[2]); r[k]=(r.get(k,0)+v1*v2)%P
    return {k:v for k,v in r.items() if v}
def pdiff(p,i):
    r={}
    for k,v in p.items():
        if k[i]>0:
            kk=list(k); kk[i]-=1; r[tuple(kk)]=(r.get(tuple(kk),0)+v*k[i])%P
    return {k:v for k,v in r.items() if v}
def pscale(p,c): return {k:(v*c)%P for k,v in p.items() if (v*c)%P}
X=[{(1,0,0):1},{(0,1,0):1},{(0,0,1):1}]
def eps(i,j,k):
    return {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.get((i,j,k),0)
def rank(rows):
    rows=[dict(r) for r in rows if r]
    piv={}; rk=0
    for r in rows:
        r=dict(r)
        while r:
            k=min(r)
            if k in piv:
                pr=piv[k]; c=r[k]*pow(pr[k],P-2,P)%P
                for kk,vv in pr.items():
                    nv=(r.get(kk,0)-c*vv)%P
                    if nv: r[kk]=nv
                    else: r.pop(kk,None)
            else:
                piv[k]=r; rk+=1; break
    return rk
def run(F,m):
    dF=[pdiff(F,i) for i in range(3)]
    Pi=[[ {} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                e=eps(i,j,k)
                if e: Pi[i][j]=padd(Pi[i][j],pscale(dF[k],e%P))
    def delta0(s): # vector Pi^{ij} d_j s
        v=[]
        for i in range(3):
            c={}
            for j in range(3): c=padd(c,pmul(Pi[i][j],pdiff(s,j)))
            v.append(c)
        return v
    def vec_apply(Xv,p): # X(p)
        c={}
        for k in range(3): c=padd(c,pmul(Xv[k],pdiff(p,k)))
        return c
    def delta1(Xv): # scalar E.b
        B=[[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                t=vec_apply(Xv,Pi[i][j])
                for k in range(3):
                    t=padd(t,pmul(Pi[k][j],pdiff(Xv[i],k)),-1)
                    t=padd(t,pmul(Pi[i][k],pdiff(Xv[j],k)),-1)
                B[i][j]=t
        sc={}
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    e=eps(k,i,j)
                    if e: sc=padd(sc,pmul(X[k],pscale(B[i][j],(e*pow(2,P-2,P))%P)))
        return sc
    # index vectors as flat dict keys (comp,mono)
    def flat(v): return {(c,)+k:val for c in range(3) for k,val in v[c].items()}
    r0=r1=None
    ms=monos(m)
    imgs=[delta0({mm:1}) for mm in ms]
    Es=[[pmul(X[i],{mm:1}) for i in range(3)] for mm in ms]
    rankfull=rank([flat(v) for v in imgs]+[flat(e) for e in Es])
    r0=rankfull-len(ms) if m>=0 else 0   # rank of delta0 in quotient V/(E P_m)
    # delta1 on all vector fields of degree m+1
    r1=0
    if m+1>=0:
        rows=[]
        for c in range(3):
            for mm in monos(m+1):
                Xv=[{},{},{}]; Xv[c]={mm:1}
                rows.append(delta1(Xv))
        r1=rank(rows)
    # check d1 d0 =0
    z=all(not delta1(v) for v in imgs)
    return r0,r1,z
if __name__=="__main__":
    Ff={(3,0,0):1,(0,3,0):1,(0,0,3):1}
    Fh=dict(Ff); Fh[(1,1,1)]=5
    for name,F in (("Fermat",Ff),("Hesse5",Fh)):
        print(name)
        for m in range(0,7):
            r0,r1,z=run(F,m)
            h0O=comb(m+2,2); h0T=(m+4)*(m+2); h0K=comb(m+5,2)
            H0=h0O-r0; H1=h0T-r0-r1; H2=h0K-r1
            print(m,"h0:",h0O,h0T,h0K,"ranks",r0,r1,"d1d0=0",z,"=> H0,H1,H2 =",H0,H1,H2)
