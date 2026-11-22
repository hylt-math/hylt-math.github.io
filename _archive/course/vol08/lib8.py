# 第8巻の検算用ライブラリ（fractions のみ。第6巻のコードは参照せず再実装）
from fractions import Fraction as F
from math import factorial, comb

def smul(a,b,n):
    r=[F(0)]*(n+1)
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if i+j<=n: r[i+j]+=x*y
    return r
def spow(a,k,n):
    r=[F(1)]+[F(0)]*n
    for _ in range(k): r=smul(r,a,n)
    return r
def sinv(a,n):
    r=[F(0)]*(n+1); r[0]=1/a[0]
    for m in range(1,n+1):
        r[m]=-sum(a[k]*r[m-k] for k in range(1,m+1))/a[0]
    return r
def sadd(a,b): return [x+y for x,y in zip(a,b)]
def ssub(a,b): return [x-y for x,y in zip(a,b)]
def sscale(a,c): return [F(c)*x for x in a]
def sub_x(a,c,n):  # a(c*x)
    return [a[k]*F(c)**k for k in range(n+1)]
def expser(n,c=1): return [F(c)**k/factorial(k) for k in range(n+1)]
# 基本の級数（変数 x、n 次まで）
def todd(n):   # x/(1-e^{-x})
    den=[F((-1)**k,factorial(k+1)) for k in range(n+1)]  # (1-e^{-x})/x
    return sinv(den,n)
def ahat(n):   # (x/2)/sinh(x/2)
    den=[ (F(1,2)**(2*k))/factorial(2*k+1) if True else 0 for k in range(n+1)]  # sinh(u)/u = sum u^{2k}/(2k+1)!, u=x/2 -> only even powers of x
    s=[F(0)]*(n+1)
    for k in range(0,n//2+1):
        s[2*k]=F(1,4**k)/factorial(2*k+1)
    return sinv(s,n)
def lgen(n):   # x/tanh x
    # tanh x / x = sinh x/(x cosh x)
    sh=[F(0)]*(n+1); ch=[F(0)]*(n+1)
    for k in range(0,n//2+1):
        sh[2*k]=F(1,factorial(2*k+1)); ch[2*k]=F(1,factorial(2*k))
    return smul(ch,sinv(sh,n),n)
def Lhalf(n):  # x/tanh(x/2)  (符号作用素のシンボルから出る形)
    return sscale(sub_x(lgen(n),F(1,2),n),2)

# ---- CP^N 上のスカラー量（H^{N+1}=0 の一変数）----
def int_top(series,N): return series[N]  # ∫_{CP^N} H^N = 1

if __name__=="__main__":
    n=8
    print("Td:",todd(6))
    print("Ahat:",ahat(8))
    print("L:",lgen(6))
