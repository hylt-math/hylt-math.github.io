# Verify the precise local stalk formula for quasi-homogeneous plane curve germs:
#   stalk_p(C_s) = C^mu[-2]  +  [s < lct] * R(s),  R(s) = [s in Z](1+t) + (t+t^2) * #{alpha in Spec : s+alpha in Z}   (s != 1)
# Spec = Steenbrink spectrum (symmetric about 1): alpha(z^i w^j) = (wz(i+1)+ww(j+1))/d for a monomial basis of the Jacobian algebra.
import sys; sys.path.insert(0,'.')
import local_stalk as L
from fractions import Fraction as Fr
P=L.P
def spec_bp(a,b):  # z^a - w^b
    return sorted(Fr(i,a)+Fr(j,b) for i in range(1,a) for j in range(1,b))
def spec_D(k):  # w(z^2 + w^{k-2}) i.e. z^2 w + w^{k-1}, weights z=(k-2), w=2, d=2(k-1)
    wz,ww,d=k-2,2,2*(k-1)
    mons=[(0,j) for j in range(0,k-1)]+[(1,0)]
    return sorted(Fr(wz*(i+1)+ww*(j+1),d) for i,j in mons)
SING={
 'A1 node':({(1,1):1},1,1,2,spec_bp(2,2)),
 'A2 cusp':({(2,0):1,(0,3):P-1},3,2,6,spec_bp(2,3)),
 'A3 tacnode':({(2,0):1,(0,4):P-1},2,1,4,spec_bp(2,4)),
 'A4':({(2,0):1,(0,5):P-1},5,2,10,spec_bp(2,5)),
 'A5':({(2,0):1,(0,6):P-1},3,1,6,spec_bp(2,6)),
 'A6':({(2,0):1,(0,7):P-1},7,2,14,spec_bp(2,7)),
 'D4':({(2,1):1,(1,2):P-1},1,1,3,None),
 'D5':({(2,1):1,(0,4):P-1},3,2,8,None),
 'D6':({(2,1):1,(0,5):P-1},2,1,5,None),
 'E6':({(3,0):1,(0,4):P-1},4,3,12,spec_bp(3,4)),
 'E8':({(3,0):1,(0,5):P-1},5,3,15,spec_bp(3,5)),
 'T236 z3-w6':({(3,0):1,(0,6):P-1},2,1,6,spec_bp(3,6)),
}
SING['D4'] = SING['D4'][:4]+([Fr(2,3),Fr(1),Fr(1),Fr(4,3)],)
# D5: z^2 w - w^4 : weights z=3,w=2? check degree: z^2 w: 2*wz+ww ; w^4: 4*ww. local_stalk uses (3,1,7): wz=3,ww=1,d=7
SING['D5']=SING['D5'][:4]+(sorted(Fr(3*(i+1)+2*(j+1),8) for i,j in [(0,0),(0,1),(0,2),(0,3),(1,0)]),)
SING['D6']=SING['D6'][:4]+(sorted(Fr(2*(i+1)+1*(j+1),5) for i,j in [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0)]),)
def pred(spec,s):
    mu=len(spec); lct=min(spec)
    R=[0,0,0]
    if s<lct:
        if s.denominator==1: R[0]+=1;R[1]+=1
        c=sum(1 for al in spec if (s+al).denominator==1)
        R[1]+=c;R[2]+=c
    return [R[0],R[1],R[2]+mu]
if __name__=="__main__":
    names=sys.argv[1:] or list(SING)
    for name in names:
        h,wz,ww,d,spec=SING[name]
        den=d if d%1==0 else d
        mu=len(spec); lct=min(spec)
        bad=0;tot=0;shown=[]
        for k in range(-2*den,2*den+1):
            s=Fr(k,den)
            if s==1: continue
            t1,_=L.stalk(h,wz,ww,d,s,4*d); t2,_=L.stalk(h,wz,ww,d,s,6*d)
            if t1!=t2: shown.append(("INF",str(s))); continue
            p=pred(spec,s)
            if s==lct: shown.append(('s=lct',str(s),list(t1),p)); continue
            tot+=1
            if list(t1)!=p: bad+=1; shown.append((str(s),t1,p))
        print(f"{name:12s} mu={mu} lct={lct} grid 1/{den}: compared {tot}, mismatches {bad}", shown[:6],flush=True)
