# independent exact check: field Q(sqrt2,sqrt3) elements as 4-vectors over Q
from fractions import Fraction as F
import itertools
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e+2*b*f+3*c*g+6*d*h, a*f+b*e+3*(c*h+d*g), a*g+c*e+2*(b*h+d*f), a*h+d*e+b*g+c*f)
def add(x,y): return tuple(p+q for p,q in zip(x,y))
def neg(x): return tuple(-p for p in x)
Z=(F(0),)*4; ONE=(F(1),F(0),F(0),F(0))
def e(a=0,b=0,c=0,d=0): return (F(a),F(b),F(c),F(d))
def conj_inv(x):
    # inverse via norm: use solving linear system
    cols=[mul(x,b) for b in (e(1),e(0,1),e(0,0,1),e(0,0,0,1))]
    M=[[cols[c][r] for c in range(4)]+[ONE[r]] for r in range(4)]
    for c in range(4):
        p=next(r for r in range(c,4) if M[r][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[v/pv for v in M[c]]
        for r in range(4):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[a-f*b for a,b in zip(M[r],M[c])]
    return tuple(M[r][4] for r in range(4))
def mm(A,B):
    n=len(A); out=[[Z]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s=Z
            for k in range(n): s=add(s,mul(A[i][k],B[k][j]))
            out[i][j]=s
    return out
def inv(A):
    n=len(A); M=[r[:]+[ONE if i==j else Z for j in range(n)] for i,r in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=Z); M[c],M[p]=M[p],M[c]
        iv=conj_inv(M[c][c]); M[c]=[mul(iv,v) for v in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=Z:
                f=M[r][c]; M[r]=[add(a,neg(mul(f,b))) for a,b in zip(M[r],M[c])]
    return [r[n:] for r in M]
def T(A): return [list(r) for r in zip(*A)]
s2=e(0,1); s3=e(0,0,1)
S=[[ONE,s2,s3,Z],[Z,ONE,Z,Z],[Z,Z,ONE,Z],[s2,Z,Z,ONE]]
J0=[[Z]*4 for _ in range(4)]
J0[1][0]=ONE; J0[0][1]=neg(ONE); J0[3][2]=ONE; J0[2][3]=neg(ONE)
def nullity(J):
    cols=[]
    for (i,j) in itertools.combinations(range(4),2):
        E=[[Z]*4 for _ in range(4)]; E[i][j]=ONE; E[j][i]=neg(ONE)
        R=mm(mm(T(J),E),J)
        R=[[add(R[a][b],neg(E[a][b])) for b in range(4)] for a in range(4)]
        cols.append([R[a][b][t] for a in range(4) for b in range(4) for t in range(4)])
    M=[[cols[c][r] for c in range(6)] for r in range(len(cols[0]))]
    rank=0
    for c in range(6):
        p=next((r for r in range(rank,len(M)) if M[r][c]!=0),None)
        if p is None: continue
        M[rank],M[p]=M[p],M[rank]; pv=M[rank][c]; M[rank]=[x/pv for x in M[rank]]
        for r in range(len(M)):
            if r!=rank and M[r][c]!=0:
                f=M[r][c]; M[r]=[x-f*y for x,y in zip(M[r],M[rank])]
        rank+=1
    return 6-rank
J=mm(mm(S,J0),inv(S))
J2=mm(J,J)
print("J^2=-1:", all(J2[i][j]==(neg(ONE) if i==j else Z) for i in range(4) for j in range(4)))
print("J0 nullity:", nullity(J0))
print("problem S nullity:", nullity(J))
# note: det S
