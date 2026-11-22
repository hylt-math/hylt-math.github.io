# Round J2: check H^k(U;L_U)=0 (k<n) for no-integer-residue case: HH should be chi(X) t^n.
import sys,itertools; sys.path.insert(0,'.')
from fractions import Fraction as Fr
from toric_hh import hh,euler
from toric_crit import FANS,randA
from toric_generic_check2 import avec
def run(name,ms,rho,seed=7):
    rays=FANS[name]; n=len(rays[0]); a=avec(name,ms); box=max(a)+n+3
    r=[sum(Fr(rho[j])*u[j] for j in range(n))-ai for u,ai in zip(rays,a)]
    A=randA(n,seed,10**9)
    p=hh(rays,a,A,rho,box)
    nint=all(x.denominator!=1 for x in r)
    print(name,ms,"rho",rho,"res",[str(x) for x in r],"all nonint",nint,"poly",p,"euler",euler(p),flush=True)
    return p,r
if __name__=="__main__":
    tests=[('P4',(1,),(Fr(1,2),Fr(1,3),Fr(1,5),Fr(1,7))),
           ('P4',(2,),(Fr(1,3),Fr(1,3),Fr(1,3),Fr(1,3))),
           ('P2xP2',(1,2),(Fr(1,2),Fr(1,3),Fr(1,2),Fr(1,3))),
           ('P2xP2',(1,1),(Fr(1,2),Fr(-1,2),Fr(1,3),Fr(1,3))),
           ('P1^4',(1,1,1,1),(Fr(1,2),Fr(1,2),Fr(1,2),Fr(1,2))),
           ('P1xP3',(1,1),(Fr(1,2),Fr(1,3),Fr(1,3),Fr(1,3)))]
    for t in tests: run(*t)
