# Independent review checks (reviewer). exact rational polynomial calculus from check.py
import check
from check import *
import random
from fractions import Fraction as Fr
random.seed(1)
# 1. d(beta) with beta = xz dy^dz + y^2 dz^dx + x dx^dy  (dz^dx = -dx^dz)
be=f1((P(x,z),(1,2)),(pscale(P(y,y),-1),(0,2)),(x,(0,1)))
print("d beta:",pr(d(be)),"  expected z+2y")
# 2. Poincare homotopy operator K w = int_0^1 t^{k-1} i_x w(tx) dt ; check dK+Kd=id for random polynomial forms
def rpoly(deg=2):
    p={}
    for _ in range(4):
        k=[0]*N
        for _ in range(random.randint(0,deg)): k[random.randrange(N)]+=1
        p=padd(p,{tuple(k):Fr(random.randint(-3,3))})
    return p
def scale_args(p,t_pow_total):  # w(tx): monomial of degree m gets t^m ; integrate t^{k-1+m} -> 1/(k+m)
    pass
def Kop(a,k):
    X=[var(i) for i in range(N)]
    iw=interior(X,a)  # coefficients at x
    r={}
    for idx,p in iw.items():
        q={}
        for mon,c in p.items():
            m=sum(mon)
            q[mon]=c*Fr(1,k-1+m)
        r=fadd(r,{idx:{m:c for m,c in q.items() if c!=0}})
    return r
for k in (1,2,3):
    import itertools
    w={}
    for idx in itertools.combinations(range(N),k):
        w=fadd(w,{idx:rpoly()})
    lhs=fadd(d(Kop(w,k)), Kop(d(w),k+1) if k<N else {})
    print("Poincare K, k=",k,": dK+Kd==id",lhs==w)
# 3. transgression: N=4 not possible with global N=3 unless set
