"""Core tensors for the Poisson-Kodaira test: (P^2, Pi_F) -> Veronese |O(m)| in P^{N-1}.
Unknown: epsilon in Hom(Lambda^2 S_1, I_2); equation: Jacobiator(B0+eps)=0 in S_3 (cubics in y).
B[a,b,k]: coefficient of quadratic monomial k=(c<=d) in {y_a,y_b}.
All arithmetic either float64 (modulus=None) or exact mod p (float64 holding ints < 2^53; p <= ~2^20 keeps all sums exact)."""
import numpy as np, itertools
from math import comb

def monos(d): return [(a,b,d-a-b) for a in range(d,-1,-1) for b in range(d-a,-1,-1)]
def padd(a,b,c=1):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,0)+c*v
        if r[k]==0: del r[k]
    return r
def pmul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=tuple(x+y for x,y in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v}
def pdiff(a,i):
    r={}
    for k,v in a.items():
        if k[i]>0:
            kk=list(k); kk[i]-=1; kk=tuple(kk); r[kk]=r.get(kk,0)+v*k[i]
    return {k:v for k,v in r.items() if v}

class Setup:
    def __init__(self,m,F):
        self.m=m; self.F=F
        self.mons=monos(m); self.N=N=len(self.mons); idx={mm:i for i,mm in enumerate(self.mons)}
        self.pairs=[(c,d) for c in range(N) for d in range(c,N)]; self.K=K=len(self.pairs)   # quadratic y-monomials
        self.pid={pr:i for i,pr in enumerate(self.pairs)}
        self.trip=[t for t in itertools.combinations_with_replacement(range(N),3)]; self.T=T=len(self.trip)
        self.tid={t:i for i,t in enumerate(self.trip)}
        # mulq one-hot: Pmul[k,f,t]=1 iff pair_k * y_f = trip_t
        Pm=np.zeros((K,N,T))
        for k,(c,d) in enumerate(self.pairs):
            for f in range(N): Pm[k,f,self.tid[tuple(sorted((c,d,f)))]]=1
        self.Pm=Pm
        self.E=np.array([c for c,d in self.pairs]); self.Fi=np.array([d for c,d in self.pairs])
        # classes: y-monomial -> x-monomial of degree 2m (quadratic) / 3m (cubic)
        def xdeg(idxs): return tuple(sum(self.mons[i][j] for i in idxs) for j in range(3))
        self.qclass=[xdeg(pr) for pr in self.pairs]; self.tclass=[xdeg(t) for t in self.trip]
        # I_2 basis: for each class with >1 monomials, q_j = y_{p0} - y_{pj}
        byc={}
        for k,c in enumerate(self.qclass): byc.setdefault(c,[]).append(k)
        self.byc=byc; I2=[]
        for c,ks in byc.items():
            for k in ks[1:]:
                v=np.zeros(K); v[ks[0]]=1; v[k]=-1; I2.append(v)
        self.I2=np.array(I2); self.nI=len(I2)        # (nI,K)
        self.upairs=list(itertools.combinations(range(N),2)); self.nunk=len(self.upairs)*self.nI
        self.triples=list(itertools.combinations(range(N),3))
        # cubic classes: keep all but one rep per class as residual coordinates
        byt={}
        for t,c in enumerate(self.tclass): byt.setdefault(c,[]).append(t)
        self.byt=byt; self.keep=np.array(sorted(t for ts in byt.values() for t in ts[1:])); self.nkeep=len(self.keep)
        self.drop=np.array(sorted(ts[0] for ts in byt.values()))
        # Q0: lift of {x^a,x^b}
        dF=[pdiff(F,i) for i in range(3)]
        xb={}
        for (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)]:
            xb[(i,j)]=dF[k]; xb[(j,i)]={kk:-v for kk,v in dF[k].items()}
        split={}
        for mu in monos(2*m):
            for g in self.mons:
                d=tuple(mu[i]-g[i] for i in range(3))
                if min(d)>=0:
                    split[mu]=self.pid[tuple(sorted((idx[g],idx[d])))]; break
        B0=np.zeros((N,N,K))
        for a in range(N):
            for b in range(a+1,N):
                res={}
                for i in range(3):
                    da=pdiff({self.mons[a]:1},i)
                    if not da: continue
                    for j in range(3):
                        db=pdiff({self.mons[b]:1},j)
                        if db and (i,j) in xb: res=padd(res,pmul(pmul(da,db),xb[(i,j)]))
                for mu,v in res.items(): B0[a,b,split[mu]]+=v; B0[b,a,split[mu]]-=v
        self.B0=B0
    # ---- operators
    def eps_to_B(self,e):
        """e: vector length nunk -> antisymmetric tensor (N,N,K)"""
        N,K=self.N,self.K; B=np.zeros((N,N,K),dtype=np.result_type(e.dtype,float)); E=e.reshape(len(self.upairs),self.nI)@self.I2
        for u,(a,b) in enumerate(self.upairs): B[a,b]=E[u]; B[b,a]=-E[u]
        return B
    def Gop(self,B):
        """G[...,a,k,t] = coeff of cubic monomial t in {y_a, m_k}, B may have leading batch dim"""
        if not hasattr(self,'_Pe'):
            self._Pe=np.ascontiguousarray(np.transpose(self.Pm[:,self.Fi,:],(1,0,2)))  # (k,p,t)
            self._Pf=np.ascontiguousarray(np.transpose(self.Pm[:,self.E,:],(1,0,2)))
        def one(Bs,P):   # Bs (...,a,k,p) -> (...,a,k,t)
            lead=Bs.shape[:-2]; Bt=np.moveaxis(Bs.reshape(-1,Bs.shape[-2],Bs.shape[-1]),1,0)  # (k, M, p)
            out=np.matmul(Bt,P)    # (k,M,t)
            return np.moveaxis(out,0,1).reshape(lead+(self._Pe.shape[0],self._Pe.shape[2]))
        return one(B[...,:,self.E,:],self._Pe)+one(B[...,:,self.Fi,:],self._Pf)
    def jac_full(self,B1,B2,G2=None,mod=None):
        """bilinear-type term X[...,a,b,c,t]=sum_k B1[b,c,k] G(B2)[a,k,t], cyc-summed, gathered at triples a<b<c"""
        raise NotImplementedError
    def Jac(self,B,mod=None):
        G=self.Gop(B)
        X=(B.reshape(-1,self.K)@G.transpose(1,0,2).reshape(self.K,-1)).reshape(self.N,self.N,self.N,self.T).transpose(2,0,1,3)
        Y=X+X.transpose(1,2,0,3)+X.transpose(2,0,1,3) if False else None
        # Y[a,b,c]=X[a,b,c]+X[b,c,a]+X[c,a,b]
        Y=X+np.transpose(X,(2,0,1,3))+np.transpose(X,(1,2,0,3))
        if mod: Y=np.mod(Y,mod)
        return Y
    def resid(self,B,mod=None):
        Y=self.Jac(B,mod)
        t=np.array(self.triples)
        R=Y[t[:,0],t[:,1],t[:,2]]   # (ntrip,T)
        return R
    def classcheck(self,R):
        """sum over class of coefficients must vanish if I is Poisson ideal (R in I_3)"""
        return max(abs(R[:,ts].sum(axis=1)).max() for ts in self.byt.values())
    def jacobian(self,B,mod=None,chunk=None,mask=None):
        """Matrix d resid / d eps at base B: rows = ntrip*nkeep, cols=nunk. Exact if mod given."""
        N,K,T=self.N,self.K,self.T; GB=self.Gop(B); tr=np.array(self.triples)
        cols=np.zeros((len(self.triples)*self.nkeep,self.nunk if mask is None else int(mask.sum())),dtype=B.dtype)
        off=0
        for u,(a0,b0) in enumerate(self.upairs):
            rs=np.arange(self.nI) if mask is None else np.nonzero(mask[u*self.nI:(u+1)*self.nI])[0]
            if len(rs)==0: continue
            nr_=len(rs); I2u=self.I2[rs]
            d=np.zeros((nr_,N,N,K)); d[:,a0,b0,:]=I2u; d[:,b0,a0,:]=-I2u
            Gd=self.Gop(d)
            GBf=GB.transpose(1,0,2).reshape(K,N*T)                       # (k, a t)
            X1=(d.reshape(-1,K)@GBf).reshape(nr_,N,N,N,T)            # r b c a t
            X1=X1.transpose(0,3,1,2,4)                                    # r a b c t
            Gdf=Gd.transpose(2,0,1,3).reshape(K,-1)                       # (k, r a t)
            X2=(B.reshape(-1,K)@Gdf).reshape(N,N,nr_,N,T).transpose(2,3,0,1,4)  # r a b c t
            X=X1+X2
            Y=X+np.transpose(X,(0,3,1,2,4))+np.transpose(X,(0,2,3,1,4))
            if mod: Y=np.mod(Y,mod)
            R=Y[:,tr[:,0],tr[:,1],tr[:,2]][:,:,self.keep]    # (nI,ntrip,nkeep)
            if mask is None: cols[:,u*self.nI:(u+1)*self.nI]=R.reshape(nr_,-1).T
            else: cols[:,off:off+nr_]=R.reshape(nr_,-1).T; off+=nr_
        return cols
    def quad_apply(self,e,mod=None):
        """J(eps) quadratic part (resid of eps-only tensor)"""
        return self.resid(self.eps_to_B(e),mod)

FS={'fermat':{(3,0,0):1,(0,3,0):1,(0,0,3):1},
    'xyz':{(1,1,1):1},
    'cusp':{(3,0,0):1,(0,2,1):-1},
    'x3':{(3,0,0):1},
    'nodal':{(0,2,1):1,(3,0,0):-1,(2,0,1):-1},
    'conicsecant':{(1,1,1):1,(3,0,0):-1}}
def hesse(lam): return {(3,0,0):1,(0,3,0):1,(0,0,3):1,(1,1,1):lam}
