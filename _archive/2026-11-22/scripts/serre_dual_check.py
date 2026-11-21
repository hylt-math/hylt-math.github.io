# Exact check (pure Python, rational polynomials) that d_L is transposed to +-d_{L'} for L' = L^v (x) K_X^2,
# module structure of K_X: V_K = (h_2, -h_1) (Lie derivative).  Surface, sigma = h d1^d2.
# Identity checked as TOTAL DIVERGENCE:  <d f,beta> + eps <f,d' beta> = d1(A)+d2(B)  for random polynomial data.
from fractions import Fraction as Fr
import random
random.seed(5)
def add(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        nv=r.get(k,0)+s*v
        if nv==0: r.pop(k,None)
        else: r[k]=nv
    return r
def mul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=(k1[0]+k2[0],k1[1]+k2[1]); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def d(p,i):
    r={}
    for k,v in p.items():
        if k[i]>0:
            kk=list(k); kk[i]-=1; r[tuple(kk)]=r.get(tuple(kk),0)+v*k[i]
    return {k:v for k,v in r.items() if v!=0}
def sc(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def rnd(deg=2):
    p={}
    for a in range(deg+1):
        for b in range(deg+1-a):
            p[(a,b)]=Fr(random.randint(-3,3))
    return {k:v for k,v in p.items() if v!=0}
neg=lambda p: sc(p,-1)
for trial in range(20):
    h,a,b,f,pp,qq,P,Q,g=[rnd() for _ in range(9)]
    h1,h2=d(h,0),d(h,1)
    ap=add(neg(a),sc(h2,2)); bp=add(neg(b),sc(h1,-2))          # V' = -V + 2 V_K
    d0=lambda f,a,b:(add(mul(h,d(f,1)),mul(f,a)), add(neg(mul(h,d(f,0))),mul(f,b)))
    def d1(p,q,a,b):
        r=mul(h,add(d(p,0),d(q,1)))
        r=add(r,mul(h1,p),-1); r=add(r,mul(h2,q),-1)
        r=add(r,mul(q,a)); r=add(r,mul(p,b),-1); return r
    # b=0->1 : <X,Y> = X1 Y2 - X2 Y1, <f,c> = f c
    X=d0(f,a,b); lhs=add(mul(X[0],qq),mul(X[1],pp),-1)
    rhs=mul(f,d1(pp,qq,ap,bp))
    tot=add(lhs,rhs)                       # eps=-1 : lhs = -rhs + div  => lhs + rhs = div
    A=mul(mul(h,f),pp); B=mul(mul(h,f),qq)
    div=add(d(A,0),d(B,1))
    assert add(tot,div,-1)=={}, "0->1 fails"
    # b=1->2 : <d1 X, g'> vs <X, d0' g'>, eps=+1 : lhs - rhs = div
    lhs=mul(d1(P,Q,a,b),g)
    Y=d0(g,ap,bp); rhs=add(mul(P,Y[1]),mul(Q,Y[0]),-1)
    A=mul(mul(h,g),P); B=mul(mul(h,g),Q)
    assert add(add(lhs,rhs,-1),add(d(A,0),d(B,1)),-1)=={}, "1->2 fails"
print("transposition identities hold exactly (20 random trials): <d f,b> = -<f,d'b> + div ; <d X,g> = +<X,d'g> + div ; L' = L^v K^2, V'=-V+2V_K")
