# Local stalk cohomology of the Lichnerowicz complex with module  prod h_i^{s_i}  (unequal residues), sigma = h d_z^d_w, h = prod h_i quasi-homogeneous.
import sys, itertools
from fractions import Fraction
import local_stalk as L
P=L.P
def build_H(branches,wz,ww):
    # branches: list of (poly_dict, s_i Fraction). returns h, Hz, Hw (mod P)
    h={(0,0):1}
    for p,_ in branches: h=L.pmul(h,p)
    Hz={};Hw={}
    for i,(p,s) in enumerate(branches):
        cof={(0,0):1}
        for j,(q,_) in enumerate(branches):
            if j!=i: cof=L.pmul(cof,q)
        S=L.frac_mod(Fraction(s))
        Hz=L.padd(Hz,L.sc(L.pmul(cof,L.dz(p)),S)); Hw=L.padd(Hw,L.sc(L.pmul(cof,L.dw(p)),S))
    return h,Hz,Hw
def strand(h,Hz,Hw,wz,ww,d,k):
    delta=d-wz-ww
    hz,hw=L.dz(h),L.dw(h)
    M0=L.monos_of_weight(k,wz,ww)
    u=k+delta
    Mp=L.monos_of_weight(u+wz,wz,ww); Mq=L.monos_of_weight(u+ww,wz,ww)
    v=u+delta; Mg=L.monos_of_weight(v+wz+ww,wz,ww)
    rows0=[]
    for m in M0:
        f={m:1}
        pz=L.padd(L.pmul(h,L.dw(f)),L.pmul(f,Hw))
        pw=L.padd(L.sc(L.pmul(h,L.dz(f)),P-1),L.sc(L.pmul(f,Hz),P-1))
        row={('z',)+kk:vv for kk,vv in pz.items()}; row.update({('w',)+kk:vv for kk,vv in pw.items()})
        rows0.append(row)
    rows1=[]
    for comp,Ms in (('z',Mp),('w',Mq)):
        for m in Ms:
            f={m:1}
            if comp=='z': e=L.padd(L.padd(L.pmul(h,L.dz(f)),L.sc(L.pmul(hz,f),P-1)),L.pmul(Hz,f))
            else: e=L.padd(L.padd(L.pmul(h,L.dw(f)),L.sc(L.pmul(hw,f),P-1)),L.pmul(Hw,f))
            rows1.append(e)
    r0=L.rank(rows0); r1=L.rank(rows1)
    n0,n1,n2=len(M0),len(Mp)+len(Mq),len(Mg)
    return (n0-r0, n1-r1-r0, n2-r1)
def stalk(branches,wz,ww,d,Kmax):
    h,Hz,Hw=build_H(branches,wz,ww)
    delta=d-wz-ww; tot=[0,0,0]
    for k in range(min(-2*delta-(wz+ww)-1,0),Kmax+1):
        a,b,c=strand(h,Hz,Hw,wz,ww,d,k); tot[0]+=a;tot[1]+=b;tot[2]+=c
    return tot
def check_equal():
    # sanity: equal residues must reproduce local_stalk
    hh,wz,ww,d=L.SING['D4 zw(z-w)']
    for s in [Fraction(0),Fraction(-1),Fraction(1,3),Fraction(2,3),Fraction(1,2)]:
        a=L.stalk(hh,wz,ww,d,s,6*d)[0]
        br=[({(1,0):1},s),({(0,1):1},s),({(1,0):1,(0,1):P-1},s)]
        b=stalk(br,1,1,3,6*3)
        assert a==b,(s,a,b)
    print("equal-residue sanity OK")
if __name__=="__main__":
    check_equal()
    z={(1,0):1}; w={(0,1):1}; zw={(1,0):1,(0,1):P-1}
    den=6; vals=[Fraction(k,den) for k in range(-6,7)]
    from collections import Counter
    res={}
    for s1,s2,s3 in itertools.product(vals,repeat=3):
        if not (s1<=s2<=s3): continue
        if s1==1 or s2==1 or s3==1: continue   # resonance r=1 excluded
        t1=tuple(stalk([(z,s1),(w,s2),(zw,s3)],1,1,3,12)); t2=tuple(stalk([(z,s1),(w,s2),(zw,s3)],1,1,3,18))
        res[(s1,s2,s3)]=(t1,t1==t2)
    c=Counter(v for v,_ in res.values())
    print(c)
    for key,(v,fin) in sorted(res.items()):
        if v!=(0,0,4) and fin: print([str(x) for x in key],v)
    print("non-stabilised:",[ [str(x) for x in k] for k,(v,f) in res.items() if not f][:10])
