import sys
sys.path.insert(0,'.')
from roundC_toric_cech import *
A=[[0,1],[P-1,0]]
rays,cones=FANS['P1xP1']
vals=[Fr(x) for x in (0,1,-1,2,-2)]+[Fr(1,2)]
p=int(sys.argv[1])
for q in (-4,-2,-1,0,1,2):
    for r1 in vals:
        for r3 in vals:
            rho=[r1,r3]; a=[p,0,q,0]
            res=[r1-p,-r1-0,r3-q,-r3-0]   # r_i=<rho,u_i>-a_i : u=(1,0),(-1,0),(0,1),(0,-1)
            pa=Pstr(cech_poly(rays,cones,a,A,rho,box=max(abs(p),abs(q))+5,kind='A'))
            print(p,q,[str(x) for x in res],pa,flush=True)
