import numpy as np, collections
from pkcore import *
def unknown_shifts(S):
    sh=[]
    for u,(a,b) in enumerate(S.upairs):
        for r in range(S.nI):
            k=np.nonzero(S.I2[r])[0][0]; cl=S.qclass[k]
            sh.append(tuple(cl[i]-S.mons[a][i]-S.mons[b][i] for i in range(3)))
    return sh
if __name__=="__main__":
    S=Setup(3,FS['fermat']); sh=unknown_shifts(S)
    cnt=collections.Counter(sh); print("number of distinct shifts",len(cnt)); 
    e=np.load('ms_m3_fermat_100.npy')
    wt=collections.defaultdict(float)
    for s,x in zip(sh,e): wt[s]+=x*x
    nu=[(2,-1,-1),(-1,2,-1),(-1,-1,2)]
    print("shifts nu_k: unknown counts",[cnt[s] for s in nu],"; minimizer norm^2 on them",[round(wt[s],3) for s in nu])
    tot=sum(wt.values()); print("total |e|^2",round(tot,3),"on nu shifts",round(sum(wt[s] for s in nu),3))
    for s,v in sorted(wt.items(),key=lambda kv:-kv[1])[:12]: print(s,round(v,3),cnt[s])
    # B0 shifts
    import itertools
    B0sh=collections.Counter()
    for a in range(S.N):
        for b in range(a+1,S.N):
            for k in np.nonzero(S.B0[a,b])[0]:
                cl=S.qclass[k]; B0sh[tuple(cl[i]-S.mons[a][i]-S.mons[b][i] for i in range(3))]+=1
    print("B0 shifts:",dict(B0sh))
