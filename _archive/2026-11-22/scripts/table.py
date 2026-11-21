from poisson import *
from math import comb
def h(p,q,k):  # h^q(P2, Omega^p(k)), Bott
    if p==0:
        if q==0: return comb(k+2,2) if k>=0 else 0
        if q==2: return comb(-k-1,2) if k<=-3 else 0
        return 0
    if p==1:
        if q==0: return (k+1)*(k-1) if k>=2 else 0
        if q==1: return 1 if k==0 else 0
        if q==2: return (1-k)*(-k-1) if -k>=2 else 0   # dual of h0(Omega1(-k))
        return 0
    if p==2: return h(0,q,k-3)   # K=O(-3): Omega^2(k)=O(k-3)
# E1 table: b=0:O(m)=Omega^0(m), b=1:T(m)=Omega^1(m+3), b=2:O(m+3)
def E1(m):
    return {(a,b):h(*( (0,a,m) if b==0 else (1,a,m+3) if b==1 else (0,a,m+3)))  for a in range(3) for b in range(3)}
Ff={(3,0,0):1,(0,3,0):1,(0,0,3):1}
def hyper(m):
    # direct computation for m>=-2; duality for m<=-4; m=-3 by hand
    if m>=-2:
        r0,r1,z=run(Ff,m); assert z
        e=E1(m); assert all(e[(a,b)]==0 for a in (1,2) for b in range(3)),(m,e)
        h0O,h0T,h0K=e[(0,0)],e[(0,1)],e[(0,2)]
        return [h0O-r0,h0T-r0-r1,h0K-r1,0,0]
    if m==-3: return [0,0,3,0,0]
    d=hyper(-m-6); return d[::-1]
for m in range(-3,10):
    e=E1(m); chi=sum((-1)**(a+b)*v for (a,b),v in e.items())
    print(m,"chi(E1)=",chi)
print("hypercohomology dims [H0..H4] of (wedge T (x) O(m), d_sigma):")
for m in range(-12,13):
    d=hyper(m); print(m,d,"chi=",sum((-1)**k*x for k,x in enumerate(d)))
