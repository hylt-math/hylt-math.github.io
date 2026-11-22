# H^*(C x J) for a genus g curve: H^*(C) = <1,alpha_i,beta_i,eta>, H^*(J)=Lambda(a_i,b_i) ; graded tensor product.
from fractions import Fraction as F
from math import factorial
import itertools
def make(g):
    # generators: C-odd: alpha_i (0..g-1), beta_i (g..2g-1); J-odd: a_i,b_i  -> 2g generators.
    # element: dict {(cC, mask): coeff}; cC in {'1',('al',i),('be',i),'eta'}; mask bitmask over 2g J-generators (a_i bit i, b_i bit g+i)
    def cdeg(c): return 0 if c=='1' else (2 if c=='eta' else 1)
    def cmul(c,d):
        # returns (sign, result) or None
        if c=='1': return (1,d)
        if d=='1': return (1,c)
        if c=='eta' or d=='eta': return None
        (t,i),(s,j)=c,d
        if t=='al' and s=='be' and i==j: return (1,'eta')
        if t=='be' and s=='al' and i==j: return (-1,'eta')
        return None
    def jmul(m1,m2):
        if m1&m2: return None
        # sign of merging: count inversions
        sign=1
        for b in range(2*g):
            if m2>>b &1:
                # number of bits in m1 above b
                cnt=bin(m1>>(b+1)).count('1')
                if cnt%2: sign=-sign
        return sign,m1|m2
    def jdeg(m): return bin(m).count('1')
    def mul(x,y):
        r={}
        for (c,m),a in x.items():
            for (d,n),b in y.items():
                cm=cmul(c,d)
                if cm is None: continue
                jm=jmul(m,n)
                if jm is None: continue
                s=cm[0]*jm[0]*(-1)**(jdeg(m)*cdeg(d))
                k=(cm[1],jm[1]); r[k]=r.get(k,0)+s*a*b
        return {k:v for k,v in r.items() if v!=0}
    def add(x,y,cy=1):
        r=dict(x)
        for k,v in y.items(): r[k]=r.get(k,0)+cy*v
        return {k:v for k,v in r.items() if v!=0}
    return mul,add
def run(g,d):
    mul,add=make(g)
    one={('1',0):F(1)}
    eta={('eta',0):F(1)}
    # theta = sum a_i b_i ; gamma = sum (a_i beta_i - b_i alpha_i)
    theta={}
    gamma={}
    for i in range(g):
        theta=add(theta,{('1',(1<<i)|(1<<(g+i))):F(1)})
        gamma=add(gamma,{(('be',i),1<<i):F(1)})
        gamma=add(gamma,{(('al',i),1<<(g+i)):F(-1)})
    g2=mul(gamma,gamma)
    et=mul(eta,theta)
    ok = g2=={k:-2*v for k,v in et.items()}
    # exp(d eta+gamma) * (1+(1-g)eta)
    x=add({k:d*v for k,v in eta.items()},gamma)
    e=dict(one); term=dict(one)
    for n in range(1,2*g+3):
        term=mul(term,x); term={k:v/n for k,v in term.items()}
        e=add(e,term)
    td=add(one,{k:(1-g)*v for k,v in eta.items()})
    ch=mul(e,td)
    # push forward along C: collect terms with cC=='eta' -> J-class
    push={}
    for (c,m),v in ch.items():
        if c=='eta': push[m]=push.get(m,0)+v
    # expected (d+1-g) - theta, theta has mask terms
    exp_={0:F(d+1-g)}
    for i in range(g): exp_[(1<<i)|(1<<(g+i))]=F(-1)
    return ok, push==exp_
for g in (1,2,3):
    for d in (-2,0,1,3,2*g):
        print(g,d,run(g,d))
