# consolidated checks for vol06 (extra to v1-v4). Run: python3 verify_all.py
import io, contextlib
from lib import *
with contextlib.redirect_stdout(io.StringIO()):
    from v2 import ci, binom_gen
# Td4 table
def td4(c,deg): return (-c[1]**4+4*c[1]**2*c[2]+3*c[2]**2+c[1]*c[3]-c[4])/720*deg
exp={ (5,(1,)):1,(5,(2,)):1,(5,(3,)):1,(5,(6,)):2 }
for (nam,degs),v in exp.items():
    c,deg=ci(nam,list(degs),nam-len(degs)); assert td4(c,deg)==v
c,deg=ci(5,[2],4); assert (c[1]**2*c[2]*deg, c[2]**2*deg, c[1]*c[3]*deg, c[4]*deg)==(224,98,48,6)
c,deg=ci(5,[3],4); assert (c[1]**2*c[2]*deg, c[2]**2*deg, c[1]*c[3]*deg, c[4]*deg)==(162,108,18,27)
# T P2(k), Sym2
chi=lambda k:F((k+1)*(k+2),2)
for k in range(-8,8): assert 3*chi(k+1)-chi(k)==(k+2)*(k+4)
assert 6*chi(2)-3*chi(1)==27
# Euler hyp formula
for n in range(1,6):
    for d in range(1,8):
        c,deg=ci(n+1,[d],n); assert c[n]*deg==F((1-d)**(n+2)-1,d)+n+2
assert [F((1-d)**5-1,d)+5 for d in range(1,7)]==[4,4,-6,-56,-200,-516]
# plurigenera quintic surface, Fano3
for m in range(2,6): assert 5+F(m*(m-1)*5,2)==binom_gen(3,m)-binom_gen(3,m-5)
for nam,degs,h0 in [(3,[],35),(4,[2],30),(4,[3],15),(5,[2,3],6),(4,[4],5),(5,[2,2],19)]:
    c,deg=ci(nam,degs,3); assert F(c[1]**3*deg,2)+3==h0 and c[1]*c[2]*deg==24
# plane curves through m points
for d in range(1,8):
    for m in range(0,7): assert 1+F((d*d-m)-(-3*d+m),2)==F((d+1)*(d+2),2)-m
# Hodge numbers of surfaces from (K2,e) q=0
for K2,e,pg,h11 in [(0,24,1,20),(5,55,4,45),(9,3,0,1),(8,4,0,2),(3,9,0,7)]:
    assert F(K2+e,12)-1==pg and F(5*e-K2,6)==h11
# Newton p4 on P4
c1,c2,c3,c4=25*0+5,10,10,5
assert F(c1**4-4*c1**2*c2+4*c1*c3+2*c2**2-4*c4,24)==F(5,24)
# Euler theorem check on P1 table
for m in range(-8,9):
    h=lambda k:(k+1,0) if k>=0 else (0,-k-1)
    a,b=h(m),h(m+2); P=[a[0],a[1]+b[0],b[1]]; assert P[0]-P[1]+P[2]==-2
# F_a Chern numbers
for a in range(0,6):
    xi2=-a; xif=1; f2=0
    c1sq=4*xi2+4*(a+2)*xif; e=4*xif
    assert (c1sq,e)==(8,4)
# BMY algebra, tau formula
for d in range(1,8):
    c,deg=ci(3,[d],2); K2=c[1]**2*deg; e=c[2]*deg
    assert F(K2-2*e,3)==-F(d*(d*d-4),3)
print("verify_all: all assertions passed")
