# Symbolic/exact check of the 2D local formulas used in ncd_theorem.md (Sect. 4):
#   sigma = h d1^d2, h = z1 z2 u (node) or z u (smooth);  module e with  nabla_beta e = Theta(beta) e,
#   Theta(dz1)=theta_2*h/z2, Theta(dz2)=-theta_1*h/z1  where theta = theta_1 dz1/z1 + theta_2 dz2/z2 = sum r_i dlog z_i + dg.
# Checks: (i) d1 d0 = 0 (consistency of d0 f = -X_f + f V  and the CE 2-cochain formula);
#         (ii) d1(p d1 + q d2) == -u[(1-r1) z2 p + (1-r2) z1 q]  mod z1 z2  for arbitrary polynomial p,q.
from fractions import Fraction as Fr
import random
random.seed(1)
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
def rnd(deg,c0=None):
    p={}
    for a in range(deg+1):
        for b in range(deg+1-a):
            if random.random()<0.6: p[(a,b)]=Fr(random.randint(-3,3))
    p={k:v for k,v in p.items() if v!=0}
    if c0 is not None: p[(0,0)]=Fr(c0)
    return p
z1={(1,0):Fr(1)}; z2={(0,1):Fr(1)}
def divvar(p,i):  # exact division by z_i
    r={}
    for k,v in p.items():
        assert k[i]>=1
        kk=list(k); kk[i]-=1; r[tuple(kk)]=v
    return r
def run(node=True):
    r1,r2=Fr(random.randint(-4,4),random.choice([1,2,3])),Fr(random.randint(-4,4),random.choice([1,2,3]))
    u=rnd(2,1)            # unit (u(0)=1)
    g=rnd(3)
    if node:
        h=mul(mul(z1,z2),u)
    else:
        h=mul(z1,u)
        # smooth model: D={z1=0}, second coordinate z2=w; theta=r1 dz1/z1 + dg  (theta_2 holomorphic)
    g1,g2=d(g,0),d(g,1)
    th1=add({(0,0):r1},mul(z1,g1))
    if node:
        th2=add({(0,0):r2},mul(z2,g2))
        a=mul(th2,divvar(h,1))             # Theta(dz1)=theta_2 h/z2
    else:
        th2=g2                             # holomorphic 1-form coefficient of dz2
        a=mul(th2,h)                       # theta(h d2)=theta_2*h   (theta_2 coefficient of dz2, not dz2/z2)
    b=sc(mul(th1,divvar(h,0)),-1)          # Theta(dz2)=-theta_1 h/z1
    def d0(f):
        # d0 f = -X_f + f V , X_f = h (f_1 d2 - f_2 d1)
        c1=add(sc(mul(h,d(f,1)),1),mul(f,a))     # +h f_2 d1 + f a d1
        c2=add(sc(mul(h,d(f,0)),-1),mul(f,b))    # -h f_1 d2 + f b d2
        return c1,c2
    def d1(p,q):
        t=mul(h,add(d(p,0),d(q,1)))
        t=add(t,add(mul(d(h,0),p),mul(d(h,1),q)),-1)
        t=add(t,mul(q,a)); t=add(t,mul(p,b),-1)
        return t
    ok=True
    for _ in range(5):
        f=rnd(3)
        c1,c2=d0(f)
        if d1(c1,c2): ok=False
    # (ii)
    ok2=True
    for _ in range(5):
        p,q=rnd(3),rnd(3)
        lhs=d1(p,q)
        if node:
            rhs=sc(mul(u,add(sc(mul(z2,p),1-r1),sc(mul(z1,q),1-r2))),-1)
            diff=add(lhs,rhs,-1)
            # divisible by z1 z2 ?
            ok2&=all(k[0]>=1 and k[1]>=1 for k in diff)
        else:
            rhs=sc(mul(u,sc(p,1-r1)),-1)   # -(1-r) u p  mod z1
            diff=add(lhs,rhs,-1)
            ok2&=all(k[0]>=1 for k in diff)
    return r1,r2,ok,ok2
for node in (True,False):
    res=[run(node) for _ in range(20)]
    print("node" if node else "smooth", "d1d0=0:",all(x[2] for x in res)," dQ formula:",all(x[3] for x in res))
