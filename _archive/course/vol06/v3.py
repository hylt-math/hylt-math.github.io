from lib import *
exec(open('v2.py').read().split("# A.")[0].split("from lib import *")[1]) if False else None
from v2 import ci, binom_gen
import sys
# ---- universal formulas for E⊗L, Sym^2, End (rank 2) ----
N=2;D=4
x1,x2=P.var(0,2,4),P.var(1,2,4)
l=P.var(0,3,4) # placeholder
# use 3 vars: x1,x2,l
x1,x2,l=[P.var(i,3,4) for i in range(3)]
def e2(a,b): return a+b, a*b
c1=x1+x2; c2=x1*x2
a,b=x1+l,x2+l
print("c1(E⊗L)=",(a+b).d, " c2(E⊗L)=",(a*b - (c2+c1*l+l*l)).iszero())
# Sym^2 E
s=[x1*2,x1+x2,x2*2]
sc2=s[0]*s[1]+s[0]*s[2]+s[1]*s[2]; sc3=s[0]*s[1]*s[2]
print("Sym2: c2 = 2c1^2+4c2:",(sc2-(c1*c1*2+c2*4)).iszero(), " c3=4c1c2:",(sc3-c1*c2*4).iszero(), "c1=3c1")
# End E
r=[P.const(0,3,4),P.const(0,3,4),x1-x2,x2-x1]
ec2=sum((r[i]*r[j] for i in range(4) for j in range(i+1,4)),P.const(0,3,4))
print("End: c2 = 4c2-c1^2:",(ec2-(c2*4-c1*c1)).iszero())
# ch of Sym^2, ∧^2 rank 3 etc: skip
# ---- 4 variables: ch(Sym^2 E) etc -----
# Td of P^n
for n in (2,3,4):
    Q=stodd(n); print("Td(P^%d)"%n,spow(Q,n+1,n))
# P^3 chern numbers
print("c(TP^3)",spow([F(1),F(1),0,0],4,3))
# Pontryagin / L / A-hat
N=4;D=4
y=[P.var(i,4,4) for i in range(4)]  # y_i = x_i^2 variables
# x/tanh x = 1 + x^2/3 - x^4/45 : as series in y
Lc=[F(1),F(1,3),F(-1,45)]
L=P.const(1,4,4)
for yi in y: L=L*series_sub(Lc,yi,4,4)
# Ahat: (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760
Ac=[F(1),F(-1,24),F(7,5760)]
A=P.const(1,4,4)
for yi in y: A=A*series_sub(Ac,yi,4,4)
# D=4 here means total degree in y; p1=e1(y), p2=e2(y)
def to_p(p):
    out=to_elem(p,4); return out
print("L deg1",to_p(L.deg(1)),"L deg2",to_p(L.deg(2)))
print("A deg1",to_p(A.deg(1)),"A deg2",to_p(A.deg(2)))
# check x/tanh(x) series and x/sinh series quickly via Fractions
from math import factorial
def ser_mul(a,b,n):
    r=[F(0)]*(n+1)
    for i in range(n+1):
        for j in range(n+1-i): r[i+j]+=a[i]*b[j]
    return r
n=8
sinh=[F(1,factorial(k)) if k%2==1 else F(0) for k in range(n+1)]
cosh=[F(1,factorial(k)) if k%2==0 else F(0) for k in range(n+1)]
# x/tanh x = x cosh/ sinh = cosh/(sinh/x)
sx=sinh[1:]+[F(0)]
inv=sinv(sx,n-1)
xt=ser_mul(cosh[:n],inv,n-1)
print("x/tanh x =",xt[:7])
# x/2 / sinh(x/2): sinh(x/2)/(x/2)
sx2=[F(1,factorial(2*k+1))*F(1,4**k) for k in range(5)]
print("Ahat series in x^2:",sinv(sx2,4)[:3])
# Td = e^{x/2} Ahat
Qs=todd_coeffs(6)
e_half=[F(1,2**k)/factorial(k) for k in range(7)]
ah=[F(0)]*7
inv4=sinv(sx2,4)
for k in range(3): ah[2*k]=inv4[k]
print("Td = e^{x/2}*Ahat:", ser_mul(e_half,ah,6)==Qs)
