import numpy as np, itertools, random
from fractions import Fraction
from scipy import integrate
np.random.seed(1)
ok=lambda name,c: print(("OK  " if c else "FAIL"),name)

# ---------- minimal polynomial / form algebra in z1,z2,w1,w2 (w=zbar) ----------
# variables index: 0:z1 1:z2 2:w1 3:w2 ; generators dz1,dz2,dw1,dw2 = 0..3
class P(dict):
    def __add__(s,o):
        r=P(s)
        for k,v in o.items():
            r[k]=r.get(k,0)+v
            if r[k]==0: del r[k]
        return r
    def __mul__(s,o):
        if not isinstance(o,P): o=P({(0,0,0,0):o}) if o!=0 else P()
        r=P()
        for k1,v1 in s.items():
            for k2,v2 in o.items():
                k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
                if r[k]==0: del r[k]
        return r
    __rmul__=__mul__
    def d(s,i):
        r=P()
        for k,v in s.items():
            if k[i]>0:
                kk=list(k);kk[i]-=1;r[tuple(kk)]=r.get(tuple(kk),0)+v*k[i]
        return r
def var(i): k=[0]*4;k[i]=1;return P({tuple(k):1})
one=P({(0,0,0,0):1})
z1,z2,w1,w2=[var(i) for i in range(4)]
# forms: dict tuple(sorted gens)->P
def fadd(a,b):
    r={k:v for k,v in a.items()}
    for k,v in b.items():
        r[k]=r.get(k,P())+v
        if not r[k]: del r[k]
    return r
def wedge_gen(gens,i):  # dgen_i ^ (dgens) -> sign, sorted tuple or None
    if i in gens: return 0,None
    pos=sum(1 for g in gens if g<i); return (-1)**pos, tuple(sorted(gens+(i,)))
def dop(form,idxs):  # sum over idx: dgen_idx ^ d_idx(coeff)
    r={}
    for k,c in form.items():
        for i in idxs:
            dc=c.d(i)
            if not dc: continue
            # dgen_i ^ dc * dgens  : gen goes in front of k
            s,kk=wedge_gen(k,i)
            if s==0: continue
            r=fadd(r,{kk:dc*s})
    return r
D=lambda f:dop(f,[0,1,2,3]); dd=lambda f:dop(f,[0,1]); dbar=lambda f:dop(f,[2,3])
def eq(a,b):
    return all(not fadd(a,{k:v*(-1) for k,v in b.items()}) for _ in [0])
# test: random polynomial forms
def randpoly():
    r=P()
    for _ in range(4):
        k=tuple(random.randint(0,2) for _ in range(4)); r=r+P({k:random.randint(1,5)})
    return r
random.seed(3)
for deg in [0,1,2]:
    for _ in range(5):
        gens=tuple(sorted(random.sample(range(4),deg)))
        f={gens:randpoly()}
        ok(f"dbar^2=0, d^2=0 etc deg{deg}", not dbar(dbar(f)) and not dd(dd(f)) and not fadd(dd(dbar(f)),dbar(dd(f))) and not D(D(f)))
# Problem 15: beta
beta={(2,):z1*w1*z2, (1,):z1*w2}
db=dbar(beta); dp=dd(beta)
exp_db={(1,3):P()+(-1)*z1}    # -z1 dz2^dz2bar
exp_dp={(0,2):w1*z2,(1,2):z1*w1,(0,1):w2}
ok("Prob15 dbar beta",eq(db,exp_db)); ok("Prob15 d beta",eq(dp,exp_dp))
# |z|^4 in 1 variable : ∂∂̄ (z^2 w^2) = 4 z w dz^dw
f={():z1*z1*w1*w1}; ok("∂∂̄|z|^4",eq(dd(dbar(f)),{(0,2):4*z1*w1}))
# Rank 2 Hbar = [[1,w],[z,1+zw]]  (z=z1,w=w1). theta = Hbar^{-1} ∂ Hbar
def mat(m): return m
Hb=[[one,w1],[z1,one+z1*w1]]
Hbinv=[[one+z1*w1,(-1)*w1],[(-1)*z1,one]]
dHb=[[Hb[i][j].d(0) for j in range(2)] for i in range(2)]
th=[[sum((Hbinv[i][k]*dHb[k][j] for k in range(2)),P()) for j in range(2)] for i in range(2)]
exp_th=[[(-1)*w1,(-1)*w1*w1],[one,w1]]
ok("Prob24 theta", all(th[i][j]==exp_th[i][j] for i in range(2) for j in range(2)))
Th=[[th[i][j].d(2) for j in range(2)] for i in range(2)]  # coefficient of dwbar^dz
print("  d_wbar theta =",Th)
# check Hbar^{-1} correct
prod=[[sum((Hb[i][k]*Hbinv[k][j] for k in range(2)),P()) for j in range(2)] for i in range(2)]
ok("Hbar*Hbar^-1=I", prod[0][0]==one and prod[1][1]==one and not prod[0][1] and not prod[1][0])
# (2,0)-part check (1 variable, trivial) skip.  Metric compat numerically
def Hf(z): return np.array([[1,z],[np.conj(z),1+abs(z)**2]],dtype=complex)  # H_ij = h(e_i,e_j)
def thf(z): zb=np.conj(z); return np.array([[-zb,-zb**2],[1,zb]],dtype=complex)  # coefficient of dz
z0=0.7-0.4j;e=1e-6
dz=(Hf(z0+e)-Hf(z0-e))/(2*e); dy=(Hf(z0+1j*e)-Hf(z0-1j*e))/(2*e)
dHz=(dz-1j*dy)/2; dHzb=(dz+1j*dy)/2
ok("dH = theta^T H + H thetabar  (z part)", np.allclose(dHz, thf(z0).T@Hf(z0),atol=1e-6))
ok("zbar part", np.allclose(dHzb, Hf(z0)@np.conj(thf(z0)),atol=1e-6))

# ---------- Wirtinger numerics ----------
def wz(f,z,e=1e-5):  # for f: C^n -> C ; returns gradient ∂_j f, ∂_jbar f
    n=len(z);g=np.zeros(n,complex);gb=np.zeros(n,complex)
    for j in range(n):
        h=np.zeros(n,complex);h[j]=e
        fx=(f(z+h)-f(z-h))/(2*e); fy=(f(z+1j*h)-f(z-1j*h))/(2*e)
        g[j]=(fx-1j*fy)/2; gb[j]=(fx+1j*fy)/2
    return g,gb
# Prob17a
u=lambda z:(1-np.exp(-abs(z[0])**2))/z[0]
zz=np.array([0.8+0.3j]); g,gb=wz(u,zz); ok("Prob17a ∂zbar u = e^{-|z|^2}",abs(gb[0]-np.exp(-abs(zz[0])**2))<1e-6)
ub=lambda z:np.conj(z[0])/(1+abs(z[0])**2); g,gb=wz(ub,zz)
ok("Prob17b ∂zbar u=(1+|z|^2)^-2",abs(gb[0]-1/(1+abs(zz[0])**2)**2)<1e-6)
# Cauchy transform check:  u(z)=(1/pi)∫ f(w)/(z-w) dA ; f=e^{-|w|^2}
f=lambda x,y:np.exp(-(x*x+y*y)); zt=1.3+0.5j
def re(x,y): w=x+1j*y; return (f(x,y)/(zt-w)).real
def im(x,y): w=x+1j*y; return (f(x,y)/(zt-w)).imag
R=8
a=integrate.dblquad(re,-R,R,-R,R,epsabs=1e-7)[0]; b=integrate.dblquad(im,-R,R,-R,R,epsabs=1e-7)[0]
ok("Cauchy transform formula gives (1-e^{-|z|^2})/z", abs((a+1j*b)/np.pi-(1-np.exp(-abs(zt)**2))/zt)<1e-4)
# Prob16 ∂_j∂_kbar log(1+|z|^2)
n=3; z=np.random.randn(n)+1j*np.random.randn(n)
def phi(z): return np.log(1+np.sum(abs(z)**2))
e=1e-3
def mixed(j,k):
    def sec(f,j,k):
        pass
    # ∂_j ∂_kbar = 1/4 (∂xj - i ∂yj)(∂xk + i ∂yk)
    def d2(a,b):  # directional second derivs in real dirs a,b (complex vectors)
        return (phi(z+e*a+e*b)-phi(z+e*a-e*b)-phi(z-e*a+e*b)+phi(z-e*a-e*b))/(4*e*e)
    ej=np.zeros(n,complex);ej[j]=1;ek=np.zeros(n,complex);ek[k]=1
    return 0.25*(d2(ej,ek)+1j*d2(ej,1j*ek)-1j*d2(1j*ej,ek)+d2(1j*ej,1j*ek))
G=np.array([[mixed(j,k) for k in range(n)] for j in range(n)])
r2=np.sum(abs(z)**2)
Gex=np.array([[ (j==k)/(1+r2) - np.conj(z[j])*z[k]/(1+r2)**2 for k in range(n)] for j in range(n)])
ok("Prob16 formula g_{j kbar}",np.allclose(G,Gex,atol=1e-4))
# determinant
ok("det g = (1+r^2)^-(n+1)",abs(np.linalg.det(Gex)-(1+r2)**(-(n+1)))<1e-10)
# positivity
v=np.random.randn(n)+1j*np.random.randn(n)
val=np.sum(Gex*np.outer(v,np.conj(v)))
ok("positivity formula",abs(val-(np.vdot(v,v).real*(1+r2)-abs(np.sum(v*np.conj(z)))**2)/(1+r2)**2)<1e-10 and val.real>0)
# FS volume
from math import factorial,pi,gamma
for n in [1,2,3,4]:
    vS=2*pi**n/gamma(n)
    I=integrate.quad(lambda r:r**(2*n-1)*(1+r*r)**(-n-1),0,np.inf)[0]
    ok(f"∫ω^n=1 n={n}",abs(factorial(n)*pi**(-n)*vS*I-1)<1e-8)
# O(k) integral
for k in [-1,1,2,3,-2]:
    f=lambda r:k/(np.pi*(1+r*r)**2)*2*np.pi*r
    ok(f"deg O({k})={k}",abs(integrate.quad(f,0,np.inf)[0]-k)<1e-8)
# Gauss curvature of g=4|dz|^2/(1+r^2)^2 ; K=-(1/2λ)Δ log λ
lam=lambda x,y:4/(1+x*x+y*y)**2
x0,y0=0.6,-0.9;e=1e-3
L=lambda x,y:np.log(lam(x,y))
lap=(L(x0+e,y0)+L(x0-e,y0)+L(x0,y0+e)+L(x0,y0-e)-4*L(x0,y0))/e**2
ok("K=1 for round sphere",abs(-lap/(2*lam(x0,y0))-1)<1e-4)
# Prob 7 quaternion
def qmul(p,q):
    a1,b1,c1,d1=p;a2,b2,c2,d2=q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2,a1*b2+b1*a2+c1*d2-d1*c2,a1*c2-b1*d2+c1*a2+d1*b2,a1*d2+b1*c2-c1*b2+d1*a2])
q=np.random.randn(4); i_=np.array([0,1,0,0.]);j_=np.array([0,0,1,0.]);k_=np.array([0,0,0,1.])
ok("ij=k", np.allclose(qmul(i_,j_),k_))
LJ=lambda q:qmul(j_,q); LI=lambda q:qmul(i_,q)
ok("JJ^2=-1,JI JJ=-JJ JI",np.allclose(LJ(LJ(q)),-q) and np.allclose(LI(LJ(q)),-LJ(LI(q))))
zq=lambda q:(q[0]+1j*q[1],q[2]+1j*q[3])  # q=z+wj : a+bi + (c+di)j
# check q = z + w j ?  z=a+bi, w=c+di, wj=(c+di)j=cj+dk ok
Jq=LJ(q); zj,wj=zq(Jq); z0_,w0_=zq(q)
ok("J_J(z,w)=(-wbar,zbar)",abs(zj+np.conj(w0_))<1e-12 and abs(wj-np.conj(z0_))<1e-12)
ze1=lambda q:(lambda z,w:z+1j*np.conj(w))(*zq(q)); ze2=lambda q:(lambda z,w:np.conj(z)+1j*w)(*zq(q))
ok("zeta1,zeta2 are J_J-holomorphic",abs(ze1(Jq)-1j*ze1(q))<1e-12 and abs(ze2(Jq)-1j*ze2(q))<1e-12)
# check J_I: coordinates z,w holomorphic
Iq=LI(q); zi,wi=zq(Iq); ok("J_I = i on (z,w)",abs(zi-1j*z0_)<1e-12 and abs(wi-1j*w0_)<1e-12)
# Beltrami J_mu
a,b=0.3,-0.2; mu=a+1j*b; den=1-abs(mu)**2
Jm=np.array([[-2*b,-((1-a)**2+b*b)],[(1+a)**2+b*b,2*b]])/den
ok("J_mu^2=-1",np.allclose(Jm@Jm,-np.eye(2)))
A=np.array([[1+a,b],[b,1-a]]); ok("J_mu=A^-1 J0 A",np.allclose(Jm,np.linalg.inv(A)@np.array([[0,-1],[1,0]])@A))
# w=z+mu zbar is J_mu-holomorphic : dw∘J = i dw
x=np.array([0.7,-0.3]);
def wmap(x): zz_=x[0]+1j*x[1]; return zz_+mu*np.conj(zz_)
lin=lambda x:wmap(x)
ok("w=z+mu zbar holomorphic for J_mu",abs(lin(Jm@x)-1j*lin(x))<1e-12)
# ---------- Nijenhuis tensor for T01=span{d_zbar1, d_zbar2 + f d_z1}, numeric ----------
def Jreal(x,fmode):
    z1_=x[0]+1j*x[1]
    f={'zbar1':np.conj(z1_),'hol':z1_,'zero':0*z1_, 'z2bar':np.conj(x[2]+1j*x[3])}[fmode]
    # basis order (dz1,dz2,dzb1,dzb2)
    W1=np.array([0,0,1,0],complex);W2=np.array([f,0,0,1],complex)
    cj=lambda v:np.array([np.conj(v[2]),np.conj(v[3]),np.conj(v[0]),np.conj(v[1])]);W1b=cj(W1);W2b=cj(W2)
    B=np.column_stack([W1b,W2b,W1,W2]); JC=B@np.diag([1j,1j,-1j,-1j])@np.linalg.inv(B)
    # real basis x1,y1,x2,y2 in terms of (dz1,dz2,dzb1,dzb2)
    S=np.column_stack([[1,0,1,0],[1j,0,-1j,0],[0,1,0,1],[0,1j,0,-1j]]).astype(complex)
    JR=np.linalg.inv(S)@JC@S
    assert np.allclose(JR.imag,0,atol=1e-12); return JR.real
def Nij(x,fmode,e=1e-5):
    J=Jreal(x,fmode)
    dJ=[ (Jreal(x+e*np.eye(4)[c],fmode)-Jreal(x-e*np.eye(4)[c],fmode))/(2*e) for c in range(4)]  # dJ[c][d,a]=∂_c J^d_a
    N=np.zeros((4,4,4))
    for a_ in range(4):
        for b_ in range(4):
            JXa=J[:,a_];JXb=J[:,b_]
            # [JX,JY]^d = JX^c ∂_c JY^d - JY^c ∂_c JX^d
            br=sum(JXa[c]*dJ[c][:,b_]-JXb[c]*dJ[c][:,a_] for c in range(4))
            JXY=-dJ[b_][:,a_]   # [JX,Y]=-∂_b J_a
            XJY=dJ[a_][:,b_]
            N[a_,b_]=br-J@JXY-J@XJY
    return N
x=np.random.randn(4)
for m in ['zero','hol','zbar1','z2bar']:
    J=Jreal(x,m); N=Nij(x,m)
    print("  fmode",m,"J^2=-1:",np.allclose(J@J,-np.eye(4)),"max|N|=",np.abs(N).max())
# N(W1,W2) = -4 d_z1 ?
x=np.random.randn(4); N=Nij(x,'zbar1')
z1v=x[0]+1j*x[1]
W1=0.5*np.array([1,1j,0,0]); W2=0.5*np.array([0,0,1,1j])+np.conj(z1v)*0.5*np.array([1,-1j,0,0])
val=np.einsum('a,b,abd->d',W1,W2,N)
ok("N(W1,W2) = -4 ∂_z1", np.allclose(val,-4*0.5*np.array([1,-1j,0,0]),atol=1e-5))
# genus/degree arithmetic
for d in range(1,7): print("  d=",d,"g=",(d-1)*(d-2)//2, "chi=",d*(3-d))
# torus Hodge numbers
from math import comb
for n in [1,2,3]:
    h={(p,q):comb(n,p)*comb(n,q) for p in range(n+1) for q in range(n+1)}
    print("  torus n=",n,[sum(h[(p,k-p)] for p in range(n+1) if 0<=k-p<=n)==comb(2*n,k) for k in range(2*n+1)], "chi_top=",sum((-1)**(p+q)*h[(p,q)] for p,q in h))
# Lambda^{p,q} counts n=3
print("  n=3 table",[[comb(3,p)*comb(3,q) for q in range(4)] for p in range(4)], sum(comb(3,p)*comb(3,q) for p in range(4) for q in range(4)))
print("  dim Lambda^{0,2}⊗T10:",[comb(n,2)*n for n in range(1,5)])
# Fourier on E=C/(Z+iZ): u=[sin(2πx)-i sin(2πy)]/π solves ∂_zbar u = cos2πx+cos2πy
uu=lambda z:(np.sin(2*np.pi*z[0].real)-1j*np.sin(2*np.pi*z[0].imag))/np.pi
zz=np.array([0.31+0.17j]); g,gb=wz(uu,zz,1e-5)
ok("Fourier solution on torus",abs(gb[0]-(np.cos(2*np.pi*0.31)+np.cos(2*np.pi*0.17)))<1e-6)
chi=lambda m,n:(lambda z:np.exp(2j*np.pi*(m*z[0].real+n*z[0].imag)))
for (m,n) in [(1,0),(0,1),(2,-1)]:
    g,gb=wz(chi(m,n),zz); ok(f"∂zbar chi_{m},{n}=pi i (m+in) chi",abs(gb[0]-np.pi*1j*(m+1j*n)*chi(m,n)(zz))<1e-5)
# K_P1 transition: dw=-z^-2 dz
print("  K_P1: e0=-z^2 e1  => f1=-z^2 f0 ~ O(-2)")
# Poincare disc K=-1
lam=lambda x,y:4/(1-x*x-y*y)**2
x0,y0=0.3,0.2;e=1e-3
L=lambda x,y:np.log(lam(x,y))
lap=(L(x0+e,y0)+L(x0-e,y0)+L(x0,y0+e)+L(x0,y0-e)-4*L(x0,y0))/e**2
ok("Poincare disc K=-1",abs(-lap/(2*lam(x0,y0))+1)<1e-4)
# SO(4)/U(2) : orth complex structures a I+bJ+cK square to -1 and are orthogonal
Mi=np.array([qmul(i_,e_) for e_ in np.eye(4)]).T;Mj=np.array([qmul(j_,e_) for e_ in np.eye(4)]).T;Mk=np.array([qmul(k_,e_) for e_ in np.eye(4)]).T
v=np.random.randn(3);v/=np.linalg.norm(v);Jm_=v[0]*Mi+v[1]*Mj+v[2]*Mk
ok("aI+bJ+cK orthogonal, squares to -1",np.allclose(Jm_@Jm_,-np.eye(4)) and np.allclose(Jm_.T@Jm_,np.eye(4)))
# orientation: det of change to coordinates (z,wbar) for right mult R_i
Ri=np.array([qmul(e_,i_) for e_ in np.eye(4)]).T
print("  R_i complex orientation sign (det of [x,Rx,y,Ry] basis):")
def orient(M):
    # basis e1, M e1, e2', M e2' with e2' ⟂ span
    e1=np.array([1,0,0,0.]);b=np.column_stack([e1,M@e1,[0,0,1,0],M@np.array([0,0,1,0.])]);return np.sign(np.linalg.det(b))
print("  left I:",orient(Mi),"right I:",orient(Ri))
# dims: Möbius check holomorphic trivial; chi twist dims
print("  h0(O(1)+O(-1) twisted -1)=",max(0+1,0)+max(-2+1,0),"vs O+O twisted:",2*max(-1+1,0))
print("  Euler seq P1 nonsplit: h0(O(-1)^2)=",2*max(0,0),"vs h0(O(-2)+O)=",max(-1,0)+1)
