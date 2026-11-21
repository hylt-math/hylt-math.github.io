# Test of conjecture C-sing on cubics with isolated singular points and (normal-crossing/tacnode) components.
# H^*(m) = [U-part] + mu_total in degree 2, with
#  m=-3 : everything in degree 2 (E1 argument)  -> [0,0,3,0,0]
#  m in 3Z, m>=0 : U-part = H^*(U;C) = [b0,b1,b2,0,0]
#  m in 3Z, m<=-6: U-part = H^*_c(U;C) = [0,0,b2,b1,b0]
#  m not in 3Z  : U-part = H^*(U;L_m) = [0,0,chi(U),0,0]  (H^0=H^1=0 assumed; chi(U)=3-chi(D))
import sys,io,contextlib
sys.path.insert(0,'.')
with contextlib.redirect_stdout(io.StringIO()):
    import sing_table as S
# name -> (c components, mu_total)  ; b1(U)=c-1 ; chi(U)=3-sum(mu) (since chi(D)=sum mu for cubics)
data={'smooth(Fermat)':(1,0),'nodal y2z-x3-x2z':(1,1),'cuspidal y2z-x3':(1,2),
      'conic+secant x(yz-x2)':(2,2),'conic+tangent y(yz-x2)':(2,3),'triangle xyz':(3,3)}
bad=0
for name,(c,mu) in data.items():
    chiU=3-mu; b0=1; b1=c-1; b2=chiU-b0+b1
    for m in range(-15,16):
        if m==-3: pred=[0,0,3,0,0]
        elif m%3==0 and m>=0: pred=[b0,b1,b2+mu,0,0]
        elif m%3==0: pred=[0,0,b2+mu,b1,b0]
        else: pred=[0,0,chiU+mu,0,0]
        d=S.hyper(S.cubics[name],m)
        if d!=pred: bad+=1; print("MISMATCH",name,m,d,pred)
print("mismatches:",bad)
