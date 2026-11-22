# Independent checks for vol03 (no sympy): integer/rational linear algebra and monomial counting
from fractions import Fraction
from itertools import product, combinations, permutations
from math import comb

def rank(M):
    M=[[Fraction(x) for x in r] for r in M]
    if not M: return 0
    r=0; rows=len(M); cols=len(M[0])
    for c in range(cols):
        p=None
        for i in range(r,rows):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(rows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]/M[r][c]
                M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        r+=1
        if r==rows: break
    return r

def smith_diag(M):
    # integer Smith normal form diagonal (simple implementation)
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    diag=[]
    r=0
    while r<min(m,n):
        # find nonzero pivot with minimal abs
        piv=None
        for i in range(r,m):
            for j in range(r,n):
                if A[i][j]!=0 and (piv is None or abs(A[i][j])<abs(A[piv[0]][piv[1]])): piv=(i,j)
        if piv is None: break
        i,j=piv
        A[r],A[i]=A[i],A[r]
        for row in A: row[r],row[j]=row[j],row[r]
        while True:
            changed=False
            for i in range(r+1,m):
                q=A[i][r]//A[r][r]
                if q:
                    A[i]=[a-q*b for a,b in zip(A[i],A[r])]
                if A[i][r]!=0:
                    A[r],A[i]=A[i],A[r]; changed=True
            for j in range(r+1,n):
                q=A[r][j]//A[r][r]
                if q:
                    for row in A: row[j]-=q*row[r]
                if A[r][j]!=0:
                    for row in A: row[r],row[j]=row[j],row[r]
                    changed=True
            if not changed:
                # check divisibility
                bad=False
                for i in range(r+1,m):
                    for j in range(r+1,n):
                        if A[i][j]%A[r][r]!=0:
                            A[r]=[a+b for a,b in zip(A[r],A[i])]; bad=True;break
                    if bad:break
                if not bad:break
        diag.append(abs(A[r][r])); r+=1
    return diag

out=[]
def log(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)

# ---- 1. Cech cohomology over Z of S^1, two covers
# 2 arcs: C0=Z^2, C1=Z^2 (A,B), d(a0,a1)=(a1-a0,a1-a0)
d=[[-1,1],[-1,1]]   # rows: components A,B ; cols: a0,a1
sd=smith_diag(d); rk=sum(1 for x in sd if x!=0)
log("S1 two arcs: rank d=",rk,"H0 rank=",2-rk,"coker rank=",2-rk,"torsion=",[x for x in sd if x>1])
# 3 arcs: C0=Z^3, C1=Z^3 (01,12,02), d(a)=(a1-a0,a2-a1,a2-a0)
d=[[-1,1,0],[0,-1,1],[-1,0,1]]
sd=smith_diag(d); rk=sum(1 for x in sd if x!=0)
log("S1 three arcs: rank d=",rk,"H0=",3-rk,"H1 rank=",3-rk,"torsion=",[x for x in sd if x>1])
# S^2 two hemispheres: C0=Z^2,C1=Z
d=[[-1,1]]; sd=smith_diag(d); rk=sum(1 for x in sd if x!=0)
log("S2 two sets: H0=",2-rk,"H1=",1-rk)
# Z/2 coefficients, 2 arcs: rank over F2
def rank_mod(M,p):
    M=[[x%p for x in r] for r in M]; r=0; rows=len(M); cols=len(M[0])
    for c in range(cols):
        pv=None
        for i in range(r,rows):
            if M[i][c]%p: pv=i;break
        if pv is None: continue
        M[r],M[pv]=M[pv],M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[(x*inv)%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        r+=1
        if r==rows:break
    return r
d=[[-1,1],[-1,1]]
log("S1 two arcs Z/2: dim H1 =",2-rank_mod(d,2))
# Z coefficient: Z^2/<(1,1)>: Smith diag
log("check Smith(1x1 etc):",smith_diag([[2,0],[0,3]]),smith_diag([[2,4],[6,8]]))

# ---- 2. O(k) on P^1 by explicit monomial Cech map in a window
def p1(k,N=40):
    # f0 = sum_{n>=0} a_n z^n ; f1=sum_{m>=0} b_m w^m ; delta = sum b_m z^{k-m} - sum a_n z^n on z^j, j in [-N,N]
    exps=list(range(-N,N+1))
    cols=[]  # basis of source (window): a_n for 0<=n<=N ; b_m for 0<=m<=2N+|k| so that k-m in window
    src=[('a',n) for n in range(0,N+1)]+[('b',m) for m in range(0,2*N+abs(k)+1)]
    idx={e:i for i,e in enumerate(exps)}
    M=[[0]*len(src) for _ in exps]
    for c,(t,n) in enumerate(src):
        if t=='a':
            if n in idx: M[idx[n]][c]=-1
        else:
            e=k-n
            if e in idx: M[idx[e]][c]=1
    r=rank(M)
    # kernel inside window: only count sources whose image fully inside window (all do), so kernel = len(src)-r
    # but sources with image outside window are mapped to 0 artificially; exclude them
    valid=[c for c,(t,n) in enumerate(src) if (t=='a' and n in idx) or (t=='b' and (k-n) in idx)]
    ker=len(valid)-rank([[M[i][c] for c in valid] for i in range(len(exps))])
    coker=len(exps)-r
    return ker,coker
log("P1 table via explicit Cech map: k: (h0,h1)")
for k in range(-7,8):
    ker,cok=p1(k)
    # cokernel in window includes boundary artifacts for exponents near +-N: subtract by comparing N values
    ker2,cok2=p1(k,60)
    assert (ker,cok)==(ker2,cok2),(k,ker,cok,ker2,cok2)
    exp_h0=max(k+1,0); exp_h1=max(-k-1,0)
    assert (ker,cok)==(exp_h0,exp_h1),(k,ker,cok)
    log(" k=",k,(ker,cok))

# ---- 3. CP^n monomial/simplicial complexes
def simplicial_cohom_dims(n,S):
    # alternating cochains on index sets I (as sorted tuples) with S subset I, I nonempty, complex C^p over |I|=p+1; non-augmented
    verts=list(range(n+1))
    levels=[]
    for p in range(n+1):
        levels.append([I for I in combinations(verts,p+1) if set(S)<=set(I)])
    dims=[len(l) for l in levels]
    ranks=[]
    for p in range(n):
        src=levels[p]; tgt=levels[p+1]
        M=[[0]*len(src) for _ in tgt]
        ti={I:i for i,I in enumerate(tgt)}; si={I:i for i,I in enumerate(src)}
        for J in tgt:
            for k in range(len(J)):
                I=J[:k]+J[k+1:]
                if I in si: M[ti[J]][si[I]]+=(-1)**k
        ranks.append(rank(M) if src and tgt else 0)
    H=[]
    for p in range(n+1):
        rk_out=ranks[p] if p<n else 0
        rk_in=ranks[p-1] if p>0 else 0
        H.append(dims[p]-rk_out-rk_in)
    return H
def Pn(n,k,R=12):
    H=[0]*(n+1)
    for a in product(range(-R,R+1),repeat=n):
        last=k-sum(a)
        if abs(last)>R: continue
        aa=a+(last,)
        S=tuple(i for i in range(n+1) if aa[i]<0)
        h=simplicial_cohom_dims(n,S)
        for q in range(n+1): H[q]+=h[q]
    return H
def formula(n,k):
    H=[0]*(n+1)
    H[0]=comb(n+k,n) if k>=0 else 0
    H[n]=H[n]+(comb(-k-1,n) if k<=-n-1 else 0)
    return H
for n in (1,2,3):
    for k in range(-7,5):
        got=Pn(n,k,R=9 if n<3 else 8); exp=formula(n,k)
        assert got==exp,(n,k,got,exp)
    log("CP^%d: H^q(O(k)) for k=-7..4 matches binomial formula (monomial/simplicial complex computation)"%n)
log("CP2 O(-3):",Pn(2,-3),"O(-4):",Pn(2,-4),"O(-6):",Pn(2,-6),"O(0):",Pn(2,0))

# ---- 4. C^2\{0}: monomials with Cech complex on U1,U2 (I subset of {0,1}); S(a)
def c2(a):
    S=tuple(i for i in range(2) if a[i]<0)
    return simplicial_cohom_dims(1,S)
tot=[0,0]
for a in product(range(-6,7),repeat=2):
    h=c2(a)
    tot=[tot[0]+h[0],tot[1]+h[1]]
log("C^2\\0 window |a|<=6: H0 monomials",tot[0],"(expected 49 = a>=0 within window?)", "H1 monomials",tot[1],"(expected a1,a2<0: 36)")
# ---- 5. chi numbers
chi=lambda k:k+1
def chiP2(k): return comb(k+2,2) if k>=0 else (comb(-k-1,2) if k<=-3 else 0)*1  # H0 or H2 (sign +)
log("CP2: chi(O)=",chiP2(0),"chi(O(1))=",chiP2(1),"chi(O(2))=",chiP2(2),"chi(O(3))=",chiP2(3),"chi(O(4))=",chiP2(4))
chiT=3*chiP2(1)-chiP2(0); log("chi(T)=",chiT,"; sum L=O:",chiP2(0)-chiT+chiP2(3))
chiT1=3*chiP2(2)-chiP2(1); log("chi(T(1))=",chiT1,"; sum L=O(1):",chiP2(1)-chiT1+chiP2(4))
# sum for general L=O(k) on P2
for k in range(-4,5):
    chiTk=3*chiP2(k+1)-chiP2(k)
    val=chiP2(k)-chiTk+chiP2(k+3)
    assert val==3,(k,val)
log("CP2: sum(-1)^p chi(Lambda^p T (x) O(k))=3 for k=-4..4")
for k in range(-6,6):
    assert chi(k)-chi(k+2)==-2
log("CP1: chi(O(k))-chi(O(k+2))=-2 for k=-6..5")
# P1 HH table (sigma=0)
log("CP1 HH table (d_sigma=0), k: (HH0,HH1,HH2), chi")
for k in range(-4,3):
    h0=lambda m:max(m+1,0); h1=lambda m:max(-m-1,0)
    HH=(h0(k),h1(k)+h0(k+2),h1(k+2)); log(" ",k,HH,HH[0]-HH[1]+HH[2])
# two-term LES [O -> O(m)] with s vanishing at m points: dims HH
for m in (1,2,3):
    # H^0(O)=1 -> H^0(O(m))=m+1 injective ; H^1(O)=0,H^1(O(m))=0
    HH0=0; HH1=(m+1)-1; HH2=0
    log("[O->O(%d)] HH dims"%m,(HH0,HH1,HH2),"expected m points:",m)
# Z/2 etc done.  O(-m) sequence
for m in range(1,6):
    # 0->H0(O(-m))=0 ->H0(O)=1 -> C^m -> H1(O(-m)) -> H1(O)=0
    log("h1(O(-%d)) from skyscraper seq ="%m, m-1, "table:",max(m-1,0))
# Euler seq chi relation
for k in range(-5,5):
    assert chi(k+1)==2*chi(k)-chi(k-1)
log("Euler seq chi relation ok")
# torus chi(O) = sum (-1)^q C(n,q)
for n in range(1,6):
    log("complex torus dim",n,"chi(O)=",sum((-1)**q*comb(n,q) for q in range(n+1)))
open('verify.log','w').write("\n".join(out)+"\n")

# duality check HH^j(L)^* = HH^{2-j}(L^vee (x) K^2) on P1 (sigma=0), L=O(k): L^vee K^2 = O(-k-4)
h0=lambda m:max(m+1,0); h1=lambda m:max(-m-1,0)
HHf=lambda k:(h0(k),h1(k)+h0(k+2),h1(k+2))
for k in range(-9,10):
    a=HHf(k); b=HHf(-k-4)
    assert all(a[j]==b[2-j] for j in range(3)),(k,a,b)
log("P1 (sigma=0): dim HH^j(O(k)) = dim HH^{2-j}(O(-k-4)) for k=-9..9 (term-wise Serre duality)")
open('verify.log','w').write("\n".join(out)+"\n")
