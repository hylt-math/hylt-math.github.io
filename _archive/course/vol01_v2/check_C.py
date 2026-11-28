# Mini exterior calculus with exact rational polynomial coefficients (no sympy available)
from fractions import Fraction as Fr
import itertools, math
N=4
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,0)+s*v
        if r[k]==0: del r[k]
    return r
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
            if r[k]==0: del r[k]
    return r
def pd(p,i):
    r={}
    for k,v in p.items():
        if k[i]>0:
            kk=list(k);kk[i]-=1;r[tuple(kk)]=v*k[i]
    return r
def const(c): return {(0,)*N:Fr(c)} if c!=0 else {}
def var(i):
    k=[0]*N;k[i]=1;return {tuple(k):Fr(1)}
def pscale(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
# forms: dict idxtuple(sorted)->poly
def fadd(a,b,s=1):
    r=dict(a)
    for k,v in b.items():
        r[k]=padd(r.get(k,{}),v,s)
        if not r[k]: del r[k]
    return r
def sortsign(idx):
    idx=list(idx);s=1
    if len(set(idx))<len(idx): return 0,None
    for i in range(len(idx)):
        for j in range(len(idx)-1-i):
            if idx[j]>idx[j+1]: idx[j],idx[j+1]=idx[j+1],idx[j]; s=-s
    return s,tuple(idx)
def wedge(a,b):
    r={}
    for k1,p1 in a.items():
        for k2,p2 in b.items():
            s,k=sortsign(k1+k2)
            if s==0: continue
            r=fadd(r,{k:pscale(pmul(p1,p2),s)})
    return r
def d(a):
    r={}
    for k,p in a.items():
        for i in range(N):
            dp=pd(p,i)
            if dp:
                s,kk=sortsign((i,)+k)
                if s: r=fadd(r,{kk:pscale(dp,s)})
    return r
def interior(X,a): # X list of polys
    r={}
    for k,p in a.items():
        for pos,i in enumerate(k):
            kk=k[:pos]+k[pos+1:]
            r=fadd(r,{kk:pscale(pmul(X[i],p),(-1)**pos)})
    return r
def lie_coord(X,a):
    # (L_X w) = sum over: X(w_I) dx^I + w_I * d(X^{i}) ...  = d i_X w + i_X d w is Cartan; here use independent formula:
    # L_X(f dx^{i1}^...^dx^{ik}) = X(f) dx^I + f sum_m dx^{i1}..d(X^{im})..dx^{ik}
    r={}
    for k,p in a.items():
        Xf={}
        for j in range(N): Xf=padd(Xf,pmul(X[j],pd(p,j)))
        r=fadd(r,{k:Xf} if Xf else {})
        for m,i in enumerate(k):
            dXi={(j,):pd(X[i],j) for j in range(N) if pd(X[i],j)}
            # replace dx^i by dX^i
            for kk,q in dXi.items():
                new=wedge(wedge({k[:m] and k[:m] or ():const(1)} if False else {tuple(k[:m]):const(1)} if m>0 else {():const(1)}, {kk:q}), {tuple(k[m+1:]):const(1)} if m<len(k)-1 else {():const(1)})
                r=fadd(r,wedge({():p},new))
    return r
def show(a): return {k:dict(v) for k,v in a.items()}
x,y,z=var(0),var(1),var(2)
one={():const(1)}
def f1(*terms): # terms (poly, idx)
    r={}
    for p,i in terms: r=fadd(r,{i:p})
    return r
dx={(0,):const(1)};dy={(1,):const(1)};dz={(2,):const(1)}
def P(*fs):
    r=const(1)
    for f in fs: r=pmul(r,f)
    return r
def pr(a): 
    return {k:{e:str(c) for e,c in v.items()} for k,v in a.items()}

# ======================= check_C.py の本体（担当 C: §7-§10 の検算） =======================
import random
import numpy as np
random.seed(11); np.random.seed(11)
tw=var(3)
def hdr(s): print("\n=== "+s+" ===")
def rpoly(deg=1,nv=4):
    p={}
    for _ in range(3):
        k=[0]*4
        for _ in range(random.randint(0,deg)): k[random.randrange(nv)]+=1
        p=padd(p,{tuple(k):Fr(random.randint(-2,2))})
    return p
def r1form(nv=4):
    r={}
    for i in range(nv):
        p=rpoly(1,nv)
        if p: r=fadd(r,{(i,):p})
    return r
def mmat(f,n):  return [[f() for _ in range(n)] for _ in range(n)]
def mw(A,B,n):
    R=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): R[i][j]=fadd(R[i][j],wedge(A[i][k],B[k][j]))
    return R
def ma(A,B,n,s=1): return [[fadd(A[i][j],B[i][j],s) for j in range(n)] for i in range(n)]
def md(A,n): return [[d(A[i][j]) for j in range(n)] for i in range(n)]
def mtr(A,n):
    r={}
    for i in range(n): r=fadd(r,A[i][i])
    return r
def mzero(A,n): return all(not A[i][j] for i in range(n) for j in range(n))
def curv(A,n): return ma(md(A,n),mw(A,A,n),n)
def sc(a,c): return {k:{m:v*c for m,v in p.items()} for k,p in a.items()}

# ---- (1) 本文・問: R^3 上の A=[[0, z dx],[x dy, 0]] の曲率と Bianchi
hdr("(1) F for A=[[0,z dx],[x dy,0]]")
A=[[{}, {(0,):z}],[{(1,):x},{}]]
F=curv(A,2)
for i in range(2):
    for j in range(2): print("F[%d][%d] ="%(i,j),pr(F[i][j]))
print("expected: F11=xz dx^dy, F12=dz^dx (= -dx^dz coefficient), F21=dx^dy, F22=-xz dx^dy")
exp11={(0,1):P(x,z)}; exp12={(0,2):{(0,0,0,0):Fr(-1)}}; exp21={(0,1):const(1)}; exp22={(0,1):pscale(P(x,z),-1)}
print("match:",F[0][0]==exp11, F[0][1]==exp12, F[1][0]==exp21, F[1][1]==exp22)
Bi=ma(ma(md(F,2),mw(A,F,2),2),mw(F,A,2),2,-1)
print("Bianchi dF+AF-FA = 0 :",mzero(Bi,2))

# ---- (2) ゲージ共変性 (g が可逆でない一般の多項式行列は逆が多項式にならないので上三角ユニポテント)
hdr("(2) gauge covariance F' = g^-1 F g, random A (3x3)")
n=3
A=mmat(r1form,n)
one={():const(1)}
g=[[one,{():rpoly(1)},{():rpoly(1)}],[{},one,{():rpoly(1)}],[{},{},one]]
# inverse of unipotent upper triangular g = I+N: I - N + N^2
Nn=[[ {} if i>=j else g[i][j] for j in range(n)] for i in range(n)]
def mmul0(A,B): # matrices of polynomial 0-forms
    R=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): R[i][j]=fadd(R[i][j],wedge(A[i][k],B[k][j]))
    return R
Id=[[one if i==j else {} for j in range(n)] for i in range(n)]
gi=ma(ma(Id,Nn,n,-1),mmul0(Nn,Nn),n)
print("g*g^-1=I:",mmul0(g,gi)==Id)
Ap=ma(mw(mw(gi,A,n),g,n),mw(gi,md(g,n),n),n)
F0=curv(A,n); Fp=curv(Ap,n)
print("F' == g^-1 F g :",Fp==mw(mw(gi,F0,n),g,n))
print("Bianchi (3x3 random):",mzero(ma(ma(md(F0,n),mw(A,F0,n),n),mw(F0,A,n),n,-1),n))

# ---- (3) d_nabla^2 s = F s
hdr("(3) d_nabla^2 s = F s")
from functools import reduce
n=2
A=mmat(r1form,n); F0=curv(A,n)
s=[{():rpoly(2)} for _ in range(n)]
def addv(a,b): return fadd(a,b)
def nab0(sv):  # column of k-forms -> d + A^
    return [fadd(d(sv[i]),reduce(addv,[wedge(A[i][j],sv[j]) for j in range(n)],{})) for i in range(n)]
ns=nab0(s); nn=nab0(ns)
Fs=[reduce(addv,[wedge(F0[i][j],s[j]) for j in range(n)],{}) for i in range(n)]
print("d_nabla^2 s == F s :",nn==Fs)

# ---- (4) transgression tr F1^k - tr F0^k = dT_k,  k=2,3,  and Chern-Simons
hdr("(4) transgression, k=2,3 (R^4, 2x2 random A0,A1)")
n=2
A0=mmat(r1form,n); A1=mmat(r1form,n)
a=ma(A1,A0,n,-1)
F0=curv(A0,n); F1=curv(A1,n)
def dnab0(Phi,deg): # d_{nabla0} on End-valued deg-form: dPhi + A0 Phi - (-1)^deg Phi A0
    t=ma(md(Phi,n),mw(A0,Phi,n),n)
    return ma(t,mw(Phi,A0,n),n,-1 if deg%2==0 else 1)
# F_t = F0 + t d0 a + t^2 a^a  ; transgression T_k = k * int_0^1 tr(a F_t^{k-1}) dt  (polynomial in t -> exact integral)
D0a=dnab0(a,1); aa=mw(a,a,n)
def Ft_poly(): # coefficients list [C0,C1,C2] of F_t as matrices of forms
    return [F0,D0a,aa]
def mpow_poly(P_,m):  # polynomial in t with matrix-of-forms coefficients
    res=[[[ {} for _ in range(n)] for _ in range(n)]]; res[0]=[[one_form if i==j else {} for j in range(n)] for i in range(n)] if False else None
    return None
one_form={():const(1)}
Id2=[[one_form if i==j else {} for j in range(n)] for i in range(n)]
def poly_mul(P1,P2):
    R=[None]*(len(P1)+len(P2)-1)
    for i,Mi in enumerate(P1):
        for j,Mj in enumerate(P2):
            t=mw(Mi,Mj,n)
            R[i+j]=t if R[i+j] is None else ma(R[i+j],t,n)
    return R
def poly_pow(P_,m):
    R=[Id2]
    for _ in range(m): R=poly_mul(R,P_)
    return R
Ftp=Ft_poly()
for k in (2,3):
    Fk1=poly_pow(Ftp,k-1)               # F_t^{k-1}
    integrand=poly_mul([a],Fk1)         # a F_t^{k-1}
    T={}
    for deg,M in enumerate(integrand):
        T=fadd(T,sc(mtr(M,n),Fr(k,deg+1)))   # int_0^1 t^deg dt = 1/(deg+1)
    Fk=poly_pow([F1],k)[0]; F0k=poly_pow([F0],k)[0]
    lhs=fadd(mtr(Fk,n),mtr(F0k,n),-1)
    print("k=%d: tr F1^k - tr F0^k == dT :"%k, lhs==d(T)," (lhs nonzero:",bool(lhs),")", "" if k==2 else "[k=3 は R^4 では 6 形式で自明に 0。非自明な検算は k=2 のみ]")
print("closedness d tr F^2 = 0, d tr F^3=0:",d(mtr(poly_pow([F0],2)[0],n))=={}, d(mtr(poly_pow([F0],3)[0],n))=={})
# Chern-Simons: tr(F^F) = d tr(A dA + 2/3 A^3)
CS=fadd(mtr(mw(A0,md(A0,n),n),n), sc(mtr(mw(A0,mw(A0,A0,n),n),n),Fr(2,3)))
print("tr F^F == d CS(A) :", mtr(mw(F0,F0,n),n)==d(CS))
# 3x3 as well
n=3
A3=mmat(r1form,n); F3=curv(A3,n)
CS3=fadd(mtr(mw(A3,md(A3,n),n),n), sc(mtr(mw(A3,mw(A3,A3,n),n),n),Fr(2,3)))
print("3x3: tr F^F == d CS(A) :", mtr(mw(F3,F3,n),n)==d(CS3))

# ---- (5) Chern forms: c1(det) , trace of Lambda^2 derivation, Newton
hdr("(5) algebraic identities (numpy)")
Xm=np.random.randn(3,3)
def lam2(X):
    # matrix of X acting as derivation on Lambda^2 R^3 with basis e12,e13,e23
    pairs=[(0,1),(0,2),(1,2)]
    M=np.zeros((3,3))
    for c,(i,j) in enumerate(pairs):
        # X(e_i ^ e_j) = Xe_i ^ e_j + e_i ^ Xe_j
        for r,(k,l) in enumerate(pairs):
            M[r,c]=X[k,i]*(1 if l==j else 0)-X[l,i]*(1 if k==j else 0)+ (1 if k==i else 0)*X[l,j]-(1 if l==i else 0)*X[k,j]
    return M
# build more carefully with explicit wedge components
def lam2b(X):
    pairs=[(0,1),(0,2),(1,2)]
    M=np.zeros((3,3))
    for c,(i,j) in enumerate(pairs):
        for r,(k,l) in enumerate(pairs):
            # coefficient of e_k^e_l in X e_i ^ e_j + e_i ^ X e_j
            M[r,c]=X[k,i]*(l==j)-X[l,i]*(k==j)+(k==i)*X[l,j]-(l==i)*X[k,j]
    return M
print("tr Lambda^2 X = 2 tr X :",np.trace(lam2b(Xm)),2*np.trace(Xm))
gm=np.eye(3)+0.3*np.random.randn(3,3)
cof=np.linalg.det(gm)*np.linalg.inv(gm).T
# Lambda^2 g = matrix of 2x2 minors; compare with det g * (g^-1)^T  composed with Hodge identification e12<->e3, e13<->-e2, e23<->e1
pairs=[(0,1),(0,2),(1,2)]
L2=np.array([[gm[np.ix_(rows,cols)].tolist() and np.linalg.det(gm[np.ix_(rows,cols)]) for cols in pairs] for rows in pairs])
H=np.array([[0,0,1],[0,-1,0],[1,0,0]],float)  # e23->e1, e13->-e2, e12->e3 as map Lambda^2->V (order e12,e13,e23): e12->e3, e13->-e2, e23->e1
Hm=np.zeros((3,3)); Hm[2,0]=1; Hm[1,1]=-1; Hm[0,2]=1
print("Hodge * Lambda^2 g * Hodge^-1 == det g (g^-1)^T :",np.allclose(Hm@L2@np.linalg.inv(Hm),cof))
M2=np.random.randn(2,2)
print("2x2: det M = (tr^2 - tr M^2)/2 :",np.linalg.det(M2),(np.trace(M2)**2-np.trace(M2@M2))/2)

# ---- (6) CP^1: tautological bundle, Chern number, Hopf connection
hdr("(6) CP^1: O(-1), L_k, Hopf connection (numerical)")
def dens_c1(k,r): return -(k/np.pi)/(1+r*r)**2
from math import pi
rr=np.linspace(0,2000,4_000_001)
for k in (1,2,-3):
    integrand=dens_c1(k,rr)*2*pi*rr
    val=np.trapezoid(integrand,rr) if hasattr(np,'trapezoid') else np.trapz(integrand,rr)
    print("k=%d  int c1(L_k) = %.5f  (expect %d)"%(k,val,-k))
# check F = d theta for theta=zbar dz/(1+|z|^2) by finite differences, and c1 density
x0,y0=0.3,-0.8; h=1e-5
def th(xx,yy):
    zb=xx-1j*yy; H=1+xx*xx+yy*yy
    return zb/H*1, zb/H*1j   # coefficients of dx, dy
ax=lambda xx,yy: th(xx,yy)[0]; by=lambda xx,yy: th(xx,yy)[1]
curlF=(by(x0+h,y0)-by(x0-h,y0))/(2*h)-(ax(x0,y0+h)-ax(x0,y0-h))/(2*h)
print("d theta = coeff*dx^dy, coeff=",curlF," expected 2i/(1+r^2)^2 =",2j/(1+x0*x0+y0*y0)**2)
# Hopf: A = s^* (ubar . du), s=(1,z)/sqrt(1+|z|^2); compare with (theta - thetabar)/2
def s_of(xx,yy):
    zz=xx+1j*yy; rho=np.sqrt(1+abs(zz)**2); return np.array([1,zz])/rho
def pullback_omega(xx,yy):
    u=s_of(xx,yy)
    ux=(s_of(xx+h,yy)-s_of(xx-h,yy))/(2*h); uy=(s_of(xx,yy+h)-s_of(xx,yy-h))/(2*h)
    return np.vdot(u,ux), np.vdot(u,uy)   # vdot conjugates first arg: ubar . du
Ax,Ay=pullback_omega(x0,y0)
thx,thy=th(x0,y0)
# thetabar coefficients: conj
print("A=s^*omega:",Ax,Ay)
print("(theta-thetabar)/2:",(thx-np.conj(thx))/2,(thy-np.conj(thy))/2)
print("omega(xi)=i check: ubar.(i u)=",np.vdot(s_of(x0,y0),1j*s_of(x0,y0)))
# transition of Hopf sections s0=(1,z)/rho, s1=(w,1)/rho' : s0 = s1 * z/|z|
zz=0.6+0.9j; s0=np.array([1,zz])/np.sqrt(1+abs(zz)**2); w=1/zz; s1=np.array([w,1])/np.sqrt(1+abs(w)**2)
print("s0 = s1 * z/|z| :",np.allclose(s0,s1*zz/abs(zz)))
# transition function of T CP^1 : e0 = -z^-2 e1 ; winding number numerically
t=np.linspace(0,2*pi,100001); zc=np.exp(1j*t)
def wind(gv): 
    ph=np.unwrap(np.angle(gv)); return (ph[-1]-ph[0])/(2*pi)
print("wind(z)=",wind(zc)," wind(-z^-2)=",wind(-zc**-2)," => int c1 = -wind: ",-wind(zc),-wind(-zc**-2))

# ---- (7) Riemann/Levi-Civita: sphere and hyperbolic plane via Christoffel symbols (numeric)
hdr("(7) Levi-Civita, curvature from metric (finite differences)")
def christoffel(gfun,p,hh=1e-4):
    nd=len(p); g0=gfun(p); gi=np.linalg.inv(g0)
    dg=np.zeros((nd,nd,nd))  # dg[k,i,j]=d_k g_ij
    for k in range(nd):
        e=np.zeros(nd); e[k]=hh
        dg[k]=(gfun(p+e)-gfun(p-e))/(2*hh)
    G=np.zeros((nd,nd,nd))   # G[l,i,j]=Gamma^l_ij
    for l in range(nd):
        for i in range(nd):
            for j in range(nd):
                G[l,i,j]=0.5*sum(gi[l,m]*(dg[i,m,j]+dg[j,m,i]-dg[m,i,j]) for m in range(nd))
    return G
def riemann_K(gfun,p,hh=1e-3):
    nd=len(p)
    G=lambda q: christoffel(gfun,q)
    dG=np.zeros((nd,nd,nd,nd))  # dG[k,l,i,j]=d_k Gamma^l_ij
    for k in range(nd):
        e=np.zeros(nd); e[k]=hh
        dG[k]=(G(p+e)-G(p-e))/(2*hh)
    G0=G(p)
    # R^l_{ijk}: R(d_j,d_k) d_i = R^l_{ijk} d_l ; R^l_{i jk}=d_j G^l_{ki}-d_k G^l_{ji}+G^l_{jm}G^m_{ki}-G^l_{km}G^m_{ji}
    def R(l,i,j,k):
        return dG[j,l,k,i]-dG[k,l,j,i]+sum(G0[l,j,m]*G0[m,k,i]-G0[l,k,m]*G0[m,j,i] for m in range(nd))
    g0=gfun(p)
    # K = g(R(e1,e2)e2,e1)/(|e1|^2|e2|^2-g12^2) with e1=d_1, e2=d_2 : R(d_1,d_2)d_2 = R^l_{2 12} d_l
    num=sum(g0[l,0]*R(l,1,0,1) for l in range(nd))
    return num/(g0[0,0]*g0[1,1]-g0[0,1]**2)
gS=lambda q: np.array([[1,0],[0,np.sin(q[0])**2]])
gH=lambda q: np.array([[1/q[1]**2,0],[0,1/q[1]**2]])
print("S^2 K at (1.0,0.3) =",riemann_K(gS,np.array([1.0,0.3])))
print("H^2 K at (0.2,1.7) =",riemann_K(gH,np.array([0.2,1.7])))
Gs=christoffel(gS,np.array([1.0,0.3]))
print("Gamma^th_{ph ph} = -sin cos :",Gs[0,1,1],-np.sin(1.0)*np.cos(1.0)," ; Gamma^ph_{th ph} = cot :",Gs[1,0,1],1/np.tan(1.0))
print("frame: nabla_{e2} e2 = omega^1_2(e2) e1 = -cot th e1 ; here Gamma^th_{ph ph}/sin^2 =",Gs[0,1,1]/np.sin(1.0)**2,"= -cot th:",-1/np.tan(1.0))

# ---- (8) holonomy around a small square = I - eps^2 F(d_i,d_j) + O(eps^3)   (non-abelian, A polynomial)
hdr("(8) holonomy of small square vs curvature (numerical ODE, RK4)")
def Afun(q):   # R^2 with 2x2 matrix-valued A = A_1 dx + A_2 dy
    xx,yy=q
    A1=np.array([[0.3*yy,1.0+xx],[0.5*xx*yy,-0.2*yy]])
    A2=np.array([[xx*0.7,0.4],[-1.0+yy,0.1*xx]])
    return A1,A2
def Ffun(q,hh=1e-5):
    xx,yy=q
    dA2dx=(Afun((xx+hh,yy))[1]-Afun((xx-hh,yy))[1])/(2*hh)
    dA1dy=(Afun((xx,yy+hh))[0]-Afun((xx,yy-hh))[0])/(2*hh)
    A1,A2=Afun(q)
    return dA2dx-dA1dy+A1@A2-A2@A1   # F_12
def transport(path_pts_fun,T=1.0,steps=400):
    # solve sigma' = -A(gamma') sigma as matrix ODE, return propagator
    P=np.eye(2); dt=T/steps
    def rhs(t,M):
        q,v=path_pts_fun(t)
        A1,A2=Afun(q); Av=A1*v[0]+A2*v[1]
        return -Av@M
    t=0.0
    for _ in range(steps):
        k1=rhs(t,P);k2=rhs(t+dt/2,P+dt/2*k1);k3=rhs(t+dt/2,P+dt/2*k2);k4=rhs(t+dt,P+dt*k3)
        P=P+dt/6*(k1+2*k2+2*k3+k4); t+=dt
    return P
def square_path(q0,eps):
    q0=np.array(q0,float)
    corners=[q0,q0+[eps,0],q0+[eps,eps],q0+[0,eps],q0]
    def f(t):
        seg=min(int(t*4),3); lt=t*4-seg
        a,b=corners[seg],corners[seg+1]
        return a+lt*(b-a), 4*(b-a)
    return f
q0=(0.4,-0.3); F12=Ffun(q0)
for eps in (0.2,0.1,0.05):
    Pm=transport(square_path(q0,eps),1.0,800)
    err=Pm-(np.eye(2)-eps**2*F12)
    print("eps=%.2f  |P-(I-eps^2 F)|=%.2e   |P-I|=%.2e"%(eps,np.linalg.norm(err),np.linalg.norm(Pm-np.eye(2))))
# also the claimed segment expansion T_i = I - eps A_i + eps^2/2 (A_i^2 - d_i A_i): checked implicitly (order eps^2 agreement above)
print("F12 at q0 =",F12.tolist())

# ---- (9) holonomy on the sphere along the latitude theta=th0, and S^1 / AB / torus
hdr("(9) S^2 latitude holonomy and S^1 holonomy")
def lat_holonomy(th0,steps=20000):
    # frame e1=d_theta, e2=(1/sin) d_phi ; A = [[0,-cos th0],[cos th0,0]] dphi ; sigma'=-A sigma on phi in [0,2pi]
    Am=np.array([[0,-np.cos(th0)],[np.cos(th0),0]])
    M=np.eye(2); dphi=2*pi/steps
    from math import cos,sin
    # exact: exp(-Am*2pi)
    ev=np.linalg.eig(-Am*2*pi)
    c=np.cos(-2*pi*np.cos(th0)); s_=np.sin(-2*pi*np.cos(th0))
    # exp(-2pi cos(th0) J) with J=[[0,-1],[1,0]] -> rotation by angle -2pi cos th0
    return np.array([[c,-s_],[s_,c]])
for th0 in (0.5,1.0,pi/2,2.0):
    R=lat_holonomy(th0)
    ang=np.arctan2(R[1,0],R[0,0])
    area=2*pi*(1-np.cos(th0))
    print("th0=%.3f: rotation angle = %.5f ; enclosed area (north cap) = %.5f ; difference mod 2pi = %.2e"%(th0,ang,area,(ang-area+pi)%(2*pi)-pi))
print("S^1: nabla=d+i*lam*dtheta, holonomy exp(-2 pi i lam):",np.exp(-2j*pi*0.3)," and gauge g=e^{ik th} does not change it (k int):",np.exp(-2j*pi*(0.3+2)))
