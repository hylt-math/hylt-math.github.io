# Hypercohomology dims of (wedge T (x) O(m), d_sigma) on CP^2 for sigma = Pi_F, various cubics F.
# Reuses poisson.run (m>=-2, E1 concentrated in a=0) and neg_check.run (m<=-4, local cohomology); m=-3: all E1 terms total degree 2.
import sys, io, contextlib
sys.path.insert(0,'.')
from poisson import run as run_pos, P
import neg_check
from table import h as bott
def mk(*terms): return {k:v%P for k,v in terms}
cubics={
 'smooth(Fermat)': mk(((3,0,0),1),((0,3,0),1),((0,0,3),1)),
 'nodal y2z-x3-x2z': mk(((0,2,1),1),((3,0,0),-1),((2,0,1),-1)),
 'cuspidal y2z-x3': mk(((0,2,1),1),((3,0,0),-1)),
 'conic+secant x(yz-x2)': mk(((1,1,1),1),((3,0,0),-1)),
 'conic+tangent y(yz-x2)': mk(((0,2,1),1),((2,1,0),-1)),
 'triangle xyz': mk(((1,1,1),1)),
 'concurrent xy(x-y)': mk(((2,1,0),1),((1,2,0),-1)),
 'double line+line x2y': mk(((2,1,0),1)),
 'sigma=0': {},
}
def hyper(F,m):
    if m>=-2:
        r0,r1,z=run_pos(F,m); assert z
        e={(a,b):0 for a in range(3) for b in range(3)}
        h0O=bott(0,0,m); h0T=bott(1,0,m+3); h0K=bott(0,0,m+3)
        for (p,q,k) in [(0,1,m),(0,2,m),(1,1,m+3),(1,2,m+3),(0,1,m+3),(0,2,m+3)]:
            assert bott(p,q,k)==0,(m,p,q,k)
        return [h0O-r0,h0T-r0-r1,h0K-r1,0,0]
    if m==-3: return [0,0,3,0,0]
    return neg_check.run(F,m)['H']
if __name__=="__main__":
    ms=range(-15,16)
    out={}
    for name,F in cubics.items():
        rows=[]
        for m in ms:
            d=hyper(F,m)
            chi=sum((-1)**k*x for k,x in enumerate(d))
            assert chi==3,(name,m,d)
            rows.append((m,d))
        out[name]=rows
        print("==",name)
        for m,d in rows: print(m,d)
