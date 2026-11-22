from lib import *
def binom_gen(n,k): # C(n+k,n) generalised
    r=F(1)
    for i in range(1,n+1): r*=F(k+i,i)
    return r
# A. Hirzebruch uniqueness [x^n]Q^{n+1}=1
for n in range(0,13):
    Q=stodd(n); c=spow(Q,n+1,n)[n]
    assert c==1,(n,c)
print("A ok: [x^n] Q^{n+1} = 1, n<=12")
# B. chi(P^n,O(k))
for n in range(1,9):
    Q=stodd(n); td=spow(Q,n+1,n)
    for k in range(-15,16):
        v=smul(sexp(k,n),td,n)[n]
        assert v==binom_gen(n,k),(n,k)
print("B ok: int e^{kH} Td(P^n) = C(n+k,n), n<=8, |k|<=15")
# D. complete intersections
def ci(nam, degs, n):  # X subset P^{nam}, codim len(degs), dim n=nam-len(degs); returns c_i in H (list) and deg
    num=spow([F(1),F(1)]+[F(0)]*n,nam+1,n)
    den=[F(1)]
    for d in degs: den=smul(den+[F(0)]*(n+1-len(den)), [F(1),F(d)]+[F(0)]*(n-1),n)
    den=den[:n+1]+[F(0)]*(n+1-len(den))
    c=smul(num,sinv(den,n),n)
    deg=1
    for d in degs: deg*=d
    return c,deg
def chi_top_dim_n(c,deg,n): return c[n]*deg
for d in range(1,8):
    c,deg=ci(3,[d],2)
    c1sq=c[1]**2*deg; c2=c[2]*deg
    chiO=(c1sq+c2)/12; tau=(c1sq-2*c2)/3
    pg=comb(d-1,3); b2=c2-2; h11=b2-2*pg
    print("surf d=%d K2=%s e=%s chiO=%s pg=%d tau=%s b2=%s h11=%s"%(d,c1sq,c2,chiO,pg,tau,b2,h11))
    assert chiO==1+pg and tau==-F(d*(d*d-4),3)
    assert c1sq==d*(d-4)**2 and c2==d*(d*d-4*d+6)
    # HRR vs exact sequence
    for k in range(-8,9):
        Q=stodd(2)
        tdX=[F(1),c[1]/2,(c[1]**2+c[2])/12]
        v=smul(sexp(k,2),tdX,2)[2]*deg
        rhs=binom_gen(3,k)-binom_gen(3,k-d)
        assert v==rhs,(d,k,v,rhs)
print("D ok: surfaces in P^3: Noether, signature, HRR for O(k) = exact sequence")
for nam,degs in [(4,[5]),(5,[2,4]),(5,[3,3]),(6,[2,2,3]),(7,[2,2,2,2])]:
    n=nam-len(degs); c,deg=ci(nam,degs,n)
    assert c[1]==0
    e=c[3]*deg; c2H=c[2]*deg  # c2 . H  = c2coef*H^2 * H *... compute c2.H
    # c2.H: c2 = c[2] H^2, H^3 -> deg
    c2H=c[2]*deg
    print(nam,degs,"H^3=",deg,"e=",e,"c2.H=",c2H,"chi(O(k)) = (%s k^3 + %s k)/6"%(deg, c2H/2))
    td=[F(1),F(0),c[2]/12,F(0)]
    for k in range(-5,6):
        v=smul(sexp(k,3),td,3)[3]*deg
        assert v==F(deg*k**3,6)+c2H*k/12
    # h11 =1 (Lefschetz), h21 from e
    h21=1-e/2
    print("   h21 =",h21)
# quintic check chi(O(k)) = h0(P^4,O(k))-h0(P^4,O(k-5))
c,deg=ci(4,[5],3)
for k in range(-6,10):
    td=[F(1),F(0),c[2]/12,F(0)]
    v=smul(sexp(k,3),td,3)[3]*deg
    assert v==binom_gen(4,k)-binom_gen(4,k-5)
print("quintic chi(O(k)) ok")
print("quintic chi(O(1)),chi(O(2)),chi(O(5)) ",[F(5*k**3+25*k,6) for k in (1,2,5)])
# K3: (4) in P^3, (2,3) in P^4, (2,2,2) in P^5
for nam,degs in [(3,[4]),(4,[2,3]),(5,[2,2,2])]:
    c,deg=ci(nam,degs,2); print("K3",nam,degs,"H^2=",deg,"e=",c[2]*deg,"c1=",c[1])
# P^2, P1xP1 etc
# C. c(E⊗L) rank 2,3 formulas
N=3;D=3
x=[P.var(i,N,D) for i in range(N)]
l=P.var(0,1,3)  # not used
