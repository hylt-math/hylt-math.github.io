import sys,random,itertools; sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
rays=[(1,0,0,0),(0,1,0,0),(-1,-1,0,0),(0,0,1,0),(0,0,0,1),(0,0,-1,-1)]
m1,m2=1,2; a=(0,0,m1,0,0,m2)
Ablock=[[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]
def randA(seed,big=997):
    r=random.Random(seed)
    A=[[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i+1,4):
            x=r.randint(-big,big); A[i][j]=x; A[j][i]=-x
    return A
def poly_mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return out
surf={'gen':[0,0,3],'Rj':[1,2,4]}
for name,A in [('product A',Ablock),('generic A',randA(5))]:
    print("==",name)
    for rho in [(Fr(1,3),Fr(2,7),Fr(1,5),Fr(3,11)),(0,0,0,0),(-1,0,0,0),(0,0,-1,0),(-1,-1,0,0),(-1,0,-1,0),(Fr(1,2),0,0,0),(Fr(1,2),0,Fr(1,3),0)]:
        r=[sum(x*y for x,y in zip(rho,u))-ai for u,ai in zip(rays,a)]
        p=hh(rays,a,A,rho,box=7)
        print(" rho",[str(x) for x in rho],"res",[str(x) for x in r],"P",p,"chi",euler(p),flush=True)
print("product-formula refs: gen*gen",poly_mul(surf['gen'],surf['gen']),"Rj*Rj",poly_mul(surf['Rj'],surf['Rj']),"Rj*gen",poly_mul(surf['Rj'],surf['gen']))
