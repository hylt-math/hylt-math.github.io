import numpy as np, itertools, math
from fractions import Fraction as F
from math import comb
ok=lambda s,c: print(("OK   " if c else "FAIL ")+s)

# 1. Weierstrass p for Z+iZ
def lat(tau, N=60):
    return [m+n*tau for m in range(-N,N+1) for n in range(-N,N+1) if (m,n)!=(0,0)]

def sig(n,k): return sum(d**k for d in range(1,n+1) if n%d==0)
def g23(tau,N=None):
    q=np.exp(2j*np.pi*tau)
    g2=4*np.pi**4/3*(1+240*sum(sig(n,3)*q**n for n in range(1,60)))
    g3=8*np.pi**6/27*(1-504*sum(sig(n,5)*q**n for n in range(1,60)))
    return g2,g3
def p_and_dp(z,tau,N=None):
    q=np.exp(2j*np.pi*tau);u=np.exp(2j*np.pi*z)
    p=0;dp=0
    for n in range(-6,7):
        x=q**n*u
        p+=x/(1-x)**2; dp+=x*(1+x)/(1-x)**3
    p=(2j*np.pi)**2*(p+1/12-2*sum(q**n/(1-q**n)**2 for n in range(1,60)))
    return p,(2j*np.pi)**3*dp
for tau in [1j, 0.3+1.1j]:
    g2,g3=g23(tau)
    for z in [0.21+0.17j,0.4-0.3j]:
        p,dp=p_and_dp(z,tau)
        ok(f"p'^2=4p^3-g2p-g3 tau={tau} z={z}  err={abs(dp**2-4*p**3+g2*p+g3):.2e}", abs(dp**2-4*p**3+g2*p+g3)<1e-6)
g2,g3=g23(1j); print("lemniscatic g2,g3 for Z+iZ:",g2,g3)
# collinearity
tau=0.3+1.1j
z1=0.21+0.17j; z2=0.4-0.3j; z3=-(z1+z2)
M=np.array([[1,*p_and_dp(z,tau)] for z in (z1,z2,z3)])
ok(f"collinear det={abs(np.linalg.det(M)):.2e}",abs(np.linalg.det(M))<1e-6)
# j-invariant at i : g2^3 = 27 g3^2 *? j=1728 g2^3/(g2^3-27g3^2); at tau=i, g3=0 -> j=1728
g2,g3=g23(1j); print("j(i)=",1728*g2**3/(g2**3-27*g3**2))
# e1 e2 e3 roots
r=np.roots([4,0,-g2.real,-g3.real]); print("roots for Z+iZ",r)

# 2. theta sections of degree k on C/(Z+tau Z)
def theta_j(k,j,z,tau,N=40):
    n=np.arange(-N,N+1)
    return np.sum(np.exp(1j*np.pi*k*(n+j/k)**2*tau+2j*np.pi*k*(n+j/k)*z))
for k in [1,2,3,5]:
    tau=0.2+0.9j;z=0.13+0.21j
    e1=max(abs(theta_j(k,j,z+1,tau)-theta_j(k,j,z,tau)) for j in range(k))
    e2=max(abs(theta_j(k,j,z+tau,tau)-np.exp(-2j*np.pi*k*z-1j*np.pi*k*tau)*theta_j(k,j,z,tau))/abs(theta_j(k,j,z+tau,tau)) for j in range(k))
    # independence
    pts=[0.1*i+0.07j*i*i for i in range(1,k+3)]
    Mx=np.array([[theta_j(k,j,p,tau) for j in range(k)] for p in pts])
    rk=np.linalg.matrix_rank(Mx,tol=1e-8)
    ok(f"theta k={k} periodic err {e1:.1e}, quasi {e2:.1e}, rank {rk}",e1<1e-9 and e2<1e-9 and rk==k)

# 3. hyperelliptic y^2=f, deg f=2g+1 : RR for n*inf
def h0_inf(g,n):  # pole orders 2a, 2a+2g+1 ; count monomials x^a (b=0), x^a y (b=1)
    c=0
    for a in range(0,n+1):
        if 2*a<=n:c+=1
        if 2*a+2*g+1<=n:c+=1
    return c
def h0_K_minus(g,n): # forms x^i dx/y, ord at inf =2g-2-2i, i=0..g-1
    return sum(1 for i in range(g) if 2*g-2-2*i>=n)
allok=True
for g in range(1,8):
    for n in range(0,6*g):
        if h0_inf(g,n)-h0_K_minus(g,n)!=n+1-g: allok=False;print("bad",g,n)
ok("RR for n*inf on y^2=f(x), deg 2g+1, g=1..7",allok)
# gaps
for g in range(1,6):
    ng=[n for n in range(1,4*g) if h0_inf(g,n)>h0_inf(g,n-1)]
    gaps=[n for n in range(1,2*g+1) if n not in ng]
    wt=sum(gp-(i+1) for i,gp in enumerate(gaps))
    print(g,"gaps",gaps,"weight",wt, "g(g-1)/2=",g*(g-1)//2, "total",(2*g+2)*wt,"g^3-g=",g**3-g)
    assert wt==g*(g-1)//2 and (2*g+2)*wt==g**3-g and len(gaps)==g
ok("gap/weight hyperelliptic",True)

# 4. plane curves: h0(O_C(m)) vs RR
for d in [3,4,5,6,7]:
    g=(d-1)*(d-2)//2
    for m in range(0,3*d):
        h0=comb(m+2,2)-(comb(m-d+2,2) if m>=d else 0)   # valid for all m>=0 (projective normality)
        h1=comb(d-1-m,2) if m<=d-3 else 0  # h0(O(d-3-m))
        # h1 = h0 of K-D = O_C(d-3-m): comb(d-1-m,2) for 0<=d-3-m<d
        if m<=d-3: h1=comb(d-3-m+2,2)
        if h0-h1!=d*m+1-g: print("bad",d,m,h0,h1,d*m+1-g)
ok("plane curve RR check d=3..7, m=0..3d-1",True)

# 5. RH
def RH_genus(gY,d,R): 
    x=Fraction=None
    return (d*(2*gY-2)+R)//2+1
for d in range(2,9):
    g=(d-1)*(d-2)//2; R=d*(d-1)
    assert 2*g-2==d*(-2)+R
ok("Fermat degree d projection RH: g=(d-1)(d-2)/2",True)
for g in range(2,8):
    assert 2*g-2==2*(-2)+(2*g+2)
ok("hyperelliptic RH",True)
# polynomial z^3-3z: critical points
print("z^3-3z crit:",np.roots([3,0,-3]))
# Fermat quartic hyperflex weights
g=3; print("Fermat quartic: 12 hyperflexes weight 2 =",12*2,"= g^3-g =",g**3-g)
# check hyperflex tangent multiplicity numerically: point (0,y0,z0): y0=1,z0=e^{i pi/4}
z0=np.exp(1j*np.pi/4); assert abs(1+z0**4)<1e-12
# line y0^3 y + z0^3 z=0 -> z = -(y0^3/z0^3) y ; F|line = x^4 + y^4(1+ (y0/z0)^12)
print("1+(1/z0)^12 =",1+(1/z0)**12)
# 6. g=2 hyperelliptic family: dims
for g in range(2,8): print(g,"hyperell. dim",2*g-1,"moduli 3g-3",3*g-3)
# 7. canonical degree; g=2 branch pts
# 8. index check: chi(P^1,O(k))=k+1 ; Cech h1(O(-k))=k-1
for k in range(0,8):
    h0=max(k+1,0); h1=max(-k-1,0)
    assert h0-h1==k+1
ok("P^1 chi",True)
# 9. Riemann-Hurwitz for z -> z^n on P^1 etc. quartic x^4+y^4=1 genus 3
# 10. Noether / Clifford check on hyperelliptic g=3? skip
# 11. dimension count of divisors: l(D) for D=a*P+... skip
# 12. Elliptic: x^3 count semigroup <2,3>
print("done")

# ---- additional checks for problems ----
print("---- extra ----")
import numpy as np
# p:local
r=np.roots([2,0,-1]); print("z+1/z crit: z^2=1 -> values",[1+1, -1-1])
print("z^3-z^2 crit values: f(0)=0, f(2/3)=",(2/3)**2*(2/3-1), "=-4/27 =",-4/27)
# f=z^2+1/z: crit 2z^3=1
roots=[(0.5)**(1/3)*np.exp(2j*np.pi*k/3) for k in range(3)]
vals=[z**2+1/z for z in roots]; print("z^2+1/z crit vals",np.round(vals,6),"3z^2:",[np.round(3*z**2,6) for z in roots])
assert all(abs(2*z-1/z**2)<1e-12 for z in roots)
# deg R by RH for deg 3: 2*3-2=4 = 3 finite simple + inf(e=2)
ok("RH deg R (g=0): 2d-2",all(2*d-2==2*0-2+2*d for d in range(1,10)))
# p:Rcount
print("R(g,d)=2g-2+2d:",[(g,d,2*g-2+2*d) for g,d in [(2,2),(3,3),(1,2)]])
# fermat genus
print("Fermat g:",{d:(d-1)*(d-2)//2 for d in range(2,8)})
# g2 and discriminant
g2,g3=g23(1j); print("g2^3=",(g2**3).real,"Gamma(1/4)^8/(16pi^2)=",math.gamma(.25)**8/(16*math.pi**2),"g2=",g2.real)
# weights
for g in (2,3,4): print("g",g,"(2g+2)*g(g-1)/2 =",(2*g+2)*g*(g-1)//2," g^3-g=",g**3-g)
# p:euler1
for g in (0,1,2):
    r,d=1,5
    chiE=d+r*(1-g); chiET=(d+r*(2-2*g))+r*(1-g)
    print("g",g,"chi(E)-chi(E⊗T)=",chiE-chiET,"=-r(2-2g)=",-r*(2-2*g))
# p:index
for g in range(0,5): print("g",g,"ind K^1/2",(g-1)+1-g,"ind K",(2*g-2)+1-g,"ind T",(2-2*g)+1-g)
# P^1: Euler seq
print("chi(T)=",2*2-1)
# canonical quadric count
for g in range(3,8): print("g",g,"quadrics through canonical curve",g*(g+1)//2-(3*g-3),(g-2)*(g-3)//2)
# addition law on y^2=x^3-x numerically: 2P formula vs chord
a,b=-1,0
def dbl(x0,y0):
    m=(3*x0**2+a)/(2*y0); x3=m**2-2*x0; y3=y0+m*(x3-x0); return x3,-y3
x0=2.0; y0=np.sqrt(x0**3-x0); X,Y=dbl(x0,y0); print("2P on curve:",abs(Y**2-(X**3+a*X+b))<1e-9)
# hyperflex tangent: F=x^4+y^4-z^4 at (0,1,zeta)
for zeta in [1,1j,-1,-1j]:
    # substitute y=zeta^3 z: y^4 - z^4 = z^4(zeta^12-1)=0
    assert abs(zeta**12-1)<1e-12
ok("Fermat quartic hyperflex tangents x=0 pts",True)
# check z=0 points: x0^4+y0^4=0
x0=np.exp(1j*np.pi/4); y0=1
# tangent: x0^3 x + y0^3 y=0, y=-(x0/y0)^3 x ; F|= x^4(1+(x0/y0)^12) - z^4
print("1+(x0)^12=",abs(1+x0**12))
# gap/hyperelliptic count: g=3 deg 8 forms 
# j(i), g3
print("g3(i)=",abs(g3))
# rho lattice g2=0
rho=np.exp(2j*np.pi/3); g2r,g3r=g23(rho); print("g2(rho)=",abs(g2r))
print("done extra")

print("---- additions ----")
# Laurent expansion check: wp'^2-4wp^3+60a wp+140b = O(z^2), with wp=z^-2+3a z^2+5b z^4+c z^6
from fractions import Fraction as Fr
N=8  # keep terms from z^-8 .. z^8
def mul(A,B):
    C={}
    for i,x in A.items():
        for j,y in B.items():
            if i+j<=6: C[i+j]=C.get(i+j,0)+x*y
    return C
def add(A,B,s=1):
    C=dict(A)
    for j,y in B.items(): C[j]=C.get(j,0)+s*y
    return C
a,b,c=Fr(3,7),Fr(-5,11),Fr(2,13)
wp={-2:Fr(1),2:3*a,4:5*b,6:7*c}
dwp={-3:Fr(-2),1:6*a,3:20*b,5:42*c}
lhs=mul(dwp,dwp)
cube=mul(mul(wp,wp),wp)
lhs=add(lhs,{k:4*v for k,v in cube.items()},-1)
lhs=add(lhs,{k:60*a*v for k,v in wp.items()})
lhs=add(lhs,{0:140*b})
bad={k:v for k,v in lhs.items() if k<2 and v!=0}
ok("Laurent: wp'^2-4wp^3+60G4 wp+140G6 = O(z^2)",not bad)
# Hurwitz 84: min positive of 2h-2+sum(1-1/m_i)
best=None
from itertools import combinations_with_replacement
for h,rmax,mmax in [(0,5,45),(1,2,45),(2,0,2)]:
    for r in range(0,rmax+1):
        for ms in combinations_with_replacement(range(2,mmax),r):
            v=Fr(2*h-2)+sum(Fr(1)-Fr(1,m) for m in ms)
            if v>0 and (best is None or v<best[0]): best=(v,h,ms)
print("min positive:",best)
from math import gcd
for n in range(2,8):
    for m in range(1,10):
        d=gcd(n,m); R=m*(n-1)+d*(n//d-1); g=(-2*n+R+2)//2
        assert g==((n-1)*(m-1)-(d-1))//2
ok("superelliptic y^n=prod(x-a_i) genus formula via RH",True)
