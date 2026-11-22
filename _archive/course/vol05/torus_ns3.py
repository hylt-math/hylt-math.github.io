from torus_ns2 import *
import random, itertools
random.seed(11)
basis=[el(0,1),el(0,0,1),el(0,0,0,1)]
res=[]
for t in range(3000):
    S=ident(4)
    k=random.choice([2,3,4])
    pos=random.sample([(i,j) for i in range(4) for j in range(4) if i!=j],k)
    for p in pos: S[p[0]][p[1]]=random.choice(basis)
    try: J=J_from_S(S)
    except StopIteration: continue
    if ns_rank(J)==0: res.append((k,pos,[S[p[0]][p[1]] for p in pos]))
res.sort(key=lambda x:x[0])
print(len(res))
for r in res[:6]: print(r)
