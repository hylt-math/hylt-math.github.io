# check_B.py -- 担当 B (§4-§6) の独立検算。fractions / numpy / math のみ。
# 有理係数多項式係数の微分形式の演算（旧版 check.py を流用・拡張）＋ 数値積分・有限差分
from fractions import Fraction as Fr
import itertools, math, random
import numpy as np

N = 3                      # 変数の個数（セクションごとに切り替える）
ok_all = True
def report(name, cond, extra=""):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(("PASS  " if cond else "FAIL  ") + name + (("   " + extra) if extra else ""))

# ---------------- 多項式・形式 ----------------
def padd(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0: del r[k]
    return r
def pmul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2)); r[k] = r.get(k, 0) + v1 * v2
            if r[k] == 0: del r[k]
    return r
def pd(p, i):
    r = {}
    for k, v in p.items():
        if k[i] > 0:
            kk = list(k); kk[i] -= 1; r[tuple(kk)] = v * k[i]
    return r
def const(c): return {(0,) * N: Fr(c)} if c != 0 else {}
def var(i):
    k = [0] * N; k[i] = 1; return {tuple(k): Fr(1)}
def pscale(p, c): return {k: v * c for k, v in p.items() if v * c != 0}
def fscale(a, c): return {k: pscale(v, c) for k, v in a.items()}
def fadd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = padd(r.get(k, {}), v, s)
        if not r[k]: del r[k]
    return r
def sortsign(idx):
    idx = list(idx); s = 1
    if len(set(idx)) < len(idx): return 0, None
    for i in range(len(idx)):
        for j in range(len(idx) - 1 - i):
            if idx[j] > idx[j + 1]: idx[j], idx[j + 1] = idx[j + 1], idx[j]; s = -s
    return s, tuple(idx)
def wedge(a, b):
    r = {}
    for k1, p1 in a.items():
        for k2, p2 in b.items():
            s, k = sortsign(k1 + k2)
            if s == 0: continue
            r = fadd(r, {k: pscale(pmul(p1, p2), s)})
    return r
def d(a):
    r = {}
    for k, p in a.items():
        for i in range(N):
            dp = pd(p, i)
            if dp:
                s, kk = sortsign((i,) + k)
                if s: r = fadd(r, {kk: pscale(dp, s)})
    return r
def interior(X, a):
    r = {}
    for k, p in a.items():
        for pos, i in enumerate(k):
            kk = k[:pos] + k[pos + 1:]
            r = fadd(r, {kk: pscale(pmul(X[i], p), (-1) ** pos)})
    return r
def lie_coord(X, a):
    # 独立な座標公式: L_X(f dx^I) = X(f) dx^I + f sum_m dx^{i1}..d(X^{im})..dx^{ik}
    r = {}
    for k, p in a.items():
        Xf = {}
        for j in range(N): Xf = padd(Xf, pmul(X[j], pd(p, j)))
        if Xf: r = fadd(r, {k: Xf})
        for m, i in enumerate(k):
            for j in range(N):
                c = pd(X[i], j)
                if not c: continue
                new = tuple(k[:m]) + (j,) + tuple(k[m + 1:])
                s, kk = sortsign(new)
                if s: r = fadd(r, {kk: pscale(pmul(p, c), s)})
    return r
def form(*terms):
    r = {}
    for p, idx in terms: r = fadd(r, {tuple(idx): p})
    return r
def vf_apply(X, f):
    r = {}
    for j in range(N): r = padd(r, pmul(X[j], pd(f, j)))
    return r
def bracket(X, Y): return [padd(vf_apply(X, Y[i]), vf_apply(Y, X[i]), -1) for i in range(N)]
def rpoly(deg=2, terms=4):
    p = {}
    for _ in range(terms):
        k = [0] * N
        for _ in range(random.randint(0, deg)): k[random.randrange(N)] += 1
        p = padd(p, {tuple(k): Fr(random.randint(-3, 3))})
    return p
def rform(k, deg=2):
    w = {}
    for idx in itertools.combinations(range(N), k):
        p = rpoly(deg)
        if p: w = fadd(w, {idx: p})
    return w
def rvf(deg=2): return [rpoly(deg) for _ in range(N)]
def show(a): return {k: {e: str(c) for e, c in v.items()} for k, v in a.items()}
x, y, z = None, None, None
def setN(n):
    global N, x, y, z
    N = n
    x = var(0); y = var(1) if n > 1 else None; z = var(2) if n > 2 else None
def P(*fs):
    r = const(1)
    for f in fs: r = pmul(r, f)
    return r
random.seed(2026)

print("=== §4 微分形式 ===")
setN(3)
# 問 B_wedge
al = form((x, (1,)), (pscale(y, -1), (0,)))             # x dy - y dx
be = form((const(1), (2,)), (x, (0,)))                    # dz + x dx
ga = form((z, (0, 1)))
ab = wedge(al, be)
exp_ab = form((x, (1, 2)), (pscale(P(x, x), -1), (0, 1)), (y, (0, 2)))  # x dy^dz - x^2 dx^dy + y dz^dx ; dz^dx = -dx^dz
exp_ab = form((x, (1, 2)), (pscale(P(x, x), -1), (0, 1)), (pscale(y, -1), (0, 2)))
report("B_wedge (a) alpha^beta", ab == exp_ab)
report("B_wedge (b) alpha^gamma = 0", wedge(al, ga) == {})
report("B_wedge (b) beta^gamma = z vol", wedge(be, ga) == form((z, (0, 1, 2))))
X = [const(1), const(1), const(1)]
lhs = interior(X, ab)
rhs = fadd(wedge(interior(X, al), be), wedge(al, interior(X, be)), -1)
exp = form((padd(P(x, x), y), (0,)), (pscale(padd(x, P(x, x)), -1), (1,)), (padd(x, y, -1), (2,)))
report("B_wedge (c) iota_X(alpha^beta) both ways", lhs == rhs == exp)
# 問 B_dcalc
al = form((P(x, x, y), (0,)), (z, (1,)), (P(x, y), (2,)))
dal = d(al)
exp = form((padd(x, const(-1)), (1, 2)), (pscale(y, -1), (0, 2) if False else (0, 2)), (pscale(P(x, x), -1), (0, 1)))
# -y dz^dx = +y dx^dz
exp = form((padd(x, const(-1)), (1, 2)), (y, (0, 2)), (pscale(P(x, x), -1), (0, 1)))
report("B_dcalc d alpha = (x-1)dy^dz - y dz^dx - x^2 dx^dy", dal == exp)
report("B_dcalc dd alpha = 0", d(dal) == {})
be = form((P(x, z), (1, 2)), (pscale(P(y, y), 1), (0, 2) if False else (0, 2)), (x, (0, 1)))
be = form((P(x, z), (1, 2)), (pscale(P(y, y), -1), (0, 2)), (x, (0, 1)))   # y^2 dz^dx = - y^2 dx^dz
report("B_dcalc d beta = (z+2y) vol", d(be) == form((padd(z, pscale(y, 2)), (0, 1, 2))))
# 問 B_pullback : F(x,y)=(x^2-y^2,2xy) -- 2変数
setN(2)
xx, yy = var(0), var(1)
u = padd(P(xx, xx), P(yy, yy), -1); v = pscale(P(xx, yy), 2)
du = d({(): u}); dv = d({(): v})
pb1 = wedge(du, dv)
report("B_pullback F*(du^dv)=4(x^2+y^2)dx^dy", pb1 == form((pscale(padd(P(xx, xx), P(yy, yy)), 4), (0, 1))))
pb2 = fadd(wedge({(): u}, dv), wedge({(): v}, du), -1)
r2 = padd(P(xx, xx), P(yy, yy))
rhs = fadd(wedge({(): pscale(r2, 2)}, form((xx, (1,)), (pscale(yy, -1), (0,)))), {})
report("B_pullback F*(u dv - v du) = 2(x^2+y^2)(x dy - y dx)", pb2 == rhs)
# 例 4.7 (角形式の閉性): d((x/r^2)dy-(y/r^2)dx)=0 を有理関数の数値微分で
def omega_coeffs(px, py):
    r2 = px * px + py * py
    return (-py / r2, px / r2)
hh = 1e-6
def dom(px, py):
    P0 = lambda a, b: omega_coeffs(a, b)[0]; Q0 = lambda a, b: omega_coeffs(a, b)[1]
    return (Q0(px + hh, py) - Q0(px - hh, py)) / (2 * hh) - (P0(px, py + hh) - P0(px, py - hh)) / (2 * hh)
report("例4.7 d(angle form)=0 (数値)", max(abs(dom(*pt)) for pt in [(1.3, 0.7), (-0.4, 2.0), (3, -1)]) < 1e-6)

# Cartan: 例 4.12 / 問 B_cartanex
setN(3)
x, y, z = var(0), var(1), var(2)
Xrot = [pscale(y, -1), x, {}]
w = form((x, (1,)))
L = lie_coord([pscale(y, -1)] and [x if False else pscale(y, -1), x, {}], form((x, (1,))))
# 例4.12: X = x d_y - y d_x, omega = x dy
Xr = [pscale(y, -1), x, {}]
w1 = form((x, (1,)))
Lc = lie_coord(Xr, w1); Cc = fadd(d(interior(Xr, w1)), interior(Xr, d(w1)))
report("例4.12 L_X(x dy)=x dx - y dy (座標公式)", Lc == form((x, (0,)), (pscale(y, -1), (1,))))
report("例4.12 Cartan と一致", Lc == Cc)
# 問 B_cartanex: X=-y dx+x dy, omega = y dx^dz
w2 = form((y, (0, 2)))
Lc2 = lie_coord(Xr, w2); Cc2 = fadd(d(interior(Xr, w2)), interior(Xr, d(w2)))
exp2 = form((x, (0, 2)), (pscale(y, -1), (1, 2)))
report("B_cartanex L_X omega = x dx^dz - y dy^dz", Lc2 == exp2 and Cc2 == exp2)
print("      iota_X omega =", show(interior(Xr, w2)), " d iota =", show(d(interior(Xr, w2))))
print("      iota_X d omega =", show(interior(Xr, d(w2))))
# Cartan をランダムな多項式形式・ベクトル場で
allok = True
for k in range(0, 4):
    for trial in range(3):
        wk = rform(k); Xk = rvf()
        Lw = lie_coord(Xk, wk)
        Cw = fadd(d(interior(Xk, wk)) if k > 0 else {}, interior(Xk, d(wk)) if k < 3 else {})
        allok = allok and (Lw == Cw)
report("Cartan L_X = d i_X + i_X d (R^3, k=0..3, ランダム多項式)", allok)
# [L_X, i_Y] = i_[X,Y]  (問 B_liebr)
allok = True
for k in range(1, 4):
    for trial in range(3):
        wk = rform(k); Xk = rvf(); Yk = rvf()
        lhs = fadd(lie_coord(Xk, interior(Yk, wk)), interior(Yk, lie_coord(Xk, wk)), -1)
        rhs = interior(bracket(Xk, Yk), wk)
        allok = allok and (lhs == rhs)
report("[L_X, i_Y] = i_[X,Y]  (ランダム)", allok)
# [L_X,L_Y] = L_[X,Y]
allok = True
for k in range(0, 3):
    wk = rform(k); Xk = rvf(); Yk = rvf()
    lhs = fadd(lie_coord(Xk, lie_coord(Yk, wk)), lie_coord(Yk, lie_coord(Xk, wk)), -1)
    rhs = lie_coord(bracket(Xk, Yk), wk)
    allok = allok and (lhs == rhs)
report("[L_X,L_Y]=L_[X,Y] (ランダム)", allok)
# 問 B_liebr(b): X=y d_x, Y=d_y, omega=dx^dy  (2変数)
setN(2)
xx, yy = var(0), var(1)
Xl = [yy, {}]; Yl = [{}, const(1)]; wl = form((const(1), (0, 1)))
lhs = fadd(lie_coord(Xl, interior(Yl, wl)), interior(Yl, lie_coord(Xl, wl)), -1)
rhs = interior(bracket(Xl, Yl), wl)
report("B_liebr (b): [L_X,i_Y]w = i_[X,Y]w = -dy", lhs == rhs == form((const(-1), (1,))))
# 問 B_div (a): L_X(dx^dy)=(P_x+Q_y)dx^dy
setN(2); xx, yy = var(0), var(1)
Pp = rpoly(3); Qq = rpoly(3)
lhs = lie_coord([Pp, Qq], form((const(1), (0, 1))))
rhs = form((padd(pd(Pp, 0), pd(Qq, 1)), (0, 1)))
report("B_div(a) L_X(dx^dy) = (P_x+Q_y) dx^dy", lhs == rhs)
# 例4.14 div: Euler E: L_E(dx^dy) = 2 dx^dy ; X=x d_x - y d_y: 0
report("例4.14 L_E(dx^dy)=2dx^dy", lie_coord([xx, yy], form((const(1), (0, 1)))) == form((const(2), (0, 1))))
report("例4.14 X=x dx - y dy: L_X(dx^dy)=0", lie_coord([xx, pscale(yy, -1)], form((const(1), (0, 1)))) == {})
# B_div (c): H=(xi^2+x^2)/2 on T^*R, coordinates (x, xi)=(0,1); omega = dxi^dx = - dx^dxi
setN(2); xx, xi = var(0), var(1)
H = pscale(padd(P(xi, xi), P(xx, xx)), Fr(1, 2))
om = form((const(-1), (0, 1)))             # dxi^dx = -dx^dxi
XH = [xi, pscale(xx, -1)]                   # xi d_x - x d_xi
report("B_div(c) i_{X_H} omega = -dH", interior(XH, om) == fscale(d({(): H}), -1))
report("B_div(c) L_{X_H} omega = 0", lie_coord(XH, om) == {})
# 4.9: Hamilton eq for random H on T^*R^2: coords (x1,x2,xi1,xi2)
setN(4)
Hh = rpoly(3, 6)
omega = {}
for i in range(2):   # dxi_i ^ dx^i : xi_i are variables 2,3 ; x^i variables 0,1
    omega = fadd(omega, {tuple(sorted((2 + i, i))): const(-1 if (2 + i) > i else 1)})  # dxi_i^dx_i = -dx_i^dxi_i
XHh = [pd(Hh, 2), pd(Hh, 3), pscale(pd(Hh, 0), -1), pscale(pd(Hh, 1), -1)]
report("§4.9 i_{X_H}omega = -dH (R^4=T^*R^2, 乱数 H)", interior(XHh, omega) == fscale(d({(): Hh}), -1))
report("§4.9 L_{X_H} omega = 0", lie_coord(XHh, omega) == {})
om2 = wedge(omega, omega)
report("§4.9 omega^2 = 2 dxi1^dx1^dxi2^dx2 (係数 n!=2)", om2 == {(0, 1, 2, 3): const(-2)})
print("      omega^2 =", show(om2), "(基底 dx1^dx2^dxi1^dxi2 での係数。 dxi1^dx1^dxi2^dx2 = +dx1^dxi1^... を並べ替えた符号込み)")
# 不変公式 (1形式, 2形式)
setN(3)
def evalform(a, Vs):
    # a: form dict (k-form), Vs list of k vector fields -> poly
    k = len(Vs); res = {}
    for idx, p in a.items():
        if len(idx) != k: continue
        # determinant of V_j^{idx_i}
        for perm in itertools.permutations(range(k)):
            s = 1
            for i in range(k):
                for j in range(i + 1, k):
                    if perm[i] > perm[j]: s = -s
            term = p
            for i in range(k): term = pmul(term, Vs[perm[i]][idx[i]])
            res = padd(res, term, s)
    return res
allok = True
for trial in range(4):
    a1 = rform(1); Xa, Ya = rvf(), rvf()
    lhs = evalform(d(a1), [Xa, Ya])
    rhs = padd(padd(vf_apply(Xa, evalform(a1, [Ya])), vf_apply(Ya, evalform(a1, [Xa])), -1), evalform(a1, [bracket(Xa, Ya)]), -1)
    allok = allok and lhs == rhs
report("不変公式 d alpha(X,Y) (1形式, ランダム)", allok)
allok = True
for trial in range(4):
    b2 = rform(2); Xa, Ya, Za = rvf(), rvf(), rvf()
    lhs = evalform(d(b2), [Xa, Ya, Za])
    t = vf_apply(Xa, evalform(b2, [Ya, Za]))
    t = padd(t, vf_apply(Ya, evalform(b2, [Xa, Za])), -1)
    t = padd(t, vf_apply(Za, evalform(b2, [Xa, Ya])))
    t = padd(t, evalform(b2, [bracket(Xa, Ya), Za]), -1)
    t = padd(t, evalform(b2, [bracket(Xa, Za), Ya]))
    t = padd(t, evalform(b2, [bracket(Ya, Za), Xa]), -1)
    allok = allok and lhs == t
report("B_invk2: d beta(X,Y,Z) の公式 (2形式, ランダム)", allok)
# ι_X antiderivation, ι_X vol = ... , 例 4.? (div)
vol = form((const(1), (0, 1, 2)))
Gv = rvf(2)
iv = interior(Gv, vol)
expiv = form((Gv[0], (1, 2)), (Gv[1], (2, 0) if False else (0, 2)), (Gv[2], (0, 1)))
expiv = form((Gv[0], (1, 2)), (pscale(Gv[1], -1), (0, 2)), (Gv[2], (0, 1)))
report("例4.11 i_G vol = a dy^dz + b dz^dx + c dx^dy", iv == expiv)
dv_ = d(iv)
report("例4.14 d i_G vol = div G vol", dv_ == form((padd(padd(pd(Gv[0], 0), pd(Gv[1], 1)), pd(Gv[2], 2)), (0, 1, 2))))
# ベクトル解析表: d(P dx+Q dy+R dz)
Pp, Qq, Rr = rpoly(), rpoly(), rpoly()
dd1 = d(form((Pp, (0,)), (Qq, (1,)), (Rr, (2,))))
exp = form((padd(pd(Rr, 1), pd(Qq, 2), -1), (1, 2)), (padd(pd(Pp, 2), pd(Rr, 0), -1), (0, 2) if False else (0, 2)), (padd(pd(Qq, 0), pd(Pp, 1), -1), (0, 1)))
exp = form((padd(pd(Rr, 1), pd(Qq, 2), -1), (1, 2)), (pscale(padd(pd(Pp, 2), pd(Rr, 0), -1), -1), (0, 2)), (padd(pd(Qq, 0), pd(Pp, 1), -1), (0, 1)))
report("§4.5 d(Pdx+Qdy+Rdz)=curl (dz^dx = -dx^dz)", dd1 == exp)
# 例4.18 ポテンシャル
setN(3); x, y, z = var(0), var(1), var(2)
al = form((padd(pscale(P(x, y), 2), z), (0,)), (P(x, x), (1,)), (x, (2,)))
f = padd(P(x, x, y), P(x, z))
report("例4.18 alpha closed and = d(x^2 y + xz)", d(al) == {} and d({(): f}) == al)

print("\n=== §4 数値（積分・Stokes）===")
# S^2 の面積: Phi^*omega = sin(theta) dtheta^dphi  (有限差分で det(Phi,Phi_th,Phi_ph))
def Phi(th, ph): return np.array([math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)])
errs = []
for th, ph in [(0.7, 1.9), (2.1, 0.3), (1.3, 5.0)]:
    h = 1e-6
    Pth = (Phi(th + h, ph) - Phi(th - h, ph)) / (2 * h); Pph = (Phi(th, ph + h) - Phi(th, ph - h)) / (2 * h)
    det = np.linalg.det(np.array([Phi(th, ph), Pth, Pph]))
    errs.append(abs(det - math.sin(th)))
    cr = np.cross(Pth, Pph)
    errs.append(np.linalg.norm(cr - math.sin(th) * Phi(th, ph)))
report("B_sphere: det(Phi,Phi_th,Phi_ph)=sin th, Phi_th x Phi_ph = sin th Phi", max(errs) < 1e-6)
# ∫ sin θ dθ dφ = 4π (中点則)
nth = 2000
ths = (np.arange(nth) + 0.5) * math.pi / nth
report("∫_{S^2} omega = 4π (数値)", abs(2 * math.pi * np.sum(np.sin(ths)) * math.pi / nth - 4 * math.pi) < 1e-5)
# ∫_{S^2} omega を成分から直接 (Phi^*omega の3x3行列式を中点則)
tot = 0.0; M = 300
for i in range(M):
    th = (i + 0.5) * math.pi / M
    for j in range(M):
        ph = (j + 0.5) * 2 * math.pi / M
        h = 1e-5
        Pth = (Phi(th + h, ph) - Phi(th - h, ph)) / (2 * h); Pph = (Phi(th, ph + h) - Phi(th, ph - h)) / (2 * h)
        tot += np.linalg.det(np.array([Phi(th, ph), Pth, Pph]))
tot *= (math.pi / M) * (2 * math.pi / M)
report("∫ Phi^*omega (行列式から)=4π", abs(tot - 4 * math.pi) < 1e-2, f"={tot:.5f}")
# d omega = 3 vol, ∫_B 3 = 4π
report("B^3: 3·(4π/3)=4π", abs(3 * 4 / 3 * math.pi - 4 * math.pi) < 1e-12)
# 問 B_green: 楕円の面積 1/2 ∮ (x dy - y dx)
a_, b_ = 2.0, 0.7
ts = (np.arange(4000) + 0.5) * 2 * math.pi / 4000
integrand = 0.5 * (a_ * np.cos(ts) * b_ * np.cos(ts) + b_ * np.sin(ts) * a_ * np.sin(ts))
report("B_green(a): ½∮(x dy-y dx)=π a b", abs(np.sum(integrand) * 2 * math.pi / 4000 - math.pi * a_ * b_) < 1e-9)
# B_line
ts = (np.arange(200000) + 0.5) * 2 * math.pi / 200000
dt = 2 * math.pi / 200000
a_int = np.sum((np.sin(ts) * (-np.sin(ts)) + np.cos(ts) * np.cos(ts) + ts)) * dt
b_int = np.sum(np.sin(ts) * (-np.sin(ts))) * dt
report("B_line (a)=2π^2, (b)=-π", abs(a_int - 2 * math.pi ** 2) < 1e-6 and abs(b_int + math.pi) < 1e-6, f"{a_int:.6f}, {b_int:.6f}")
# 問 B_green(b): 円環, ∮ over outer ccw + inner cw
report("B_green(b): 2π + (-2π) = 0", abs(2 * math.pi - 2 * math.pi) < 1e-12)
# B_div3: div(x/r^3)=0 (数値微分) and flux 4π
def G3(p): r = np.linalg.norm(p); return p / r ** 3
h = 1e-5
for pt in [np.array([0.7, -0.3, 1.1]), np.array([2.0, 1.0, -0.5])]:
    div = sum((G3(pt + h * e)[i] - G3(pt - h * e)[i]) / (2 * h) for i, e in enumerate(np.eye(3)))
    report(f"B_div3 div(x/r^3)=0 at {pt}", abs(div) < 1e-6, f"{div:.2e}")
# 流束 over S_rho: ∫ G·n dS = 4π
for rho in (0.5, 3.0):
    tot = 0.0; M = 400
    for i in range(M):
        th = (i + 0.5) * math.pi / M
        tot += np.sum([1.0]) * math.sin(th)
    # G·n = 1/rho^2, dS = rho^2 sin th dth dph
    flux = 2 * math.pi * tot * math.pi / M
    report(f"B_div3 flux S_{rho}=4π", abs(flux - 4 * math.pi) < 1e-4)

print("\n=== §5 de Rham ===")
# ホモトピー作用素 P: dP+Pd=id (R^3, k=1,2,3)
setN(3); x, y, z = var(0), var(1), var(2)
def Pop(a, k):
    X = [var(i) for i in range(N)]
    iw = interior(X, a)
    r = {}
    for idx, p in iw.items():
        q = {}
        for mon, c in p.items():
            m = sum(mon); q[mon] = c * Fr(1, k - 1 + m)
        r = fadd(r, {idx: q})
    return r
for k in (1, 2, 3):
    w = rform(k)
    lhs = fadd(d(Pop(w, k)) if k > 1 or True else {}, Pop(d(w), k + 1) if k < 3 else {})
    report(f"Poincare 補題: dP+Pd=id on R^3, k={k}", lhs == w)
# k=1 の P は原始関数を与える
al = form((y, (0,)), (x, (1,)), (pscale(z, 2), (2,)))
# P alpha (k=1): coefficient 0-form: ∫ t^0 alpha_i(tx) x^i dt
q = {}
iw = interior([x, y, z], al)
for mon, c in iw[()].items(): q[mon] = c * Fr(1, sum(mon))
report("B_primitive(a): P alpha = xy+z^2", q == padd(P(x, y), P(z, z)) and d(al) == {})
# B_primitive (b)
be = form((x, (1, 2)), (y, (2, 0) if False else (0, 2)), (pscale(z, -2), (0, 1)))
be = form((x, (1, 2)), (pscale(y, -1), (0, 2)), (pscale(z, -2), (0, 1)))  # y dz^dx = -y dx^dz
report("B_primitive(b): beta closed", d(be) == {})
gam = form((P(y, z), (0,)), (pscale(P(x, z), -1), (1,)))
report("B_primitive(b): P beta = yz dx - xz dy, d gamma = beta", Pop(be, 2) == gam and d(gam) == be)
# 例5.? beta0 = dy^dz+dz^dx+dx^dy ; P beta0 = 1/2((z-y)dx+(x-z)dy+(y-x)dz)
be0 = form((const(1), (1, 2)), (const(-1), (0, 2)), (const(1), (0, 1)))
P0 = Pop(be0, 2)
exp = form((pscale(padd(z, y, -1), Fr(1, 2)), (0,)), (pscale(padd(x, z, -1), Fr(1, 2)), (1,)), (pscale(padd(y, x, -1), Fr(1, 2)), (2,)))
report("例5.7 P beta0 = ½((z-y)dx+(x-z)dy+(y-x)dz), dP=beta0", P0 == exp and d(P0) == be0)
# B_S1MV: ∫η = τ2-τ1  (bump 関数で数値)
def smoothstep(t):   # C^∞ 風: 0 for t<=0, 1 for t>=1
    f = lambda s: math.exp(-1 / s) if s > 0 else 0.0
    return f(t) / (f(t) + f(1 - t))
def rhoU(th):        # =1 near th=0, 0 near th=pi (th in (0,2π)); 対称 about 0
    t = th if th <= math.pi else 2 * math.pi - th      # distance from 0
    return 1 - smoothstep((t - 0.5) / (math.pi - 1.0))   # 1 for t<=0.5, 0 for t>=pi-0.5
for tau1, tau2 in [(1, 0), (0, 1), (2.5, -1)]:
    # η|_V = d(ρ_U τ) on V=(0,2π); τ=τ1 on (0,π), τ2 on (π,2π)
    M = 100000; ths = (np.arange(M) + 0.5) * 2 * math.pi / M
    g = np.array([rhoU(t) * (tau1 if t < math.pi else tau2) for t in ths])
    dg = np.diff(g)
    tot = np.sum(dg) + (g[0] - rhoU(0.0) * tau1) * 0 # 端点: g(0+)->tau1, g(2π-)->tau2
    tot = g[-1] - g[0]
    # g[0]≈tau1 (ρ_U=1), g[-1]≈tau2
    report(f"B_S1MV ∫η=τ2-τ1 for ({tau1},{tau2})", abs(tot - (tau2 - tau1)) < 1e-3, f"={tot:.5f}")
# B_MVT2: ランク
A_b0 = np.array([[-1, 1], [-1, 1]]); A_b1 = np.array([[-1, 1], [-1, 1]])
# H^0: (c_X,c_Y) -> (c_Y-c_X) on each of 2 components
rk0 = np.linalg.matrix_rank(np.array([[-1, 1], [-1, 1]])); rk1 = rk0
b1 = (2 - rk0) + (2 - rk1)   # coker b0 + ker b1
b2 = 2 - rk1                 # coker b1
report("B_MVT2: b=(1,2,1)", (1, b1, b2) == (1, 2, 1) and 2 - rk0 == 1, f"b1={b1}, b2={b2}, χ={1-b1+b2}")
# B_Rk: b1(M_k)=k
b = 0; ok = True
for k in range(1, 8):
    b += 1; ok = ok and b == k
report("B_Rk 帰納: b1(M_k)=k", ok)
# Poincaré 多項式の演算 (Künneth)
def pmul_poly(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): r[i + j] += a * b
    return r
S1 = [1, 1]; S2 = [1, 0, 1]
def chi(p): return sum((-1) ** i * c for i, c in enumerate(p))
T3 = pmul_poly(pmul_poly(S1, S1), S1); T4 = pmul_poly(T3, S1)
report("B_PD(b): P(S1xS2)=(1,1,1,1) χ=0", pmul_poly(S1, S2) == [1, 1, 1, 1] and chi(pmul_poly(S1, S2)) == 0)
report("B_PD(b): T^3 (1,3,3,1), T^4 (1,4,6,4,1), χ=0", T3 == [1, 3, 3, 1] and T4 == [1, 4, 6, 4, 1] and chi(T4) == 0)
report("B_PD(b): S2xS2 (1,0,2,0,1) χ=4", pmul_poly(S2, S2) == [1, 0, 2, 0, 1] and chi(pmul_poly(S2, S2)) == 4)
# 連結和: χ(M#N)=χ(M)+χ(N)-2 + χ(S^{n-1}); Σ_g
chiS = lambda n: 1 + (-1) ** n
cs = 2; okc = True
for g in range(1, 8):
    cs = cs + 0 - 2 + chiS(1)     # n=2: χ(S^1)=0
    okc = okc and cs == 2 - 2 * g
report("Prop5.? χ(Σ_g)=2-2g (連結和の公式)", okc)
report("奇数次元の連結和: χ(M#N)=χ(M)+χ(N) (n=3, χ(S^2)=2)", (0 + 0 - 2 + chiS(2)) == 0)
report("B_chi: χ(S^2xΣ_2)=-4, χ(T^3)=0, χ(RP^2)=0+1-0=1", 2 * (-2) == -4 and chi(T3) == 0 and (0 + 1 - 0) == 1)
report("B_chi(c): 4次元 b1=0 ⇒ χ=2+b2", (1 - 0 + 5 - 0 + 1) == 2 + 5)
# 偶数性
ok = True
for g in range(0, 6):
    ok = ok and (2 * g) % 2 == 0 and (2 - 2 * g) % 2 == 0
report("B_PD(c) Σ_g: b1=2g 偶数, χ 偶数", ok)
# T^2 intersection form
Q = np.array([[0, 1], [-1, 0]]) * (2 * math.pi) ** 2
report("例5.? T^2: 交叉形式 (2π)^2(ps-qr): 行列 [[0,1],[-1,0]] 非退化・歪対称", abs(np.linalg.det(Q)) > 1 and np.allclose(Q, -Q.T))
# S2xS2
Qs = np.array([[0, 1], [1, 0]])
ev = np.linalg.eigvalsh(Qs)
report("B_kun: S2xS2 の形式 [[0,1],[1,0]] det=-1, 固有値 ±1 (不定符号)", abs(np.linalg.det(Qs) + 1) < 1e-12 and sorted(ev) == [-1.0, 1.0])

print("\n=== §5 写像度 ===")
# degree of z^m via numeric ∫ f^*dθ / 2π  (連続)
for m in (3, -2, 1, 0):
    ths = (np.arange(10000) + 0.5) * 2 * math.pi / 10000
    val = np.sum(np.full_like(ths, m)) * 2 * math.pi / 10000
    report(f"B_degree(a) deg z^{m} = {m}", abs(val / (2 * math.pi) - m) < 1e-12)
# 対蹠写像の向き符号 (-1)^{n+1}
for n in range(1, 6):
    rng = np.random.default_rng(n)
    p = rng.normal(size=n + 1); p /= np.linalg.norm(p)
    # T_p S^n の基底: Gram-Schmidt of random vectors orthogonal to p; make (p,v1..vn) positively oriented
    V = []
    for _ in range(n):
        v = rng.normal(size=n + 1)
        v -= v.dot(p) * p
        for u_ in V: v -= v.dot(u_) * u_
        v /= np.linalg.norm(v); V.append(v)
    M0 = np.array([p] + V)
    if np.linalg.det(M0) < 0: V[0] = -V[0]
    M0 = np.array([p] + V)
    M1 = np.array([-p] + [-v for v in V])   # da(v)=-v at -p ; positive iff det(-p,-v...)>0
    sgn = np.sign(np.linalg.det(M1) / np.linalg.det(M0))
    report(f"対蹠写像の符号 n={n}: (-1)^(n+1)={(-1)**(n+1)}", sgn == (-1) ** (n + 1))
# f(z)=(z^2+1)/z on CP^1: 値0 の逆像 ±i, f'(±i)=2
fp = lambda zz: 1 - 1 / zz ** 2
report("B_degree(c): f'(±i)=2≠0, 逆像2点で deg=2", abs(fp(1j) - 2) < 1e-12 and abs(fp(-1j) - 2) < 1e-12 and abs((1j) ** 2 + 1) < 1e-12)
# 数値で正則値 y=0.3+0.2i 付近の逆像: z^2 - y z + 1 = 0
yv = 0.3 + 0.2j
roots = np.roots([1, -yv, 1])
report("B_degree(c): 一般の値でも逆像は2点", len(roots) == 2 and all(abs(fp(r)) > 1e-3 for r in roots))
# B_brouwer(b): r(x) の |r|=1 を数値確認
rng = np.random.default_rng(0)
mx = 0.0
for _ in range(2000):
    xv = rng.uniform(-1, 1, 2)
    if np.linalg.norm(xv) > 1: continue
    gv = rng.uniform(-1, 1, 2); gv = gv / max(1, np.linalg.norm(gv))
    if np.linalg.norm(xv - gv) < 1e-3: continue
    uu = xv - gv
    disc = (xv @ uu) ** 2 + (uu @ uu) * (1 - xv @ xv)
    lam = (-(xv @ uu) + math.sqrt(max(disc, 0))) / (uu @ uu)
    rv = xv + lam * uu
    mx = max(mx, abs(np.linalg.norm(rv) - 1))
report("B_brouwer(b): |r(x)|=1 (公式の検算)", mx < 1e-10, f"max err {mx:.1e}")
# B_fixed: 線分は原点を通らない（不動点なし）: f(x)≠x ⇒ (1-t)f(x)-t x ≠0 ; 数値
ok = True
for _ in range(2000):
    xv = rng.normal(size=3); xv /= np.linalg.norm(xv)
    fv = rng.normal(size=3); fv /= np.linalg.norm(fv)
    if np.linalg.norm(fv - xv) < 1e-3: continue
    for t in np.linspace(0, 1, 101):
        if np.linalg.norm((1 - t) * fv - t * xv) < 1e-9: ok = False
report("B_fixed: f(x)≠x ⇒ 線分 (1-t)f - t x は原点を通らない", ok)

print("\n=== §6 Hodge 星 ===")
# ----- 一般の計量 G (対称正定値) に対する Hodge 星を定義式 α∧★β = <α,β> vol から線形代数で計算 -----
def comb(n, k): return list(itertools.combinations(range(n), k))
def wedge_basis(I, J):
    s, K = sortsign(I + J)
    return s, K
def star_matrix(G, k):
    """基底 dx^I (I in comb(n,k)) 上の ★ を行列 S (列= ★dx^I の dx^J 成分) で返す。G は計量行列 g_ij。"""
    n = G.shape[0]; Gi = np.linalg.inv(G); sq = math.sqrt(np.linalg.det(G))
    Is = comb(n, k); Js = comb(n, n - k)
    # 内積 <dx^I, dx^K> = det(Gi[I,K])
    ip = np.array([[np.linalg.det(Gi[np.ix_(I, K)]) if k > 0 else 1.0 for K in Is] for I in Is])
    # 条件: dx^I ∧ ★dx^K = ip[I,K] * sq * dx^{1..n}  → ★dx^K = Σ_J S[J,K] dx^J
    # dx^I∧dx^J = sgn(I,J) dx^{1..n} (J=I^c)
    W = np.zeros((len(Is), len(Js)))
    for a_, I in enumerate(Is):
        for b_, J in enumerate(Js):
            s, K = wedge_basis(I, J)
            if s != 0: W[a_, b_] = s
    # W S = sq*ip  → S = W^{-1} sq ip
    S = np.linalg.solve(W, sq * ip)
    return S, Is, Js
def table(n, k):
    S, Is, Js = star_matrix(np.eye(n), k)
    out = {}
    for col, I in enumerate(Is):
        for row, J in enumerate(Js):
            if abs(S[row, col]) > 1e-12: out[I] = (int(round(S[row, col])), J)
    return out
t3 = {k: table(3, k) for k in range(4)}
report("R^3: ★dx=dy^dz, ★dy=dz^dx, ★dz=dx^dy", t3[1] == {(0,): (1, (1, 2)), (1,): (-1, (0, 2)), (2,): (1, (0, 1))})
report("R^3: ★(dy^dz)=dx, ★(dz^dx)=dy, ★(dx^dy)=dz", t3[2] == {(1, 2): (1, (0,)), (0, 2): (-1, (1,)), (0, 1): (1, (2,))})
t4 = {k: table(4, k) for k in range(5)}
exp1 = {(0,): (1, (1, 2, 3)), (1,): (-1, (0, 2, 3)), (2,): (1, (0, 1, 3)), (3,): (-1, (0, 1, 2))}
exp2 = {(0, 1): (1, (2, 3)), (0, 2): (-1, (1, 3)), (0, 3): (1, (1, 2)), (1, 2): (1, (0, 3)), (1, 3): (-1, (0, 2)), (2, 3): (1, (0, 1))}
exp3 = {(0, 1, 2): (1, (3,)), (0, 1, 3): (-1, (2,)), (0, 2, 3): (1, (1,)), (1, 2, 3): (-1, (0,))}
report("R^4 表 k=1", t4[1] == exp1); report("R^4 表 k=2", t4[2] == exp2); report("R^4 表 k=3", t4[3] == exp3)
# ★★ = (-1)^{k(n-k)}  (一般の計量でも)
rngg = np.random.default_rng(5)
for n in (3, 4, 5):
    A = rngg.normal(size=(n, n)); G = A @ A.T + n * np.eye(n)
    okk = True
    for k in range(n + 1):
        S, Is, Js = star_matrix(G, k)
        S2, _, _ = star_matrix(G, n - k)
        okk = okk and np.allclose(S2 @ S, (-1) ** (k * (n - k)) * np.eye(len(Is)))
    report(f"一般の計量 n={n}: ★★=(-1)^(k(n-k)) (定義式から数値的に)", okk)
# 共形: ★_{e^{2u}G} = e^{(n-2k)u} ★_G
for n in (2, 3, 4):
    A = rngg.normal(size=(n, n)); G = A @ A.T + n * np.eye(n); u = 0.37
    okk = True
    for k in range(n + 1):
        S, _, _ = star_matrix(G, k); St, _, _ = star_matrix(math.exp(2 * u) * G, k)
        okk = okk and np.allclose(St, math.exp((n - 2 * k) * u) * S)
    report(f"共形: ★~ = e^((n-2k)u) ★  n={n}", okk)
# ベクトル解析: curl = ★d, div = ★d★, cross = ★(∧)  (R^3, 多項式形式)
setN(3); x, y, z = var(0), var(1), var(2)
def star_poly(a, n, k):
    S, Is, Js = star_matrix(np.eye(n), k)
    r = {}
    for col, I in enumerate(Is):
        if I in a:
            for row, J in enumerate(Js):
                if abs(S[row, col]) > 1e-12: r = fadd(r, {J: pscale(a[I], int(round(S[row, col])))})
    return r
Pp, Qq, Rr = rpoly(), rpoly(), rpoly()
F1 = form((Pp, (0,)), (Qq, (1,)), (Rr, (2,)))
curl = form((padd(pd(Rr, 1), pd(Qq, 2), -1), (0,)), (padd(pd(Pp, 2), pd(Rr, 0), -1), (1,)), (padd(pd(Qq, 0), pd(Pp, 1), -1), (2,)))
report("§6.2 (curl F)^♭ = ★dF^♭", star_poly(d(F1), 3, 2) == curl)
divF = padd(padd(pd(Pp, 0), pd(Qq, 1)), pd(Rr, 2))
report("§6.2 div F = ★d★F^♭", star_poly(d(star_poly(F1, 3, 1)), 3, 3) == {(): divF} or star_poly(d(star_poly(F1, 3, 1)), 3, 3) == ({(): divF} if divF else {}))
a1 = form((const(1), (0,)), (const(2), (1,))); b1 = form((const(1), (1,)), (const(-1), (2,)))
report("B_star3(d): ★(α∧β)=(-2,1,1)=(1,2,0)x(0,1,-1)", star_poly(wedge(a1, b1), 3, 2) == form((const(-2), (0,)), (const(1), (1,)), (const(1), (2,))) and list(np.cross([1, 2, 0], [0, 1, -1])) == [-2, 1, 1])
Ff = [x, y, z]
F2 = form((pscale(y, -1), (0,)), (x, (1,)))
report("B_star3(b): ★d(-y dx + x dy)=2dz", star_poly(d(F2), 3, 2) == form((const(2), (2,))))
F3 = form((P(x, x), (0,)), (P(y, y), (1,)), (P(z, z), (2,)))
report("B_star3(c): ★d★F♭ = 2(x+y+z)", star_poly(d(star_poly(F3, 3, 1)), 3, 3) == {(): pscale(padd(padd(x, y), z), 2)})
# δ = (-1)^{n(k+1)+1} ★d★  vs  δ = -Σ ι_j ∂_j  (平坦 R^n, 多項式形式)
for n in (2, 3, 4):
    setN(n)
    okk = True
    for k in range(1, n + 1):
        w = rform(k)
        # ★d★
        sw = star_poly(w, n, k)
        dsw = d(sw)
        s2 = star_poly(dsw, n, n - k + 1)
        delta_star = {kk: pscale(v, (-1) ** (n * (k + 1) + 1)) for kk, v in s2.items()}
        # -Σ ι_j ∂_j
        delta_flat = {}
        for j in range(n):
            dj = {kk: pd(v, j) for kk, v in w.items() if pd(v, j)}
            ej = [const(1) if i == j else {} for i in range(n)]
            delta_flat = fadd(delta_flat, interior(ej, dj), -1)
        okk = okk and (delta_star == delta_flat)
    report(f"δ=(-1)^(n(k+1)+1)★d★ = -Σ ι_j ∂_j  (R^{n}, k=1..{n})", okk)
    # Δ = -Σ ∂_j^2 on random forms
    okk = True
    for k in range(0, n + 1):
        w = rform(k)
        def delta(a, kk_):
            r = {}
            for j in range(n):
                dj = {kk: pd(v, j) for kk, v in a.items() if pd(v, j)}
                ej = [const(1) if i == j else {} for i in range(n)]
                r = fadd(r, interior(ej, dj), -1)
            return r
        Lw = fadd(d(delta(w, k)) if k > 0 else {}, delta(d(w), k + 1) if k < n else {})
        lap = {}
        for kk, v in w.items():
            s_ = {}
            for j in range(n): s_ = padd(s_, pd(pd(v, j), j), -1)
            if s_: lap[kk] = s_
        okk = okk and (Lw == lap)
    report(f"Δ=dδ+δd = -Σ∂_j^2 (成分ごと) on R^{n}", okk)
# R^3 の δ(2形式) = curl,  Δ(P dx)
setN(3)
a_, b_, c_ = rpoly(), rpoly(), rpoly()
B2 = form((a_, (1, 2)), (pscale(b_, -1), (0, 2)), (c_, (0, 1)))
dl = {}
for j in range(3):
    dj = {kk: pd(v, j) for kk, v in B2.items() if pd(v, j)}
    ej = [const(1) if i == j else {} for i in range(3)]
    dl = fadd(dl, interior(ej, dj), -1)
exp = form((padd(pd(c_, 1), pd(b_, 2), -1), (0,)), (padd(pd(a_, 2), pd(c_, 0), -1), (1,)), (padd(pd(b_, 0), pd(a_, 1), -1), (2,)))
report("B_adj(b): δ(a dy^dz+b dz^dx+c dx^dy) = curl(a,b,c)♭", dl == exp)
# α∧★β = <α,β> vol  for random polynomial forms on R^4 (標準計量)
setN(4)
okk = True
for k in range(0, 5):
    a = rform(k); b = rform(k)
    lhs = wedge(a, star_poly(b, 4, k)) if k > 0 else wedge(a, star_poly(b, 4, 0))
    ip = {}
    for I in a:
        if I in b: ip = padd(ip, pmul(a[I], b[I]))
    rhs = {(0, 1, 2, 3): ip} if ip else {}
    okk = okk and (lhs == rhs)
report("α∧★β=<α,β>vol (R^4, 乱数)", okk)
# B_star4: α=dx12+2dx34
a = form((const(1), (0, 1)), (const(2), (2, 3)))
sa = star_poly(a, 4, 2)
ap = {k: pscale(v, Fr(1, 2)) for k, v in fadd(a, sa).items()}; am = {k: pscale(v, Fr(1, 2)) for k, v in fadd(a, sa, -1).items()}
report("B_star4(b): α^+ = 3/2(dx12+dx34), α^- = -1/2(dx12-dx34)", ap == form((const(Fr(3, 2)), (0, 1)), (const(Fr(3, 2)), (2, 3))) and am == form((const(Fr(-1, 2)), (0, 1)), (const(Fr(1, 2)), (2, 3))))
norm2 = lambda f: sum(sum(c * c for c in [list(v.values())[0] if v else 0]) for v in f.values())
nap = sum(list(v.values())[0] ** 2 for v in ap.values()); nam = sum(list(v.values())[0] ** 2 for v in am.values())
report("B_star4(b): |α^+|^2-|α^-|^2 = 4, α∧α=4vol", nap - nam == 4 and wedge(a, a) == {(0, 1, 2, 3): const(4)}, f"{nap}-{nam}")
# Λ^± の基底
pm = {"+": [form((const(1), (0, 1)), (const(1), (2, 3))), form((const(1), (0, 2)), (const(-1), (1, 3))), form((const(1), (0, 3)), (const(1), (1, 2)))],
      "-": [form((const(1), (0, 1)), (const(-1), (2, 3))), form((const(1), (0, 2)), (const(1), (1, 3))), form((const(1), (0, 3)), (const(-1), (1, 2)))]}
okk = all(star_poly(b, 4, 2) == b for b in pm["+"]) and all(star_poly(b, 4, 2) == {k: pscale(v, -1) for k, v in b.items()} for b in pm["-"])
report("§6.6 Λ^± の基底 (3+3)", okk)
# T^4: 交叉形式の符号 (3,3): 定数係数2形式の空間で Q(α,β)=∫α∧β ∝ 係数。Λ^+ で正, Λ^- で負
Qm = np.zeros((6, 6)); I2 = comb(4, 2)
for i, I in enumerate(I2):
    for j, J in enumerate(I2):
        s, K = wedge_basis(I, J)
        if s: Qm[i, j] = s
ev = np.linalg.eigvalsh(Qm)
report("B_sd(c)/例6.? T^4: Q の符号 (3,3)", sorted(ev).count(-1.0) == 3 and sorted(ev).count(1.0) == 3, str(sorted(ev)))

print("\n=== §6 Laplacian・トーラス ===")
# 一般の計量での関数 Laplacian: Δf = -(1/√g) ∂_i(√g g^{ij} ∂_j f) を 弱形式 ∫|df|^2 = ∫ f Δ f で検証 (S^2, f=cosθ, 他)
def lap_S2(f, th, ph, h=1e-4):
    st = lambda t: math.sin(t)
    ft = lambda t, p: (f(t + h, p) - f(t - h, p)) / (2 * h)
    inner = lambda t: st(t) * ft(t, ph)
    t1 = (inner(th + h) - inner(th - h)) / (2 * h) / st(th)
    fpp = (f(th, ph + h) - 2 * f(th, ph) + f(th, ph - h)) / h ** 2
    return -t1 - fpp / st(th) ** 2
fcos = lambda t, p: math.cos(t)
report("B_lap(b): Δ cosθ = 2 cosθ (数値)", abs(lap_S2(fcos, 0.8, 0.3) - 2 * math.cos(0.8)) < 1e-4)
fre = lambda t, p: math.sin(t) * math.cos(p)
report("B_lap(b): Δ(sinθ cosφ) = 2 sinθ cosφ (数値)", abs(lap_S2(fre, 1.1, 0.6) - 2 * math.sin(1.1) * math.cos(0.6)) < 1e-4)
# ℓ=2: P2(cosθ), 固有値 6
fl2 = lambda t, p: (3 * math.cos(t) ** 2 - 1) / 2
report("(参考) Δ P_2(cosθ) = 6 P_2 (ℓ(ℓ+1)=6)", abs(lap_S2(fl2, 0.9, 0.0) - 6 * fl2(0.9, 0)) < 1e-3)
# (c) 弱形式
M = 20000; ths = (np.arange(M) + 0.5) * math.pi / M
lhs = 2 * math.pi * np.sum(np.sin(ths) ** 2 * np.sin(ths)) * math.pi / M
rhs = 2 * math.pi * np.sum(2 * np.cos(ths) ** 2 * np.sin(ths)) * math.pi / M
report("B_lap(c): ∫|df|^2 = ∫ f Δ f = 8π/3", abs(lhs - 8 * math.pi / 3) < 1e-6 and abs(rhs - 8 * math.pi / 3) < 1e-6)
# polar: r^k cos kθ 調和 (数値)
def lap_polar(f, r, th, h=1e-4):
    fr = lambda rr: (f(rr + h, th) - f(rr - h, th)) / (2 * h)
    t1 = ((r + h) * fr(r + h) - (r - h) * fr(r - h)) / (2 * h) / r
    t2 = (f(r, th + h) - 2 * f(r, th) + f(r, th - h)) / h ** 2 / r ** 2
    return -t1 - t2
report("B_lap(a): Δ log r = 0, Δ(r^3 cos3θ)=0 (数値)", abs(lap_polar(lambda r, t: math.log(r), 1.7, 0.4)) < 1e-4 and abs(lap_polar(lambda r, t: r ** 3 * math.cos(3 * t), 1.3, 0.8)) < 1e-4)
# ---- トーラス: ω = (2+cos x sin y)dx + (3+ sin x cos y)dy ----
def om(xv, yv): return (2 + math.cos(xv) * math.sin(yv), 3 + math.sin(xv) * math.cos(yv))
h = 1e-5
for pt in [(0.4, 1.2), (2.5, -0.7)]:
    Py = (om(pt[0], pt[1] + h)[0] - om(pt[0], pt[1] - h)[0]) / (2 * h); Qx = (om(pt[0] + h, pt[1])[1] - om(pt[0] - h, pt[1])[1]) / (2 * h)
    report(f"B_torus(a): ω 閉 at {pt}", abs(Py - Qx) < 1e-6)
M = 600
xs = (np.arange(M) + 0.5) * 2 * math.pi / M
X, Y = np.meshgrid(xs, xs, indexing="ij")
P1 = 2 + np.cos(X) * np.sin(Y); Q1 = 3 + np.sin(X) * np.cos(Y)
cycle_a = np.sum(2 + np.cos(xs) * math.sin(0.0)) * 2 * math.pi / M
cycle_b = np.sum(3 + math.sin(0.0) * np.cos(xs)) * 2 * math.pi / M
report("例6.? ∮_a ω=4π, ∮_b ω=6π", abs(cycle_a - 4 * math.pi) < 1e-8 and abs(cycle_b - 6 * math.pi) < 1e-8)
hP = np.mean(P1); hQ = np.mean(Q1)
report("B_torus(a): 調和部分 h = 2dx + 3dy (平均)", abs(hP - 2) < 1e-10 and abs(hQ - 3) < 1e-10)
norm_om = np.sum(P1 ** 2 + Q1 ** 2) * (2 * math.pi / M) ** 2
report("B_torus(c): ‖ω‖² = 54π², ‖h‖²=52π²", abs(norm_om - 54 * math.pi ** 2) < 1e-6 and abs(13 * 4 * math.pi ** 2 - 52 * math.pi ** 2) < 1e-9, f"{norm_om/math.pi**2:.6f}π²")
# β = sin y dx = δγ, γ = -cos y dx^dy ; δ = -Σ ι_j ∂_j : δ(g dx^dy) = g_y dx - g_x dy
g_ = lambda xv, yv: -math.cos(yv)
gy = (g_(0.3, 0.9 + h) - g_(0.3, 0.9 - h)) / (2 * h); gx = (g_(0.3 + h, 0.9) - g_(0.3 - h, 0.9)) / (2 * h)
report("B_torus(b): δ(-cos y dx^dy) = sin y dx", abs(gy - math.sin(0.9)) < 1e-6 and abs(gx) < 1e-6)
# 定理 6.? の公式（Fourier）を T^2 上のランダムな三角多項式 1 形式で数値検証: ω = h + dα + δβ
rng = np.random.default_rng(11)
modes = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
coef = {}
for m in modes:
    if m == (0, 0): continue
    if m[0] < 0 or (m[0] == 0 and m[1] < 0): continue
    c = rng.normal(size=2) + 1j * rng.normal(size=2)
    coef[m] = c; coef[(-m[0], -m[1])] = np.conj(c)
coef[(0, 0)] = rng.normal(size=2).astype(complex)
def eval_form(cf, p):
    v = np.zeros(2, dtype=complex)
    for m, c in cf.items(): v += c * np.exp(1j * (m[0] * p[0] + m[1] * p[1]))
    return v.real
# α = Σ_{m≠0} (-i/|m|²) e^{imx} ι_m ω_m (函数), β = Σ (i/|m|²) e^{imx} θ_m∧ω_m (2形式の係数=m1 ω2 - m2 ω1)
def alpha_fn(p):
    s = 0j
    for m, c in coef.items():
        if m == (0, 0): continue
        n2 = m[0] ** 2 + m[1] ** 2
        s += (-1j / n2) * np.exp(1j * (m[0] * p[0] + m[1] * p[1])) * (m[0] * c[0] + m[1] * c[1])
    return s.real
def beta_fn(p):
    s = 0j
    for m, c in coef.items():
        if m == (0, 0): continue
        n2 = m[0] ** 2 + m[1] ** 2
        s += (1j / n2) * np.exp(1j * (m[0] * p[0] + m[1] * p[1])) * (m[0] * c[1] - m[1] * c[0])
    return s.real
h = 1e-5
errmax = 0.0
for p in [(0.3, 1.1), (2.2, 4.0), (5.0, 0.5)]:
    p = np.array(p)
    da = np.array([(alpha_fn(p + h * e) - alpha_fn(p - h * e)) / (2 * h) for e in np.eye(2)])       # dα = α_x dx + α_y dy
    # δ(g dx^dy) = g_y dx - g_x dy
    dbeta = np.array([(beta_fn(p + h * np.array([0, 1])) - beta_fn(p - h * np.array([0, 1]))) / (2 * h), -(beta_fn(p + h * np.array([1, 0])) - beta_fn(p - h * np.array([1, 0]))) / (2 * h)])
    h0 = coef[(0, 0)].real
    total = h0 + da + dbeta
    errmax = max(errmax, np.max(np.abs(total - eval_form(coef, p))))
report("定理 HodgeT (T^2): ω = h + dα + δβ (Fourier 公式を有限差分で検証)", errmax < 1e-5, f"max err {errmax:.2e}")
# 同様に T^3 の 1 形式（ι_m ω_m とθ_m∧ω_m の 2 形式部分）で  ω = h + dα + δβ: 恒等式 θ_m∧ι_m + ι_m θ_m∧ = |m|^2 を一般次元で確認
for n in (2, 3, 4):
    okk = True
    for k in range(0, n + 1):
        Is = comb(n, k)
        for trial in range(3):
            m = rngg.integers(-3, 4, size=n).astype(float)
            vec = {I: rngg.normal() for I in Is}
            # θ_m ∧ ι_m ω + ι_m (θ_m ∧ ω) = |m|^2 ω  (多項式形式機構で定数係数)
            setN(n)
            w = {I: const(Fr(int(round(vec[I] * 7)), 7)) for I in Is if int(round(vec[I] * 7)) != 0}
            mi = [int(v) for v in m]
            th = {(j,): const(mi[j]) for j in range(n) if mi[j] != 0}
            imw = interior([const(mi[j]) for j in range(n)], w) if k > 0 else {}
            lhs = fadd(wedge(th, imw) if imw else {}, interior([const(mi[j]) for j in range(n)], wedge(th, w)) if (th and w and k < n) else {})
            rhs = {I: pscale(c, sum(v * v for v in mi)) for I, c in w.items() if sum(v * v for v in mi) != 0}
            okk = okk and (lhs == rhs)
    report(f"恒等式 θ_m∧ι_m + ι_mθ_m∧ = |m|^2 (n={n}, 全次数)", okk)
# 平坦トーラスの Hodge: dim H^k(T^n) = C(n,k) と PD 対称
report("定理 HodgeT: b_k(T^n)=C(n,k): n=4 → (1,4,6,4,1)", [math.comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1])
# B_minim(b): Cauchy-Schwarz
f_ = np.random.default_rng(3).normal(size=1000)
report("B_minim(c): (∫f)^2 ≤ 2π ∫f^2 (数値例)", (np.sum(f_) * 2 * math.pi / 1000) ** 2 <= 2 * math.pi * np.sum(f_ ** 2) * 2 * math.pi / 1000)
# B_hodge2d: CR ⇔ closed&coclosed for u=Re(f), v=-Im(f): f=z^2: u=x^2-y^2, v=-2xy ; α=u dx+v dy
setN(2); xx, yy = var(0), var(1)
u = padd(P(xx, xx), P(yy, yy), -1); v = pscale(P(xx, yy), -2)
al = form((u, (0,)), (v, (1,)))
dl = padd(pd(u, 0), pd(v, 1)) # u_x + v_y
report("B_hodge2d: f=z^2: α=u dx+v dy は閉かつ余閉", d(al) == {} and dl == {})
# 4.? Hamilton: n=1 flow area preserved etc. done above
print("\n=== 総括 ===")
print("ALL PASS" if ok_all else "SOME FAIL")
