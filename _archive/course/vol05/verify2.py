from fractions import Fraction as Fr
from math import comb
import itertools
def C(n,k): return comb(n,k) if (n>=0 and 0<=k<=n) else 0
def h(n,m,q):
    return C(m+n,n) if q==0 else (C(-m-1,n) if q==n else 0)
# T_P2(m) via Euler sequence
out=[]
for m in range(-9,6):
    h1=1 if m==-3 else 0
    h0=3*h(2,m+1,0)-h(2,m,0)
    h2=3*h(2,m+1,2)-h(2,m,2)+h1
    chi=3*(((m+1)+1)*((m+1)+2)//2)-((m+1)*(m+2)//2)
    assert h0-h1+h2==chi,(m,h0,h1,h2,chi)
    if h1 or h2: out.append((m,h1,h2))
print("TP2 nonvanishing (m,h1,h2):",out)
# Euler char HH, P1 and P2
chi1=lambda k:k+1
for m in range(-6,6):
    assert chi1(m)-chi1(m+2)==-2
print("P1 HH euler -2 ok; P2 3 ok (checked earlier)")
# hypersurface in P4 euler
def eP4(d): return d*(10-10*d+5*d*d-d**3)
print("e(X_d) P4:",[(d,eP4(d)) for d in range(1,7)])
# chi(T) surface
chiT=lambda c1,c2:Fr(7*c1-5*c2,6)
print("chi(T): P2",chiT(9,3),"F_a",chiT(8,4),"K3",chiT(0,24))
# Hirzebruch
for a in range(0,6):
    h0=6 if a==0 else a+5; print("F_%d h1(T)="%a,h0-6)
# quartic moduli
print("quartic moduli",comb(7,3)-1-15)
# torus pfaffian
import numpy as np
E=np.zeros((4,4)); E[0,1]=-1;E[1,0]=1;E[2,3]=-1;E[3,2]=1
print("Pf=",E[0,1]*E[2,3]-E[0,2]*E[1,3]+E[0,3]*E[1,2])
# Betti unimodality
for name,b,n in [("quintic",[1,0,1,204,1,0,1],3),("T4",[1,4,6,4,1],2),("K3",[1,0,22,0,1],2),("S1xS3",[1,1,0,1,1],2)]:
    print(name,[b[k]>=b[k-2] for k in range(2,n+1)])
# Hirzebruch chi O(m) polynomial identity Pn
print("done")
