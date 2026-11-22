from lib import *
# 1. ch_k, Td_k in c_i
N=4;D=4
x=[P.var(i) for i in range(N)]
ch=sum((series_sub(expser(D),xi) for xi in x),P.const(0))
for k in range(0,5):
    print("ch_%d ="%k, show(to_elem(ch.deg(k)) if k>0 else {(0,0,0,0):F(4)}))
Q=todd_coeffs(D)
td=P.const(1)
for xi in x: td=td*series_sub(Q,xi)
print("Q coeffs",Q)
for k in range(1,5):
    print("Td_%d ="%k, show(to_elem(td.deg(k))))
