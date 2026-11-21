import sys,itertools,random; sys.path.insert(0,'.')
from toric_crit import *
from collections import Counter
def avec(name,ms):
    rays=FANS[name]; a=[0]*len(rays)
    if name=='P4': a[4]=ms[0]
    if name=='P2xP2': a[2]=ms[0];a[5]=ms[1]
    if name=='P1^4':
        for k in range(4): a[2*k+1]=ms[k]
    if name=='P1xP3': a[1]=ms[0]; a[5]=ms[1]
    if name=='P1xP1xP2': a[1]=ms[0];a[3]=ms[1];a[6]=ms[2]
    return a
tests=[('P4',(1,)),('P4',(2,)),('P2xP2',(1,2)),('P1^4',(1,1,1,1)),('P1^4',(1,2,1,3)),('P1xP3',(1,1)),('P1xP1xP2',(1,1,1))]
tot=0;bad=0;kinds=Counter()
for name,ms in tests:
    rays=FANS[name]; n=4; a=avec(name,ms); box=max(a)+n+3
    for seed in [101,102]:
        A=randA(n,seed,997)
        for rho in itertools.product(range(-2,2),repeat=4):
            p1=crit_poly(rays,a,A,rho,box); p2=generic_pred(rays,a,rho,box)
            tot+=1
            if p1!=p2: bad+=1; print("MISMATCH",name,ms,rho,p1,p2)
            else: kinds[(name,ms)]+=1
        for rho in [(Fr(1,2),0,0,0),(Fr(1,3),Fr(1,2),0,0),(0,0,Fr(2,5),-1)]:
            p1=crit_poly(rays,a,A,rho,box); p2=generic_pred(rays,a,rho,box); tot+=1
            if p1!=p2: bad+=1; print("MISMATCH",name,ms,rho,p1,p2)
print("generic prediction vs criterion: mismatches",bad,"of",tot)
