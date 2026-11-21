import sys; sys.path.insert(0,'.')
from toric_hh import *
from math import comb
def dims(rays,a,box):
    n=len(rays[0]); tot=[0]*(n+1)
    for chi in itertools.product(range(-box,box+1),repeat=n):
        cons=[];ok=True
        for u,ai in zip(rays,a):
            c=sum(x*y for x,y in zip(chi,u))+ai
            if c<-1: ok=False;break
            if c==-1: cons.append(u)
        if not ok: continue
        for b in range(n+1):
            rows=[]
            for u in cons:
                if b<n: rows+=wedge_matrix([x%P for x in u],n,b)
            tot[b]+=len(nullspace(rows,len(subsets(n,b))))
    return tot
n=4
rays=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
for m in [1,2]:
    print(m,dims(rays,(0,0,0,0,m),m+2),[comb(m+n+1+n-(n-b),m+n+1)*comb(m+n,n-b) if m+n>=n-b else 0 for b in range(n+1)])
