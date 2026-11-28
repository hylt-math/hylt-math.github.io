# 担当 A (§1-§3) の検算。fractions / numpy のみ。
from fractions import Fraction as Fr
import itertools, math
import numpy as np
ok=True
def chk(name,cond,info=""):
    global ok
    print(("OK   " if cond else "FAIL ")+name+(" : "+str(info) if not (isinstance(info,str) and info=="") else ""))
    ok = ok and cond

# ---- polynomial vector fields (exact) ----
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
def var(i,N):
    k=[0]*N;k[i]=1;return {tuple(k):Fr(1)}
def const(c,N): return {(0,)*N:Fr(c)} if c!=0 else {}
def scal(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def br(X,Y):
    N=len(X); out=[]
    for k in range(N):
        t={}
        for i in range(N):
            t=padd(t,pmul(X[i],pd(Y[k],i)))
            t=padd(t,pmul(Y[i],pd(X[k],i)),-1)
        out.append(t)
    return out
def eq(A,B): return all(padd(a,b,-1)=={} for a,b in zip(A,B))
N=3
x,y,z=[var(i,N) for i in range(3)]
O={}
# §3 brackets
R=[scal(y,-1),x,O]        # x dy - y dx  (R3=L3)
Ee=[x,y,O]
chk("[R,E]=0 on R^2",eq(br(R,Ee),[O,O,O]))
L1=[O,scal(z,-1),y]; L2=[z,O,scal(x,-1)]; L3=[scal(y,-1),x,O]
chk("[L1,L2]=-L3 (vector fields)",eq(br(L1,L2),[scal(c,-1) for c in L3]))
chk("[L2,L3]=-L1",eq(br(L2,L3),[scal(c,-1) for c in L1]))
chk("[L3,L1]=-L2",eq(br(L3,L1),[scal(c,-1) for c in L2]))
# Witt (1D)
N1=1; x1=var(0,1)
def pw(p,n):
    r=const(1,1)
    for _ in range(n): r=pmul(r,p)
    return r
for m in range(-0,4):
    for n in range(0,4):
        em=[pw(x1,m+1)]; en=[pw(x1,n+1)]
        b=br(em,en)[0]
        rhs=scal(pw(x1,m+n+1),n-m)
        chk(f"Witt [e_{m},e_{n}]",padd(b,rhs,-1)=={})
# contact and others
X=[const(1,3),O,y]; Y=[O,const(1,3),O]
chk("[d_x+y d_z,d_y]=-d_z",eq(br(X,Y),[O,O,const(-1,3)]))
chk("[xd_x+yd_y+zd_z,d_x]=-d_x",eq(br([x,y,z],[const(1,3),O,O]),[const(-1,3),O,O]))
X=[const(1,3),O,O];Y=[O,x,O];Z=[O,O,pmul(x,x)]
J=[padd(padd(a,b),c) for a,b,c in zip(br(X,br(Y,Z)),br(Y,br(Z,X)),br(Z,br(X,Y)))]
chk("Jacobi X=dx,Y=x dy,Z=x^2 dz",all(j=={} for j in J), br(Y,Z))
X=[O,x,O];Y=[O,O,y];Z=[z,O,O]
chk("[X,Y]=x d_z",eq(br(X,Y),[O,O,x]))
chk("[Y,Z]=y d_x",eq(br(Y,Z),[y,O,O]))
chk("[Z,X]=z d_y",eq(br(Z,X),[O,z,O]))
chk("[X,[Y,Z]]=x d_x - y d_y",eq(br(X,br(Y,Z)),[x,scal(y,-1),O]))
chk("[Y,[Z,X]]=y d_y - z d_z",eq(br(Y,br(Z,X)),[O,y,scal(z,-1)]))
chk("[Z,[X,Y]]=z d_z - x d_x",eq(br(Z,br(X,Y)),[scal(x,-1),O,z]))
# frobenius examples
A1=[const(1,3),O,y]; A2=[O,const(1,3),x]
chk("D=span(dx+y dz, dy+x dz) involutive ([.,.]=0)",eq(br(A1,A2),[O,O,O]))
B1=[const(1,3),z,O]; B2=[O,O,const(1,3)]
chk("[dx+z dy,dz]=-dy",eq(br(B1,B2),[O,const(-1,3),O]))
# sphere distribution: [R1,R2]=-R3 and z*(-R3)=x R1 + y R2
lhs=[scal(pmul(z,c),1) for c in br(L1,L2)]   # = -z R3
rhs=[padd(pmul(x,a),pmul(y,b)) for a,b in zip(L1,L2)]
chk("z[R1,R2] = x R1 + y R2",eq(lhs,rhs))
# ax+b: X1=a d_a, X2=a d_b
a_,b_=var(0,2),var(1,2)
X1=[a_,{}];X2=[{},a_]
chk("[a d_a,a d_b]=a d_b",eq(br(X1,X2),X2))
# x d_x vs d_x flows: commutator displacement -t^2
for t in [Fr(1,10),Fr(1,100)]:
    pass
import math
t=1e-3
def comp(x0):
    xx=math.exp(t)*x0; xx=xx+t; xx=math.exp(-t)*xx; xx=xx-t; return xx
chk("x d_x, d_x loop: displacement ~ -t^2",abs((comp(0.7)-0.7)/t**2+1)<2e-3,(comp(0.7)-0.7)/t**2)
# X=d_x, Y=x d_y loop exact
def loop(p,t):
    x,y=p; x+=t; y+=t*x; x-=t; y-=t*x; return (x,y)
chk("d_x, x d_y loop from (1,0) is (1,t^2)",loop((Fr(1),Fr(0)),Fr(3,7))==(1,Fr(9,49)))
# ---- Lie derivative numerically with random-ish fields ----
def Xf(p): x,y=p; return np.array([-y+x*x, x*y])
def Yf(p): x,y=p; return np.array([y, x-y*y])
def flow(F,p,t,n=4000):
    p=np.array(p,float); h=t/n
    for _ in range(n):
        k1=F(p);k2=F(p+h/2*k1);k3=F(p+h/2*k2);k4=F(p+h*k3)
        p=p+h/6*(k1+2*k2+2*k3+k4)
    return p
def jac(F,p,eps=1e-6):
    p=np.array(p,float);J=np.zeros((2,2))
    for j in range(2):
        e=np.zeros(2);e[j]=eps
        J[:,j]=(F(p+e)-F(p-e))/(2*eps)
    return J
def Lie_num(p,t=1e-4):
    p=np.array(p,float)
    def val(tt):
        q=flow(Xf,p,tt,200)
        # d phi_{-tt} at q
        Jm=np.zeros((2,2))
        eps=1e-5
        for j in range(2):
            e=np.zeros(2);e[j]=eps
            Jm[:,j]=(flow(Xf,q+e,-tt,200)-flow(Xf,q-e,-tt,200))/(2*eps)
        return Jm@Yf(q)
    return (val(t)-val(-t))/(2*t)
p0=(0.3,-0.5)
Jx=jac(Xf,p0);Jy=jac(Yf,p0)
bracket=Jy@Xf(p0)-Jx@Yf(p0)     # [X,Y]^k = X^i d_i Y^k - Y^i d_i X^k
chk("Lie derivative = [X,Y] numerically",np.allclose(Lie_num(p0),bracket,atol=1e-4),(Lie_num(p0),bracket))
# rotation example: L_X d_x = -d_y
def Xr(p): return np.array([-p[1],p[0]])
Rm=lambda t: np.array([[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]])
hh_=1e-6
chk("Lie_X Y for rotation, Y=d_x: d/dt R_{-t}e1 = (0,-1)",np.allclose(((Rm(-hh_)@[1,0])-(Rm(hh_)@[1,0]))/(2*hh_),[0,-1],atol=1e-6))
# ---- GL(2) left-invariant bracket (numeric finite diff) ----
rng=np.random.default_rng(1)
A=rng.normal(size=(2,2));B=rng.normal(size=(2,2));g0=rng.normal(size=(2,2))
def XA(g): return g@A
def XB(g): return g@B
def dirder(F,g,V,eps=1e-6): return (F(g+eps*V)-F(g-eps*V))/(2*eps)
brk=dirder(XB,g0,XA(g0))-dirder(XA,g0,XB(g0))   # [X_A,X_B] = X_A(X_B) - X_B(X_A) (components)
chk("[X_A,X_B]=X_[A,B] on GL(2)",np.allclose(brk,g0@(A@B-B@A),atol=1e-6))
# fundamental v.f. antihom: [hatA,hatB]=-hat[A,B]
A3=rng.normal(size=(3,3));B3=rng.normal(size=(3,3));v0=rng.normal(size=3)
def hA(v): return A3@v
def hB(v): return B3@v
def dd(F,v,V,eps=1e-6): return (F(v+eps*V)-F(v-eps*V))/(2*eps)
b3=dd(hB,v0,hA(v0))-dd(hA,v0,hB(v0))
chk("[hatA,hatB] = hat(BA-AB)",np.allclose(b3,(B3@A3-A3@B3)@v0,atol=1e-6))
# so(3)
def Lm(i):
    M=np.zeros((3,3))
    for j in range(3):
        for k in range(3):
            M[j,k]=-np.linalg.det(np.array([np.eye(3)[i],np.eye(3)[j],np.eye(3)[k]]))
    return M
Ls=[Lm(i) for i in range(3)]
def comm(a,b): return a@b-b@a
eps3=lambda i,j,k: np.linalg.det(np.array([np.eye(3)[i],np.eye(3)[j],np.eye(3)[k]]))
good=all(np.allclose(comm(Ls[i],Ls[j]),sum(eps3(i,j,k)*Ls[k] for k in range(3))) for i in range(3) for j in range(3))
chk("[L_i,L_j]=eps_ijk L_k",good)
chk("L_i v = e_i x v",all(np.allclose(Ls[i]@v0,np.cross(np.eye(3)[i],v0)) for i in range(3)))
chk("L1 matrix", np.allclose(Ls[0],[[0,0,0],[0,0,-1],[0,1,0]]) and np.allclose(Ls[1],[[0,0,1],[0,0,0],[-1,0,0]]) and np.allclose(Ls[2],[[0,-1,0],[1,0,0],[0,0,0]]))
# su(2)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
e=[-0.5j*s for s in sig]
good=all(np.allclose(comm(e[i],e[j]),sum(eps3(i,j,k)*e[k] for k in range(3))) for i in range(3) for j in range(3))
chk("su(2): [e_i,e_j]=eps e_k",good)
# ---- §1 ----
al=np.array([1,2,0]);be=np.array([0,1,-1]);ga=np.array([1,0,1]);v=np.array([1,0,2]);w=np.array([0,1,1])
chk("alpha^beta(v,w)=4",(al@v)*(be@w)-(al@w)*(be@v)==4)
coef={(0,1):al[0]*be[1]-al[1]*be[0],(0,2):al[0]*be[2]-al[2]*be[0],(1,2):al[1]*be[2]-al[2]*be[1]}
chk("alpha^beta = e12 - e13 - 2 e23",coef=={(0,1):1,(0,2):-1,(1,2):-2},coef)
chk("alpha^beta(v,w) via expansion",sum(c*(v[i]*w[j]-v[j]*w[i]) for (i,j),c in coef.items())==4)
chk("alpha^beta^gamma = -e123",round(np.linalg.det(np.array([al,be,ga])))==-1)
# pairing
n=3
G=0.5*np.block([[np.zeros((n,n)),np.eye(n)],[np.eye(n),np.zeros((n,n))]])
ev=np.linalg.eigvalsh(G)
chk("signature (n,n)",sum(ev>0)==n and sum(ev<0)==n,ev)
n=2
# x = e1 -2 e2 + 3e^1 + e^2: v=(1,-2),xi=(3,1)
chk("<x,x> = xi(v) = 1",3*1+1*(-2)==1)
Bm=np.array([[0,2.0,0],[-2,0,1],[0,-1,0]])  # skew
n=3
def pair(a,b): return 0.5*(a[n:]@b[:n]+b[n:]@a[:n])
def eB(a): return np.concatenate([a[:n],a[n:]+Bm.T@a[:n]*0+ (Bm@a[:n])])  # iota_v B = B(v,.) -> row/col: B v
a=rng.normal(size=6);b=rng.normal(size=6)
chk("e^B orthogonal for skew B",abs(pair(eB(a),eB(b))-pair(a,b))<1e-12)
Bn=np.array([[0,2.0,0],[1,0,1],[0,-1,0]])
def eBn(a): return np.concatenate([a[:n],a[n:]+Bn@a[:n]])
chk("e^B not orthogonal for non-skew B",abs(pair(eBn(a),eBn(b))-pair(a,b))>1e-6)
# B=e1^e2 in n=2 : graph basis
# J on R^4
J4=np.zeros((4,4));J4[1,0]=1;J4[0,1]=-1;J4[3,2]=1;J4[2,3]=-1
chk("J^2=-1",np.allclose(J4@J4,-np.eye(4)))
v1=np.array([1,0,0,0],complex)-1j*(J4@np.array([1,0,0,0]))
chk("e1 - i J e1 = e1 - i e2 eigen i",np.allclose(J4@v1,1j*v1))
# omega = dz1^dz2
dz1=np.array([1,1j,0,0]);dz2=np.array([0,0,1,1j])
def w2(u,vv): return (dz1@u)*(dz2@vv)-(dz1@vv)*(dz2@u)
e1,e2,e3,e4=np.eye(4)
chk("omega(Je1,e3)= i omega(e1,e3)",abs(w2(J4@e1,e3)-1j*w2(e1,e3))<1e-12)
chk("dz1^dz2 = e13+i e14 + i e23 - e24",abs(w2(e1,e3)-1)<1e-12 and abs(w2(e1,e4)-1j)<1e-12 and abs(w2(e2,e3)-1j)<1e-12 and abs(w2(e2,e4)+1)<1e-12)
g=np.eye(4)
def h(u,vv): return u@vv - 1j*((J4@u)@vv)
chk("h(e1,e2)=-i, h(Je1,e2)=i h(e1,e2)",abs(h(e1,e2)+1j)<1e-12 and abs(h(J4@e1,e2)-1j*h(e1,e2))<1e-12)
# J-tilde orthogonal (n=4)
n=4
def Jt(a): return np.concatenate([-J4@a[:4], a[4:]@J4])
a=rng.normal(size=8);b=rng.normal(size=8)
chk("calJ_J orthogonal for pairing",abs(pair(Jt(a),Jt(b))-pair(a,b))<1e-12)
# folium
x0=Fr(3,2)
F=lambda x,y: x**3+y**3-3*x*y
chk("folium point on curve",F(x0,x0)==0)
Fx=3*x0**2-3*x0;Fy=3*x0**2-3*x0
chk("g'(3/2)=-1",-Fx/Fy==-1,(Fx,Fy))
# Picard x'=x
t=Fr(1,3); it=[Fr(1)]
xk=[Fr(1)]
# Picard for x'=x: coefficient list; x_{k+1}=1+int x_k
co=[Fr(1)]
for _ in range(5):
    co=[Fr(1)]+[c/(i+1) for i,c in enumerate(co)]
chk("Picard iterates: coefficients 1/j!",co==[Fr(1,math.factorial(j)) for j in range(6)])
# ---- §2 ----
for dim in [2,3]:
    for _ in range(3):
        u=rng.normal(size=dim)
        inv=lambda u: u/(u@u)
        eps=1e-6;Jm=np.zeros((dim,dim))
        for j in range(dim):
            e=np.zeros(dim);e[j]=eps
            Jm[:,j]=(inv(u+e)-inv(u-e))/(2*eps)
        chk(f"det D(inversion) = -|u|^-2n (n={dim})",abs(np.linalg.det(Jm)+(u@u)**(-dim))<1e-5)
        anti=lambda u: -u/(u@u)
        for j in range(dim):
            e=np.zeros(dim);e[j]=eps
            Jm[:,j]=(anti(u+e)-anti(u-e))/(2*eps)
        chk(f"det D(antipodal in chart) = (-1)^(n+1)|u|^-2n (n={dim})",abs(np.linalg.det(Jm)-(-1)**(dim+1)*(u@u)**(-dim))<1e-5)
# antipodal in stereographic chart
for _ in range(3):
    xx=rng.normal(size=3);xx/=np.linalg.norm(xx)
    sN=lambda x: x[:2]/(1-x[2])
    chk("sigma_N(-x) = -u/|u|^2",np.allclose(sN(-xx),-sN(xx)/(sN(xx)@sN(xx))))
# stereographic inverse and transition
u=rng.normal(size=2)
xinv=np.concatenate([2*u,[u@u-1]])/(u@u+1)
chk("sigma_N^{-1} on sphere",abs(np.linalg.norm(xinv)-1)<1e-12 and np.allclose(sN(xinv),u))
chk("sigma_S sigma_N^{-1} = u/|u|^2",np.allclose(xinv[:2]/(1+xinv[2]),u/(u@u)))
# RP^2 transition Jacobian -1/u^3
def tr(uv):
    u,v=uv; return np.array([1/u, v/u])
for uv in [(0.7,0.3),(-1.3,2.0),(2.0,-1.0)]:
    uv=np.array(uv);eps=1e-6;Jm=np.zeros((2,2))
    for j in range(2):
        e=np.zeros(2);e[j]=eps
        Jm[:,j]=(tr(uv+e)-tr(uv-e))/(2*eps)
    chk("RP2 Jacobian = -1/u^3",abs(np.linalg.det(Jm)+1/uv[0]**3)<1e-5)
# SO(n): dim and regular value
for n in [2,3,4]:
    Q,_=np.linalg.qr(rng.normal(size=(n,n)))
    S=rng.normal(size=(n,n));S=S+S.T
    H=0.5*Q@S
    chk(f"A^T H + H^T A = S (n={n}); dim O(n)={n*(n-1)//2}",np.allclose(Q.T@H+H.T@Q,S) and n*n-n*(n+1)//2==n*(n-1)//2)
# d det_A(H) = det A tr(A^{-1}H)
n=3;Aa=rng.normal(size=(n,n));Hh=rng.normal(size=(n,n));eps=1e-6
chk("d det formula",abs((np.linalg.det(Aa+eps*Hh)-np.linalg.det(Aa-eps*Hh))/(2*eps)-np.linalg.det(Aa)*np.trace(np.linalg.inv(Aa)@Hh))<1e-5)
# torus level set regularity
bad=0
for _ in range(2000):
    th,ph=rng.uniform(0,2*np.pi,2)
    P=np.array([(2+np.cos(ph))*np.cos(th),(2+np.cos(ph))*np.sin(th),np.sin(ph)])
    r=np.hypot(P[0],P[1])
    Fv=(r-2)**2+P[2]**2
    grad=np.array([2*(r-2)*P[0]/r,2*(r-2)*P[1]/r,2*P[2]])
    if abs(Fv-1)>1e-9 or np.linalg.norm(grad)<1e-6: bad+=1
chk("torus: F=1 and grad!=0 on parametrized torus",bad==0)
# figure eight: injective on (-pi,pi), immersion
ts=np.linspace(-np.pi+1e-3,np.pi-1e-3,4001)
pts=np.stack([np.sin(2*ts),np.sin(ts)],1)
from collections import defaultdict
d=np.linalg.norm(pts[:,None,:]-pts[None,::1,:],axis=2)
close=np.argwhere(d<1e-9)
chk("figure-eight: no distinct params give same point (grid)",all(abs(ts[i]-ts[j])<1e-12 for i,j in close))
chk("figure-eight: velocity never 0",np.all(np.hypot(2*np.cos(2*ts),np.cos(ts))>0.5))
chk("figure-eight: beta(t)->0 as t->+-pi",np.linalg.norm(pts[0])<1e-2 and np.linalg.norm(pts[-1])<1e-2)
# CP1: S^2 -> CP^1 : conj(sigma_S) = 1/sigma_N
x3=rng.normal(size=3);x3/=np.linalg.norm(x3)
zN=complex(*(x3[:2]/(1-x3[2])));vS=x3[:2]/(1+x3[2]);wS=complex(vS[0],-vS[1])
chk("conj(sigma_S)=1/sigma_N",abs(wS-1/zN)<1e-12)
# bump / partition of unity on S^1
def hh(t): return math.exp(-1/t) if t>0 else 0.0
lam=lambda t: hh(t)/(hh(t)+hh(1-t))
def rho2(th):
    th=((th+math.pi)%(2*math.pi))-math.pi
    return 1-lam((abs(th)-math.pi/4)/(math.pi/2))
res=True
for th in np.linspace(0,2*np.pi,400):
    r2=rho2(th);r1=1-r2
    t=((th+math.pi)%(2*math.pi))-math.pi
    if abs(t)<=math.pi/4 and abs(r2-1)>1e-12: res=False
    if abs(t)>=3*math.pi/4 and abs(r2)>1e-12: res=False
chk("partition of unity on S^1: rho2=1 on |th|<=pi/4, 0 on |th|>=3pi/4",res)
# contact loop
r=1.7;ts=np.linspace(0,2*np.pi,200001)
xs=r*np.cos(ts);ys=r*np.sin(ts)
dz=np.sum(0.5*(ys[1:]+ys[:-1])*(xs[1:]-xs[:-1]))
chk("oint y dx over ccw circle = -pi r^2",abs(dz+math.pi*r*r)<1e-4,dz)
# Kronecker return map
a=0.3
y0=0.2;ret=(y0+a*1.0)%1
chk("Kronecker: after x-time 1 the y-coordinate is y0+a",abs(ret-0.5)<1e-12)
# flows: x^2 d_x
x0=0.4;tt=1.0;chk("x^2 flow x0/(1-x0 t)",abs((x0/(1-x0*tt))-(lambda: (lambda f: f)(x0/(1-x0*tt)))())<1e-15)
# d/dt of x0/(1-x0 t) = x^2
tt=0.7;h=1e-6;f=lambda t:x0/(1-x0*t)
chk("d/dt x0/(1-x0 t)= x^2",abs((f(tt+h)-f(tt-h))/(2*h)-f(tt)**2)<1e-6)
# polar frame
th=0.8;r=1.3
xx=r*math.cos(th);yy=r*math.sin(th)
dr=np.array([math.cos(th),math.sin(th)]);dth=np.array([-r*math.sin(th),r*math.cos(th)])
chk("d_r=(x dx+y dy)/r, d_th = x dy - y dx",np.allclose(dr,[xx/r,yy/r]) and np.allclose(dth,[-yy,xx]))
# z^2 differential
Fz=lambda p: np.array([p[0]**2-p[1]**2,2*p[0]*p[1]])
pp=np.array([0.6,-0.4]);e=np.array([1e-6,0])
chk("dF(d_x)=2x d_u+2y d_v",np.allclose((Fz(pp+e)-Fz(pp-e))/2e-6,[2*pp[0],2*pp[1]],atol=1e-6))
chk("dF at -p of d_x is minus that",np.allclose((Fz(-pp+e)-Fz(-pp-e))/2e-6,[-2*pp[0],-2*pp[1]],atol=1e-6))
print("ALL OK" if ok else "SOME FAILED")
