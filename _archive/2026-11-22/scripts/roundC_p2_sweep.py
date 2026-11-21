import sys,itertools,json
sys.path.insert(0,'.')
from roundC_toric_cech import *
A=[[0,1],[P-1,0]]
rays,cones=FANS['P2']
vals=[Fr(x) for x in (-2,-1,0,1,2,3)]+[Fr(1,2),Fr(-1,2)]
out={}
m=int(sys.argv[1])
for r1 in vals:
    for r2 in vals:
        r3=-m-r1-r2
        a=[0,0,m]; rho=[r1,r2]
        pa=Pstr(cech_poly(rays,cones,a,A,rho,box=abs(m)+4,kind='A'))
        pb=Pstr(cech_poly(rays,cones,a,A,rho,box=abs(m)+4,kind='B'))
        print(m,str(r1),str(r2),str(r3),"A",pa,"B",pb,flush=True)
