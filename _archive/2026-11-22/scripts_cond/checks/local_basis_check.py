# Check the (e, chi_h)-basis formulas used in the proof of the local theorem (this paper):
#   d0 f = -(chi_h f / N) e + ((e f + sN f)/N) chi_h
#   d1(a e + b chi_h) = [ (e + sN - delta) a + chi_h b ] * h dz^dw
# against the defining formulas  d0 f=(h f_w + s f h_w)d_z-(h f_z + s f h_z)d_w ,  d1(p,q)=h(p_z+q_w)-(1-s)(h_z p+h_w q).
# Exact rational arithmetic, random polynomial data, several quasi-homogeneous h.
import random
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
def psc(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def dz(p): return {(a-1,b):v*a for (a,b),v in p.items() if a>0}
def dw(p): return {(a,b-1):v*b for (a,b),v in p.items() if b>0}
Z={(1,0):F(1)}; W={(0,1):F(1)}
types={'A1 zw':({(1,1):F(1)},1,1,2),'A2':({(2,0):F(1),(0,3):F(1)},3,2,6),'D5':({(2,1):F(1),(0,4):F(1)},3,2,8),
 'D4b z w(z-w)':({(2,1):F(1),(1,2):F(-1)},1,1,3),'E8':({(3,0):F(1),(0,5):F(1)},5,3,15),'z4w5':({(4,0):F(1),(0,5):F(1)},5,4,20),'z5w5':({(5,0):F(1),(0,5):F(1)},1,1,5)}
bad=0;tot=0
for name,(h,wz,ww,N) in types.items():
    # sanity: quasi-homogeneity
    assert all(a*wz+b*ww==N for (a,b) in h), name
    delta=N-wz-ww; hz,hw=dz(h),dw(h)
    e=lambda f: padd(psc(pmul(Z,dz(f)),wz),psc(pmul(W,dw(f)),ww))
    chi=lambda f: padd(pmul(hw,dz(f)),pmul(hz,dw(f)),-1)
    for t in range(15):
        s=F(random.randint(-12,12),random.randint(1,9))
        rp=lambda: {(random.randint(0,4),random.randint(0,4)):F(random.randint(-4,4)) for _ in range(5)}
        f=rp(); a=rp(); b=rp()
        # d0 f definition -> components (p,q)
        p0=padd(pmul(h,dw(f)),psc(pmul(f,hw),s)); q0=psc(padd(pmul(h,dz(f)),psc(pmul(f,hz),s)),-1)
        # basis formula: coefficient of d_z/d_w in  A e + B chi
        A=psc(chi(f),F(-1,N)); B=psc(padd(e(f),psc(f,s*N)),F(1,N))
        p1=padd(psc(pmul(A,Z),wz),pmul(B,hw)); q1=padd(psc(pmul(A,W),ww),pmul(B,hz),-1)
        # (A e + B chi) has d_z-comp A*wz*z + B*hw ; d_w comp A*ww*w - B*hz
        tot+=1
        if padd(p0,p1,-1) or padd(q0,q1,-1): bad+=1; print('d0 mismatch',name)
        # d1 of a e + b chi
        p=padd(psc(pmul(a,Z),wz),pmul(b,hw)); q=padd(psc(pmul(a,W),ww),pmul(b,hz),-1)
        d1=padd(pmul(h,padd(dz(p),dw(q))),padd(pmul(hz,p),pmul(hw,q)),-(1-s))
        pred=pmul(h,padd(padd(e(a),psc(a,s*N-delta)),chi(b)))
        tot+=1
        if padd(d1,pred,-1): bad+=1; print('d1 mismatch',name)
        # contraction (homotopy) check at kappa != 0 is algebraic; also d1 d0 = 0
        c0=padd(psc(pmul(A,Z),wz),pmul(B,hw))
print('checks',tot,'mismatches',bad)
