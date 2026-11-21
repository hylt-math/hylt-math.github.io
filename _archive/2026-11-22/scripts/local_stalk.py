# Local (germ at 0 of the) cohomology of the twisted Lichnerowicz complex  C_s : O -> O^2 -> O,  sigma = h d_z^d_w,
#   d0 f = (h f_w + s f h_w) d_z + (-h f_z - s f h_z) d_w
#   d1 (p d_z + q d_w) = h (p_z+q_w) - (1-s)(h_z p + h_w q)
# (module O h^s: flat section ~ h^{-s}; global O(m) on P^2 has s=-m/3, on P1xP1 s=-m/2.)
# h quasi-homogeneous (weights wz,ww; degree d): complex splits by weight; finite-dimensional pieces. Exact arithmetic mod P.
import sys
from fractions import Fraction
P=1000003
def inv(a): return pow(a%P,P-2,P)
def frac_mod(fr): return fr.numerator%P*inv(fr.denominator)%P
def pmul(p,q):
    r={}
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            k=(a+c,b+d); r[k]=(r.get(k,0)+v*w)%P
    return {k:v for k,v in r.items() if v}
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        nv=(r.get(k,0)+s*v)%P
        if nv: r[k]=nv
        else: r.pop(k,None)
    return r
def dz(p): return {(a-1,b):v*a%P for (a,b),v in p.items() if a>0 and v*a%P}
def dw(p): return {(a,b-1):v*b%P for (a,b),v in p.items() if b>0 and v*b%P}
def sc(p,c): return {k:v*c%P for k,v in p.items() if v*c%P}
def rank(rows):
    piv={}; rk=0
    for r in rows:
        r=dict(r)
        while r:
            k=min(r)
            if k in piv:
                pr=piv[k]; c=r[k]*inv(pr[k])%P
                for kk,vv in pr.items():
                    nv=(r.get(kk,0)-c*vv)%P
                    if nv: r[kk]=nv
                    else: r.pop(kk,None)
            else: piv[k]=r; rk+=1; break
    return rk
def monos_of_weight(k,wz,ww):
    # monomials z^i w^j with i*wz+j*ww==k
    out=[]
    if k<0: return out
    for i in range(k//wz+1):
        rem=k-i*wz
        if rem%ww==0: out.append((i,rem//ww))
    return out
def strand(h,wz,ww,d,s,k):
    """strand starting at C^0 weight k. returns (dim C0,C1,C2, h0,h1,h2)."""
    delta=d-wz-ww
    S=frac_mod(Fraction(s))
    hz,hw=dz(h),dw(h)
    M0=monos_of_weight(k,wz,ww)
    # C1 weight u=k+delta: p d_z with wt(p)=u+wz ; q d_w with wt(q)=u+ww
    u=k+delta
    Mp=monos_of_weight(u+wz,wz,ww); Mq=monos_of_weight(u+ww,wz,ww)
    # C2 weight v=u+delta: g d_z^d_w with wt(g)=v+wz+ww
    v=u+delta
    Mg=monos_of_weight(v+wz+ww,wz,ww)
    idxp={m:i for i,m in enumerate(Mp)}
    rows0=[]
    for m in M0:
        f={m:1}
        pz=padd(pmul(h,dw(f)),sc(pmul(f,hw),S))                       # coefficient of d_z
        pw=padd(sc(pmul(h,dz(f)),P-1),sc(pmul(f,hz),(-S)%P))        # coefficient of d_w
        row={('z',)+kk:vv for kk,vv in pz.items()}
        row.update({('w',)+kk:vv for kk,vv in pw.items()})
        rows0.append(row)
    rows1=[]
    for comp,Ms in (('z',Mp),('w',Mq)):
        for m in Ms:
            f={m:1}
            if comp=='z':
                e=padd(pmul(h,dz(f)), sc(pmul(hz,f),(-(1-S))%P))
            else:
                e=padd(pmul(h,dw(f)), sc(pmul(hw,f),(-(1-S))%P))
            rows1.append(e)
    r0=rank(rows0); r1=rank(rows1)
    n0,n1,n2=len(M0),len(Mp)+len(Mq),len(Mg)
    return (n0,n1,n2, n0-r0, n1-r1-r0, n2-r1)
def stalk(h,wz,ww,d,s,Kmax):
    delta=d-wz-ww
    tot=[0,0,0]; where=[]
    kmin=-2*delta-(wz+ww)-1
    for k in range(min(kmin,0),Kmax+1):
        n0,n1,n2,a,b,c=strand(h,wz,ww,d,s,k)
        if a or b or c:
            where.append((k,a,b,c))
        tot[0]+=a; tot[1]+=b; tot[2]+=c
    return tot,where
SING={
 'smooth z':({(1,0):1},1,1,1),
 'node zw':({(1,1):1},1,1,2),
 'cusp z2-w3':({(2,0):1,(0,3):P-1},3,2,6),
 'tacnode z2-w4':({(2,0):1,(0,4):P-1},2,1,4),
 'A4 z2-w5':({(2,0):1,(0,5):P-1},5,2,10),
 'D4 zw(z-w)':({(2,1):1,(1,2):P-1},1,1,3),
 'D5 z2w-w4':({(2,1):1,(0,4):P-1},3,1,7),
 'xyz-like: z(z2-w2)... = D4':None,
 'nonreduced z2':({(2,0):1},1,1,2),
 'nonreduced z2w':({(2,1):1},1,1,3),
 'z3 (triple)':({(3,0):1},1,1,3),
}
if __name__=="__main__":
    names=[n for n in SING if SING[n]] if len(sys.argv)<2 else sys.argv[1:]
    S=[Fraction(k,12) for k in range(-60,61)]
    for name in names:
        h,wz,ww,d=SING[name]
        print("==",name,"weights",(wz,ww),"deg",d)
        prev=None
        for s in S:
            tot,where=stalk(h,wz,ww,d,s,Kmax=6*d)
            key=tuple(tot)
            print("s=%s"%s, tot, "weights(k:h0,h1,h2)",where[:6])
        sys.stdout.flush()
