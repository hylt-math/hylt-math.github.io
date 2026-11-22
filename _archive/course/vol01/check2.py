from check import *
import numpy as np
from scipy import integrate
def pcompose(p,Fs):
    r={}
    for k,v in p.items():
        t=const(v)
        for i,e in enumerate(k):
            for _ in range(e): t=pmul(t,Fs[i])
        r=padd(r,t)
    return r
def pullback(a,Fs):
    r={}
    for k,p in a.items():
        t={():pcompose(p,Fs)}
        for i in k:
            dF=d({():Fs[i]})
            t=wedge(t,dF)
        r=fadd(r,t)
    return r
Fs=[padd(P(x,x),P(y,y),-1),pscale(P(x,y),2),{}]
print("F*(dx^dy)",pr(pullback(f1((const(1),(0,1))),Fs)))
print("F*(xdy-ydx)",pr(pullback(f1((x,(1,)),(pscale(y,-1),(0,))),Fs)))
# polar: x=r cos t -> use (r,t) not polynomial; check via numeric jacobian later
# Matrix-valued forms: A = [[0, z dx],[x dy,0]]
def mform_wedge(A,B):
    n=2; R=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j]=fadd(R[i][j],wedge(A[i][k],B[k][j]))
    return R
def madd(A,B,s=1): return [[fadd(A[i][j],B[i][j],s) for j in range(2)] for i in range(2)]
def md(A): return [[d(A[i][j]) for j in range(2)] for i in range(2)]
A=[[{}, {(0,):z}],[{(1,):x},{}]]
F=madd(md(A),mform_wedge(A,A))
print("F=",[[pr(F[i][j]) for j in range(2)] for i in range(2)])
# Bianchi dF + A F - F A
B=madd(madd(md(F),mform_wedge(A,F)),mform_wedge(F,A),-1)
print("Bianchi",B)
# gauge: g = [[1,x],[0,1]] -> g^{-1}=[[1,-x],[0,1]]
g=[[ {():const(1)},{():x}],[{}, {():const(1)}]]
gi=[[ {():const(1)},{():pscale(x,-1)}],[{}, {():const(1)}]]
Ap=madd(mform_wedge(mform_wedge(gi,A),g),mform_wedge(gi,md(g)))
Fp=madd(md(Ap),mform_wedge(Ap,Ap))
print("gauge F'=g^-1 F g:",Fp==mform_wedge(mform_wedge(gi,F),g))
# numeric checks
# stereographic jacobian
def inv(u,v): r2=u*u+v*v; return np.array([u/r2,v/r2])
u,v=0.7,-0.4;h=1e-6
J=np.column_stack([(inv(u+h,v)-inv(u-h,v))/(2*h),(inv(u,v+h)-inv(u,v-h))/(2*h)])
print("det J",np.linalg.det(J),-1/(u*u+v*v)**2)
# check stereographic relation with a point on S^2
p=np.array([0.3,0.4,np.sqrt(1-.25)]);xx,yy,zz=p
print("u'=",xx/(1+zz), "u/r2", (xx/(1-zz))/((xx/(1-zz))**2+(yy/(1-zz))**2))
# CP1: c1 integral for h=(1+|z|^2)^k : density = -(k/pi)/(1+r^2)^2
for k in [1,2,-3]:
    val,_=integrate.dblquad(lambda r,t: -(k/np.pi)/(1+r*r)**2*r,0,2*np.pi,0,np.inf)
    print("k",k,"int c1 =",val)
# verify F = dtheta numerically: theta = k zbar dz/(1+|z|^2); F = d zbar^dz *k/(1+|z|^2)^2
# check via finite differences of components: theta = (a dx + b dy), a= k*(x - i y)/(1+r2), b = i*k*(x-iy)/(1+r2)
k=1
def a(x,y): return k*(x-1j*y)/(1+x*x+y*y)
def b(x,y): return 1j*k*(x-1j*y)/(1+x*x+y*y)
x0,y0=0.3,-0.8;h=1e-5
curl=(b(x0+h,y0)-b(x0-h,y0))/(2*h)-(a(x0,y0+h)-a(x0,y0-h))/(2*h)
print("dtheta coefficient of dx^dy",curl," expected 2i k/(1+r2)^2 =",2j*k/(1+x0*x0+y0*y0)**2)
# theta0-theta1 = dz/z on |z|... pointwise
z0=0.6+0.9j; 
th0=np.conj(z0)/(1+abs(z0)**2); th1=-1/(z0*(1+abs(z0)**2)); print("th0-th1",th0-th1,"1/z",1/z0)
# holonomy: ds/dt=-i lam s ; s(2pi)=exp(-2 pi i lam)
# density of omega_theta closed: (x dy - y dx)/r^2
def Pf(x,y): return -y/(x*x+y*y)
def Qf(x,y): return x/(x*x+y*y)
print("closed",(Qf(x0+h,y0)-Qf(x0-h,y0))/(2*h)-(Pf(x0,y0+h)-Pf(x0,y0-h))/(2*h))
# polar pullback: jacobian of (r,t)->(r cos t, r sin t) = r
# torus gradient
# F^*(dx dy)=4(x^2+y^2): jac
