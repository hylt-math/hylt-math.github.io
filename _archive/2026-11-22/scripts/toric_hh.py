# Hypercohomology of the generalized Dolbeault complex C(A;L) for TORIC log-symplectic structures.
# X smooth complete toric variety (fan rays u_i in N=Z^n), sigma = sum a_ij E_i^E_j (constant in log frame, a skew nondegenerate),
# L = O(sum a_i D_i) with flat log connection d+rho (rho in M_C), residue along D_i: r_i = <rho,u_i> - a_i.
# Valid when E_1^{a>0}=0 (L sufficiently ample), then HH = cohomology of the global-section complex:
#   weight chi:  G^b_chi = {w in wedge^b N_C : u_i ^ w = 0 for every i with <chi,u_i> = -a_i-1}  (empty if some <chi,u_i> < -a_i-1),
#   d = v_chi ^,  v_chi = A (chi+rho).
import itertools, sys
from fractions import Fraction
P = (1<<61)-1
def inv(x): return pow(x%P, P-2, P)
def modfrac(q):
    q = Fraction(q); return (q.numerator % P) * inv(q.denominator) % P

def subsets(n,b): return [s for s in itertools.combinations(range(n),b)]
def wedge_matrix(vec,n,b):
    """matrix of (vec ^ .): wedge^b -> wedge^{b+1}, rows indexed by target basis, columns by source basis; vec mod P"""
    src=subsets(n,b); tgt=subsets(n,b+1); ti={s:i for i,s in enumerate(tgt)}
    M=[[0]*len(src) for _ in tgt]
    for j,s in enumerate(src):
        for i in range(n):
            if vec[i]%P==0 or i in s: continue
            t=tuple(sorted(s+(i,))); pos=sum(1 for x in s if x<i)
            M[ti[t]][j]=(M[ti[t]][j]+(-1)**pos*vec[i])%P
    return M

def rref(M,ncols):
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(ncols):
        pr=None
        for i in range(r,len(M)):
            if M[i][c]%P: pr=i;break
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]; iv=inv(M[r][c]); M[r]=[x*iv%P for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%P:
                f=M[i][c]; M[i]=[(x-f*y)%P for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==len(M): break
    return M[:r],piv
def rank(M,ncols):
    if not M or ncols==0: return 0
    return len(rref(M,ncols)[1])
def nullspace(M,ncols):
    if not M: return [[1 if i==j else 0 for i in range(ncols)] for j in range(ncols)]
    R,piv=rref(M,ncols); free=[c for c in range(ncols) if c not in piv]; basis=[]
    for f in free:
        v=[0]*ncols; v[f]=1
        for row,pc in zip(R,piv): v[pc]=(-row[f])%P
        basis.append(v)
    return basis
def matvec(M,v): return [sum(a*b for a,b in zip(row,v))%P for row in M]

def hh(rays,avec,A,rho,box=None,verbose=False):
    n=len(rays[0]); a=avec
    rhoP=[modfrac(x) for x in rho]
    if box is None: box=max(abs(x) for x in a)+3
    poly=[0]*(n+1)
    for chi in itertools.product(range(-box,box+1),repeat=n):
        cons=[]; ok=True
        for u,ai in zip(rays,a):
            c=sum(x*y for x,y in zip(chi,u))+ai
            if c<-1: ok=False;break
            if c==-1: cons.append(u)
        if not ok: continue
        v=[sum(A[i][j]*(chi[j]*1+0) for j in range(n)) for i in range(n)]
        v=[(sum(A[i][j]*((chi[j]%P)+rhoP[j]) for j in range(n)))%P for i in range(n)]
        # subspaces
        S=[];
        for b in range(n+1):
            dimb=len(subsets(n,b))
            rows=[]
            for u in cons:
                if b<n: rows+=wedge_matrix([x%P for x in u],n,b)
            S.append(nullspace(rows,dimb) if rows or True else None)
        # differential ranks on S
        rk=[0]*(n+1)
        for b in range(n):
            if not S[b]: continue
            Mw=wedge_matrix(v,n,b)
            imgs=[matvec(Mw,w) for w in S[b]]
            rk[b]=rank(imgs,len(subsets(n,b+1)))
        for b in range(n+1):
            h=len(S[b])-rk[b]-(rk[b-1] if b>0 else 0)
            poly[b]+=h
    return poly

def euler(p): return sum((-1)**k*x for k,x in enumerate(p))
