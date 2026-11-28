import re,sys
# 問題数と解答の対応を機械的に確認
P=[];S=[]
for f in 'ABC':
    P+=re.findall(r'\\begin\{probl\}\{([^}]*)\}\{([^}]*)\}',open('part%s.tex'%f).read())
    S+=re.findall(r'\\begin\{soll\}\{([^}]*)\}',open('sol%s.tex'%f).read())
pk=[k for _,k in P]
print('問題数',len(P),' 解答数',len(S))
print('キー一致(集合)',set(pk)==set(S),' 順序一致',pk==S)
print('重複キー',[k for k in set(pk) if pk.count(k)>1])
from collections import Counter
print('レベル別',Counter(l for l,_ in P))
# aux の番号
import os
aux=open('vol01.aux' if os.path.exists('vol01.aux') else 'main.aux').read()
nums=dict(re.findall(r'\\newlabel\{pr:([^}]*)\}\{\{(\d+)\}',aux))
print('aux 番号数',len(nums),' 最大',max(map(int,nums.values())),' 連番',sorted(map(int,nums.values()))==list(range(1,len(P)+1)))
# 参照されている pr: が全て定義されているか
txt=''.join(open(f).read() for f in ['partA.tex','partB.tex','partC.tex','solA.tex','solB.tex','solC.tex','back.tex','front.tex'])
refs=set(re.findall(r'pr:([A-Za-z0-9_]+)',txt))
print('未定義 pr 参照',sorted(r for r in refs if r not in pk))
# 節ごと
import collections
sec=collections.Counter()
for f in 'ABC':
    t=open('part%s.tex'%f).read()
    cur=None
    for m in re.finditer(r'\\subsection\*\{[^}]*§(\d+)|\\begin\{probl\}',t):
        if m.group(1): cur=int(m.group(1))
        else: sec[cur]+=1
print('節ごとの問題数',dict(sorted(sec.items())))
