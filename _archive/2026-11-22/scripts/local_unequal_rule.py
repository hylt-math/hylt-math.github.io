# Test the rule for the triple point xy(x-y) with unequal residues:
#  stalk = C^4[-2] + R, R = (1,2,1)-stalk-like: all s_i in Z_{<=0}: (1,2,1)+... ; sum s in Z, sum<=1, not all integers: (0,1,0); else 0.
import itertools,sys
from fractions import Fraction
import local_unequal as U
P=U.P
z={(1,0):1}; w={(0,1):1}; zw={(1,0):1,(0,1):P-1}
den=6; vals=[Fraction(k,den) for k in range(-12,13)]
def rule(s):
    tot=sum(s)
    if any(x==1 for x in s): return None
    if all(x.denominator==1 and x<=0 for x in s): return (1,3,6)
    if tot.denominator==1 and tot<=1 and not all(x.denominator==1 for x in s): return (0,1,5)
    if all(x.denominator==1 for x in s) and tot<=1:  # integers but some positive>=2: unclear
        return 'int-pos'
    return (0,0,4)
bad=0;n=0;unk=0
import random
random.seed(1)
trip=[t for t in itertools.combinations_with_replacement(vals,3)]
random.shuffle(trip)
for s in trip[:600]:
    r=rule(s)
    if r is None: continue
    got=tuple(U.stalk([(z,s[0]),(w,s[1]),(zw,s[2])],1,1,3,18))
    n+=1
    if r=='int-pos': unk+=1; print("int-pos",[str(x) for x in s],got); continue
    if got!=r: bad+=1; print("MISMATCH",[str(x) for x in s],got,r,flush=True)
print("tested",n,"mismatches",bad,"unclassified",unk)
