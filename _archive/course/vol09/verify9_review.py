# 第9巻 査読者の別実装（numpy / fractions のみ）
import numpy as np
from fractions import Fraction as F
from math import comb, factorial

def sec(s): print("\n==",s)

# ---------- 1. Berry/Chern 符号の較正：S^2 上の P_+ （解析的に c1=-1）
sec("1. link-variable sign calibration on S^2 (P_+ has c1=-1 analytically)")
def u(th,ph): return np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)])
def plaq_sum(Nth=60,Nph=120):
    # gauge-invariant plaquette phase: arg( <u00,u10><u10,u11><u11,u01><u01,u00> ), (theta,phi) counterclockwise
    ths=np.linspace(0.02,np.pi-0.02,Nth+1); phs=np.linspace(0,2*np.pi,Nph+1)
    tot=0
    for i in range(Nth):
        for j in range(Nph):
            a=u(ths[i],phs[j]); b=u(ths[i+1],phs[j]); c=u(ths[i+1],phs[j+1]); d=u(ths[i],phs[j+1])
            z=np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a)
            tot+=np.angle(z)
    return tot/(2*np.pi)
s=plaq_sum()
print("sum of plaquette phases/2pi (theta,phi order) =",s," -> c1 = -sum =",-s," (analytic: -1)  [polar caps cut: ~%g]"%(1-0.02**2))
# conclusion: c1 = -(1/2pi) sum arg(U1 U2 U1^-1 U2^-1) with U_mu=<u(k),u(k+mu)>

# ---------- 2. Landau family: independent c1 via the same plaquette convention
sec("2. Landau level kernel bundle, c1 in (alpha,beta) orientation")
def frame(k,al,be,X,Y,J=6):
    fs=[]
    for rho in range(k):
        n0=rho+be/(2*np.pi); w=np.zeros_like(X,dtype=complex)
        for j in range(-J,J+1):
            n=n0+j*k
            w+=np.exp(1j*j*al-2*np.pi*n0*j-np.pi*k*j*j)*np.exp(n*X-k*X**2/(4*np.pi)+1j*n*Y)
        fs.append(w*np.exp(-1j*(al*X+be*Y)/(2*np.pi)))
    return np.array(fs)
def check_dbar(k,al,be):
    # residual of (d_x + i d_y + k x/(2 pi)) u = 0 by finite differences, in untwisted gauge
    h=1e-5; x0,y0=1.1,0.7
    def U(x,y,rho):
        n0=rho+be/(2*np.pi); s=0
        for j in range(-8,9):
            n=n0+j*k; s+=np.exp(1j*j*al-2*np.pi*n0*j-np.pi*k*j*j)*np.exp(n*x-k*x**2/(4*np.pi)+1j*n*y)
        return s
    r=0
    for rho in range(k):
        ux=(U(x0+h,y0,rho)-U(x0-h,y0,rho))/(2*h); uy=(U(x0,y0+h,rho)-U(x0,y0-h,rho))/(2*h)
        r=max(r,abs(ux+1j*uy+k*x0/(2*np.pi)*U(x0,y0,rho))/abs(U(x0,y0,rho)))
    return r
def chern(k,N=12,Nx=120,Ny=72):
    x=np.linspace(0,2*np.pi,Nx,endpoint=False);y=np.linspace(0,2*np.pi,Ny,endpoint=False)
    X,Y=np.meshgrid(x,y,indexing='ij'); w=1/(Nx*Ny); Fr={}
    for a in range(N+1):
        for b in range(N+1):
            f=frame(k,2*np.pi*a/N,2*np.pi*b/N,X,Y).reshape(k,-1)
            G=(f.conj()@f.T)*w; L=np.linalg.cholesky(G); Fr[(a,b)]=np.linalg.solve(L,f)
    def link(p,q):
        d=np.linalg.det((Fr[p].conj()@Fr[q].T)*w); return d/abs(d)
    tot=0
    for a in range(N):
        for b in range(N):
            z=link((a,b),(a+1,b))*link((a+1,b),(a+1,b+1))*link((a+1,b+1),(a,b+1))*link((a,b+1),(a,b))
            tot+=np.angle(z)
    return tot/(2*np.pi)
for k in (1,2,3):
    sm=chern(k)
    print("k=%d dbar residual %.1e  sum plaq/2pi=%.6f  => c1=%.6f"%(k,check_dbar(k,0.9,2.1),sm,-sm))

# ---------- 3. spectral flow of -i d/dth + f(t) with perturbation, general f
sec("3. spectral flow: signed integer crossings of f(t)-eps")
def SF(f,eps=1e-3,n=200001):
    t=np.linspace(0,1,n); v=f(t)-eps
    fl=np.floor(v); return int(fl[-1]-fl[0])
print("f=t:",SF(lambda t:t)," f=-t:",SF(lambda t:-t)," f=3t:",SF(lambda t:3*t)," f=2t+0.3 sin(8 pi t):",SF(lambda t:2*t+0.3*np.sin(8*np.pi*t)))
# direct eigenvalue count for D_t=-i d/dth+3t, eigenvalues n+3t, eps-shift
for eps in (1e-3,-1e-3):
    cnt=0
    ts=np.linspace(0,1,30001)
    for n in range(-10,11):
        ev=n+3*ts-eps
        cnt+=np.sum((ev[:-1]<0)&(ev[1:]>=0))-np.sum((ev[:-1]>=0)&(ev[1:]<0))
    print(" eps=%g, D_t=-i d+3t crossing count = %d"%(eps,cnt))

# ---------- 4. Toeplitz A_b: injective, cokernel = e0 x P_+ ; check via finite section SVD of A^*
sec("4. Toeplitz A_b index bundle")
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
def A(b,Nn=30):
    P=lambda s: 0.5*(np.eye(2)+s*(b[0]*sx+b[1]*sy+b[2]*sz))
    S=np.diag(np.ones(Nn-1),-1)
    return np.kron(S,P(+1))+np.kron(np.eye(Nn),P(-1)), P(+1)
b=np.array([np.sin(1.1)*np.cos(0.4),np.sin(1.1)*np.sin(0.4),np.cos(1.1)])
M,Pp=A(b)
x=np.kron(np.eye(30)[0],np.linalg.eigh(Pp)[1][:,1])  # e0 x (+1 eigvec)
print(" |A^* (e0 x u+)| =",np.linalg.norm(M.conj().T@x), " eigenvalue of b.sigma for u+:",np.linalg.eigh(Pp)[0])

# ---------- 5. P(V) direct image, exact: chi on Hirzebruch via HRR (independent of the Lagrange formula)
sec("5. Hirzebruch surface chi(O(k)) via surface HRR  (h^2=-n, f h=1, f^2=0)")
for n in (1,2):
    row=[]
    for k in range(0,5):
        # chi = 1 + k h.(-K)/2 + k^2 h^2/2 ; -K = 2h + (n+2) f
        chi=F(1)+F(k)*(2*(-n)+(n+2))/2+F(k*k)*(-n)/2
        row.append(chi)
    print(" n=%d:"%n,[str(c) for c in row], "formula sum(1-n i):",[sum(1-n*i for i in range(k+1)) for k in range(5)])

# ---------- 6. chi(P^2,wedge^b T(m)) and P_HH tables, exact via truncated series in h
sec("6. P^n tables")
def ser_exp(c,N): return [F(c)**i/factorial(i) for i in range(N+1)]
def mul(a,b,N):
    r=[F(0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N: r[i+j]+=x*y
    return r
def td_line(x,N):  # x=c1 coefficient times h: series of x/(1-e^{-x}) in h with x=c*h
    # use Bernoulli: t/(1-e^-t)=sum B_k^+ t^k/k!  with B1=+1/2
    B=[F(1),F(1,2),F(1,6),F(0),F(-1,30),F(0),F(1,42)]
    return [B[i]/factorial(i) for i in range(N+1)]
def chiPn(n,m,b):
    # T_P^n = (n+1)O(1) - O ; ch(wedge^b T) via generating function: sum_b s^b ch wedge^b T = (1+s e^h)^{n+1}/(1+s)
    N=n
    # ch(wedge^b ((n+1)L))
    from itertools import product
    # coefficient extraction: wedge^b T = sum_{j}(-1)^j wedge^{b-j}((n+1)L)  (since 1/(1+s)=sum (-s)^j)
    tot=[F(0)]*(N+1)
    for j in range(b+1):
        bb=b-j
        if bb<0 or bb>n+1: continue
        e=ser_exp(bb,N)
        for i in range(N+1): tot[i]+=(-1)**j*comb(n+1,bb)*e[i]
    tdn=[F(1)]+[F(0)]*N
    tdl=td_line(1,N)
    for _ in range(n+1): tdn=mul(tdn,tdl,N)
    em=ser_exp(m,N)
    r=mul(mul(tot,em,N),tdn,N)
    return r[N]
for n in (1,2):
    for m in range(0,4):
        vals=[chiPn(n,m,b) for b in range(n+1)]
        alt=sum((-1)**b*v for b,v in enumerate(vals))
        print(" P^%d m=%d chi(wedge^bT(m))="%(n,m),[str(v) for v in vals]," alt=",alt," expected (-1)^n(n+1)=",(-1)**n*(n+1))
def mult(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r
for Y,PY in (("S2",[1,0,1]),("T2",[1,2,1])):
    for m in (1,2,3):
        vals=[int(chiPn(2,m,b)) for b in range(3)]
        P=mult(PY,vals); print(" Y=%s X=P2 m=%d P_HH="%(Y,m),P," Euler",sum((-1)**i*c for i,c in enumerate(P)))
# P1xP1
for m in (1,):
    vals=[(m+1)**2,2*(m+3)*(m+1),(m+3)**2]; P=mult([1,0,1],vals); print(" S2 x (P1xP1) m=1:",P,sum((-1)**i*c for i,c in enumerate(P)))

# ---------- 7. Legendre PF and monodromy
sec("7. Legendre")
c=[F(1)]
for n in range(60): c.append(c[-1]*F(2*n+1,2*n+2)**2)
bad=0
for n in range(0,58):
    co=(n+1)*n*c[n+1]-n*(n-1)*c[n]+(n+1)*c[n+1]-2*n*c[n]-F(1,4)*c[n]
    bad+= (co!=0)
print(" PF residual nonzero count (n<58):",bad)
M0=np.array([[1,2],[0,1]]);M1=np.array([[1,0],[-2,1]]);P=M0@M1
print(" M0M1=",P.tolist()," (P+I)^2=",((P+np.eye(2,dtype=int))@(P+np.eye(2,dtype=int))).tolist(), " Minf=",np.round(np.linalg.inv(P)).astype(int).tolist())

# ---------- 8. superconnection (1,1): graded tensor-product algebra implemented explicitly
sec("8. superconnection (1,1) with Koszul signs, f=z and f=z^2")
# elements: dict {(form_subset tuple): 2x2 matrix}; forms from generators dx,dy (indices 0,1)
def parity(M):  # matrix parity: odd if off-diagonal only, even if diagonal only
    return 1 if (abs(M[0,0])+abs(M[1,1])<1e-14) and (abs(M[0,1])+abs(M[1,0])>0) else 0
def fmul(A,B):
    R={}
    for fa,Ma in A.items():
        for fb,Mb in B.items():
            if set(fa)&set(fb): continue
            # form product sign: sort
            lst=list(fa)+list(fb); sign=1
            for i in range(len(lst)):
                for j in range(i+1,len(lst)):
                    if lst[i]>lst[j]: sign=-sign
            # Koszul sign from moving matrix parts: (w (x) Ma)(w' (x) Mb) = (-1)^{|Ma||w'|} w w' (x) Ma Mb
            # need parity of Ma as a *matrix*; split into even/odd parts
            Mae=np.diag(np.diag(Ma)); Mao=Ma-Mae
            res=Mae@Mb+((-1)**len(fb))*(Mao@Mb)
            key=tuple(sorted(lst))
            R[key]=R.get(key,0)+sign*res
    return R
def fadd(A,B,cb=1):
    R=dict(A)
    for k,v in B.items(): R[k]=R.get(k,0)+cb*v
    return R
def fscale(A,c): return {k:c*v for k,v in A.items()}
def test(f,df, t, x,y):
    fv=f(x+1j*y); dfz=df(x+1j*y)  # holomorphic f: df/dx=f', df/dy=i f'
    D=np.array([[0,np.conj(fv)],[fv,0]],dtype=complex)
    Dx=np.array([[0,np.conj(dfz)],[dfz,0]]); Dy=np.array([[0,np.conj(1j*dfz)],[1j*dfz,0]])
    N={(0,):Dx,(1,):Dy}
    A2=fscale(N,np.sqrt(t))   # nilpotent part sqrt t N ; D^2=|f|^2 scalar commutes, factor out
    # exp(-A2) up to 2-forms
    E={():np.eye(2,dtype=complex)}; term={():np.eye(2,dtype=complex)}
    for k in range(1,5):
        term=fscale(fmul(term,A2),-1.0/k); E=fadd(E,term)
    M=E.get((0,1),np.zeros((2,2)))
    return np.exp(-t*abs(fv)**2)*(M[0,0]-M[1,1])   # Str of dx^dy coefficient
for name,f,df in (("z",lambda z:z,lambda z:1.0),("z^2",lambda z:z*z,lambda z:2*z)):
    for t in (0.5,2.0):
        # integrate Str e^{-A^2}/(2 pi i) over plane
        R=(5/np.sqrt(t) if name=='z' else 4/t**0.25); g=np.linspace(-R,R,241); h=g[1]-g[0]
        tot=sum(test(f,df,t,x,y) for x in g for y in g)*h*h/(2j*np.pi)
        print(" f=%s t=%g  (1/2pi i) int Str e^{-A^2} = %s"%(name,t,np.round(tot,4)))

# ---------- 9. Lagrange identity (Prop Pbundle) independent re-check incl. k<=-r branch, exact Fractions
sec("9. Prop Pbundle exact check")
import itertools, random
def hk(xs,k):
    if k<0: return F(0)
    tot=F(0)
    for comb_ in itertools.combinations_with_replacement(range(len(xs)),k):
        p=F(1)
        for i in comb_: p*=xs[i]
        tot+=p
    return tot
random.seed(1)
bad=0
for r in (2,3,4):
    xs=[F(random.randint(2,9),random.randint(1,5))+i for i in range(r)]
    xs=list(dict.fromkeys(xs))
    assert len(xs)==r
    for k in range(-9,8):
        lhs=F(0)
        for i in range(r):
            pr=F(1)
            for j in range(r):
                if j!=i: pr*=(1-xs[j]/xs[i])
            lhs+=xs[i]**k/pr
        if k>=0: rhs=hk(xs,k)
        elif k>-r: rhs=F(0)
        else:
            pe=F(1)
            for x in xs: pe*=x
            rhs=(-1)**(r-1)/pe*hk([1/x for x in xs],-k-r)
        bad+= (lhs!=rhs)
print(" mismatches:",bad)
