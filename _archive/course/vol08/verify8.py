import numpy as np
from fractions import Fraction as F
from math import comb, factorial
from lib8 import *
np.random.seed(7)
def binom_gen(a,N):  # a(a-1)...(a-N+1)/N!, a integer (negative OK)
    r=F(1)
    for i in range(N): r*=F(a-i)
    return r/factorial(N)

print("=== A. Clifford identity: sum R_ijkl g_i g_j g_k g_l = 2 scal ===")
# gamma matrices with g_i^2=-1 for n=4 (and n=2,3 via submatrices of n=4 set)
s0=np.eye(2); sx=np.array([[0,1],[1,0]],dtype=complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex)
def kron(*a):
    r=np.eye(1)
    for x in a: r=np.kron(r,x)
    return r
g4=[1j*kron(sx,s0),1j*kron(sy,s0),1j*kron(sz,sx),1j*kron(sz,sy)]   # square = -1
for i in range(4):
    for j in range(4):
        ac=g4[i]@g4[j]+g4[j]@g4[i]
        assert np.allclose(ac,-2*np.eye(4)*(i==j))
print("Clifford relations ok (n=4)")
def alg_curv(n):
    R=np.zeros((n,n,n,n))
    for _ in range(3):
        h=np.random.randn(n,n); h=h+h.T
        # Kulkarni-Nomizu h∧h : R_ijkl = h_il h_jk - h_ik h_jl (convention R_ijji = h_ii h_jj - h_ij^2 )
        R+= np.einsum('il,jk->ijkl',h,h)-np.einsum('ik,jl->ijkl',h,h)
    return R
for n in [2,3,4]:
    g=g4[:n] if n==4 else None
R=alg_curv(4)
# Bianchi and symmetries
assert np.allclose(R+R.transpose(1,0,2,3),0) and np.allclose(R+R.transpose(0,1,3,2),0)
assert np.allclose(R+R.transpose(1,2,0,3)+R.transpose(2,0,1,3),0)
scal=sum(R[i,j,j,i] for i in range(4) for j in range(4))
K=sum(R[i,j,k,l]*g4[i]@g4[j]@g4[k]@g4[l] for i in range(4) for j in range(4) for k in range(4) for l in range(4))
print("scal=",scal,"  K/(2scal) max dev from identity:",np.abs(K-2*scal*np.eye(4)).max())
# sphere
R=np.zeros((4,4,4,4))
for i in range(4):
    for j in range(4): R[i,j,j,i]+=1; R[i,j,i,j]-=1
K=sum(R[i,j,k,l]*g4[i]@g4[j]@g4[k]@g4[l] for i in range(4) for j in range(4) for k in range(4) for l in range(4))
print("S^4: K=",np.round(K[0,0],6)," expected 2n(n-1)=",2*4*3)
# volume element in n=4: w=-g1g2g3g4? check w^2 = 1
w=g4[0]@g4[1]@g4[2]@g4[3]
print("(g1g2g3g4)^2 = +1 ?",np.allclose(w@w,np.eye(4)), " eigenvalues",np.round(np.linalg.eigvals(w).real,6))
# n=2: complex volume element i*g1g2
g2=[1j*sx,1j*sy]; w2=1j*g2[0]@g2[1]
print("n=2: (i g1 g2)^2=1:",np.allclose(w2@w2,np.eye(2)),"  eig",np.round(np.linalg.eigvals(w2).real,6))
# Clifford: n=3 irreps: g1g2g3 = +-1 scalar (center)
g3=[1j*sx,1j*sy,1j*sz]; print("n=3: g1g2g3 =",np.round((g3[0]@g3[1]@g3[2])[0,0],6)," (scalar:",np.allclose(g3[0]@g3[1]@g3[2],(g3[0]@g3[1]@g3[2])[0,0]*np.eye(2)),")")
# quaternions: Cl_{0,2}: g1,g2 with g1g2=-g2g1, squares -1 -> H
# 2d Dirac symbol: i c(xi) squares to |xi|^2
xi=np.random.randn(4); c=sum(x*gm for x,gm in zip(xi,g4)); sig=1j*c
print("sigma(D)(xi)^2 = |xi|^2 :",np.allclose(sig@sig,(xi@xi)*np.eye(4)))
# Spin(3)=SU(2): exp(theta/2 e1e2) is a rotation by theta on R^3: check Ad
import scipy.linalg as sl
th=0.7; s=sl.expm(0.5*th*g3[0]@g3[1]); v=np.array([0.3,-0.4,0.9]); Cv=sum(x*gm for x,gm in zip(v,g3))
Cw=s@Cv@np.linalg.inv(s)  # should equal c(Rv) with rotation in 1-2 plane by angle -th or +th
cs=[(np.trace(Cw@(-g)).real/2) for g in g3]  # coefficient: c(e_k)^{-1}... tr(c(e_i)c(e_j)) = -2 delta
print("Ad(s) c(v) = c(Rv): coefficients",np.round(cs,6)," vs rotation by +/-th:",
      np.round([np.cos(th)*v[0]-np.sin(th)*v[1], np.sin(th)*v[0]+np.cos(th)*v[1], v[2]],6),
      np.round([np.cos(th)*v[0]+np.sin(th)*v[1], -np.sin(th)*v[0]+np.cos(th)*v[1], v[2]],6))
# s(theta=2pi) = -1
print("exp(pi g1g2) = ",np.round(sl.expm(np.pi*g3[0]@g3[1])[0,0],6))

print("\n=== B. Toeplitz index = -winding ===")
def toeplitz_small_sv(coeffs,N):
    # symbol f(z)=sum_k a_k z^k ; Toeplitz T_f = P_+ f P_+, matrix T[m,n]=a_{m-n}
    T=np.zeros((N,N),dtype=complex)
    for m in range(N):
        for n in range(N):
            T[m,n]=coeffs.get(m-n,0)
    return np.linalg.svd(T,compute_uv=False)
def winding(coeffs):
    th=np.linspace(0,2*np.pi,200001); z=np.exp(1j*th)
    f=sum(a*z**k for k,a in coeffs.items()); ph=np.unwrap(np.angle(f)); return round((ph[-1]-ph[0])/(2*np.pi))
tests={"z":{1:1.0},"z^2":{2:1.0},"z^-1":{-1:1.0},"z-0.3":{1:1.0,0:-0.3},"(z-0.3)(z-0.5)":{2:1,1:-0.8,0:0.15},
       "(z-2)(z-0.5)":{2:1,1:-2.5,0:1.0},"z^-2(z-0.3)(z-0.5)":{0:1,-1:-0.8,-2:0.15},"1+0.3z+0.2z^-1":{0:1,1:0.3,-1:0.2}}
for name,c in tests.items():
    sv=toeplitz_small_sv(c,60); nsmall=int(np.sum(sv<1e-6)); w=winding(c)
    print(f"{name:22s} winding={w:3d}  #tiny singular values={nsmall}  (index of T_f = -winding = {-w})")

print("\n=== C. Heat traces / McKean-Singer ===")
def tr_S1(t,M=4000):
    k=np.arange(-M,M+1); return np.sum(np.exp(-t*k**2.0))
for t in [0.5,0.1,0.01]:
    print(f"S^1 (length 2pi): Tr e^(-tΔ)={tr_S1(t):.10f}  sqrt(pi/t)={np.sqrt(np.pi/t):.10f}")
def tr_S2(t,L=4000):
    l=np.arange(0,L); return np.sum((2*l+1)*np.exp(-t*l*(l+1.0)))
def tr_S2_forms(t,L=4000):
    l=np.arange(1,L); return 2*np.sum((2*l+1)*np.exp(-t*l*(l+1.0)))
for t in [0.1,0.03,0.01,0.003]:
    t0=tr_S2(t); t1=tr_S2_forms(t); t2=t0
    print(f"S^2: t={t}: Tr0-Tr1+Tr2 = {t0-t1+t2:.12f} (chi=2);  Tr0-(1/t+1/3)={t0-(1/t+1/3):.6f} (~t/15={t/15:.6f});  Tr1-(2/t-4/3)={t1-(2/t-4/3):.6f}")
def tr_S2_dirac(t,L=4000):
    m=np.arange(1,L); return 4*np.sum(m*np.exp(-t*m**2.0))
for t in [0.1,0.03,0.01]:
    print(f"S^2 Dirac (spec ±m, mult 2m each sign... total 4m): Tr e^-tD^2={tr_S2_dirac(t):.8f}  2/t-1/3={2/t-1/3:.8f}")
# T^2 flat (R^2/ (2pi Z)^2): heat trace
def tr_T2(t,M=300):
    k=np.arange(-M,M+1); s=np.sum(np.exp(-t*k**2.0)); return s*s
for t in [0.1,0.01]:
    print(f"T^2: Tr0 = {tr_T2(t):.8f},  area/(4 pi t)={4*np.pi**2/(4*np.pi*t):.8f}; Tr0-Tr1+Tr2 = {tr_T2(t)-2*tr_T2(t)+tr_T2(t):.3f} (chi=0)")
# Landau levels on T^2 for L of degree k: Tr_s = k exactly
for k_,t in [(3,0.2),(1,1.0),(5,0.05)]:
    B=1.0; n=np.arange(0,4000)
    trD0=np.sum(k_*np.exp(-t*B*n)); trD1=np.sum(k_*np.exp(-t*B*(n+1)))
    print(f"Landau: k={k_}, t={t}: Tr(e^-t D-D+)-Tr(e^-t D+D-) = {trD0-trD1:.10f}")

print("\n=== D. Mehler 1D ===")
def mehler_check(w,t,Lbox=12,Npts=4001):
    x=np.linspace(-Lbox,Lbox,Npts); h=x[1]-x[0]
    H=np.diag(2/h**2+w**2*x**2)+np.diag(-np.ones(Npts-1)/h**2,1)+np.diag(-np.ones(Npts-1)/h**2,-1)
    ev,V=np.linalg.eigh(H)
    tr=np.sum(np.exp(-t*ev)); i0=Npts//2
    K0=np.sum(np.exp(-t*ev)*V[i0,:]**2)/h
    return tr,K0
for w,t in [(1.0,0.3),(2.0,0.2),(0.5,1.0)]:
    tr,K0=mehler_check(w,t)
    print(f"w={w}, t={t}: Tr={tr:.6f} vs 1/(2sinh(wt))={1/(2*np.sinh(w*t)):.6f};  K(0,0)={K0:.6f} vs sqrt(w/(2π sinh 2wt))={np.sqrt(w/(2*np.pi*np.sinh(2*w*t))):.6f}")

print("\n=== E. Per-root integrands of the four operators ===")
n=10
Td=todd(n+2)             # x/(1-e^{-x})
def Tdm(n): return sub_x(todd(n),-1,n)   # (-x)/(1-e^{x}) = Td(-x)
TT=smul(todd(n+2),sub_x(todd(n+2),-1,n+2),n+2)
def shift_div_x(a):  # a = x*b -> b
    assert a[0]==0; return a[1:]
ex=expser(n+2); exm=sub_x(ex,-1,n+2)
e_half=expser(n+2,F(1,2)); e_mhalf=sub_x(e_half,-1,n+2)
one=[F(1)]+[F(0)]*(n+1)
# Dolbeault: ch(1-e^x) * TT / x   expect  -Td(x)
Lg=n+3; Tdx=todd(Lg-1); TTx=smul(Tdx,sub_x(Tdx,-1,Lg-1),Lg-1); exx=expser(Lg-1); onex=[F(1)]+[F(0)]*(Lg-1)
dd=smul(ssub(onex,exx),TTx,Lg-1)
print("Dolbeault: (1-e^x)Td(x)Td(-x)/x == -Td(x):",dd[0]==0 and dd[1:n]==[-c for c in todd(n)][:n-1])
# de Rham: (1-e^x)(1-e^-x) TT / x == -x
a=smul(ssub(one+[F(0)],ex),ssub(one+[F(0)],exm),n+2); b=smul(a,TT,n+2); lhs=shift_div_x(b)[:n]
print("de Rham: (1-e^x)(1-e^-x)Td(x)Td(-x)/x == -x:",lhs==[F(0),F(-1)]+[F(0)]*(n-2))
# signature: (e^x-e^-x) TT / x == x/tanh(x/2)
b=smul(ssub(ex,exm),TT,n+2); lhs=shift_div_x(b)[:n]
print("signature: (e^x-e^-x)Td(x)Td(-x)/x == x/tanh(x/2):",lhs==Lhalf(n)[:n])
# Dirac: (e^{x/2}-e^{-x/2}) TT / x == (x/2)/sinh(x/2)
b=smul(ssub(e_half,e_mhalf),TT,n+2); lhs=shift_div_x(b)[:n]
print("Dirac: (e^{x/2}-e^{-x/2})Td(x)Td(-x)/x == Ahat(x):",lhs==ahat(n)[:n])
# identity  L(x)=x/tanh x ; x/tanh(x/2) = 2 L(x/2)
print("x/tanh(x/2)=2*L(x/2):",Lhalf(n)==sscale(sub_x(lgen(n),F(1,2),n),2))
print("Td(x)=e^{x/2}Ahat(x):",smul(expser(n,F(1,2)),ahat(n),n)==todd(n))

print("\n=== F. CP^N: Dolbeault / Dirac / signature / Euler ===")
def ch_line(k,N): return expser(N,k)
def chi_CPN(N,k):
    T=spow(todd(N),N+1,N); return smul(ch_line(k,N),T,N)[N]
for N in range(1,8):
    assert all(chi_CPN(N,k)==binom_gen(N+k,N) for k in range(-12,13))
print("chi(CP^N,O(k))=binom(N+k,N) for N<=7, |k|<=12 : OK")
# Euler class: c_N(T CP^N)= (N+1) H^N
for N in range(1,8): assert comb(N+1,N)==N+1
# signature of CP^{2j}: L genus with roots H (N+1 times) ; L multiplicative
for N in [2,4,6,8]:
    Lc=spow(lgen(N),N+1,N)
    print(f"CP^{N}: signature = ∫L = {Lc[N]}")
print("CP^2xCP^2: ∫L = (∫L(CP^2))^2 =",1)
# Ahat(CP^N) odd N => spin; twisted Dirac D_{O(k)} on CP^3 : ∫ e^{kH} Ahat vs chi(O(k-2))
N=3
for k in range(-4,6):
    ind=smul(expser(N,k),spow(ahat(N),N+1,N),N)[N]
    assert ind==chi_CPN(N,k-2)==binom_gen(k+1,3)
print("CP^3: ind D_{O(k)} = ∫ e^{kH}Ahat = chi(O(k-2)) = C(k+1,3): OK for -4..5")
N=5
vals=[smul(expser(N,k),spow(ahat(N),N+1,N),N)[N] for k in range(-3,5)]
print("CP^5: ind D_{O(k)}=",[str(v) for v in vals]," vs chi(O(k-3)):",[str(chi_CPN(5,k-3)) for k in range(-3,5)])
print("CP^2 Ahat (real dim 4)=",spow(ahat(2),3,2)[2]," (-1/8: not spin)")
print("CP^4 Ahat (real dim 8)=",spow(ahat(4),5,4)[4], " (CP^4 not spin; non-integer)")
print("CP^2: Td integral:",spow(todd(2),3,2)[2])

print("\n=== G. hypersurfaces X_d in CP^{N}  (m=N-1) ===")
def hyper(N,d):
    m=N-1
    num=lambda f:  smul(spow(f,N+1,m),sinv(sub_x(f,d,m),m),m)
    Tdc=num(todd(m)); Ah=num(ahat(m)); Lc=num(lgen(m))
    cH=[F(comb(N+1,i)) for i in range(m+1)]; cinv=sinv([F(1),F(d)]+[F(0)]*(m-1),m); c=smul(cH,cinv,m)
    return {"td":d*Tdc[m],"ahat":d*Ah[m],"L":d*Lc[m],"e":d*c[m],"c1":(N+1-d)}
print("K3 = quartic surface in CP^3:",hyper(3,4))
for d in range(1,9):
    h=hyper(3,d)
    sig=F(-d*(d*d-4),3)
    ok= (h['L']==sig)
    print(f"d={d}: chi(O)={h['td']}, Ahat={h['ahat']}, sigma(L)={h['L']} formula {sig} {ok}, e={h['e']}, c1={(4-d)}H, spin={((4-d)%2==0)}, -sigma/8={-h['L']/8}, sigma%16={(h['L']%16) if h['L'].denominator==1 else '-'}")
print("quintic 3-fold (N=4,d=5): chi(O)=",hyper(4,5)['td']," e=",hyper(4,5)['e'])
for d in range(1,9):
    h=hyper(5,d); print(f"X_{d} in CP^5 (dim_C 4): chi(O)={h['td']}, Ahat={h['ahat']}, L={h['L']}, e={h['e']}, spin={(6-d)%2==0}")
# Bott-Hirzebruch: Ahat of CP^1xCP^1 etc
print("Ahat(CP^1 x CP^1)=0 ; K3 e=24")
# Dolbeault on curves
for g in [0,1,2,3]:
    pass
print("\n=== H. ind d+d* : chi_top = ∫ c_top for CP^N etc ===")
for N in range(1,7): print(f"CP^{N}: chi={N+1}",end="; ")
print()

print("\n=== I. Clifford module on Lambda^{0,*}C^m: chirality, S^+ = even degree ===")
def fock(m):
    # basis: subsets of range(m) as bitmasks; eps_j wedge, iota_j contraction
    dim=2**m
    eps=[np.zeros((dim,dim),dtype=complex) for _ in range(m)]
    for j in range(m):
        for s in range(dim):
            if not (s>>j)&1:
                sign=(-1)**bin(s&((1<<j)-1)).count("1")
                eps[j][s|(1<<j),s]=sign
    iota=[e.conj().T for e in eps]
    return eps,iota
for m in [1,2,3]:
    eps,iota=fock(m); dim=2**m
    c=[]
    for j in range(m):
        c.append(eps[j]-iota[j]); c.append(1j*(eps[j]+iota[j]))
    ok=all(np.allclose(c[a]@c[b]+c[b]@c[a],-2*(a==b)*np.eye(dim)) for a in range(2*m) for b in range(2*m))
    w=np.eye(dim,dtype=complex)
    for a in range(2*m): w=w@c[a]
    w=(1j**m)*w
    deg=np.array([bin(s).count("1") for s in range(dim)])
    print(f"m={m}: Clifford relations {ok}; omega^2=1: {np.allclose(w@w,np.eye(dim))}; omega=+1 exactly on even degree: {np.allclose(np.diag(w), np.where(deg%2==0,1,-1)) and np.allclose(w,np.diag(np.diag(w)))}")
