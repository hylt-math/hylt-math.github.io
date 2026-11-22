# independent re-check (reviewer): Bott formula vs Cech complex on P^n via numpy; HH tables; chi identities; S^1 Cech
import numpy as np, itertools
from math import comb
def bott(n,k):
    h=[0]*(n+1)
    if k>=0: h[0]=comb(n+k,n)
    if k<=-n-1: h[n]=comb(-k-1,n)
    return h
# independent Cech: complex for exponent a: cochains on nonempty I containing S(a); compute by numpy rank
def coh(n,S):
    lv=[[I for I in itertools.combinations(range(n+1),p+1) if set(S)<=set(I)] for p in range(n+1)]
    d=[len(l) for l in lv]; r=[]
    for p in range(n):
        M=np.zeros((len(lv[p+1]),len(lv[p])))
        ix={I:i for i,I in enumerate(lv[p])}
        for j,J in enumerate(lv[p+1]):
            for t in range(len(J)):
                I=J[:t]+J[t+1:]
                if I in ix: M[j,ix[I]]+=(-1)**t
        r.append(np.linalg.matrix_rank(M) if M.size else 0)
    return [d[p]-(r[p] if p<n else 0)-(r[p-1] if p>0 else 0) for p in range(n+1)]
def cech(n,k,R):
    H=[0]*(n+1)
    for a in itertools.product(range(-R,R+1),repeat=n):
        l=k-sum(a)
        if abs(l)>R: continue
        S=[i for i,x in enumerate(a+(l,)) if x<0]
        h=coh(n,S)
        H=[x+y for x,y in zip(H,h)]
    return H
for n,R in((1,14),(2,9),(3,7)):
    for k in range(-6,5):
        assert cech(n,k,R)==bott(n,k),(n,k)
print("Cech==Bott ok")
# chi polynomial
for n in (1,2,3):
    for k in range(-8,8):
        b=bott(n,k); assert sum((-1)**q*b[q] for q in range(n+1))==comb(n+k,n) if k>=-n else True
# HH table P1 sigma=0,V=0
h=lambda m:bott(1,m)
print("HH table k:(HH0,HH1,HH2),chi")
for k in range(-4,3):
    a=h(k); b=h(k+2)
    HH=(a[0],a[1]+b[0],b[1]); print(k,HH,HH[0]-HH[1]+HH[2])
# duality term-wise
for k in range(-9,10):
    a=h(k);b=h(k+2); A=(a[0],a[1]+b[0],b[1])
    a2=h(-k-4);b2=h(-k-2); B=(a2[0],a2[1]+b2[0],b2[1])
    assert A==B[::-1]
print("duality ok")
# CP2 chi(Lambda^p T (x) O(k)) sum = 3 ; chi(T(k))=3chi(O(k+1))-chi(O(k)), L2T=O(3)
chi=lambda n,k:sum((-1)**q*bott(n,k)[q] for q in range(n+1))
for k in range(-6,7):
    assert chi(2,k)-(3*chi(2,k+1)-chi(2,k))+chi(2,k+3)==3
# P3: sum (-1)^p chi(Lambda^p T(k)) = -4 ; Lambda^pT via Euler: sum over Koszul
from math import comb as C
for k in range(-6,7):
    # ch-level: Lambda^p T has class  C(4,p+1)... use K-theory: T=(n+1)O(1)-O ; Lambda^p T = sum_j (-1)^j ... use generating (1+t)^{4}O(1)-> Lambda_t(T)=Lambda_t(O(1))^4/Lambda_t(O)
    # Lambda_t(O(1))^4=(1+tO(1))^4 ; 1/(1+t)= sum(-t)^j  => coefficient of t^p
    for_p=[]
    n=3
    for p in range(n+1):
        c=0
        for i in range(0,p+1):
            c+=C(4,i)*(-1)**(p-i)*chi(3,k+i)
        for_p.append(c)
    assert sum((-1)**p*for_p[p] for p in range(n+1))==(-1)**3*4,(k,for_p)
print("P3 total chi = -4 ok")
# Smith/H^1 S^1: rank checks
d=np.array([[-1,1,0],[0,-1,1],[-1,0,1]]);print("S1 3 arcs rank",np.linalg.matrix_rank(d))
print("ok")
