import numpy as np
from math import pi
# |x| Fourier coefficients
N=200000; x=np.linspace(-pi,pi,N,endpoint=False)+pi/N; u=np.abs(x)
for k in [1,2,3,4,5]:
    fk=np.mean(u*np.exp(-1j*k*x)); print(k,fk.real.round(8),round(((-1)**k-1)/(pi*k*k),8))
print("u^(0)",np.mean(u),pi/2)
# r_2
def r2(mu): return sum(1 for a in range(-60,61) for b in range(-60,61) if a*a+b*b==mu)
print([ (m,r2(m)) for m in [1,2,3,5,25]])
# Hodge 1-form decomposition check via finite differences
f=lambda x,y: np.sin(x+y)
x0,y0=0.37,1.1; h=1e-5
phi=lambda x,y:-0.5*np.cos(x+y); h2=lambda x,y:-0.5*np.cos(x+y)
dphi_x=(phi(x0+h,y0)-phi(x0-h,y0))/(2*h); dphi_y=(phi(x0,y0+h)-phi(x0,y0-h))/(2*h)
hy=(h2(x0,y0+h)-h2(x0,y0-h))/(2*h); hx=(h2(x0+h,y0)-h2(x0-h,y0))/(2*h)
dstar_x=hy; dstar_y=-hx
print("dx comp",dphi_x+dstar_x,f(x0,y0)," dy comp",dphi_y+dstar_y)
# also d*alpha = -cos(x+y) and Delta phi consistency: d^*d phi = d^* alpha
# Landau k=2 check
k=2
for rho in range(k):
    v=lambda x:np.exp(rho*x-k*x**2/(4*np.pi))
    def u2(x,y,J=15): return sum(v(x-2*np.pi*j)*np.exp(1j*(rho+j*k)*y) for j in range(-J,J+1))
    x0,y0=0.9,0.4; h=1e-5
    ux=(u2(x0+h,y0)-u2(x0-h,y0))/(2*h); uy=(u2(x0,y0+h)-u2(x0,y0-h))/(2*h)
    print("k=2 rho",rho,abs(u2(x0+2*np.pi,y0)-np.exp(1j*k*y0)*u2(x0,y0)),abs(0.5*(ux+1j*uy+(k/(2*np.pi))*x0*u2(x0,y0))))
# Toeplitz f=z^2+0.3 coker vectors: check S^*-conj(a) eigenvectors  (a^2=-0.3) : T_f^* x=0 for x_j = conj(a)^j
a=1j*np.sqrt(0.3); n=400
x=np.array([np.conj(a)**j for j in range(n)])
# T_f^*= (S^*)^2+0.3 acting: (S^* x)_j=x_{j+1}
Sx=lambda x: np.append(x[1:],0)
print("T_f^* x residual",np.abs(Sx(Sx(x))+0.3*x)[:300].max())
x2=np.array([np.conj(-a)**j for j in range(n)]); print(np.abs(Sx(Sx(x2))+0.3*x2)[:300].max())
# self-adjoint and index: A_f kernel w=-2 : e0-e_{-2}
# ODE d/dtheta - b: periodic solution u=exp(c theta + eps sin theta), c=in
c=2j; eps=1.3; th=np.linspace(0,2*np.pi,5)
uu=np.exp(c*th+eps*np.sin(th)); print("periodic:",abs(uu[0]-uu[-1]))
# b-toy numerics: discretize T_c = d/dt + c on L2(0,T) with no BC, count small singular values (T large)
def sv(c,T=40.0,n=800):
    h=T/n
    # unknown at nodes 0..n ; operator rows: midpoints
    A=np.zeros((n,n+1),dtype=complex)
    for i in range(n):
        A[i,i]=-1/h+c/2; A[i,i+1]=1/h+c/2
    A*=np.sqrt(h)  # weights; also column weights ~ sqrt(h) for node norm
    s=np.linalg.svd(A*1.0,compute_uv=False); return s
for c in [1.0,-1.0,0.0+0.5j]:
    s=sv(c); 
    # nullspace dimension of rectangular n x (n+1) is at least 1 numerically; look at smallest singular value
    print("c",c,"smallest sv",s[-1],"2nd",s[-2])
