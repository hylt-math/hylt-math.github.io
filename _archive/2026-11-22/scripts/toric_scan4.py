import sys,random,itertools; sys.path.insert(0,'.')
from toric_hh import *
from fractions import Fraction as Fr
from collections import Counter
rays=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
def randA(seed):
    r=random.Random(seed)
    while True:
        a={}
        A=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i+1,4):
                x=r.randint(-4,4); A[i][j]=x; A[j][i]=-x
        if A[0][1]*A[2][3]-A[0][2]*A[1][3]+A[0][3]*A[1][2]!=0: return A
m=int(sys.argv[1]) if len(sys.argv)>1 else 1
a=(0,0,0,0,m)
base=[1,4,6,4,6]
for seed in [1,2,3]:
    A=randA(seed); print("seed",seed,"A",A)
    cnt=Counter(); ex={}
    for rho in itertools.product(range(-2,2),repeat=4):
        r=[sum(x*y for x,y in zip(rho,u))-ai for u,ai in zip(rays,a)]
        cls=("allnonpos" if all(x<=0 for x in r) else "other")
        p=tuple(hh(rays,a,A,rho,box=m+6))
        cnt[(cls,p)]+=1; ex.setdefault((cls,p),(rho,r))
    for k,v in sorted(cnt.items()): print(" ",k,v,"e.g. rho",ex[k][0],"res",ex[k][1])
