# Exact check, any complex dimension n, of the transposition identity behind HH duality:
#   <[σ,P]+V^P , Q> + s <P, [σ,Q]+V'^Q> = total divergence  (tested by Res = coefficient of z^(-1,..,-1) on Laurent polynomials)
# for P in wedge^b T, Q in wedge^(n-b-1) T, σ an ARBITRARY bivector (Poisson not needed), and V' = -V + c*M, M^j = sum_i d_i σ^{ij}.
# Result: c = ?  (solve per trial; must be constant).
import random, itertools, sys
from fractions import Fraction as Fr
random.seed(11)
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        nv=r.get(k,0)+s*v
        if nv==0: r.pop(k,None)
        else: r[k]=nv
    return r
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def pd(p,i):
    r={}
    for k,v in p.items():
        if k[i]!=0:
            kk=list(k); kk[i]-=1; r[tuple(kk)]=r.get(tuple(kk),0)+v*k[i]
    return {k:v for k,v in r.items() if v!=0}
def psc(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def rndpoly(n,rng=1,terms=3):
    p={}
    for _ in range(terms):
        k=tuple(random.randint(-rng,rng) for _ in range(n)); p[k]=Fr(random.randint(-3,3))
    return {k:v for k,v in p.items() if v!=0}
# multivectors: dict sorted-index-tuple -> poly
def madd(A,B,s=1):
    R={k:dict(v) for k,v in A.items()}
    for k,v in B.items():
        R[k]=padd(R.get(k,{}),v,s)
        if not R[k]: del R[k]
    return R
def msc(A,c): return {k:psc(v,c) for k,v in A.items() if psc(v,c)}
def sign_sort(idx):
    idx=list(idx); s=1
    for i in range(len(idx)):
        for j in range(len(idx)-1-i):
            if idx[j]>idx[j+1]: idx[j],idx[j+1]=idx[j+1],idx[j]; s=-s
    return s,tuple(idx)
def wedge(A,B):
    R={}
    for I,p in A.items():
        for J,q in B.items():
            if set(I)&set(J): continue
            s,K=sign_sort(I+J)
            R[K]=padd(R.get(K,{}),psc(pmul(p,q),s))
            if not R[K]: del R[K]
    return R
def deg(A):
    for k in A: return len(k)
    return None
def dtheta_right(A,i):
    R={}
    for I,p in A.items():
        if i in I:
            pos=I.index(i); s=(-1)**(len(I)-1-pos)
            K=tuple(x for x in I if x!=i)
            R[K]=padd(R.get(K,{}),psc(p,s))
    return R
def dz(A,i): return {I:pd(p,i) for I,p in A.items() if pd(p,i)}
def schouten(A,a,B,b,n):
    R={}
    for i in range(n):
        R=madd(R,wedge(dtheta_right(A,i),dz(B,i)))
        R=madd(R,msc(wedge(dtheta_right(B,i),dz(A,i)),-((-1)**((a-1)*(b-1)))))
    return R
def rmult(n,b,terms=2):
    A={}
    for I in itertools.combinations(range(n),b):
        A[I]=rndpoly(n,terms=terms)
    return {k:v for k,v in A.items() if v}
def res(p,n): return p.get(tuple([-1]*n),Fr(0))
def top(A,n): return A.get(tuple(range(n)),{})
def rmult_k(n,b,k):
    A={}
    for I in itertools.combinations(range(n),b):
        c=Fr(random.randint(-3,3))
        if c!=0: A[I]={tuple(k):c}
    return A
def run(n):
    out={}
    for b in range(0,n):
        for s in (1,-1):
            cs=[]
            for trial in range(8):
                i0=random.randrange(n)
                ks=[random.randint(-2,2) for _ in range(n)]; kp=[random.randint(-2,2) for _ in range(n)]
                kq=[-1-ks[j]-kp[j]+(1 if j==i0 else 0) for j in range(n)]
                kv=[ks[j]-(1 if j==i0 else 0) for j in range(n)]
                sigma=rmult_k(n,2,ks); V=rmult_k(n,1,kv); P=rmult_k(n,b,kp); Q=rmult_k(n,n-b-1,kq)
                M={}
                for j in range(n):
                    m={}
                    for i in range(n):
                        if i==j: continue
                        key=(min(i,j),max(i,j)); sg=1 if i<j else -1
                        m=padd(m,pd(sigma.get(key,{}),i),sg)
                    if m: M[(j,)]=m
                def G(c):
                    dP=madd(schouten(sigma,2,P,b,n) if b>=0 else {}, wedge(V,P))
                    Vp=madd(msc(V,-1),msc(M,c))
                    dQ=madd(schouten(sigma,2,Q,n-b-1,n), wedge(Vp,Q))
                    return padd(top(wedge(dP,Q),n), psc(top(wedge(P,dQ),n),s))
                r0=res(G(Fr(0)),n); r1=res(G(Fr(1)),n)-r0
                if r1==0: cs.append(('r1=0',r0))
                else: cs.append(-r0/r1)
            out[(b,s)]=cs
    return out
if __name__=="__main__":
    for n in (2,3,4):
        print("n=",n)
        o=run(n)
        for k,v in o.items(): print("  b,s=",k,[str(x) for x in v])
