# Round F: test the local stalk formula in the regime lct < 1/2 (ordinary quadruple/quintuple points, z^4-w^5), and the weight claim k0=-s*d.
import sys; sys.path.insert(0,'.')
from fractions import Fraction as Fr
import local_stalk as L
import roundF_local_B as B
import roundC_local_verify as V
P=L.P
CASES={
 'z4-w4 (ordinary 4-fold)':({(4,0):1,(0,4):P-1},1,1,4,V.spec_bp(4,4)),
 'z5-w5 (ordinary 5-fold)':({(5,0):1,(0,5):P-1},1,1,5,V.spec_bp(5,5)),
 'z4-w5':({(4,0):1,(0,5):P-1},5,4,20,V.spec_bp(4,5)),
}
name=sys.argv[1]
h,wz,ww,d,spec=CASES[name]
mu=len(spec); lct=min(spec); delta=d-wz-ww
print(name,"mu",mu,"lct",lct,"delta/d",Fr(delta,d))
den=2*d
rows=[]
for k in range(-2*den,2*den+1):
    s=Fr(k,den)
    if s==1: continue
    tc,wc=L.stalk(h,wz,ww,d,s,4*d)
    tc2,_=L.stalk(h,wz,ww,d,s,6*d)
    if tc!=tc2: rows.append((str(s),'INF')); continue
    p=V.pred(spec,s)
    rows.append((s,tc,p,[w[0] for w in B.stalkB(h,wz,ww,d,s,4*d)[1]]))
bad=[(str(r[0]),r[1],r[2],r[3]) for r in rows if r[1]!=r[2] and r[1]!='INF'] if rows else []
print("compared",len(rows),"mismatches",len(bad))
for b in bad[:20]: print(b)
