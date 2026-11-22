"""RELAXED formulation: only require a Poisson structure on P^{N-1} (not on C^N).  The quadratic bivector Pi~ on C^N is determined by the P^{N-1}-structure only
modulo E^v (v linear vector field), so we require
    Jacobiator(B0 + eps + E^v) in  E ^ (quadratic bivectors)    (psi unknown, eliminated by orthogonal projection),
with eps in Hom(L^2 S_1, I_2) and v in gl_N arbitrary (N^2 unknowns).  Real LM.  usage: relaxed.py m F nstarts"""
import numpy as np, sys, time, scipy.sparse as sp
from pkcore import *
m=int(sys.argv[1]); name=sys.argv[2]; ns=int(sys.argv[3])
F=FS[name] if name in FS else hesse(float(name))
S=Setup(m,F); N,K,T=S.N,S.K,S.T; tr=np.array(S.triples); nt=len(tr)
tid={t:i for i,t in enumerate(S.triples)}; pidx={pr:i for i,pr in enumerate(S.upairs)}
# U: psi_{bc,k} -> (E^psi)_{abc} = y_a psi_bc - y_b psi_ac + y_c psi_ab on triple a<b<c
rows=[];cols=[];vals=[]
for ti,(a,b,c) in enumerate(S.triples):
    for (y,(p,q),sg) in ((a,(b,c),1),(b,(a,c),-1),(c,(a,b),1)):
        for k in range(K):
            t=int(np.argmax(S.Pm[k,y,:]))
            rows.append(ti*T+t); cols.append(pidx[(p,q)]*K+k); vals.append(sg)
U=sp.csr_matrix((vals,(rows,cols)),shape=(nt*T,len(S.upairs)*K))
t0=time.time(); M=(U.T@U).toarray(); lam,V=np.linalg.eigh(M); pos=lam>1e-8*lam.max(); print("U rank",pos.sum(),"of",M.shape[0],"(%.0fs)"%(time.time()-t0),flush=True)
Q=(U@V[:,pos])/np.sqrt(lam[pos]); 
def proj(R): return R-Q@(Q.T@R)          # R: (nt*T,) or (nt*T,ncol)
# v directions: v = y_c d_b ; E^v : B[a,b'] += y_a v_b' - y_b' v_a
def Ev(V):   # V (N,N): v_b = sum_c V[b,c] y_c
    B=np.zeros((N,N,K))
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if V[b,c]==0: continue
                # + y_a*y_c in B[a,b]  and  - y_a*y_c in B[b,a]... (E^v)_{a b} = y_a v_b - y_b v_a
                k=S.pid[tuple(sorted((a,c)))]; B[a,b,k]+=V[b,c]; B[b,a,k]-=V[b,c]
    return B
Vdirs=[Ev(np.eye(N*N)[i].reshape(N,N)) for i in range(N*N)]
def fullB(x): 
    e=x[:S.nunk]; V=x[S.nunk:].reshape(N,N); return S.B0+S.eps_to_B(e)+Ev(V)
def res(x): return proj(S.resid(fullB(x)).ravel())
def jac(x):
    B=fullB(x); Je=S.jacobian(B)   # keep-coordinates only! need full coordinates: recompute below
    return None
def jacfull(B,dirs):
    GB=S.Gop(B); out=[]
    for i0 in range(0,len(dirs),20):
        d=np.array(dirs[i0:i0+20]); r=len(d); Gd=S.Gop(d)
        X1=(d.reshape(-1,K)@GB.transpose(1,0,2).reshape(K,N*T)).reshape(r,N,N,N,T).transpose(0,3,1,2,4)
        X2=(B.reshape(-1,K)@Gd.transpose(2,0,1,3).reshape(K,-1)).reshape(N,N,r,N,T).transpose(2,3,0,1,4)
        X=X1+X2; Y=X+np.transpose(X,(0,3,1,2,4))+np.transpose(X,(0,2,3,1,4))
        out.append(Y[:,tr[:,0],tr[:,1],tr[:,2]].reshape(r,-1).T)
    return np.concatenate(out,axis=1)
epsdirs=[]
for (a0,b0) in S.upairs:
    for r in range(S.nI):
        d=np.zeros((N,N,K)); d[a0,b0]=S.I2[r]; d[b0,a0]=-S.I2[r]; epsdirs.append(d)
alldirs=epsdirs+Vdirs
def jacobian(x):
    J=jacfull(fullB(x),alldirs); return proj(J)
def lm(x,iters=120):
    lam=1e-2; r=res(x); f=r@r
    for it in range(iters):
        J=jacobian(x); g=J.T@r; H=J.T@J
        while True:
            d=np.linalg.lstsq(H+lam*np.eye(len(x)),-g,rcond=None)[0]; r2=res(x+d); f2=r2@r2
            if f2<f: x,r,f=x+d,r2,f2; lam=max(lam/3,1e-15); break
            lam*=4
            if lam>1e12: return x,np.sqrt(f)
        if np.sqrt(f)<1e-11: break
    return x,np.sqrt(f)
n=S.nunk+N*N
print(f"RELAXED m={m} F={name}: unknowns eps {S.nunk} + v {N*N}; E^psi image rank {pos.sum()}",flush=True)
print("initial projected residual |P J0| =",np.linalg.norm(res(np.zeros(n))),flush=True)
for s in range(ns):
    rng=np.random.default_rng(500+s); x0=rng.normal(size=n)*10**rng.uniform(-1,1.3)
    t=time.time(); x,nr=lm(x0); print(f" start {s}: min projected |r| = {nr:.6e}, |eps|={np.linalg.norm(x[:S.nunk]):.3f}, |v|={np.linalg.norm(x[S.nunk:]):.3f} ({time.time()-t:.0f}s)",flush=True)
