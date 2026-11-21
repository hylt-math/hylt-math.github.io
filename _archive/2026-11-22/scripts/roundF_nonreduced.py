# Round F: non-reduced D on P^2: sigma=Pi_F, F=x^2 y (double line + line) and F=x^3 (triple line), F = x^2(x+y)?? (same type as x^2y).
# Computes HH dims for m=-15..15 via sing_table.hyper and checks fitted closed formulas.
import sys; sys.path.insert(0,'.')
import sing_table as S
P=S.P
def mk(*t): return {k:v%P for k,v in t}
F={'x2y':mk(((2,1,0),1)),'x3':mk(((3,0,0),1)),'x2(x+y)':mk(((3,0,0),1),((2,1,0),1))}
def formula_x2y(m):
    """P(t) as list [H0..H4]: m>=-2: [3|m](1+t)+3t^2+(m+2)(t+t^2); m<=-4: [3|m](t^3+t^4)+3t^2+(-m-4)(t^2+t^3); m=-3: 3t^2"""
    c=1 if m%3==0 else 0
    if m>=-2: return [c, c+m+2, 3+m+2, 0, 0]
    if m==-3: return [0,0,3,0,0]
    k=-m-4
    return [0,0,3+k,c+k,c]
if __name__=="__main__":
    name=sys.argv[1]
    rows=[]
    for m in range(-15,16):
        d=S.hyper(F[name],m); rows.append((m,d))
    bad=0
    for m,d in rows:
        chi=sum((-1)**k*x for k,x in enumerate(d))
        f=formula_x2y(m) if name in('x2y','x2(x+y)') else None
        flag='' if f is None else ('OK' if f==d else 'MISMATCH'); bad+= (f is not None and f!=d)
        print(m,d,'chi',chi,flag)
    print("mismatches",bad)
