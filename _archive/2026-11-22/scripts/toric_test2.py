import sys; sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
# P^2: rays e1,e2,-e1-e2 ; L=O(m D_0) , D_0 = third ray
rays=[(1,0),(0,1),(-1,-1)]
A=[[0,1],[-1,0]]
for m in [1,2,3,4]:
    for rho in [(Fr(1,3),Fr(2,7)), (0,0), (-1,-1),(-2,0),(1,0),(Fr(1,2),0),(-3,-5),(2,3)]:
        a=(0,0,m)
        r=[sum(x*y for x,y in zip(rho,u))-ai for u,ai in zip(rays,a)]
        p=hh(rays,a,A,rho)
        print("m",m,"rho",rho,"res",[str(x) for x in r],"P",p,"chi",euler(p))
