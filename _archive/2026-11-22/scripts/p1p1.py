# Hypercohomology of (wedge^b T (x) O(m,m), d_sigma) on P^1 x P^1, sigma = Pi_F, F in V_{2,2} (bidegree (2,2) in x0,x1,y0,y1).
# Cone model: multivector fields on C^4 of bi-weight (m,m) modulo ideal (E_x, E_y); d = Schouten bracket with
#   Pi~ = sum c_ij d_{xi}^d_{yj},  c_ij = eps_ik eps_jl d_{xk}d_{yl} F   (represents 4 F d_x^d_y in the affine chart).
# Exact linear algebra mod P.  m>=-1: H^0 of all terms (E_1 in a=0).  m<=-4: H^2 (Laurent monomials, all exps<=-1).
# m=-2,-3 by hand (all E_1 terms in total degree 2).   Serre duality m <-> -m-4 used only as a cross-check.
import sys
sys.path.insert(0,'.')
from itertools import product
P=32003
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        nv=(r.get(k,0)+s*v)%P
        if nv: r[k]=nv
        else: r.pop(k,None)
    return r
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=(r.get(k,0)+v1*v2)%P
    return {k:v for k,v in r.items() if v}
def pd(p,i):
    r={}
    for k,v in p.items():
        if k[i]!=0:
            kk=list(k); kk[i]-=1; kk=tuple(kk); r[kk]=(r.get(kk,0)+v*k[i])%P
    return {k:v for k,v in r.items() if v}
def psc(p,c): return {k:(v*c)%P for k,v in p.items() if (v*c)%P}
def var(i):
    e=[0,0,0,0]; e[i]=1; return {tuple(e):1}
EPS={(0,1):1,(1,0):-1}
def rank(rows):
    piv={}; rk=0
    for r in rows:
        r=dict(r)
        while r:
            k=min(r)
            if k in piv:
                pr=piv[k]; c=r[k]*pow(pr[k],P-2,P)%P
                for kk,vv in pr.items():
                    nv=(r.get(kk,0)-c*vv)%P
                    if nv: r[kk]=nv
                    else: r.pop(kk,None)
            else:
                piv[k]=r; rk+=1; break
    return rk
def bimonos(p,q):  # monomials of bidegree (p,q), nonneg exps
    if p<0 or q<0: return []
    return [(a,p-a,b,q-b) for a in range(p+1) for b in range(q+1)]
def neg_bimonos(p,q): # all four exps <= -1, x-sum p, y-sum q
    out=[]
    if p>-2 or q>-2: return out
    for a in range(-1,p,-1):
        b=p-a
        if b>=0 or b>-1: continue
        for c in range(-1,q,-1):
            d=q-c
            if d>-1: continue
            out.append((a,b,c,d))
    return out
def setup(F):
    # c_ij = eps_ik eps_jl d_xk d_yl F ;  Pi[a][b], a,b in 0..3 (x0,x1,y0,y1)
    c=[[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    e=EPS.get((i,k),0)*EPS.get((j,l),0)
                    if e: c[i][j]=padd(c[i][j],psc(pd(pd(F,k),2+l),e%P))
    Pi=[[{} for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            Pi[i][2+j]=c[i][j]; Pi[2+j][i]=psc(c[i][j],P-1)
    return Pi
def mk(F):
    Pi=setup(F)
    def d0(s):
        v=[]
        for a in range(4):
            t={}
            for b in range(4): t=padd(t,pmul(Pi[a][b],pd(s,b)))
            v.append(t)
        return v
    def vap(X,p):
        t={}
        for k in range(4): t=padd(t,pmul(X[k],pd(p,k)))
        return t
    def d1(X): # L_X Pi
        B={}
        for a in range(4):
            for b in range(a+1,4):
                t=vap(X,Pi[a][b])
                for k in range(4):
                    t=padd(t,pmul(pd(X[a],k),Pi[k][b]),-1)
                    t=padd(t,pmul(pd(X[b],k),Pi[a][k]),-1)
                B[(a,b)]=t
        return B
    xs=[var(i) for i in range(4)]
    def S(B): # scalar: sum eps_ik eps_jl x_k y_l B_{i,2+j}
        sc={}
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        e=EPS.get((i,k),0)*EPS.get((j,l),0)
                        if e: sc=padd(sc,psc(pmul(pmul(xs[k],xs[2+l]),B[(i,2+j)]),e%P))
        return sc
    return Pi,d0,d1,S,xs
def flat(v): return {(c,)+k:val for c in range(len(v)) for k,val in v[c].items()}
def run_pos(F,m):
    Pi,d0,d1,S,xs=mk(F)
    V0=bimonos(m,m)
    comps=[bimonos(m+1,m),bimonos(m+1,m),bimonos(m,m+1),bimonos(m,m+1)]
    h0O=len(V0); h0K=len(bimonos(m+2,m+2)); h0T=len(bimonos(m+2,m))+len(bimonos(m,m+2))
    imgs=[d0({a:1}) for a in V0]
    def euler(s):  # E_x s, E_y s as vectors
        return [[pmul(xs[0],s),pmul(xs[1],s),{},{}],[{},{},pmul(xs[2],s),pmul(xs[3],s)]]
    Es=[]
    for a in V0: Es+=euler({a:1})
    rE=rank([flat(e) for e in Es])
    rfull=rank([flat(v) for v in imgs]+[flat(e) for e in Es])
    r0=rfull-rE
    rows=[]
    for c in range(4):
        for a in comps[c]:
            X=[{},{},{},{}]; X[c]={a:1}
            rows.append(S(d1(X)))
    r1=rank(rows)
    # checks
    ok_comp=all(not S(d1(v)) for v in imgs)
    ok_E=all(not S(d1(e)) for e in Es)
    dimT_check=sum(len(c) for c in comps)-rE
    assert dimT_check==h0T,(dimT_check,h0T)
    return dict(H=[h0O-r0,h0T-r0-r1,h0K-r1,0,0],d1d0=ok_comp,d1E=ok_E,r0=r0,r1=r1)
def proj(p): return {k:v for k,v in p.items() if all(e<0 for e in k)}
def run_neg(F,m):
    Pi,d0,d1,S,xs=mk(F)
    V0=neg_bimonos(m,m)
    comps=[neg_bimonos(m+1,m),neg_bimonos(m+1,m),neg_bimonos(m,m+1),neg_bimonos(m,m+1)]
    V2=neg_bimonos(m+2,m+2)
    def pj(v): return [proj(t) for t in v]
    imgs=[pj(d0({a:1})) for a in V0]
    Es=[]
    for a in V0:
        s={a:1}
        Es.append(pj([pmul(xs[0],s),pmul(xs[1],s),{},{}]))
        Es.append(pj([{},{},pmul(xs[2],s),pmul(xs[3],s)]))
    rE=rank([flat(e) for e in Es]); assert rE==2*len(V0)
    rfull=rank([flat(v) for v in imgs]+[flat(e) for e in Es])
    r0=rfull-rE
    dimT=sum(len(c) for c in comps)-rE
    rows=[]
    for c in range(4):
        for a in comps[c]:
            X=[{},{},{},{}]; X[c]={a:1}
            rows.append(proj(S(d1(X))))
    r1=rank(rows)
    # d1 must kill Euler images and d1 d0 = 0 (projected)
    ok_E=all(not proj(S(d1(e))) for e in Es)
    ok_c=all(not proj(S(d1(v))) for v in imgs)
    return dict(H=[0,0,len(V0)-r0,dimT-r1-r0,len(V2)-r1],dims=(len(V0),dimT,len(V2)),d1E=ok_E,d1d0=ok_c)
def hyper(F,m):
    if m>=-1: r=run_pos(F,m); assert r['d1d0'] and r['d1E'],(m,r); return r['H']
    if m in (-2,-3): return [0,0,4,0,0]
    r=run_neg(F,m); assert r['d1E'] and r['d1d0'],(m,r); return r['H']
def mkF(*terms): return {k:v%P for k,v in terms}
def prodpoly(*ps):
    r={(0,0,0,0):1}
    for p in ps: r=pmul(r,p)
    return r
X0,X1,Y0,Y1=var(0),var(1),var(2),var(3)
def lin(*cs): # linear form sum c_i var_i
    r={}
    for i,c in enumerate(cs):
        if c: r=padd(r,psc(var(i),c%P))
    return r
Fs={}
# smooth (2,2): x0^2y0^2+x1^2y1^2+x0x1y0y1*3 + (x0^2 y1^2 + x1^2 y0^2) ... generic-ish
def gen_smooth():
    import random
    random.seed(5)
    r={}
    for k in bimonos(2,2): r[k]=random.randrange(1,P)
    return r
Fs['smooth(random 2,2)']=gen_smooth()
Fs['two (1,1) conics, transverse']=prodpoly(padd(pmul(X0,Y0),pmul(X1,Y1),1),padd(pmul(X0,Y1),pmul(X1,Y0),1)) # x0y0+x1y1 , x0y1+x1y0
Fs['four lines x0x1y0y1']=prodpoly(X0,X1,Y0,Y1)
Fs['(1,1)+(1,0)+(0,1)']=prodpoly(padd(pmul(X0,Y0),pmul(X1,Y1),1),X0,Y1)
Fs['(1,1) tangent pair']=prodpoly(padd(pmul(X0,Y0),pmul(X1,Y1),1),padd(pmul(X0,Y0),pmul(X1,Y1),1)) # double conic (non-reduced)
Fs['sigma=0']={}
if __name__=="__main__":
    names=sys.argv[1:] or list(Fs)
    for name in names:
        F=Fs[name]; print("==",name)
        for m in range(-9,9):
            d=hyper(F,m)
            chi=sum((-1)**k*x for k,x in enumerate(d))
            print(m,d,"chi",chi, "" if chi==4 else "!!!")
            sys.stdout.flush()
