import sys; sys.path.insert(0,'.')
import local_stalk as L
from fractions import Fraction
names=sys.argv[1:] or ['smooth z','node zw','cusp z2-w3','tacnode z2-w4','A4 z2-w5','D4 zw(z-w)','D5 z2w-w4']
den=int(12)
for name in names:
    h,wz,ww,d=L.SING[name]
    print("==",name,"weights",(wz,ww),"deg",d,flush=True)
    res={}
    for k in range(-5*den,5*den+1):
        s=Fraction(k,den)
        t1,_=L.stalk(h,wz,ww,d,s,6*d); t2,_=L.stalk(h,wz,ww,d,s,8*d)
        inf = (t1!=t2)
        res[s]=(tuple(t1),inf)
    from collections import Counter
    gen=Counter(v for v,i in res.values() if not i).most_common(1)[0][0]
    print(" generic",gen)
    for s,(v,inf) in res.items():
        if inf: print("  s=%s INFINITE-DIM (cutoff-dependent)"%s)
        elif v!=gen: print("  s=%s"%s, v)
