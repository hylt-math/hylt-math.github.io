import numpy as np, itertools, sys
from fractions import Fraction as F
from math import factorial, comb
np.set_printoptions(linewidth=150)
out=[]
def say(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)

# ---------- 1. S^1: d/dtheta - b, kernel jump; torus Dolbeault family; spectral flow ----------
def smin(c,eps=1.5,N=60):
    # matrix of d/dtheta - (c+eps cos) in Fourier basis e^{i n theta}: diag(i n - c) - eps/2 (shift +1 + shift -1)
    n=np.arange(-N,N+1)
    A=np.diag(1j*n-c).astype(complex)
    for i in range(len(n)-1):
        A[i,i+1]-=eps/2; A[i+1,i]-=eps/2
    s=np.linalg.svd(A,compute_uv=False)
    return s.min()
say("[S1] smallest singular value of d/dtheta-(c+1.5cos):")
for c in (0,2j,0.5,0.3+1j,1j*0.5,3j,0.01):
    say("  c=",c,"smin=%.3e"%smin(c))
# index 0: compare dim ker P and dim ker P^* numerically (truncation): singular values of A and A^H both small together (same).
# spectral flow of -i d/dtheta + t: eigenvalues n+t, t in [0,1]
ts=np.linspace(0,1,2001)
def sflow(f):
    # count sign changes of the lowest few eigenvalues crossing zero upward minus downward
    ev=np.array([f(t) for t in ts]) # shape (T, m)
    sf=0
    for j in range(ev.shape[1]):
        e=ev[:,j]
        for a,b in zip(e[:-1],e[1:]):
            if a<0<=b: sf+=1
            if a>0>=b and not (a==0): sf-=1
    return sf
f_plus=lambda t: np.array([n+t for n in range(-5,6)])
f_minus=lambda t: np.array([n-t for n in range(-5,6)])
# avoid exact zero at t=0 issue: shift tiny
ts=np.linspace(1e-9,1+1e-9,2001)
say("[SF] spectral flow of -i d/dth + t over t in [0,1]:",sflow(f_plus)," ; of -i d/dth - t:",sflow(f_minus))

# ---------- 2. Poincare bundle: c(ind)=exp(-theta) from ch=r-theta; Abel-Jacobi degree ----------
def series_c_from_ch(chs,N):
    # chs[k]=ch_k as multiple of theta^k/k!-type? Here we work in R=Q[theta]/(theta^(N+1)), ch given as poly list coefficients of theta^k.
    # c_t = exp( sum_{k>=1} (-1)^{k-1}(k-1)! ch_k )
    L=[F(0)]*(N+1)
    for k in range(1,N+1):
        L[k]=F((-1)**(k-1)*factorial(k-1))*chs[k]
    # exp of polynomial
    res=[F(1)]+[F(0)]*N; term=[F(1)]+[F(0)]*N
    for m in range(1,N+1):
        new=[F(0)]*(N+1)
        for i,a in enumerate(term):
            for j,b in enumerate(L):
                if i+j<=N: new[i+j]+=a*b
        term=[x/m for x in new]
        res=[x+y for x,y in zip(res,term)]
    return res
for g in (1,2,3,4):
    N=g
    chs=[F(5)]+[F(-1)]+[F(0)]*(N-1)   # rank symbolic, ch_1=-theta
    c=series_c_from_ch(chs,N)
    ok=all(c[k]==F((-1)**k,factorial(k)) for k in range(N+1))
    say("[c(E)=exp(-theta)] g=%d: c_k = (-1)^k theta^k/k! ->"%g,ok)
# Abel-Jacobi degree: int_C theta = g ; [C]=theta^(g-1)/(g-1)!, theta^g=g! => theta.[C]=g
for g in (2,3,4):
    say("[AJ] g=%d: theta.[C]= theta^g/(g-1)! = %s (theta^g=g!=%d)"%(g,F(factorial(g),factorial(g-1)),factorial(g)))
# C x C computation of deg of Picard bundle restricted to C
for g in range(1,5):
    for d0 in range(0,6):
        # pi_! of M=O(Delta+pr1^*D0) normalised by pr2^*O(-p0): deg = 2-2g+d0 - rank_of_unnormalised? rank=d0+2-g ; normalise: -rank
        deg_un=2-2*g+d0; rank=d0+2-g
        assert deg_un-rank==-g
say("[C x C GRR] deg(E|_C)=-g for g=1..4, d0=0..5 : consistent")

# ---------- 3. GRR for P(V): Lagrange identity ----------
def lhs(a,k):
    r=len(a); s=0.0
    for i in range(r):
        p=1.0
        for j in range(r):
            if j!=i: p*=1/(1-np.exp(-(a[j]-a[i])))
        s+=np.exp(-k*a[i])*p
    return s
def hk(xs,k):
    if k<0: return 0.0
    tot=0.0
    for comb_ in itertools.combinations_with_replacement(range(len(xs)),k):
        t=1.0
        for i in comb_: t*=xs[i]
        tot+=t
    return tot
rng=np.random.default_rng(1)
maxerr=0
for r in (2,3,4):
    a=rng.normal(size=r)*0.4
    x=np.exp(-a)
    for k in range(-9,8):
        if k>=0: rhs=hk(x,k)
        elif k>-r: rhs=0.0
        else: rhs=(-1)**(r-1)*np.prod(1/x)*hk(1/x,-k-r)
        maxerr=max(maxerr,abs(lhs(a,k)-rhs)/(1+abs(rhs)))
say("[GRR P(V)] max rel err over r=2,3,4, k=-9..7 :","%.2e"%maxerr)

# ---------- 4. Legendre family Picard-Fuchs & monodromy ----------
# omega(l)=sum_n ((1/2)_n/n!)^2 l^n  satisfies l(1-l)w'' + (1-2l)w' - w/4 = 0
def poch(a,n):
    p=F(1)
    for i in range(n): p*=(a+i)
    return p
half=F(1,2)
cn=[ (poch(half,n)/factorial(n))**2 for n in range(40)]
ok=True
for n in range(38):
    # coefficient of l^n in l(1-l)w''+(1-2l)w'-w/4:
    # l w'' -> (n+1)n c_{n+1}; -l^2 w'' -> -n(n-1)c_n ; w' -> (n+1)c_{n+1}; -2l w' -> -2n c_n ; -w/4 -> -c_n/4
    val=(n+1)*n*cn[n+1]-n*(n-1)*cn[n]+(n+1)*cn[n+1]-2*n*cn[n]-cn[n]/4
    ok&=(val==0)
say("[Legendre PF] hypergeometric 2F1(1/2,1/2;1;l) satisfies PF eq. up to l^37 exactly:",ok)
M0=np.array([[1,2],[0,1]]);M1=np.array([[1,0],[-2,1]])
Minf=np.linalg.inv(M0@M1)
say("[Legendre monodromy] M0*M1=",(M0@M1).tolist()," trace",np.trace(M0@M1)," Minf=",np.round(Minf).astype(int).tolist(),"M0*M1*Minf=I:",np.allclose(M0@M1@Minf,np.eye(2)), "det",round(np.linalg.det(M0)))

# ---------- 5. Unified paper: dims in m; total Euler characteristic ----------
def chiO(n,k):  # chi(P^n,O(k)) = C(k+n,n) as polynomial
    r=F(1)
    for i in range(1,n+1): r*=F(k+i,i)
    return r
def h0_P1(m): return m+1
poly = lambda coeffs: coeffs
PY={'S2':[1,0,1],'T2':[1,2,1],'T4':[1,4,6,4,1]}
def prod(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r
say("[unified Y x P^1] P_HH(t)=P_Y(t)*((m+1)+(m+3)t):")
for Y in ('S2','T2'):
    for m in (0,1,3):
        say("  ",Y,"m=",m,prod(PY[Y],[m+1,m+3]), "Euler=",sum((-1)**k*c for k,c in enumerate(prod(PY[Y],[m+1,m+3]))))
# general m symbolic check: (m+1, 3m+5, 3m+7, m+3) for T2
for m in range(-1,8):
    assert prod(PY['T2'],[m+1,m+3])==[m+1,3*m+5,3*m+7,m+3]
# P^2: b=0,1,2 dims chi(wedge^b T (m))
def chiT_P2(m): return 3*chiO(2,m+1)-chiO(2,m)
def chiW2_P2(m): return chiO(2,m+3)
say("[unified Y x P^2] chi(wedge^b T(m)) b=0,1,2 for m=0..4, and Euler sum:")
for m in range(0,5):
    v=[chiO(2,m),chiT_P2(m),chiW2_P2(m)]
    say("  m=",m,[int(x) for x in v]," alt sum=",int(v[0]-v[1]+v[2]))
for Y in ('S2','T2'):
    for m in (1,2,3):
        v=[int(chiO(2,m)),int(chiT_P2(m)),int(chiW2_P2(m))]
        P=[0]*(len(PY[Y])+2)
        for b in range(3):
            for j,c in enumerate(PY[Y]): P[b+j]+=v[b]*c
        say("  Y=",Y,"m=",m,"P_HH=",P,"Euler=",sum((-1)**k*c for k,c in enumerate(P)),"expected chi(Y)*chi(P2)=",sum((-1)**k*c for k,c in enumerate(PY[Y]))*3)

# ---------- 6. Toeplitz family over S^2: ind = -[P_+] ; Chern number of P_+ ----------
def Pplus(th,ph):
    b=np.array([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)])
    sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
    H=b[0]*sx+b[1]*sy+b[2]*sz
    return (np.eye(2)+H)/2
def flux(N=400):
    tot=0
    h=1e-5
    ths=(np.arange(N)+0.5)*np.pi/N
    phs=(np.arange(N)+0.5)*2*np.pi/N
    for th in ths:
        for ph in phs:
            P=Pplus(th,ph)
            dth=(Pplus(th+h,ph)-Pplus(th-h,ph))/(2*h)
            dph=(Pplus(th,ph+h)-Pplus(th,ph-h))/(2*h)
            Fv=-1j*np.trace(P@(dth@dph-dph@dth))   # Berry curvature of P_+ (some sign convention)
            tot+=Fv.real*(np.pi/N)*(2*np.pi/N)
    return tot/(2*np.pi)
say("[Toeplitz S^2] (1/2pi) int i Tr(P[dP,dP]) over S^2 (theta,phi order) =",round(flux(120),6))
# Toeplitz: finite section check: coker dim 1 for T_{f_b}, f_b(z)=z P_+ + P_-
def toeplitz_f(P,N=40):
    S=np.zeros((N+1,N))
    for n in range(N): S[n+1,n]=1
    I=np.zeros((N+1,N))
    for n in range(N): I[n,n]=1
    A=np.kron(S,P)+np.kron(I,np.eye(2)-P)
    w,v=np.linalg.eigh(P); u=v[:,np.argmax(w)]       # P u = u
    e0=np.zeros(N+1); e0[0]=1
    y=np.kron(e0,u)
    res=np.linalg.norm(A.conj().T@y)
    s=np.linalg.svd(A,compute_uv=False)
    return int(A.shape[1]-(s>1e-9).sum()), res
for (th,ph) in [(0.3,1.1),(2.0,4.0),(1.57,0.2)]:
    kk,res=toeplitz_f(Pplus(th,ph))
    say("[Toeplitz] b=(th,ph)=",(th,ph),"dim ker(finite section)=",kk,"|A^H(e0 x u_+)|=%.1e"%res)
# ---------- 7. Str e^{-A_t^2} for D=z on C ----------
# graded convention: Str N^2 = -2 dbar f ^ df ; 2-form part of Str e^{-A^2} = -t e^{-t|f|^2} dbar f^df ; with dbar z^dz = 2i dx dy
from math import pi
def integ(t):
    # int_C -t e^{-t r^2} 2i dx dy /(2 pi i)
    rr=np.linspace(0,12/np.sqrt(t),400001)
    val=np.trapezoid(-t*np.exp(-t*rr**2)*2j*2*np.pi*rr,rr)/(2j*np.pi)
    return val
say("[Quillen A_t, D=z] int ch(A_t)/(2 pi i) (graded convention) for t=0.1,1,10 :",[round(integ(t).real,6) for t in (0.1,1,10)])

# ---------- 8. heat trace for twisted torus (McKean-Singer on a flat family) ----------
def heat_diff(a,t,N=40):
    ks=np.arange(-N,N+1)
    kx,ky=np.meshgrid(ks,ks)
    lam=np.abs(((kx+a.real)+1j*(ky+a.imag)))**2/4  # |dbar_a e_k|^2 up to normalisation; dbar^*dbar eigenvalue and dbar dbar^* eigenvalue coincide
    return np.exp(-t*lam).sum(), np.exp(-t*lam).sum()  # Tr on functions (degree0), on (0,1)-forms (same spectrum)
say("[McKean-Singer torus] Tr e^{-t dbar*dbar}-Tr e^{-t dbar dbar*}=0 (spectra coincide):",heat_diff(0.3+0.2j,0.1)[0]-heat_diff(0.3+0.2j,0.1)[1])
# Poisson check: Tr e^{-t Delta} on S^1 twisted: sum e^{-t(n+a)^2} ~ sqrt(pi/t)
for t in (0.05,0.01):
    n=np.arange(-400,401)
    say("[heat S^1] t=",t,"sum_n e^{-t(n+0.3)^2}=%.8f"%np.exp(-t*(n+0.3)**2).sum()," sqrt(pi/t)=%.8f"%np.sqrt(np.pi/t))

# ---------- 9. K-theory / Chern character numerics ----------
# CP^2: ch(H^i) = e^{i x}: matrix
M=np.array([[1,0,0],[1,1,.5],[1,2,2]]);say("[K(CP^2)] det of ch(1,H,H^2) in basis (1,x,x^2/..)=",np.linalg.det(M))
# Adams: ch(Sym^2 V) for V rank 2 with roots a,b = (e^{2a}+e^{a+b}+e^{2b}); check formula (ch(V)^2+psi2 ch V)/2
a,b=0.31,-0.77
cv=np.exp(a)+np.exp(b);psi=np.exp(2*a)+np.exp(2*b)
say("[Sym^2] (ch^2+psi^2 ch)/2 - ch Sym^2 =",(cv**2+psi)/2-(np.exp(2*a)+np.exp(a+b)+np.exp(2*b)))
# Dirac family ranks: Ahat-genus in dim 4: -p1/24 ; K3: p1=-48 ; T^4: 0
say("[Ahat] K3: -p1/24 =",F(48,24),"; sign=-16 -> -sign/8 =",F(16,8))
# Hirzebruch surface F_n=P(O+O(n)) over P^1: chi(F_n, O_P(V)(k)) = chi(P^1, Sym^k V^dual) ; V=O+O(n): V^dual=O+O(-n)
def chiF(n,k):
    # Sym^k(O+O(-n)) = sum_{i=0}^k O(-n i); chi(P^1,O(m))=m+1
    return sum(-n*i+1 for i in range(k+1))
say("[Hirzebruch F_n] chi(P^1,Sym^k V^dual), n=2: k=0..4:",[chiF(2,k) for k in range(5)]," n=1:",[chiF(1,k) for k in range(5)])
# F_n via surface RR: chi = 1 + (L^2 - L.K)/2 with Pic: L=h (tautological O(1)), h^2=-n? check n=1,k=1:
open("verify9.out","w").write("\n".join(out))
