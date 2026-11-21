import sys,time; sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
def run(name,rays,a,A,rhos,box=None):
    print("==",name,flush=True)
    for rho in rhos:
        t=time.time()
        r=[sum(x*y for x,y in zip(rho,u))-ai for u,ai in zip(rays,a)]
        p=hh(rays,a,A,rho,box=box)
        print(" rho",[str(x) for x in rho],"res",[str(x) for x in r],"P",p,"chi",euler(p),"%.1fs"%(time.time()-t),flush=True)
A4=[[0,1,2,-1],[-1,0,3,5],[-2,-3,0,7],[1,-5,-7,0]]   # generic skew, check det !=0
# Pfaffian nonzero check: a01*a23-a02*a13+a03*a12
assert A4[0][1]*A4[2][3]-A4[0][2]*A4[1][3]+A4[0][3]*A4[1][2]!=0
# P^4
rays=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
for m in [1,2]:
    a=(0,0,0,0,m)
    rhos=[(Fr(1,3),Fr(2,7),Fr(1,5),Fr(3,11)),(0,0,0,0),(Fr(1,2),0,0,0),(-1,0,0,0),(0,0,0,-1)]
    run("P^4 m=%d generic sigma"%m,rays,a,A4,rhos,box=m+6)
