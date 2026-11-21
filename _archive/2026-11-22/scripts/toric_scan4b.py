import sys,random,itertools; sys.path.insert(0,'.')
from toric_hh import *
from collections import Counter
rays=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
def randA(seed,big):
    r=random.Random(seed)
    while True:
        A=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i+1,4):
                x=r.randint(-big,big); A[i][j]=x; A[j][i]=-x
        if A[0][1]*A[2][3]-A[0][2]*A[1][3]+A[0][3]*A[1][2]!=0: return A
m=1; a=(0,0,0,0,m)
for seed in [11,12,13,14]:
    A=randA(seed,997); cnt=Counter(); ex={}
    for rho in itertools.product(range(-2,2),repeat=4):
        r=[sum(x*y for x,y in zip(rho,u))-ai for u,ai in zip(rays,a)]
        if not all(x<=0 and x!=1 for x in r): continue
        p=tuple(hh(rays,a,A,rho,box=m+6)); cnt[p]+=1; ex.setdefault(p,(rho,r))
    print("seed",seed,{k:(v,ex[k]) for k,v in cnt.items()})
