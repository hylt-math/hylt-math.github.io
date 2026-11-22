# Neron-Severi rank of the real torus (Z^4, J) with J^2=-1, exact arithmetic in Q(sqrt2,sqrt3)
from fractions import Fraction as Fr
import itertools, sys
# element: tuple (a,b,c,d) = a + b s2 + c s3 + d s6
def add(x,y): return tuple(p+q for p,q in zip(x,y))
def neg(x): return tuple(-p for p in x)
def smul(c,x): return tuple(c*p for p in x)
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e+2*b*f+3*c*g+6*d*h,
            a*f+b*e+3*(c*h+d*g),
            a*g+c*e+2*(b*h+d*f),
            a*h+d*e+b*g+c*f)
Z=(Fr(0),)*4; ONE=(Fr(1),Fr(0),Fr(0),Fr(0))
def el(a=0,b=0,c=0,d=0): return (Fr(a),Fr(b),Fr(c),Fr(d))
def matmul(A,B):
    n=len(A); return [[ (lambda s: s)(sum_el([mul(A[i][k],B[k][j]) for k in range(n)])) for j in range(n)] for i in range(n)]
def sum_el(l):
    r=Z
    for x in l: r=add(r,x)
    return r
def ident(n): return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def matadd(A,B): return [[add(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def matneg(A): return [[neg(a) for a in r] for r in A]
def transpose(A): return [list(r) for r in zip(*A)]
def make_J(S_entries):
    n=4
    S=ident(n)
    N=[[Z]*n for _ in range(n)]
    for (i,j),v in S_entries.items():
        S[i][j]=v; N[i][j]=v
    # inverse of unipotent upper-triangular S = I+N: I - N + N^2 - N^3
    N2=matmul(N,N); N3=matmul(N2,N)
    Sinv=matadd(matadd(ident(n),matneg(N)),matadd(N2,matneg(N3)))
    J0=[[Z]*4 for _ in range(4)]
    one=ONE
    J0[1][0]=one; J0[0][1]=neg(one); J0[3][2]=one; J0[2][3]=neg(one)
    J=matmul(matmul(S,J0),Sinv)
    return J,S
def ns_rank(J):
    # unknown E antisymmetric 4x4: basis E_ij (i<j), 6 unknowns. equation J^T E J - E = 0
    pairs=list(itertools.combinations(range(4),2))
    rows=[]
    cols=[]
    for (i,j) in pairs:
        E=[[Z]*4 for _ in range(4)]
        E[i][j]=ONE; E[j][i]=neg(ONE)
        R=matadd(matmul(matmul(transpose(J),E),J),matneg(E))
        cols.append([R[a][b][t] for a in range(4) for b in range(4) for t in range(4)])
    M=[[cols[c][r] for c in range(6)] for r in range(len(cols[0]))]
    # rank over Q
    M=[row[:] for row in M]; rank=0
    rws=len(M)
    for c in range(6):
        piv=None
        for r in range(rank,rws):
            if M[r][c]!=0: piv=r;break
        if piv is None: continue
        M[rank],M[piv]=M[piv],M[rank]
        pv=M[rank][c]
        M[rank]=[x/pv for x in M[rank]]
        for r in range(rws):
            if r!=rank and M[r][c]!=0:
                f=M[r][c]; M[r]=[x-f*y for x,y in zip(M[r],M[rank])]
        rank+=1
    return 6-rank  # dim of rational solution space
if __name__=="__main__":
    J,S=make_J({})
    print("product torus nullity:",ns_rank(J))
    cands={
      "A":{(0,2):el(0,1),(1,3):el(0,0,1)},
      "B":{(0,2):el(0,1),(1,3):el(0,0,1),(0,3):el(0,0,0,1)},
      "C":{(0,2):el(0,1),(1,3):el(0,0,1),(0,3):el(0,0,0,1),(0,1):el(1)},
      "D":{(0,2):el(0,1),(1,3):el(0,0,1),(0,1):el(0,0,0,1)},
      "E":{(0,2):el(0,1),(1,3):el(0,0,1),(0,1):el(0,1,0,0)},
      "F":{(0,2):el(0,1),(1,3):el(0,0,1),(0,1):el(0,0,0,1),(2,3):el(0,0,0,1)},
    }
    for k,v in cands.items():
        J,S=make_J(v)
        J2=matmul(J,J)
        assert all(J2[i][j]==(neg(ONE) if i==j else Z) for i in range(4) for j in range(4))
        print(k,"nullity (NS rank over Q):",ns_rank(J))
