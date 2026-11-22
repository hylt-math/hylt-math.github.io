# Independent re-verification (does not import lib.py). Python only, Fractions.
from fractions import Fraction as F
from math import comb, factorial
import random, itertools

def smul(a,b,n):
    r=[F(0)]*(n+1)
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if i+j>n: break
            r[i+j]+=x*y
    return r
def sinv(a,n):
    r=[F(0)]*(n+1); r[0]=1/a[0]
    for m in range(1,n+1):
        r[m]=-sum(a[k]*r[m-k] for k in range(1,m+1) if k<len(a))/a[0]
    return r
def expser(c,n): return [F(c)**k/factorial(k) for k in range(n+1)]
def padd(a,b): 
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

# Todd series via Bernoulli numbers (different from lib: via recursion for Bernoulli)
def bernoulli(n):
    B=[F(0)]*(n+1); B[0]=F(1)
    for m in range(1,n+1):
        B[m]=-sum(comb(m+1,k)*B[k] for k in range(m))/(m+1)
    return B  # B_1=-1/2
Bn=bernoulli(14)
def todd_series(n): return [Bn[k]*(-1)**k/factorial(k) for k in range(n+1)]  # sum B_k (-x)^k/k!
def inv_ser_check(n):
    den=[F((-1)**k,factorial(k+1)) for k in range(n+1)]
    return sinv(den,n)
assert todd_series(10)==inv_ser_check(10)
print("Todd series: Bernoulli == inversion ok:", todd_series(6))

def esym(xs,k):
    return sum((__import__('math').prod(c) for c in itertools.combinations(xs,k)),F(0)) if k>0 else F(1)
random.seed(1)
def rr(): return F(random.randint(-9,9),random.randint(1,5))
for trial in range(5):
    xs=[rr() for _ in range(5)]
    e=[esym(xs,k) for k in range(6)]
    c1,c2,c3,c4=e[1],e[2],e[3],e[4]
    # multiplicative genus coefficient extraction by series in t
    def mult(Q,n=4):
        tot=[F(1)]+[F(0)]*n
        for x in xs:
            tot=smul(tot,[Q[k]*x**k for k in range(n+1)],n)
        return tot
    Td=mult(todd_series(4))
    assert Td[1]==c1/2
    assert Td[2]==(c1**2+c2)/12
    assert Td[3]==c1*c2/24
    assert Td[4]==(-c1**4+4*c1**2*c2+3*c2**2+c1*c3-c4)/720
    # ch
    ch=[sum(x**k for x in xs)/factorial(k) for k in range(5)]
    assert ch[2]==(c1**2-2*c2)/2
    assert ch[3]==(c1**3-3*c1*c2+3*c3)/6
    assert ch[4]==(c1**4-4*c1**2*c2+4*c1*c3+2*c2**2-4*c4)/24
    # Pontryagin/L/Ahat in y=x^2
    p1=sum(x*x for x in xs); p2=esym([x*x for x in xs],2)
    Lq=[F(1),F(0),F(1,3),F(0),F(-1,45)]
    L=mult(Lq)
    assert L[2]==p1/3 and L[4]==(7*p2-p1**2)/45
    Aq=[F(1),F(0),F(-1,24),F(0),F(7,5760)]
    A=mult(Aq)
    assert A[2]==-p1/24 and A[4]==(7*p1**2-4*p2)/5760
    # check the series themselves: x/tanh x, (x/2)/sinh(x/2) by inversion of sinh/cosh
    # p1 = c1^2-2c2, p2=c2^2-2c1c3+2c4
    assert p1==c1**2-2*c2 and p2==c2**2-2*c1*c3+2*c4
print("A: ch,Td,L,Ahat formulas ok")
# x/tanh x series: cosh x/(sinh x / x)
n=8
sh=[F(1,factorial(2*k+1)) for k in range(n)]  # sinh x/x in x^2
ch_=[F(1,factorial(2*k)) for k in range(n)]
q=smul(ch_,sinv(sh,n-1),n-1); print("x/tanh x:",q[:4]); assert q[:3]==[1,F(1,3),F(-1,45)]
sh2=[F(1,factorial(2*k+1))/4**k for k in range(n)]
a=sinv(sh2,n-1); print("Ahat:",a[:3]); assert a[:3]==[1,F(-1,24),F(7,5760)]
# Hirzebruch & P^n
def Q(n): return todd_series(n)
def pw(a,k,n):
    r=[F(1)]+[F(0)]*n
    for _ in range(k): r=smul(r,a,n)
    return r
for n in range(0,15):
    assert pw(Q(n),n+1,n)[n]==1
def binom_gen(n,k):
    r=F(1)
    for i in range(1,n+1): r*=F(k+i,i)
    return r
for n in range(1,10):
    td=pw(Q(n),n+1,n)
    for k in range(-20,21):
        assert smul(expser(k,n),td,n)[n]==binom_gen(n,k)
print("B: Hirzebruch + chi(P^n,O(k)) ok")

# Complete intersections: Chern numbers
def ci(N,degs):
    n=N-len(degs)
    num=pw([F(1),F(1)]+[F(0)]*n,N+1,n)
    den=[F(1)]+[F(0)]*n
    for d in degs: den=smul(den,[F(1),F(d)]+[F(0)]*(n-1) if n>=1 else [F(1)],n)
    c=smul(num,sinv(den,n),n)
    deg=1
    for d in degs: deg*=d
    return c,deg,n
def numbers(N,degs):
    c,deg,n=ci(N,degs)
    return [x*deg for x in c]  # c_i * H^{n-i} ... times deg: c_i H^{n-i} integrals
# surfaces in P^3
for d in range(1,8):
    c,deg,n=ci(3,[d])
    K2=c[1]**2*deg; e=c[2]*deg
    assert K2==d*(d-4)**2 and e==d*(d*d-4*d+6)
    chi=(K2+e)/12; assert chi==1+comb(d-1,3)
    assert (K2-2*e)/3==-F(d*(d*d-4),3)
    print("d",d,K2,e,chi,(K2-2*e)/3,e-2,(5*e-K2)/6)
# CY3 table
for N,degs in [(4,[5]),(5,[2,4]),(5,[3,3]),(6,[2,2,3]),(7,[2,2,2,2])]:
    c,deg,n=ci(N,degs); assert c[1]==0
    print(N,degs,"H3",deg,"c2H",c[2]*deg,"e",c[3]*deg,"h21",1-c[3]*deg/2)
# problem hyperCI and Fano3
c,deg,n=ci(5,[2,3]); print("(2,3) in P5:",c,deg,"c1^3",c[1]**3*deg,"c1c2",c[1]*c[2]*deg,"e",c[3]*deg)
c,deg,n=ci(4,[2,3]); print("(2,3) in P4:",c,deg,"e",c[2]*deg)
c,deg,n=ci(5,[3,3]); print("(3,3)",c)
# problem integral
for d in range(1,8):
    c,deg,n=ci(4,[d]); print("P4 hyp d",d,"c1c2",c[1]*c[2]*deg, "mod24", (c[1]*c[2]*deg)%24, "e",c[3]*deg)
# Td4 table
def td4(c,deg): return (-c[1]**4+4*c[1]**2*c[2]+3*c[2]**2+c[1]*c[3]-c[4])/720*deg
for N,degs in [(4,[]),(5,[2]),(5,[3]),(5,[6])]:
    c,deg,n=ci(N,degs)
    print(N,degs,[c[1]**4*deg,c[1]**2*c[2]*deg,c[2]**2*deg,c[1]*c[3]*deg,c[4]*deg],td4(c,deg))
# Fano 3-folds h0(-K)
for N,degs in [(3,[]),(4,[2]),(4,[3]),(5,[2,3]),(4,[4]),(5,[2,2])]:
    c,deg,n=ci(N,degs); print("Fano",N,degs,"c1^3",c[1]**3*deg,"c1c2",c[1]*c[2]*deg,"h0(-K)",c[1]**3*deg/2+3)
# Euler number hypersurface
for n in range(1,7):
    for d in range(1,9):
        c,deg,_=ci(n+1,[d]); assert c[n]*deg==F((1-d)**(n+2)-1,d)+n+2
# chi(O_X(k)) on quintic
c,deg,_=ci(4,[5])
for k in range(-6,10):
    td=[F(1),F(0),c[2]/12,F(0)]
    v=smul(expser(k,3),td,3)[3]*deg
    assert v==binom_gen(4,k)-binom_gen(4,k-5)
print("quintic chi(O(k)) ok; k=1..5:",[F(5*k**3+25*k,6) for k in range(1,6)])
# surfaces d in P3: HRR vs sequence
for d in range(1,8):
    c,deg,_=ci(3,[d])
    for k in range(-9,10):
        td=[F(1),c[1]/2,(c[1]**2+c[2])/12]
        v=smul(expser(k,2),td,2)[2]*deg
        assert v==binom_gen(3,k)-binom_gen(3,k-d)
print("surface HRR ok")
# T P2(k), Sym2
chi2=lambda k:F((k+1)*(k+2),2)
for k in range(-9,9): assert 3*chi2(k+1)-chi2(k)==(k+2)*(k+4)
print("Sym2 T chi:",6*chi2(2)-3*chi2(1))
# Omega^1(k) on P2
print("Omega1(k) P2:",[3*binom_gen(2,k-1)-binom_gen(2,k) for k in (0,1,2,3)])
# chi^1 for P^3: should be -1; P^2 -1
def chi1_3(c1c2,c3): return F(c1c2,24)-F(c3,2)
print("chi^1 P3",chi1_3(24,4),"quintic",chi1_3(0,-200))
# Euler total check on P2 by formula
for m in range(-8,9):
    v=chi2(m)-(3*chi2(m+1)-chi2(m))+chi2(m+3)
    assert v==3
print("P2 total Euler ok")
# F_a numbers
for a in range(6):
    xi2=-a; c1sq=4*xi2+4*(a+2); assert c1sq==8
# p:RRsurf etc trivial.
# Hirzebruch chi_y formula check for surfaces via independent expansion
for trial in range(3):
    xs=[rr(),rr()]
    c1=xs[0]+xs[1]; c2=xs[0]*xs[1]
    def chiy(y,n=2):
        tot=[F(1)]+[F(0)]*n
        for x in xs:
            # x(1+y e^{-x})/(1-e^{-x}) = Q(x)*(1+y e^{-x})
            f=smul(todd_series(n),padd([F(1)],[y*(-1)**k/factorial(k) for k in range(n+1)]),n)
            f=[f[k]*x**k for k in range(n+1)]
            tot=smul(tot,f,n)
        return tot[n]
    # chi^0=(c1^2+c2)/12 ; chi^1 = (c1^2-5c2)/6 ; chi^2 same as chi^0
    # chi_y = chi0 + chi1 y + chi2 y^2
    y0=chiy(F(0)); y1=chiy(F(1)); ym=chiy(F(-1)); y2=chiy(F(2))
    chi0=(c1**2+c2)/12; chi1=(c1**2-5*c2)/6
    assert y0==chi0 and ym==c2 and y1==(c1**2-2*c2)/3 and y2==chi0+2*chi1+4*chi0
print("chi_y surfaces ok")
# 3-fold chi_y
for trial in range(3):
    xs=[rr(),rr(),rr()]
    e=[esym(xs,k) for k in range(4)]
    c1,c2,c3=e[1],e[2],e[3]
    def chiy3(y,n=3):
        tot=[F(1)]+[F(0)]*n
        for x in xs:
            f=smul(todd_series(n),padd([F(1)],[y*(-1)**k/factorial(k) for k in range(n+1)]),n)
            f=[f[k]*x**k for k in range(n+1)]
            tot=smul(tot,f,n)
        return tot[n]
    # chi_y = chi0 + chi1 y + chi2 y^2 + chi3 y^3 with chi0=c1c2/24 chi1=c1c2/24-c3/2 chi2=-chi1 chi3=-chi0
    chi0=c1*c2/24; chi1=chi0-c3/2
    for y in (F(0),F(1),F(-1),F(3)):
        assert chiy3(y)==chi0+chi1*y-chi1*y**2-chi0*y**3
print("chi_y 3-folds ok")
# Total Euler theorem n=3 test with random roots? integrand: ch(E) prod(1-e^{x}) Td, degree 3 part, with ch(E) = r + l t...
for trial in range(3):
    xs=[rr(),rr(),rr()]
    e=[esym(xs,k) for k in range(4)]
    l=rr(); r=2
    # E = L1+L2 with c_1 = l1+l2 arbitrary: E=O(a)+O(b)
    for (a,b) in [(rr(),rr())]:
        chE=[F(0)]*4
        chE=padd(expser(a,3),expser(b,3))
        tot=chE
        for x in xs:
            f=smul([F(1)]+[F(0)]*3,[F(1)-F(1)] ,3)
        td=[F(1)]+[F(0)]*3
        for x in xs:
            q=[todd_series(3)[k]*x**k for k in range(4)]
            td=smul(td,q,3)
            om=[ (F(1) if k==0 else F(0)) - x**k/factorial(k) for k in range(4)]  # 1-e^{x}
            tot=smul(tot,om,3)
        val=smul(tot,td,3)[3]
        assert val==(-1)**3*r*e[3], (val,(-1)**3*r*e[3])
print("Euler total (n=3, formal) ok")
print("ALL OK")
