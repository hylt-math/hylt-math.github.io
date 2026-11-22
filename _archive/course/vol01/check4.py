import check
check.N=4
from check import *
import random, itertools
from fractions import Fraction as Fr
random.seed(7)
n=2
def rpoly(deg=1):
    p={}
    for _ in range(3):
        k=[0]*4
        for _ in range(random.randint(0,deg)): k[random.randrange(4)]+=1
        p=padd(p,{tuple(k):Fr(random.randint(-2,2))})
    return p
def r1form():
    r={}
    for i in range(4):
        p=rpoly()
        if p: r=fadd(r,{(i,):p})
    return r
def rmat(): return [[r1form() for _ in range(n)] for _ in range(n)]
def mw(A,B):
    R=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): R[i][j]=fadd(R[i][j],wedge(A[i][k],B[k][j]))
    return R
def ma(A,B,s=1): return [[fadd(A[i][j],B[i][j],s) for j in range(n)] for i in range(n)]
def md(A): return [[d(A[i][j]) for j in range(n)] for i in range(n)]
def msc(A,c): return [[{k:pscale(v,c) for k,v in A[i][j].items()} for j in range(n)] for i in range(n)]
def tr(A):
    r={}
    for i in range(n): r=fadd(r,A[i][i])
    return r
def curv(A): return ma(md(A),mw(A,A))
A0=rmat();A1=rmat()
a=ma(A1,A0,-1)
F0=curv(A0);F1=curv(A1)
dA=ma(ma(md(a),mw(A0,a)),mw(a,A0))   # d_{nabla0} a = da + A0^a + a^A0
T=fadd(fadd(tr(mw(a,F0)),{k:{m:c*Fr(1,2) for m,c in v.items()} for k,v in tr(mw(a,dA)).items()}),
       {k:{m:c*Fr(1,3) for m,c in v.items()} for k,v in tr(mw(a,mw(a,a))).items()})
T={k:{m:2*c for m,c in v.items()} for k,v in T.items()}
lhs=fadd(tr(mw(F1,F1)),tr(mw(F0,F0)),-1)
print("tr F1^2 - tr F0^2 == dT :", lhs==d(T), " (nonzero:",bool(lhs),")")
# Bianchi random
Bi=ma(ma(md(F0),mw(A0,F0)),mw(F0,A0),-1)
print("Bianchi random A:",all(not Bi[i][j] for i in range(n) for j in range(n)))
# gauge: F' = g^-1 F g with random polynomial invertible g (unipotent-ish)
one=lambda:{():const(1)}
g=[[one(),{():rpoly()}],[{},one()]]
# g = [[1,p],[0,1]] -> inverse [[1,-p],[0,1]]
gi=[[one(),{():pscale(g[0][1][()],-1)}],[{},one()]]
Ap=ma(mw(mw(gi,A0),g),mw(gi,md(g)))
Fp=curv(Ap)
print("gauge covariance random:",Fp==mw(mw(gi,F0),g))
# d_nabla^2 s = F s: s column of functions
s=[{():rpoly()} for _ in range(n)]
def ds_plus(sv): # nabla s = ds + A s  (E-valued 1-form as column of 1-forms)
    return [fadd(d(sv[i]), (lambda r:r)( __import__('functools').reduce(lambda u,v:fadd(u,v),[wedge(A0[i][j],sv[j]) for j in range(n)],{}))) for i in range(n)]
ns=ds_plus(s)
# d_nabla of column of 1-forms tau: d tau + A ^ tau
nn=[fadd(d(ns[i]), __import__('functools').reduce(lambda u,v:fadd(u,v),[wedge(A0[i][j],ns[j]) for j in range(n)],{})) for i in range(n)]
Fs=[__import__('functools').reduce(lambda u,v:fadd(u,v),[wedge(F0[i][j],s[j]) for j in range(n)],{}) for i in range(n)]
print("d_nabla^2 s = F s :",nn==Fs)
