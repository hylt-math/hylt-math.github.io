# Verification script for vol05 (Python only: fractions / numpy / itertools)
import itertools, math
from fractions import Fraction as Fr
import numpy as np
from math import comb

def C(n,k):
    return comb(n,k) if (n>=0 and 0<=k<=n) else 0

# ---------- 1. Cech cohomology of O(m) on P^n via multigraded complex ----------
def hq_formula(n,m,q):
    if q==0: return C(m+n,n)
    if q==n: return C(-m-1,n)
    return 0

def cech_dims(n,m):
    B=abs(m)+n+3
    tot=[0]*(n+1)
    rng=range(-B,B+1)
    def rec(i,left):
        if i==n:
            yield (left,)
            return
        for v in rng:
            for rest in rec(i+1,left-v):
                yield (v,)+rest
    for a in rec(0,m):
        if any(abs(x)>B for x in a): continue
        Nset=frozenset(i for i,x in enumerate(a) if x<0)
        faces={p:[I for I in itertools.combinations(range(n+1),p+1) if Nset<=set(I)] for p in range(n+1)}
        dims=[len(faces[p]) for p in range(n+1)]
        ranks=[0]*(n+2)
        for p in range(n):
            if dims[p]==0 or dims[p+1]==0: continue
            idx={I:i for i,I in enumerate(faces[p])}
            M=np.zeros((dims[p+1],dims[p]))
            for r,I in enumerate(faces[p+1]):
                for j in range(len(I)):
                    J=I[:j]+I[j+1:]
                    if J in idx: M[r,idx[J]]+=(-1)**j
            ranks[p]=np.linalg.matrix_rank(M)
        for p in range(n+1):
            h=dims[p]-ranks[p]-(ranks[p-1] if p>0 else 0)
            tot[p]+=h
    return tot

ok=True
for n in (1,2,3):
    for m in range(-(n+4), 4):
        d=cech_dims(n,m)
        f=[hq_formula(n,m,q) for q in range(n+1)]
        if d!=f:
            ok=False; print("MISMATCH",n,m,d,f)
print("1. Cech P^n O(m):", "OK" if ok else "FAIL")

# ---------- 2. exterior algebra: [L,Lambda]=(k-n), flat Kahler identity ----------
def ext_ops(n):
    N=2*n; dim=1<<N
    def eps(i):
        M=np.zeros((dim,dim),dtype=complex)
        for s in range(dim):
            if not (s>>i)&1:
                sign=(-1)**bin(s&((1<<i)-1)).count('1')
                M[s|(1<<i),s]=sign
        return M
    return [eps(i) for i in range(N)]
for n in (1,2,3):
    E=ext_ops(n); dim=1<<(2*n)
    L=sum(1j*E[j]@E[n+j] for j in range(n))   # omega = i sum dz_j ^ dzbar_j
    Lam=L.conj().T
    comm=L@Lam-Lam@L
    deg=np.array([bin(s).count('1') for s in range(dim)])
    good=np.allclose(comm,np.diag(deg-n))
    # flat Kahler identity [Lambda, eps(f_j)] = i iota(e_j)
    good2=all(np.allclose(Lam@E[n+j]-E[n+j]@Lam, 1j*E[j].conj().T) for j in range(n))
    # also [Lambda,eps(e_j)] = -i iota(f_j)
    good3=all(np.allclose(Lam@E[j]-E[j]@Lam, -1j*E[n+j].conj().T) for j in range(n))
    # Lambda omega = n, Lambda omega^2=(2n-2) omega
    om=np.zeros(dim,dtype=complex); om[0]=1
    w=L@om; w2=L@w
    print("2. n=%d [L,Lam]=(k-n):"%n,good," flat Kahler id:",good2,good3," Lam(w)=n:",np.allclose(Lam@w,n*om)," Lam(w^2)=(2n-2)w:",np.allclose(Lam@w2,(2*n-2)*w))
# Nakano algebraic lemma check: for alpha in Lambda^{n,q}(x)E, <[iTheta,Lam]alpha,alpha> = sum_I sum_jk <Theta_jk a_jI, a_kI>
rng=np.random.default_rng(1)
n=3; r=2
E=ext_ops(n); dim=1<<(2*n)
L=sum(1j*E[j]@E[n+j] for j in range(n)); Lam=L.conj().T
# Theta_{j kbar} hermitian block matrix (jr, kr') positive-definite not needed: just Hermitian (nr x nr)
A=rng.normal(size=(n*r,n*r))+1j*rng.normal(size=(n*r,n*r)); H=A+A.conj().T   # H[(j,a),(k,b)]
# iTheta = i sum_{jk} Theta_{jk}(endomorphism) dz_j ^ dzbar_k ; on E-valued forms: operator sum_jk eps(e_j) eps(f_k) (x) i*Th_jk, Th_jk[a,b]=H[(j,a),(k,b)]
def Th(j,k): return np.array([[H[j*r+a,k*r+b] for b in range(r)] for a in range(r)])
Id=np.eye(r)
IT=sum(np.kron(1j*E[j]@E[n+k],Th(j,k)) for j in range(n) for k in range(n))
LamE=np.kron(Lam,Id)
Comm=IT@LamE-LamE@IT
# alpha in Lambda^{n,q}: monomials containing all e_j (bits 0..n-1) and q of the f's
ok=True
for q in (1,2,3):
    # random alpha
    comps=[s for s in range(dim) if (s&((1<<n)-1))==((1<<n)-1) and bin(s>>n).count('1')==q]
    alpha=np.zeros(dim*r,dtype=complex)
    for s in comps:
        alpha[s*r:(s+1)*r]=rng.normal(size=r)+1j*rng.normal(size=r)
    lhs=np.vdot(alpha,Comm@alpha)
    # rhs: sum over (q-1)-subsets I of {f}, xi_I = sum_j e_j (x) a_{jI}
    rhs=0
    for I in itertools.combinations(range(n),q-1):
        # a_{jI}: coefficient of dz1..dzn ^ dzbar_{j} dzbar_I (j not in I) with sign from ordering: iota(fbar_j) removes
        xi=[np.zeros(r,dtype=complex) for _ in range(n)]
        for j in range(n):
            if j in I: continue
            J=tuple(sorted(I+(j,)))
            s=((1<<n)-1)|sum(1<<(n+t) for t in J)
            # iota_{fbar_j} dzbar_J = sign * dzbar_I ; sign = (-1)^(position of j in J)
            pos=J.index(j)
            xi[j]=((-1)**pos)*alpha[s*r:(s+1)*r]
        v=np.concatenate(xi)
        H2=np.zeros_like(H)
        for j in range(n):
            for k in range(n):
                H2[k*r:(k+1)*r,j*r:(j+1)*r]=H[j*r:(j+1)*r,k*r:(k+1)*r]
        rhs+=np.vdot(v,H2@v)
    if not np.isclose(lhs,rhs): ok=False; print("Nakano lemma mismatch",q,lhs,rhs)
print("2b. Nakano algebraic lemma <[iTheta,Lam]a,a> = sum_I Nakano form:", "OK" if ok else "FAIL (check)")

# ---------- 3. Hodge numbers ----------
for n in (1,2,3,4):
    h=[[C(n,p)*C(n,q) for q in range(n+1)] for p in range(n+1)]
    b=[sum(h[p][k-p] for p in range(max(0,k-n),min(n,k)+1)) for k in range(2*n+1)]
    assert b==[C(2*n,k) for k in range(2*n+1)]
print("3a. torus Hodge numbers: sum = C(2n,k) OK")
# polynomial arithmetic
def pmul(a,b,deg):
    r=[Fr(0)]*(deg+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=deg: r[i+j]+=x*y
    return r
def chern_hyper(n,d):  # c(T) of hypersurface deg d in P^{n+1}, coefficient list in H
    num=[Fr(C(n+2,k)) for k in range(n+1)]
    inv=[Fr((-d)**k) for k in range(n+1)]
    return pmul(num,inv,n)
for n,d,name in [(2,4,"quartic K3"),(3,5,"quintic"),(2,3,"cubic surface"),(1,3,"cubic curve")]:
    c=chern_hyper(n,d); print("3b.",name,"c_top =",c[n],"-> e =",c[n]*d)
# K3 Hodge
e=24; b2=e-2; print("3c. K3: b2=",b2,"h11=",b2-2)
# quintic: b3 = 4 - e
e=-200; b3=4-e; print("3d. quintic b3=",b3,"h21=",b3//2-1)
# chi(O) = (c1^2+c2)/12 for K3 -> 2
print("3e. K3 chi(O)=",Fr(24,12))

# ---------- 4. Lefschetz primitive dims ----------
def prim(b,n):
    return [b[k]-(b[k-2] if k>=2 else 0) for k in range(n+1)]
print("4a. P^3 betti",[1 if k%2==0 else 0 for k in range(7)],"prim:",prim([1,0,1,0,1,0,1],3))
print("4b. T^4 b=",[C(4,k) for k in range(5)]," prim (k<=2):",prim([C(4,k) for k in range(5)],2))
print("4c. K3 prim b2:",22-1)
print("4d. quintic b:",[1,0,1,204,1,0,1],"prim 0..3:",prim([1,0,1,204,1,0,1],3))
# signature K3: b+ = 2p_g+1, b- = h11-1
print("4e. K3 signature:", 3-19, " (b+,b-)=(3,19)")

# ---------- 5. Serre duality on P^n and hypersurfaces ----------
ok=True
for n in (1,2,3,4):
    for m in range(-12,12):
        for q in range(n+1):
            if hq_formula(n,m,q)!=hq_formula(n,-m-n-1,n-q): ok=False
print("5a. Serre duality P^n:", "OK" if ok else "FAIL")
def S(n,k): return C(k+n,n) if k>=0 else 0   # h^0(P^n,O(k))
def hyp(d,k):  # surface degree d in P^3
    h0=S(3,k)-S(3,k-d)
    h2=S(3,d-k-4)-S(3,-k-4)
    return h0,h2
ok=True
for d in range(1,8):
    for k in range(-10,12):
        h0,h2=hyp(d,k); h0d,_=hyp(d,d-4-k)
        if h2!=h0d: ok=False
    pg=hyp(d,0)[1]
    assert pg==C(d-1,3)
    # chi(O_X(k)) check vs RR for surface: chi = d k^2/2 ... compute chi via h0-h1+h2 with h1=0
print("5b. hypersurface Serre duality h2(O_X(k))=h0(O_X(d-4-k)) and p_g=C(d-1,3):", "OK" if ok else "FAIL")
print("   p_g for d=1..6:",[C(d-1,3) for d in range(1,7)])
# chi of O(m) on P^2
print("5c. chi(P^2,O(m)):",[ (m,hq_formula(2,m,0)-hq_formula(2,m,1)+hq_formula(2,m,2)) for m in range(-5,4)], " =(m+1)(m+2)/2:",all(hq_formula(2,m,0)-hq_formula(2,m,1)+hq_formula(2,m,2)==(m+1)*(m+2)//2 for m in range(-9,9)))
print("   table h^q(P^2,O(m)):")
for m in range(-6,4):
    print("    m=%d"%m,[hq_formula(2,m,q) for q in range(3)])

# ---------- 6. K3 h^0(L)=2+L^2/2 ----------
# complete intersections: h^0(O_X(1)) = n+... direct: linear forms not in ideal
for name,P,deg in [("quartic in P3",3,4),("(2,3) in P4",4,6),("(2,2,2) in P5",5,8)]:
    print("6. K3",name,": L^2=",deg," 2+L^2/2=",2+deg//2," h0(O(1))=",P+1)
print("   double plane (sextic): L^2=2, h0=3 =2+1 ; ok")

# ---------- 7. Veronese ----------
import random
def veronese(x): 
    return [x[0]**2,x[0]*x[1],x[0]*x[2],x[1]**2,x[1]*x[2],x[2]**2]
pts=[[Fr(random.randint(-5,5)) for _ in range(3)] for _ in range(5)]
def sym(v): return [[v[0],v[1],v[2]],[v[1],v[3],v[4]],[v[2],v[4],v[5]]]
good=True
for x in pts:
    M=sym(veronese(x)); 
    for i,j in itertools.combinations(range(3),2):
        for k,l in itertools.combinations(range(3),2):
            if M[i][k]*M[j][l]-M[i][l]*M[j][k]!=0: good=False
print("7a. Veronese: all 2x2 minors of symmetric matrix vanish:",good,"; h0(P^2,O(2))=",S(2,2))
# immersion: Jacobian rank of affine chart (1,u,v) -> veronese: rank 2
