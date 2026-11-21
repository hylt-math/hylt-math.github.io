import glob,ast,itertools
from fractions import Fraction as Fr
# rays 0:(1,0) 1:(-1,0) 2:(0,1) 3:(0,-1); cycle 0-2-1-3-0 ; D_0,D_1 ~ F1, D_2,D_3 ~ F2 ; L=O(p,q)
adj={0:{2,3},1:{2,3},2:{0,1},3:{0,1}}
nodes=[(0,2),(0,3),(1,2),(1,3)]
def comps(S):
    S=set(S); seen=set(); k=0
    for s in S:
        if s in seen: continue
        k+=1; st=[s]
        while st:
            x=st.pop()
            if x in seen: continue
            seen.add(x); st+= [y for y in adj[x] if y in S]
    return k
def reduced_betti(S):
    # reduced cohomology of induced subcomplex of the 4-cycle on S (as dict deg->dim), H^{-1}(empty)=1
    S=set(S)
    if not S: return {-1:1}
    if len(S)==4: return {1:1}
    return {0:comps(S)-1} if comps(S)-1>0 else {}
def poly_main(r,integral):
    P=[0]*6
    for q in range(6): pass
    P[2]+=4
    if integral:
        S=[i for i in range(4) if r[i]>=2]
        for deg,dim in reduced_betti(S).items():
            q=deg+1  # H^q(X;..)_chi = Htilde^{q-1}
            for j,c in enumerate([1,2,1]): P[q+j]+=dim*c
    return P
def h0_forest(Rset,deg):
    # components in Rset (P^1's), glue at nodes whose both rays in Rset; deg: dict ray->degree. returns (h0,h1)
    comp=sorted(Rset)
    nds=[n for n in nodes if n[0] in Rset and n[1] in Rset]
    # variables: coefficients of each component with deg>=0 ; evaluation at node: point 0 or inf (two rays: ray a<b ordering)
    var={}
    for c in comp:
        d=deg[c]
        if d>=0:
            for k in range(d+1): var[(c,k)]=len(var)
    rows=[]
    for (a,b) in nds:
        row=[0]*len(var)
        for c,sign in ((a,1),(b,-1)):
            d=deg[c]
            if d<0: continue
            # node point on component c: determined by the other ray's position: use 0 for smaller other ray index else inf
            other=b if c==a else a
            pos=0 if other==min(adj[c]) else d
            row[var[(c,pos)]]+=sign
        rows.append(row)
    import numpy
    rk=int(numpy.linalg.matrix_rank(numpy.array(rows,dtype=float))) if rows and var else 0
    h0=len(var)-rk
    chi=sum(deg[c]+1 for c in comp)-len(nds)
    return h0,h0-chi
def poly_res(r,p,q):
    R={i for i in range(4) if r[i]==1}
    LD={0:q,1:q,2:p,3:p}
    N={i:LD[i] for i in R}          # N_{D_i}=O(0)
    K={i:LD[i]+2 for i in R}
    P=[0]*6
    h0N=sum(max(N[i]+1,0) for i in R); h1N=sum(max(-N[i]-1,0) for i in R)
    h0K,h1K=h0_forest(R,K)
    nu=sum(1 for (a,b) in nodes if a not in R and b not in R)
    P[1]+=h0N; P[2]+=h1N+h0K+nu; P[3]+=h1K
    return P
tot=bad=0; resn=resbad=0
for fn in sorted(glob.glob('p1p1A_p*.txt')):
    for line in open(fn):
        if not line.startswith(('-','0','1','2')): continue
        i=line.index('['); head=line[:i].split(); 
        p,q=int(head[0]),int(head[1]); rr=ast.literal_eval(line[i:line.index(']')+1]); r=[Fr(x) for x in rr]
        rest=line[line.index(']')+1:].strip(); P=ast.literal_eval(rest); P=P+[0]*(6-len(P))
        integral=all(x.denominator==1 for x in r)
        if any(x==1 for x in r):
            if len([x for x in r if x==1])==4: continue
            if integral: continue   # trivial L_U: connecting maps with H_c(T); not predicted by the simple sheaf formula
            pr=poly_res(r,p,q); resn+=1
            if pr!=P: resbad+=1; print("RES MISMATCH",p,q,[str(x) for x in r],P,pr)
        else:
            pr=poly_main(r,integral); tot+=1
            if pr!=P: bad+=1; print("MISMATCH",p,q,[str(x) for x in r],P,pr)
print("non-resonant rows",tot,"mismatches",bad,"| resonant rows with L_U nontrivial",resn,"mismatches",resbad)
