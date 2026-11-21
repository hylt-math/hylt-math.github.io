import glob,re,ast
from fractions import Fraction as Fr
rows=[]
for fn in glob.glob('sweepA_m*.txt')+['sweep_m0.txt','sweep_m-3.txt']:
    for line in open(fn):
        line=line.strip()
        if not line: continue
        if ' A ' in line:   # old format
            head,rest=line.split(' A ',1); pa=rest.split(' B ')[0]; f=head.split()
        else:
            f=line.split()[:4]; pa=line[line.index('['):]
        m=int(f[0]); r=[Fr(x) for x in f[1:4]]; P=ast.literal_eval(pa)
        rows.append((m,r,P+[0]*(3-len(P))))
print(len(rows),"rows")
def pred(r):
    allint=all(x.denominator==1 for x in r)
    if any(x==1 for x in r): return None
    base=[0,0,3]
    if allint and all(x<=0 for x in r): return [1,2,4]
    if allint and all(x>=2 for x in r): return [0,0,4,2,1]
    return base
bad=0;n=0
for m,r,P in rows:
    p=pred(r)
    if p is None: continue
    Pp=P+[0]*(5-len(P)); pp=p+[0]*(5-len(p)); n+=1
    if Pp!=pp: bad+=1; print("MISMATCH",m,[str(x) for x in r],P,p)
print("all r_i!=1 rows:",n,"mismatches",bad)
# resonance rows
res={}
for m,r,P in rows:
    k=sum(1 for x in r if x==1)
    if k: res.setdefault((k,m),[]).append(([str(x) for x in r],P))
for key in sorted(res):
    print(key); 
    for r,P in res[key][:40]: print("   ",r,P)
