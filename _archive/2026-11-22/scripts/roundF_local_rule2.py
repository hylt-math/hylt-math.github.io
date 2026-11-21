# Round F: corrected unified local stalk rule (valid also for lct<1/2):
#   stalk = C^mu[-2] + R(s),  R(s) = [s in Z, s<=0](1+t) + (t+t^2) * #{alpha in Spec : s+alpha in Z, s+alpha <= 1},   s != 1.
import sys; sys.path.insert(0,'.')
from fractions import Fraction as Fr
import local_stalk as L
import roundC_local_verify as V
P=L.P
EXTRA={
 'z4-w4':({(4,0):1,(0,4):P-1},1,1,4,V.spec_bp(4,4)),
 'z5-w5':({(5,0):1,(0,5):P-1},1,1,5,V.spec_bp(5,5)),
 'z4-w5':({(4,0):1,(0,5):P-1},5,4,20,V.spec_bp(4,5)),
 'z3-w3 (D4 again via z3-w3)':({(3,0):1,(0,3):P-1},1,1,3,V.spec_bp(3,3)),
}
ALL=dict(V.SING); ALL.update(EXTRA)
def pred2(spec,s):
    mu=len(spec)
    R0=1 if (s.denominator==1 and s<=0) else 0
    c=sum(1 for al in spec if (s+al).denominator==1 and s+al<=1)
    return [R0,R0+c,c+mu]
if __name__=="__main__":
    name=sys.argv[1]
    h,wz,ww,d,spec=ALL[name]
    mu=len(spec); lct=min(spec)
    den=2*d if d<8 else d
    bad=[];tot=0
    for k in range(-2*den,2*den+1):
        s=Fr(k,den)
        if s==1: continue
        t1,_=L.stalk(h,wz,ww,d,s,4*d); t2,_=L.stalk(h,wz,ww,d,s,6*d)
        if t1!=t2: continue
        tot+=1
        if list(t1)!=pred2(spec,s): bad.append((str(s),t1,pred2(spec,s)))
    print(f"{name:12s} mu={mu} lct={lct} grid 1/{den}: compared {tot}, mismatches {len(bad)}",bad[:5],flush=True)
