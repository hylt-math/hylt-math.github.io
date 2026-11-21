# Weight-graded model of the node (sigma = z1 z2 d1^d2, nabla e = sum r_i dlog z_i e) used in ncd_theorem.md.
# In the log basis E_i = z_i d_i, monomials z^gamma E_I (gamma in Z^2):
#   d0 z^g     = lam2 z^g E1 - lam1 z^g E2          (lam_i = g_i + r_i)
#   d1 (x E1 + y E2) z^g = (lam1 x + lam2 y) z^g E12
# Three complexes (all Z^2-graded, differential preserves gamma):
#  FULL (= C(A;L)), LOG (= wedge T_D (x) L), Q = FULL/LOG.
#  stalk at the node (power series):   FULL: 0:(g>=0) E1:(g1>=-1,g2>=0) E2:(g1>=0,g2>=-1) E12:(g>=(-1,-1))
#                                      LOG : all four basis elements need g>=0
#  local cohomology H^*_p (Cech, Laurent tails): FULL: 0:(g<=-1) E1:(g1<=-2,g2<=-1) E2:(g1<=-1,g2<=-2) E12:(g<=-2)
#                                      LOG : all four need g<=-1       (shift all degrees by +2 for H^2_p(O))
# We check dim H(FULL) = dim H(LOG) + dim H(Q) in each degree (=> all connecting maps vanish, in particular
# the extension class e_p in H^3_p(LOG) of the triangle LOG -> FULL -> Q is 0).
from fractions import Fraction as Fr
import itertools
def rank(M):
    M=[row[:] for row in M]; rk=0
    if not M: return 0
    cols=len(M[0])
    for c in range(cols):
        piv=None
        for i in range(rk,len(M)):
            if M[i][c]!=0: piv=i;break
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]
                M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk

NAMES=[0,'E1','E2','E12']; DEG={0:0,'E1':1,'E2':1,'E12':2}
def present(g,kind,which):
    g1,g2=g
    if kind=='stalk':
        full={0:g1>=0 and g2>=0,'E1':g1>=-1 and g2>=0,'E2':g1>=0 and g2>=-1,'E12':g1>=-1 and g2>=-1}
        log={k:(g1>=0 and g2>=0) for k in NAMES}
    else:
        full={0:g1<=-1 and g2<=-1,'E1':g1<=-2 and g2<=-1,'E2':g1<=-1 and g2<=-2,'E12':g1<=-2 and g2<=-2}
        log={k:(g1<=-1 and g2<=-1) for k in NAMES}
    return {k for k,v in (full if which=='full' else log).items() if v}
def dmat(g,r,P):
    """full 4x4 differential matrix D[target][source] restricted to present set P"""
    lam1,lam2=g[0]+r[0],g[1]+r[1]
    D={(t,s_):Fr(0) for t in NAMES for s_ in NAMES}
    D[('E1',0)]=lam2; D[('E2',0)]=-lam1
    D[('E12','E1')]=lam1; D[('E12','E2')]=lam2
    return {(t,s_):v for (t,s_),v in D.items() if t in P and s_ in P}
def nullspace_dim_and_rank(M,rows,cols):
    return rank([[M.get((t,s_),Fr(0)) for s_ in cols] for t in rows]) if rows and cols else 0
def cohom_data(g,r,kind,which):
    P=present(g,kind,which)
    D=dmat(g,r,P)
    deg=lambda k:[n for n in NAMES if n in P and DEG[n]==k]
    C=[deg(0),deg(1),deg(2)]
    r0=nullspace_dim_and_rank(D,C[1],C[0]); r1=nullspace_dim_and_rank(D,C[2],C[1])
    h=[len(C[0])-r0,len(C[1])-r0-r1,len(C[2])-r1]
    return P,D,C,h
def fstar_rank(g,r,kind):
    """rank of f_*: H(LOG_g)->H(FULL_g) in each degree (f = inclusion of basis elements present in both; zero otherwise)"""
    PL,DL,CL,hL=cohom_data(g,r,kind,'log'); PF,DF,CF,hF=cohom_data(g,r,kind,'full')
    out=[]
    for k in range(3):
        # cocycles of LOG in degree k (as vectors in basis CL[k]): kernel of d_k
        # compute kernel basis via simple Gaussian elimination
        nL=len(CL[k])
        if nL==0: out.append(0); continue
        if k<2 and CL[k+1]:
            M=[[DL.get((t,s_),Fr(0)) for s_ in CL[k]] for t in CL[k+1]]
        else: M=[]
        Z=kernel(M,nL)
        # coboundaries of FULL in degree k
        if k>0 and CF[k-1]:
            Bm=[[DF.get((t,s_),Fr(0)) for s_ in CF[k-1]] for t in CF[k]] if CF[k] else []
            Bcols=[[Bm[i][j] for i in range(len(CF[k]))] for j in range(len(CF[k-1]))] if CF[k] else []
        else: Bcols=[]
        idx={n:i for i,n in enumerate(CF[k])}
        # f(z): vector in CF[k]
        fz=[]
        for z in Z:
            v=[Fr(0)]*len(CF[k])
            for n,c in zip(CL[k],z):
                if n in idx: v[idx[n]]+=c
            fz.append(v)
        rB=rank(Bcols) if Bcols else 0
        rBF=rank(Bcols+fz) if (Bcols+fz) else 0
        out.append(rBF-rB)
    return out,hL,hF
def kernel(M,n):
    # basis of {x: M x = 0}, M list of rows (len n)
    if not M: return [[Fr(1) if i==j else Fr(0) for i in range(n)] for j in range(n)]
    A=[row[:] for row in M]; piv=[]; rk=0
    for c in range(n):
        p=None
        for i in range(rk,len(A)):
            if A[i][c]!=0: p=i;break
        if p is None: continue
        A[rk],A[p]=A[p],A[rk]
        A[rk]=[a/A[rk][c] for a in A[rk]]
        for i in range(len(A)):
            if i!=rk and A[i][c]!=0:
                f=A[i][c]; A[i]=[a-f*b for a,b in zip(A[i],A[rk])]
        piv.append(c); rk+=1
    free=[c for c in range(n) if c not in piv]
    ker=[]
    for fcol in free:
        x=[Fr(0)]*n; x[fcol]=Fr(1)
        for i,pc in enumerate(piv): x[pc]=-A[i][fcol]
        ker.append(x)
    return ker
import itertools
def analyse(r,kind,W=8):
    totF=[0,0,0]; totL=[0,0,0]; totI=[0,0,0]
    for g in itertools.product(range(-W,W+1),repeat=2):
        img,hL,hF=fstar_rank(g,r,kind)
        totF=[a+b for a,b in zip(totF,hF)]; totL=[a+b for a,b in zip(totL,hL)]; totI=[a+b for a,b in zip(totI,img)]
    inj=(totI==totL)           # f_* injective on cohomology  <=> all connecting maps (cone -> LOG[1]) vanish
    # cone cohomology dims: H^k(cone)= coker(f_*)_k + ker(f_*)_{k+1}
    cone=[ (totF[k]-totI[k]) + ((totL[k+1]-totI[k+1]) if k+1<3 else 0) for k in range(3)]
    return totF,totL,totI,inj,cone
vals=[Fr(x) for x in (-3,-2,-1,0,1,2,3)]+[Fr(1,2),Fr(-1,2),Fr(1,3),Fr(-2,3),Fr(5,2)]
bad=0
for r1 in vals:
    for r2 in vals:
        if r1<r2: continue
        r=(r1,r2); res=(r1==1 or r2==1)
        sF,sL,sI,sinj,scone=analyse(r,'stalk')
        lF,lL,lI,linj,lcone=analyse(r,'loc')
        if not res:
            # stalk cone Q=[0,0,1] (degree 2); local-cohomology cone [1,0,0] (= H^2_p, i.e. RGamma_p(C_p[-2])); f_* injective
            if not (sinj and linj and scone==[0,0,1] and lcone==[1,0,0]): bad+=1; print("VIOLATION",r,sF,sL,scone,lF,lL,lcone,sinj,linj)
        if res or r in [(Fr(-3),Fr(-3)),(Fr(2),Fr(3)),(Fr(2),Fr(2)),(Fr(0),Fr(-2)),(Fr(1,2),Fr(-1,2)),(Fr(3),Fr(1,2)),(Fr(3),Fr(3))]:
            print("r=",(str(r1),str(r2)),"RESONANT" if res else "",
                  "| stalk FULL",sF,"LOG",sL,"coneQ",scone,"inj" if sinj else "NOT-inj",
                  "| locH(deg shifted by 2) FULL",lF,"LOG",lL,"coneQ",lcone,"inj" if linj else "NOT-inj")
print("non-resonant cases violating (Q=C_p[-2] and connecting map zero):",bad)
