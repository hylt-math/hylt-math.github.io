# Exact polynomial identities (no residue trick) behind Prop 14 (HH duality in all dimensions).
#  (I)  G := <[σ,P]+V^P,Q> + (-1)^b <P,[σ,Q]+V'^Q>  with V' = -V - 2M  equals  -Σ_i ∂_i( Σ_j σ^{ij} u_j ),  T=P^Q=Σ(-1)^j u_j ∂_{hat j}
#  (II) [σ,T]_top = -Σ ∂_i(σ^{ij}u_j) + 2 M.u   (Lemma D)
#  (III) for a Poisson σ (σ = z1 z2 d1^d2 type, [σ,σ]=0): [σ,[σ,P]]=0 and [σ,M]=0 (modular field is Poisson), d^2=0 with V=M.
from duality_ndim import *
def Mvec(sigma,n):
    M={}
    for j in range(n):
        m={}
        for i in range(n):
            if i==j: continue
            key=(min(i,j),max(i,j)); sg=1 if i<j else -1
            m=padd(m,pd(sigma.get(key,{}),i),sg)
        if m: M[(j,)]=m
    return M
def Tcomp(T,n):  # u_j with T = sum (-1)^j u_j d_{hat j}
    u=[]
    for j in range(n):
        I=tuple(x for x in range(n) if x!=j)
        u.append(psc(T.get(I,{}),(-1)**j))
    return u
random.seed(7)
for n in (2,3,4):
    ok1=ok2=True
    for trial in range(4):
        for b in range(n):
            sigma=rmult(n,2,terms=2); V=rmult(n,1,terms=2); P=rmult(n,b,terms=1); Q=rmult(n,n-b-1,terms=1)
            M=Mvec(sigma,n)
            Vp=madd(msc(V,-1),msc(M,-2))
            dP=madd(schouten(sigma,2,P,b,n),wedge(V,P)); dQ=madd(schouten(sigma,2,Q,n-b-1,n),wedge(Vp,Q))
            G=padd(top(wedge(dP,Q),n),psc(top(wedge(P,dQ),n),(-1)**b))
            T=wedge(P,Q); u=Tcomp(T,n)
            S=lambda i,j: ({} if i==j else (sigma.get((i,j),{}) if i<j else psc(sigma.get((j,i),{}),-1)))
            div={}
            for i in range(n):
                for j in range(n): div=padd(div,pd(pmul(S(i,j),u[j]),i))
            ok1&= (padd(G,div)=={})
            # Lemma D
            MT=top(wedge(M,T),n)
            lhs=top(schouten(sigma,2,T,n-1,n),n)
            ok2&= (padd(lhs,padd(psc(div,-1),psc(MT,2)),-1)=={})
    print("n=",n,"(I) G=-div(σu):",ok1,"  (II) Lemma D:",ok2)
# (III): Poisson σ = z1 z2 d1^d2 (+ z3 z4 d3^d4 for n=4), Laurent monomial data
for n in (3,4):
    sigma={(0,1):{tuple([1,1]+[0]*(n-2)):Fr(1)}}
    if n==4: sigma[(2,3)]={(0,0,1,1):Fr(1)}
    M=Mvec(sigma,n)
    print("n=",n,"[σ,σ]=0:",schouten(sigma,2,sigma,2,n)=={}, " [σ,M]=0:",schouten(sigma,2,M,1,n)=={} if M else True)
    for b in range(0,n):
        P=rmult(n,b,terms=2)
        dP=madd(schouten(sigma,2,P,b,n),wedge(M,P))
        d2=madd(schouten(sigma,2,dP,b+1,n) if dP else {},wedge(M,dP) if dP else {})
        print("   b=",b,"d^2 P=0 (V=M):",d2=={})
