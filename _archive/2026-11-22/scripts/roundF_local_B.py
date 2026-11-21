# Round F: subcomplex B_s = (O -> Theta(-log D) -> hO) of the local twisted Lichnerowicz complex C_s,
# quotient Q = C/B = [Theta/Theta(-log D) -> O/h]. Checks (weight-graded, exact mod P) for quasi-homogeneous h:
#   (1) H^*(C_s) = H^*(B_s) + T[-2] dimensionwise (T = Tjurina algebra O/(h,h_z,h_w)), s != 1;
#   (2) H^*(B_s) lives in a single weight strand k0(s).
import sys; sys.path.insert(0,'.')
from fractions import Fraction as Fr
import local_stalk as L
P=L.P
inv=L.inv
def nullspace(rows, ncols):
    """rows: list of dict col->val (equations); return basis of nullspace as list of dict."""
    # gaussian elimination to RREF
    piv={}  # pivot col -> row dict (normalized)
    for r in rows:
        r=dict(r)
        for c,pr in list(piv.items()):
            if c in r:
                f=r[c]
                for kk,vv in pr.items():
                    nv=(r.get(kk,0)-f*vv)%P
                    if nv: r[kk]=nv
                    else: r.pop(kk,None)
        if not r: continue
        c=min(r); f=inv(r[c]); r={k:v*f%P for k,v in r.items()}
        for c2,pr in list(piv.items()):
            if c in pr:
                g=pr[c]
                for kk,vv in r.items():
                    nv=(pr.get(kk,0)-g*vv)%P
                    if nv: pr[kk]=nv
                    else: pr.pop(kk,None)
        piv[c]=r
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for fc in free:
        v={fc:1}
        for c,pr in piv.items():
            if fc in pr: v[c]=(-pr[fc])%P
        basis.append(v)
    return basis
def Bstrand(h,wz,ww,d,s,k):
    delta=d-wz-ww
    S=L.frac_mod(Fr(s))
    hz,hw=L.dz(h),L.dw(h)
    M0=L.monos_of_weight(k,wz,ww)
    u=k+delta
    Mp=L.monos_of_weight(u+wz,wz,ww); Mq=L.monos_of_weight(u+ww,wz,ww)
    v=u+delta
    Mg=L.monos_of_weight(v+wz+ww,wz,ww)
    Mh=L.monos_of_weight(u,wz,ww)            # c with h*c of weight u+d
    # C^1_B: (p,q,c): p h_z + q h_w - h c = 0
    cols={}
    for i,m in enumerate(Mp): cols[('p',m)]=i
    for i,m in enumerate(Mq): cols[('q',m)]=len(Mp)+i
    for i,m in enumerate(Mh): cols[('c',m)]=len(Mp)+len(Mq)+i
    ncols=len(cols)
    eqs={}
    def addeq(mon,col,val):
        eqs.setdefault(mon,{})
        eqs[mon][col]=(eqs[mon].get(col,0)+val)%P
    for m in Mp:
        for mon,val in L.pmul({m:1},hz).items(): addeq(mon,cols[('p',m)],val)
    for m in Mq:
        for mon,val in L.pmul({m:1},hw).items(): addeq(mon,cols[('q',m)],val)
    for m in Mh:
        for mon,val in L.pmul({m:1},h).items(): addeq(mon,cols[('c',m)],-val)
    ns=nullspace([r for r in eqs.values() if r],ncols)
    # basis vectors of C^1_B as (p,q) pairs; (p,q) determines c, so dim = dim of nullspace
    basisB=[]
    for nv_ in ns:
        p={m:nv_.get(cols[("p",m)],0) for m in Mp if nv_.get(cols[("p",m)],0)}
        q={m:nv_.get(cols[("q",m)],0) for m in Mq if nv_.get(cols[("q",m)],0)}
        basisB.append((p,q))
    n1B=len(basisB)
    # C^2_B = h*O : g in h*(monos of weight v+wz+ww-d)
    Mc2=L.monos_of_weight(v+wz+ww-d,wz,ww); n2B=len(Mc2)
    # d0
    rows0=[]
    for m in M0:
        f={m:1}
        pz=L.padd(L.pmul(h,L.dw(f)),L.sc(L.pmul(f,hw),S))
        pw=L.padd(L.sc(L.pmul(h,L.dz(f)),P-1),L.sc(L.pmul(f,hz),(-S)%P))
        row={('z',)+kk:vv for kk,vv in pz.items()}; row.update({('w',)+kk:vv for kk,vv in pw.items()})
        rows0.append(row)
    r0=L.rank(rows0)
    rows1=[]
    for p,q in basisB:
        e=L.padd(L.padd(L.pmul(h,L.dz(p)),L.pmul(h,L.dw(q))), L.padd(L.sc(L.pmul(hz,p),(-(1-S))%P),L.sc(L.pmul(hw,q),(-(1-S))%P)))
        rows1.append(e)
    r1=L.rank(rows1)
    n0=len(M0)
    return (n0,n1B,n2B, n0-r0, n1B-r1-r0, n2B-r1)
def stalkB(h,wz,ww,d,s,Kmax):
    delta=d-wz-ww
    tot=[0,0,0]; where=[]
    kmin=-2*delta-(wz+ww)-1
    for k in range(min(kmin,0),Kmax+1):
        n0,n1,n2,a,b,c=Bstrand(h,wz,ww,d,s,k)
        if a or b or c: where.append((k,a,b,c))
        tot[0]+=a;tot[1]+=b;tot[2]+=c
    return tot,where
def tjurina(h,wz,ww,d):
    # dim O/(h,h_z,h_w): count monomials not in ideal, by weight-graded linear algebra up to large weight
    hz,hw=L.dz(h),L.dw(h)
    tot=0
    for k in range(0,4*d):
        M=L.monos_of_weight(k,wz,ww)
        if not M: continue
        rows=[]
        for g,wg in ((h,d),(hz,d-wz),(hw,d-ww)):
            for m in L.monos_of_weight(k-wg,wz,ww):
                rows.append(L.pmul({m:1},g))
        tot+=len(M)-L.rank(rows)
    return tot
if __name__=="__main__":
    SING={'A2 cusp':({(2,0):1,(0,3):P-1},3,2,6),'A3 tacnode':({(2,0):1,(0,4):P-1},2,1,4),
          'A1 node':({(1,1):1},1,1,2),'D4':({(2,1):1,(1,2):P-1},1,1,3),'E6':({(3,0):1,(0,4):P-1},4,3,12)}
    names=sys.argv[1:] or list(SING)
    for name in names:
        h,wz,ww,d=SING[name]
        T=tjurina(h,wz,ww,d)
        print("==",name,"Tjurina",T)
        bad=0
        for k12 in range(-30,31):
            s=Fr(k12,6)
            if s==1: continue
            tc,wc=L.stalk(h,wz,ww,d,s,6*d)
            tb,wb=stalkB(h,wz,ww,d,s,6*d)
            ok=(tc[0]==tb[0] and tc[1]==tb[1] and tc[2]==tb[2]+T)
            if not ok: bad+=1
            if tb!=[0,0,0] or not ok:
                print(" s=%s C=%s B=%s wB=%s ok=%s"%(s,tc,tb,[w[0] for w in wb],ok))
        print(" mismatches of H(C)=H(B)+T[-2]:",bad)
