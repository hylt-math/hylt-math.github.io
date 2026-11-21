"""Round E: does the Poisson structure sigma=Pi_F on P^2 extend to a quadratic Poisson structure on P^N
under the Veronese embedding by O(m)?  Modular arithmetic mod p.  Usage: python3 roundE_veronese_poisson.py m Fname
Steps: (1) lift bracket {y_a,y_b}=Q_ab (quadratic) using a linear section R_2 -> S_2 (almost-Poisson biderivation on S=Sym(R_1));
(2) compute Jacobiator J0; (3) correction eps in Hom(Lambda^2 S_1, I_2): solve J0 + L(eps) + J(eps) = 0
   - linear part by linear algebra; report solvability of the linear part; then test the quadratic equation."""
import sys, itertools, random
p = 32003
def inv(a): return pow(a % p, p-2, p)

# polynomials in x0,x1,x2 as dict {(e0,e1,e2):coef}
def padd(a,b,c=1):
    r=dict(a)
    for k,v in b.items():
        r[k]=(r.get(k,0)+c*v)%p
        if r[k]==0: del r[k]
    return r
def pmul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=tuple(x+y for x,y in zip(k1,k2)); r[k]=(r.get(k,0)+v1*v2)%p
    return {k:v for k,v in r.items() if v}
def pdiff(a,i):
    r={}
    for k,v in a.items():
        if k[i]>0:
            kk=list(k); kk[i]-=1; r[tuple(kk)]=(r.get(tuple(kk),0)+v*k[i])%p
    return {k:v for k,v in r.items() if v}

FS = {
 'fermat': {(3,0,0):1,(0,3,0):1,(0,0,3):1},
 'xyz': {(1,1,1):1},
 'hesse': {(3,0,0):1,(0,3,0):1,(0,0,3):1,(1,1,1):(-3*7)%p},   # x^3+y^3+z^3-21xyz (generic-ish member)
 'cusp': {(3,0,0):1,(0,2,1):p-1},        # y^2 z - x^3 type
}
def run(m, fname):
    F = FS[fname]
    dF = [pdiff(F,i) for i in range(3)]
    # {x_i,x_j} = eps_ijk d_k F
    xb = {}
    for (i,j,k,s) in [(0,1,2,1),(1,2,0,1),(2,0,1,1)]:
        xb[(i,j)] = {kk:(s*v)%p for kk,v in dF[k].items()}
        xb[(j,i)] = {kk:(-s*v)%p for kk,v in dF[k].items()}
    for i in range(3): xb[(i,i)]={}
    mons = [(a,b,m-a-b) for a in range(m,-1,-1) for b in range(m-a,-1,-1)]
    n1=len(mons); idx={mm:i for i,mm in enumerate(mons)}
    mons2 = [(a,b,2*m-a-b) for a in range(2*m,-1,-1) for b in range(2*m-a,-1,-1)]
    # section R_2 -> S_2: for each degree-2m monomial choose a split
    split={}
    for mu in mons2:
        done=False
        for g in mons:
            d=tuple(mu[i]-g[i] for i in range(3))
            if min(d)>=0 and sum(d)==m:
                split[mu]=tuple(sorted((idx[g],idx[d]))); done=True;break
        assert done
    # P_ab(x) = {x^a,x^b}
    def bracket_mon(a,b):
        ma={a:1}; mb={b:1}
        res={}
        for i in range(3):
            da=pdiff(ma,i)
            if not da: continue
            for j in range(3):
                db=pdiff(mb,j)
                if not db: continue
                res=padd(res,pmul(pmul(da,db),xb[(i,j)]))
        return res
    # quadratic polynomials in y: dict {(i,j) sorted: coef}
    def lift(P):
        r={}
        for mu,v in P.items():
            k=split[mu]; r[k]=(r.get(k,0)+v)%p
        return {k:v for k,v in r.items() if v}
    Q0={}
    for a in range(n1):
        for b in range(n1):
            Q0[(a,b)] = lift(bracket_mon(mons[a],mons[b])) if a!=b else {}
    # antisymmetry check
    for a in range(n1):
        for b in range(a+1,n1):
            s=padd(Q0[(a,b)],Q0[(b,a)])
            assert not s
    # polynomials in y: dict {sorted tuple: coef}
    def yadd(a,b,c=1):
        r=dict(a)
        for k,v in b.items():
            r[k]=(r.get(k,0)+c*v)%p
            if r[k]==0: del r[k]
        return r
    def ylin_mul(i,poly): # y_i * poly
        r={}
        for k,v in poly.items():
            kk=tuple(sorted(k+(i,))); r[kk]=(r.get(kk,0)+v)%p
        return r
    def br_gen_poly(B, a, poly):
        """{y_a, poly}_B via Leibniz; B: dict (a,b)->quadratic poly"""
        r={}
        for k,v in poly.items():
            # derivative of monomial prod y_{k_t}: sum_t {y_a,y_{k_t}} * prod others
            for t in range(len(k)):
                others=k[:t]+k[t+1:]
                bb=B.get((a,k[t]),{})
                if not bb: continue
                term={}
                for kk,vv in bb.items():
                    key=tuple(sorted(kk+others)); term[key]=(term.get(key,0)+vv*v)%p
                r=yadd(r,term)
        return r
    def jacobiator(B):
        J={}
        for (a,b,c) in itertools.combinations(range(n1),3):
            tot={}
            for (u,v,w) in [(a,b,c),(b,c,a),(c,a,b)]:
                tot=yadd(tot,br_gen_poly(B,u,B.get((v,w),{})))
            if tot: J[(a,b,c)]=tot
        return J
    J0=jacobiator(Q0)
    nz=sum(len(v) for v in J0.values())
    print(f"m={m} F={fname}: N+1={n1}, nonzero Jacobiator triples={len(J0)}, total terms={nz}")
    return Q0,J0,n1,mons,idx,jacobiator,yadd,br_gen_poly,ylin_mul

if __name__=="__main__":
    m=int(sys.argv[1]); fn=sys.argv[2]
    run(m,fn)
