# P1xP1: twisted Lichnerowicz complex  d A = D A - (m/2) Z ^ A,  D = [Pi~, .],  Z = Pi~^#(dF)/F (mod Euler),
# which equals F^{m/2} D (F^{-m/2} A): the unique flat log module on O(m,m) with residue -m/2 along every component of D.
import sys, random
sys.path.insert(0,'.')
import p1p1 as Q
from p1p1 import *
inv2=pow(2,P-2,P)
def solve_lin(rows, rhs, nunk):
    # rows: list of dict {unk:coef}; rhs list; Gaussian elimination mod P; returns solution (free vars=0) or None
    A=[dict(r) for r in rows]; b=list(rhs)
    piv={}  # col -> (row dict, rhs)
    for r,bb in zip(A,b):
        r=dict(r)
        while r:
            k=min(r)
            if k in piv:
                pr,pb=piv[k]; c=r[k]*pow(pr[k],P-2,P)%P
                for kk,vv in pr.items():
                    nv=(r.get(kk,0)-c*vv)%P
                    if nv: r[kk]=nv
                    else: r.pop(kk,None)
                bb=(bb-c*pb)%P
            else:
                piv[k]=(r,bb); break
        else:
            if bb%P: return None
    sol=[0]*nunk
    for k in sorted(piv,reverse=True):
        r,bb=piv[k]
        s=bb
        for kk,vv in r.items():
            if kk!=k: s=(s-vv*sol[kk])%P
        sol[k]=s*pow(r[k],P-2,P)%P
    return sol
def Zfield(F):
    """find Z (vector with linear coeffs) with Pi~^#(dF) = F*Z + E_x*alpha + E_y*beta."""
    Pi=setup(F)
    V=[]
    for a in range(4):
        t={}
        for b in range(4): t=padd(t,pmul(Pi[a][b],pd(F,b)))
        V.append(t)
    # unknowns: Z comps: x comps (bidegree (1,0)): 2 each; y comps (0,1): 2 each; alpha,beta in V_{2,2}: 9 each
    unk=[]  # (kind, idx, mono)
    for a in range(2):
        for mo in bimonos(1,0): unk.append(('Z',a,mo))
    for a in range(2,4):
        for mo in bimonos(0,1): unk.append(('Z',a,mo))
    for mo in bimonos(2,2): unk.append(('al',0,mo))
    for mo in bimonos(2,2): unk.append(('be',0,mo))
    idx={u:i for i,u in enumerate(unk)}
    xs=[var(i) for i in range(4)]
    # equations: for each comp a and each monomial: V[a][mono] = sum over unknown contributions
    eqs={}  # (a,mono) -> {unk:coef}
    def add(a,mono,u,c):
        eqs.setdefault((a,mono),{})
        eqs[(a,mono)][idx[u]]=(eqs[(a,mono)].get(idx[u],0)+c)%P
    for a in range(4):
        for mo in (bimonos(1,0) if a<2 else bimonos(0,1)):
            for k,v in F.items():
                add(a,tuple(x+y for x,y in zip(k,mo)),('Z',a,mo),v)
    for mo in bimonos(2,2):
        for a in range(2): add(a,tuple(x+y for x,y in zip(xs[a].__iter__().__next__(),mo)),('al',0,mo),1)
        for a in range(2,4): add(a,tuple(x+y for x,y in zip(next(iter(xs[a])),mo)),('be',0,mo),1)
    keys=set(eqs)|{(a,k) for a in range(4) for k in V[a]}
    rows=[];rhs=[]
    for key in keys:
        rows.append(eqs.get(key,{})); rhs.append(V[key[0]].get(key[1],0))
    sol=solve_lin(rows,rhs,len(unk))
    if sol is None: return None
    Z=[{} for _ in range(4)]
    for u,i in idx.items():
        if u[0]=='Z' and sol[i]: Z[u[1]][u[2]]=sol[i]
    return Z
def kappa_test(F):
    Pi,d0,d1,S,xs=mk(F)
    random.seed(1)
    def rp(deg_choices):
        r={}
        for k in deg_choices: r[k]=random.randrange(1,P)
        return r
    f=rp(bimonos(1,1)); X=[rp(bimonos(2,1)) for _ in range(4)]
    Vf=[]
    for a in range(4):
        t={}
        for b in range(4): t=padd(t,pmul(Pi[a][b],pd(f,b)))
        Vf.append(t)
    fX=[pmul(f,x) for x in X]
    L1=d1(fX); L2=d1(X)
    res={}
    for kap in (1,-1):
        ok=True
        for (a,b),v in L1.items():
            rhs=padd(padd(pmul(Vf[a],X[b]),pmul(Vf[b],X[a]),-1), psc(pmul(f,L2[(a,b)]),kap%P))
            if psc(v,kap%P)!=rhs: ok=False
        res[kap]=ok
    return res
if __name__=="__main__":
    F=Fs['smooth(random 2,2)']
    print("kappa test",kappa_test(F))
    Z=Zfield(F); print("Z",Z)
