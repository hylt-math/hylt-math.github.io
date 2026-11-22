# Mini exterior calculus with exact rational polynomial coefficients (no sympy available)
from fractions import Fraction as Fr
import itertools, math
N=3
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,0)+s*v
        if r[k]==0: del r[k]
    return r
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
            if r[k]==0: del r[k]
    return r
def pd(p,i):
    r={}
    for k,v in p.items():
        if k[i]>0:
            kk=list(k);kk[i]-=1;r[tuple(kk)]=v*k[i]
    return r
def const(c): return {(0,)*N:Fr(c)} if c!=0 else {}
def var(i):
    k=[0]*N;k[i]=1;return {tuple(k):Fr(1)}
def pscale(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
# forms: dict idxtuple(sorted)->poly
def fadd(a,b,s=1):
    r=dict(a)
    for k,v in b.items():
        r[k]=padd(r.get(k,{}),v,s)
        if not r[k]: del r[k]
    return r
def sortsign(idx):
    idx=list(idx);s=1
    if len(set(idx))<len(idx): return 0,None
    for i in range(len(idx)):
        for j in range(len(idx)-1-i):
            if idx[j]>idx[j+1]: idx[j],idx[j+1]=idx[j+1],idx[j]; s=-s
    return s,tuple(idx)
def wedge(a,b):
    r={}
    for k1,p1 in a.items():
        for k2,p2 in b.items():
            s,k=sortsign(k1+k2)
            if s==0: continue
            r=fadd(r,{k:pscale(pmul(p1,p2),s)})
    return r
def d(a):
    r={}
    for k,p in a.items():
        for i in range(N):
            dp=pd(p,i)
            if dp:
                s,kk=sortsign((i,)+k)
                if s: r=fadd(r,{kk:pscale(dp,s)})
    return r
def interior(X,a): # X list of polys
    r={}
    for k,p in a.items():
        for pos,i in enumerate(k):
            kk=k[:pos]+k[pos+1:]
            r=fadd(r,{kk:pscale(pmul(X[i],p),(-1)**pos)})
    return r
def lie_coord(X,a):
    # (L_X w) = sum over: X(w_I) dx^I + w_I * d(X^{i}) ...  = d i_X w + i_X d w is Cartan; here use independent formula:
    # L_X(f dx^{i1}^...^dx^{ik}) = X(f) dx^I + f sum_m dx^{i1}..d(X^{im})..dx^{ik}
    r={}
    for k,p in a.items():
        Xf={}
        for j in range(N): Xf=padd(Xf,pmul(X[j],pd(p,j)))
        r=fadd(r,{k:Xf} if Xf else {})
        for m,i in enumerate(k):
            dXi={(j,):pd(X[i],j) for j in range(N) if pd(X[i],j)}
            # replace dx^i by dX^i
            for kk,q in dXi.items():
                new=wedge(wedge({k[:m] and k[:m] or ():const(1)} if False else {tuple(k[:m]):const(1)} if m>0 else {():const(1)}, {kk:q}), {tuple(k[m+1:]):const(1)} if m<len(k)-1 else {():const(1)})
                r=fadd(r,wedge({():p},new))
    return r
def show(a): return {k:dict(v) for k,v in a.items()}
x,y,z=var(0),var(1),var(2)
one={():const(1)}
def f1(*terms): # terms (poly, idx)
    r={}
    for p,i in terms: r=fadd(r,{i:p})
    return r
dx={(0,):const(1)};dy={(1,):const(1)};dz={(2,):const(1)}
def P(*fs):
    r=const(1)
    for f in fs: r=pmul(r,f)
    return r
def pr(a): 
    return {k:{e:str(c) for e,c in v.items()} for k,v in a.items()}
if __name__=="__main__":
    # 11
    al=f1((P(x,x,y),(0,)),(z,(1,)),(P(x,y),(2,)))
    print("d alpha",pr(d(al)), "d d",d(d(al)))
    be=f1((P(x,z),(1,2)),(pscale(P(y,y),-1),(0,2)),(x,(0,1)))  # y^2 dz^dx = -y^2 dx^dz
    print("d beta",pr(d(be)))
    # 13 Cartan
    X=[pmul(const(-1),y),x,{}]
    w=f1((x,(1,)))
    L=lie_coord(X,w); C=fadd(d(interior(X,w)),interior(X,d(w)))
    print("Cartan 1form L",pr(L),"C",pr(C), L==C)
    # random 2-form Cartan test
    w2=f1((P(x,y),(0,1)),(P(z,z),(1,2)),(P(x,z,y),(0,2)))
    X2=[P(y,z),pmul(x,x),padd(x,z)]
    print("Cartan 2form",lie_coord(X2,w2)==fadd(d(interior(X2,w2)),interior(X2,d(w2))))
    w1=f1((P(x,y),(0,)),(P(z,z),(1,)),(P(x,z,y),(2,)))
    print("Cartan 1form gen",lie_coord(X2,w1)==fadd(d(interior(X2,w1)),interior(X2,d(w1))))
    # invariant formula for d alpha(X,Y)
    def ev1(a,V):
        r={}
        for k,p in a.items(): r=padd(r,pmul(p,V[k[0]]))
        return r
    def vf(X,f): 
        r={}
        for j in range(N): r=padd(r,pmul(X[j],pd(f,j)))
        return r
    def br(X,Y): return [padd(vf(X,Y[i]),vf(Y,X[i]),-1) for i in range(N)]
    Y2=[P(x,x),P(y,z),const(1)]
    dal=d(w1)
    lhs={}
    for k,p in dal.items():
        i,j=k
        lhs=padd(lhs,pmul(p,padd(pmul(X2[i],Y2[j]),pmul(X2[j],Y2[i]),-1)))
    rhs=padd(padd(vf(X2,ev1(w1,Y2)),vf(Y2,ev1(w1,X2)),-1),ev1(w1,br(X2,Y2)),-1)
    print("invariant formula", lhs==rhs)
    # 6,7 brackets
    Eul=[x,y,{}];Rot=[pscale(y,-1),x,{}]
    print("[Euler,Rot]",br(Eul,Rot))
    L1=[{},pscale(z,-1),y]; # y d_z - z d_y -> components (x,y,z)=(0,-z,y)
    L2=[z,{},pscale(x,-1)]; L3=[pscale(y,-1),x,{}]
    print("[L1,L2]+L3=0:",[padd(a,b) for a,b in zip(br(L1,L2),L3)])
    print("[L2,L3]+L1=0:",[padd(a,b) for a,b in zip(br(L2,L3),L1)])
    print("[L3,L1]+L2=0:",[padd(a,b) for a,b in zip(br(L3,L1),L2)])
    print("[dx,x^2 dy]",br([const(1),{},{}],[{},P(x,x),{}]))
    Xc=[const(1),{},y];Yc=[{},const(1),{}]
    print("contact [X,Y]",br(Xc,Yc))
    # 15 sphere omega
    om=f1((x,(1,2)),(y,(0,2)),(z,(0,1)))
    # careful: y dz^dx = -y dx^dz
    om=f1((x,(1,2)),(pscale(y,-1),(0,2)),(z,(0,1)))
    print("d omega",pr(d(om)))
    # 17 homotopy: primitive
    a17=f1((y,(0,)),(x,(1,)),(pscale(z,2),(2,)))
    print("closed a17",d(a17)=={}, " d(xy+z^2) = ", pr(d({():padd(P(x,y),P(z,z))})), "==a17?", d({():padd(P(x,y),P(z,z))})==a17)
