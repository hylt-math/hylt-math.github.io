import numpy as np, itertools
from math import comb
np.random.seed(1)
# ---------- exterior algebra helpers ----------
def basis(n): 
    return [tuple(s) for k in range(n+1) for s in itertools.combinations(range(n),k)]
def wedge_mat(v,n):
    B=basis(n); idx={b:i for i,b in enumerate(B)}
    M=np.zeros((len(B),len(B)),dtype=complex)
    for b in B:
        for j in range(n):
            if j in b: continue
            nb=tuple(sorted(b+(j,))); sign=(-1)**sum(1 for t in b if t<j)
            M[idx[nb],idx[b]]+=sign*v[j]
    return M
def deg_blocks(n):
    B=basis(n); return [[i for i,b in enumerate(B) if len(b)==k] for k in range(n+1)]
ok=True
# C1: sigma(d+d*)^2=|xi|^2, Koszul exactness
for n in [2,3,4,5]:
    xi=np.random.randn(n)
    W=wedge_mat(xi,n); I=W.conj().T  # contraction = adjoint
    S=1j*(W-I)   # sigma(d+d^*)
    print(n,"|S^2-|xi|^2|=",np.abs(S@S-(xi@xi)*np.eye(len(S))).max())
    # exactness: rank of wedge from degree k-1 to k plus rank k to k+1 = dim Lambda^k
    blk=deg_blocks(n)
    for k in range(n+1):
        rk_in = np.linalg.matrix_rank(W[np.ix_(blk[k],blk[k-1])]) if k>0 else 0
        rk_out= np.linalg.matrix_rank(W[np.ix_(blk[k+1],blk[k])]) if k<n else 0
        assert rk_in+rk_out==comb(n,k),(n,k)
print("Koszul exact OK")
# C2: Dolbeault symbol: nonzero (0,1)-covector wedge exact; real xi -> xi^{0,1} nonzero
for n in [1,2,3,4]:
    xi=np.random.randn(2*n)  # real covector on R^{2n}: coords x_j,y_j
    # xi = sum a_j dx_j + b_j dy_j ; (0,1) part coefficient on dzbar_j: (a_j + i b_j)/2
    v=(xi[0::2]+1j*xi[1::2])/2
    W=wedge_mat(v,n); blk=deg_blocks(n)
    for k in range(n+1):
        rk_in = np.linalg.matrix_rank(W[np.ix_(blk[k],blk[k-1])]) if k>0 else 0
        rk_out= np.linalg.matrix_rank(W[np.ix_(blk[k+1],blk[k])]) if k<n else 0
        assert rk_in+rk_out==comb(n,k)
print("Dolbeault symbol exact OK")
# C2b: total symbol s0+t s1 (filtration argument): complex Lambda^{0,a} x Lambda^b T, s1 = wedge by a vector on Lambda^b T
for n in [1,2,3]:
    for t in [0,0.3,1,5]:
        xi=np.random.randn(2*n); v=(xi[0::2]+1j*xi[1::2])/2
        w=np.random.randn(n)+1j*np.random.randn(n)   # pi^#(xi^{1,0}) generic vector
        A=wedge_mat(v,n); Bm=wedge_mat(w,n)
        # total space = Lambda^{0,*} (x) Lambda^* T ; differential: s0 x 1 + (-1)^a 1 x s1 ; sigma-graded
        Bs=basis(n); N=len(Bs)
        deg=np.array([len(b) for b in Bs])
        D=np.kron(A,np.eye(N))+t*np.kron(np.diag((-1.0)**deg),Bm)
        tot=np.array([len(a)+len(b) for a in Bs for b in Bs])
        # check D^2=0 and exactness
        assert np.abs(D@D).max()<1e-12
        ranks=[np.linalg.matrix_rank(D[np.ix_(np.where(tot==k+1)[0],np.where(tot==k)[0])]) for k in range(2*n+1)] if True else None
        dims=[int((tot==k).sum()) for k in range(2*n+1)]
        for k in range(2*n+1):
            rin=ranks[k-1] if k>0 else 0; rout=ranks[k] if k<2*n else 0
            assert rin+rout==dims[k],(n,t,k,rin,rout,dims[k])
print("total symbol (filtered) exact OK")
# C3: torus Dolbeault: at k=0 cohomology dim = C(n,q), euler char 0
for n in range(1,6): print("T^2n Dolbeault h^{0,q}:",[comb(n,q) for q in range(n+1)], sum((-1)**q*comb(n,q) for q in range(n+1)))
# C4: composition formula for Kohn-Nirenberg quantization on S^1
N=64; x=2*np.pi*np.arange(N)/N; ks=np.fft.fftfreq(N,1/N)
def Op(a):   # a(x,k) function
    def A(u):
        uh=np.fft.fft(u)/N
        return np.array([sum(a(xj,k)*uh[i]*np.exp(1j*k*xj) for i,k in enumerate(ks)) for xj in x])
    return A
a=lambda x,k:(2+np.cos(x))*k+np.sin(x)
b=lambda x,k:(1+0.5*np.sin(x))*k**2+np.cos(2*x)*k
# a#b = a b + (-i) d_xi a * d_x b + (1/2!)(-i)^2 d_xi^2 a d_x^2 b ; here a is degree 1 in xi => 2 terms
db=lambda x,k:0.5*np.cos(x)*k**2-2*np.sin(2*x)*k
da=lambda x,k:(2+np.cos(x))
c=lambda x,k:a(x,k)*b(x,k)+(-1j)*da(x,k)*db(x,k)
u=np.cos(3*x)+0.5*np.sin(5*x)+0.2*np.exp(2j*x)
lhs=Op(a)(Op(b)(u)); rhs=Op(c)(u)
print("composition residual",np.abs(lhs-rhs).max())
# C5: d/dtheta - b : kernel jump.  Fourier matrix, b=c0+ b1 cos(theta): int b=2pi c0
def sv_min(c0,b1,M=60):
    ks=np.arange(-M,M+1); n=len(ks)
    P=np.zeros((n,n),dtype=complex)
    for i,k in enumerate(ks):
        P[i,i]=1j*k-c0
        if i+1<n: P[i,i+1]+=-b1/2   # cos coefficient: (P u)_k gets -b1/2 (u_{k-1}+u_{k+1})
        if i-1>=0: P[i,i-1]+=-b1/2
    s=np.linalg.svd(P,compute_uv=False); return s[-1],s[-2]
for c0 in [0,0.5,1j*2,0.3+1j]:
    print("c0",c0,"smallest sv",sv_min(c0,1.5)) if False else None
for c0 in [0,0.5,2j,0.3+1j]:
    print("c0",c0,"two smallest sv",sv_min(c0,1.5))
# C6 Toeplitz-type PsiDO A_f=Pi_+ f + Pi_-, f=e^{2i th}+0.3
def Af_sv(fco,N=80):
    ks=np.arange(-N,N+1); n=len(ks); M=np.zeros((n,n),dtype=complex)
    for i,k in enumerate(ks):
        for j,l in enumerate(ks):
            if k>=0: M[i,j]=fco.get(k-l,0)
            else: M[i,j]=1.0 if k==l else 0
    return np.linalg.svd(M,compute_uv=False)
for name,f in [("e^{2i}+0.3 (w=2)",{2:1,0:0.3}),("e^{-i}+0.3 (w=-1)",{-1:1,0:0.3}),("1+0.3e^{i} (w=0)",{0:1,1:0.3}),("e^{3i}+0.5e^{i}+... (w=3)",{3:1,1:0.5})]:
    s=Af_sv(f); print(name,"smallest svs",np.sort(s)[:5])
# C7 Landau on T^2: section u=sum_j v(x-2pi j)e^{i(rho+jk)y}
k=3
for rho in range(k):
    v=lambda x:np.exp(rho*x-k*x**2/(4*np.pi))
    def u(x,y,J=12): return sum(v(x-2*np.pi*j)*np.exp(1j*(rho+j*k)*y) for j in range(-J,J+1))
    x0,y0=0.7,1.3; h=1e-5
    # quasi-periodicity
    qp=abs(u(x0+2*np.pi,y0)-np.exp(1j*k*y0)*u(x0,y0))
    ux=(u(x0+h,y0)-u(x0-h,y0))/(2*h); uy=(u(x0,y0+h)-u(x0,y0-h))/(2*h)
    dbar=0.5*(ux+1j*uy+(k/(2*np.pi))*x0*u(x0,y0))
    print("rho",rho,"quasi-per err",qp,"dbar_L u",abs(dbar),"|u|",abs(u(x0,y0)))
