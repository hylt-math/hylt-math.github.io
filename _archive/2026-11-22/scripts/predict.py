# Compare the topological prediction  H^*(P^2,(wedge T(m),d_sigma)) vs direct computation.
# Prediction (derived sketch): let U=P^2\D, L_m = rank-1 local system on U with monodromy exp(2 pi i m/3).
#   m in 3Z, m>=0 : H^*(U,C)   = [1,0,2,0,0]
#   m in 3Z, m<=-6: H^*_c(U,C) = [0,0,2,0,1]
#   m not in 3Z   : H^*(U,L_m)=H^*_c(U,L_m) = [0,0,3,0,0]
#   m = -3        : exceptional (quotient complex Q has zero differential): [0,0,3,0,0]
import io,contextlib,sys
sys.path.insert(0,'.')
with contextlib.redirect_stdout(io.StringIO()):
    import table
    import neg_check
def pred(m):
    if m%3==0:
        if m>=0: return [1,0,2,0,0]
        if m==-3: return [0,0,3,0,0]
        return [0,0,2,0,1]
    return [0,0,3,0,0]
bad=0
for m in range(-15,16):
    d=table.hyper(m)           # m>=-3 direct; m<=-4 via Serre duality
    if m<=-4:                  # also direct (no duality) via neg_check
        r=neg_check.run(table.Ff,m); d2=r['H']
        assert d2==d,(m,d,d2)
    ok=(d==pred(m)); bad+=not ok
    print(m,d,"pred",pred(m),"OK" if ok else "MISMATCH")
print("mismatches:",bad)
