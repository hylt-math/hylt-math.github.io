from torus_ns import *
import random
def finv(x):
    # solve x*y=1 over Q
    cols=[mul(x,b) for b in (el(1),el(0,1),el(0,0,1),el(0,0,0,1))]
    M=[[cols[c][r] for c in range(4)]+[ONE[r]] for r in range(4)]
    n=4
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c]!=0)
        M[c],M[piv]=M[piv],M[c]
        pv=M[c][c]; M[c]=[v/pv for v in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return tuple(M[r][4] for r in range(4))
def isz(x): return all(v==0 for v in x)
def matinv(A):
    n=len(A)
    M=[row[:]+[ONE if i==j else Z for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        piv=next(r for r in range(c,n) if not isz(M[r][c]))
        M[c],M[piv]=M[piv],M[c]
        iv=finv(M[c][c]); M[c]=[mul(iv,v) for v in M[c]]
        for r in range(n):
            if r!=c and not isz(M[r][c]):
                f=M[r][c]; M[r]=[add(a,neg(mul(f,b))) for a,b in zip(M[r],M[c])]
    return [row[n:] for row in M]
J0=[[Z]*4 for _ in range(4)]
J0[1][0]=ONE; J0[0][1]=neg(ONE); J0[3][2]=ONE; J0[2][3]=neg(ONE)
def J_from_S(S): return matmul(matmul(S,J0),matinv(S))
random.seed(5)
found=None
for t in range(200):
    S=[[el(random.choice([0,0,1,-1]),random.choice([0,0,1,-1]),random.choice([0,0,1]),random.choice([0,0,1])) for _ in range(4)] for _ in range(4)]
    try:
        J=J_from_S(S)
    except StopIteration:
        continue
    n=ns_rank(J)
    if n==0:
        found=S;break
print("found" if found else "none")
if found:
    for r in found: print([tuple(str(v) for v in x) for x in r])
