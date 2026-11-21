# Round C: full (all H^a) weight-graded Cech computation of generalized Dolbeault hypercohomology for toric log-symplectic surfaces
# (and the log subcomplex C(B;L)=DR_log), for arbitrary L=O(sum a_i D_i), arbitrary rho (arbitrary residues r_i=<rho,u_i>-a_i).
# Model (same as toric_hh.py / ncd_theorem.md Lemma 3): weight chi in M; sections over U_tau of weight chi:
#   A-complex: G^b = {w in wedge^b N: u_i ^ w = 0 for i in tau with c_i=-1}, zero if some i in tau has c_i<-1 ; c_i = <chi,u_i>+a_i
#   B-complex (log): G^b = wedge^b N if all i in tau have c_i>=0 else 0.
# d = v ^ , v = A(chi+rho).  Total complex = Cech (over maximal cones, intersections = common rays) x d.
import sys, itertools
sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
from math import comb

FANS={
 'P2':([(1,0),(0,1),(-1,-1)],[(0,1),(1,2),(2,0)]),
 'P1xP1':([(1,0),(-1,0),(0,1),(0,-1)],[(0,2),(0,3),(1,2),(1,3)]),
}
def cech_poly(rays,cones,a,A,rho,box,kind='A'):
    n=len(rays[0]); rhoP=[modfrac(x) for x in rho]
    nc=len(cones); tot=[0]*(len(cones)+n+2)
    tuples=[[t for t in itertools.combinations(range(nc),p+1)] for p in range(nc)]
    for chi in itertools.product(range(-box,box+1),repeat=n):
        c=[sum(x*y for x,y in zip(chi,u))+ai for u,ai in zip(rays,a)]
        v=[(sum(A[i][j]*((chi[j]%P)+rhoP[j]) for j in range(n)))%P for i in range(n)]
        # per tuple: ray set
        def raysof(t):
            s=set(cones[t[0]])
            for q in t[1:]: s&=set(cones[q])
            return s
        # basis of G^b for each (tuple,b)
        data={}  # (p,ti,b)-> (basis list)
        for p in range(nc):
            for ti,t in enumerate(tuples[p]):
                R=raysof(t)
                if kind=='A':
                    bad=any(c[i]<-1 for i in R); cons=[rays[i] for i in R if c[i]==-1]
                else:
                    bad=any(c[i]<0 for i in R); cons=[]
                for b in range(n+1):
                    dimb=comb(n,b)
                    if bad: data[(p,ti,b)]=[]; continue
                    rows=[]
                    for u in cons:
                        if b<n: rows+=wedge_matrix([x%P for x in u],n,b)
                    data[(p,ti,b)]=nullspace(rows,dimb)
        # total degree k=p+b ; ambient coordinates index
        amb={}  # (k)-> dict (p,ti,b)->offset
        ambdim={}
        for k in range(nc+n):
            off=0; amb[k]={}
            for p in range(nc):
                b=k-p
                if b<0 or b>n: continue
                for ti in range(len(tuples[p])):
                    amb[k][(p,ti,b)]=off; off+=comb(n,b)
            ambdim[k]=off
        dimK={k:sum(len(data[key]) for key in amb[k]) for k in amb}
        ranks={}
        for k in range(nc+n-1):
            imgs=[]
            tgtamb=amb[k+1]
            for (p,ti,b),off in amb[k].items():
                t=tuples[p][ti]
                for w in data[(p,ti,b)]:
                    vec=[0]*ambdim[k+1]
                    # d part: (-1)^p v^w in (p,ti,b+1)
                    if b<n:
                        Mw=wedge_matrix(v,n,b); dw=matvec(Mw,w); o=tgtamb[(p,ti,b+1)]
                        for i,x in enumerate(dw): vec[o+i]=(vec[o+i]+(-1)**p*x)%P
                    # Cech part: x in tuple t -> add to tuples t' of length p+2 containing t as sub-tuple omitting position j
                    if p+1<nc:
                        for ti2,t2 in enumerate(tuples[p+1]):
                            for j in range(len(t2)):
                                if t2[:j]+t2[j+1:]==t:
                                    o=tgtamb[(p+1,ti2,b)]
                                    for i,x in enumerate(w): vec[o+i]=(vec[o+i]+(-1)**j*x)%P
                    imgs.append(vec)
            ranks[k]=rank(imgs,ambdim[k+1]) if imgs else 0
        for k in dimK:
            h=dimK[k]-ranks.get(k,0)-ranks.get(k-1,0)
            tot[k]+=h
    return tot
def Pstr(p):
    while p and p[-1]==0: p=p[:-1]
    return p
if __name__=="__main__":
    A=[[0,1],[P-1,0]]
    # sanity vs earlier tables: P2 triangle, symmetric residues r=-m/3 -> rho=(r,r)
    for m in [-4,-3,-2,0,1,3,6]:
        r=Fr(-m,3)
        rays,cones=FANS['P2']; a=[0,0,m]
        print("P2 triangle m",m,"A-complex",Pstr(cech_poly(rays,cones,a,A,[r,r],box=abs(m)+4,kind='A')),
              "B-complex",Pstr(cech_poly(rays,cones,a,A,[r,r],box=abs(m)+4,kind='B')))
