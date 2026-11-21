import sys
sys.path.insert(0,'.')
from roundC_toric_cech import *
A=[[0,1],[P-1,0]]
rays,cones=FANS['P2']
vals=[Fr(x) for x in (-2,-1,0,1,2,3)]+[Fr(1,2),Fr(-1,2)]
m=int(sys.argv[1])
for r1 in vals:
    for r2 in vals:
        r3=-m-r1-r2
        pa=Pstr(cech_poly(rays,cones,[0,0,m],A,[r1,r2],box=abs(m)+5,kind='A'))
        print(m,str(r1),str(r2),str(r3),pa,flush=True)
