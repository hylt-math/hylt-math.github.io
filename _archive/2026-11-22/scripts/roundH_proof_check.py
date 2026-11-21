# Round H: check (1) the algebraic identities behind the proof of the local stalk rule R(s),
# (2) K, Cok dims of chi: O_{k0}->O_{k0+delta} vs R(s) for quasi-homogeneous plane curve germs. Pure python, Fractions.
import random, itertools
from fractions import Fraction as F

def padd(p,q,c=1):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,0)+c*v
        if r[k]==0: del r[k]
    return r
def pmul(p,q):
    r={}
    for (a,b),u in p.items():
        for (c,d),v in q.items():
            r[(a+c,b+d)]=r.get((a+c,b+d),0)+u*v
    return {k:v for k,v in r.items() if v!=0}
def pscal(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def dz(p): return {(a-1,b):v*a for (a,b),v in p.items() if a>0}
def dw(p): return {(a,b-1):v*b for (a,b),v in p.items() if b>0}
Z={(1,0):F(1)}; W={(0,1):F(1)}

def check_identities(h,wz,ww,N,trials=3):
    delta=N-wz-ww
    hz,hw=dz(h),dw(h)
    def e(f): return padd(pscal(pmul(Z,dz(f)),wz),pscal(pmul(W,dw(f)),ww))
    def chi(f): return padd(pmul(hw,dz(f)),pmul(hz,dw(f)),-1)
    for t in range(trials):
        s=F(random.randint(-9,9),random.randint(1,7))
        rp=lambda: {(random.randint(0,3),random.randint(0,3)):F(random.randint(-3,3)) for _ in range(4)}
        a=rp(); b=rp(); f=rp()
        # omega=(U dz+V dw)/h
        U=pscal(padd(pmul(a,hz),pscal(pmul(b,W),ww)),F(1,N))
        V=pscal(padd(pmul(a,hw),pscal(pmul(b,Z),wz),-1),F(1,N))
        # d1 on Theta-element (p,q)=(V,-U)
        p,q=V,pscal(U,-1)
        d1=padd(pmul(h,padd(dz(p),dw(q))), padd(pmul(hz,p),pmul(hw,q)), -(1-s))
        # predicted: (h/N)[chi(a) - (e+sN-delta) b]
        eb=padd(e(b),pscal(b,s*N-delta))
        pred=pscal(pmul(h,padd(chi(a),eb,-1)),F(1,N))
        assert padd(d1,pred,-1)=={}, "d1 mismatch"
        # d0 f = h(f_w dz - f_z dw) + s f (h_w dz - h_z dw)  vs Phi^1 of ((e f + sN f) w_e + chi f w_chi)
        d0=(padd(pmul(h,dw(f)),pscal(pmul(f,hw),s)), padd(pscal(pmul(h,dz(f)),-1),pscal(pmul(f,hz),-s)))
        a2=padd(e(f),pscal(f,s*N)); b2=chi(f)
        U2=pscal(padd(pmul(a2,hz),pscal(pmul(b2,W),ww)),F(1,N)); V2=pscal(padd(pmul(a2,hw),pscal(pmul(b2,Z),wz),-1),F(1,N))
        assert padd(d0[0],V2,-1)=={} and padd(d0[1],pscal(U2,-1),-1)=={}, "d0 mismatch"
    return True

def monos(k,wz,ww):  # monomials of weight k
    r=[]
    if k<0: return r
    a=0
    while a*wz<=k:
        rem=k-a*wz
        if rem%ww==0: r.append((a,rem//ww))
        a+=1
    return r

def rank(rows,ncols):
    rows=[r[:] for r in rows]; rk=0; col=0
    m=len(rows)
    for col in range(ncols):
        piv=None
        for i in range(rk,m):
            if rows[i][col]!=0: piv=i;break
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        pv=rows[rk][col]
        rows[rk]=[x/pv for x in rows[rk]]
        for i in range(m):
            if i!=rk and rows[i][col]!=0:
                c=rows[i][col]; rows[i]=[x-c*y for x,y in zip(rows[i],rows[rk])]
        rk+=1
    return rk

def spec_weights(h,wz,ww,N):
    # weights (multiset) of monomial basis of T=O/J
    hz,hw=dz(h),dw(h); delta=N-wz-ww
    res={}
    for m in range(0,2*delta+1):
        mon=monos(m,wz,ww)
        if not mon: continue
        idx={x:i for i,x in enumerate(mon)}
        rows=[]
        for g,wg in ((hz,N-wz),(hw,N-ww)):
            for (a,b) in monos(m-wg,wz,ww):
                row=[F(0)]*len(mon)
                for (c,d),v in g.items(): row[idx[(a+c,b+d)]]+=v
                rows.append(row)
        dimT=len(mon)-(rank(rows,len(mon)) if rows else 0)
        if dimT: res[m]=dimT
    return res

def chi_dims(h,wz,ww,N,k0):
    delta=N-wz-ww; hz,hw=dz(h),dw(h)
    src=monos(k0,wz,ww); tgt=monos(k0+delta,wz,ww)
    if not src: return 0,(len(tgt))
    idx={x:i for i,x in enumerate(tgt)}
    rows=[]
    for (a,b) in src:
        row=[F(0)]*max(len(tgt),1)
        f={(a,b):F(1)}
        c=padd(pmul(hw,dz(f)),pmul(hz,dw(f)),-1)
        for k,v in c.items(): row[idx[k]]+=v
        rows.append(row)
    rk=rank(rows,max(len(tgt),1)) if tgt else 0
    K=len(src)-rk; Cok=len(tgt)-rk
    return K,Cok

def poly(*terms):
    return {(a,b):F(c) for c,a,b in terms}

types={
 'A1 zw':(poly((1,1,1)),1,1,2),
 'A2 z2+w3':(poly((1,2,0),(1,0,3)),3,2,6),
 'A3 z2+w4':(poly((1,2,0),(1,0,4)),2,1,4),
 'A6 z2+w7':(poly((1,2,0),(1,0,7)),7,2,14),
 'D4 z2w+w3':(poly((1,2,1),(1,0,3)),1,1,3),
 'D5 z2w+w4':(poly((1,2,1),(1,0,4)),3,2,8),
 'E6 z3+w4':(poly((1,3,0),(1,0,4)),4,3,12),
 'E8 z3+w5':(poly((1,3,0),(1,0,5)),5,3,15),
 'T236 z3+w6':(poly((1,3,0),(1,0,6)),2,1,6),
 'z4+w5 (lct9/20)':(poly((1,4,0),(1,0,5)),5,4,20),
 'z5+w5':(poly((1,5,0),(1,0,5)),1,1,5),
 'z4+w4':(poly((1,4,0),(1,0,4)),1,1,4),
 'z3+w7':(poly((1,3,0),(1,0,7)),7,3,21),
 'z5+w6':(poly((1,5,0),(1,0,6)),6,5,30),
}
if __name__=="__main__":
    random.seed(1)
    bad=0
    for name,(h,wz,ww,N) in types.items():
        # sanity: h quasi-homogeneous of degree N
        assert all(a*wz+b*ww==N for (a,b) in h)
        check_identities(h,wz,ww,N)
        delta=N-wz-ww; ell=wz+ww
        sp=spec_weights(h,wz,ww,N)
        mu=sum(sp.values())
        tested=0
        for k0 in range(-delta-3, 4*N+1):   # s=-k0/N
            K,Cok=chi_dims(h,wz,ww,N,k0)
            Kpred=1 if (k0>=0 and k0%N==0) else 0
            S=sum(d for m,d in sp.items() if (m+ell-k0)%N==0 and (m+ell-k0)//N<=1)
            if K!=Kpred or Cok!=S:
                bad+=1; print("MISMATCH",name,k0,K,Kpred,Cok,S)
            tested+=1
        print(f"{name}: mu={mu}, identities OK, {tested} values of k0 checked")
    print("total mismatches:",bad)
