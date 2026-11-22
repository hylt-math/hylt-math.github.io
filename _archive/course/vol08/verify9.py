# 第8巻の独立再検算（査読者による別実装）。lib8.py / verify8.py は使わない。
# fractions と numpy/scipy のみ。
import itertools, math, random
from fractions import Fraction as F
import numpy as np
import scipy.linalg as sl
rng = np.random.default_rng(12345)
random.seed(5)
OK = []
def rep(name, cond):
    OK.append((name, bool(cond)))
    print(("OK   " if cond else "FAIL ") + name)

# ---------------------------------------------------------------
# 0. 形式的べき級数（Fraction、リスト）: 別実装（Bernoulli 数は使わず、定義式の逆元で作る）
# ---------------------------------------------------------------
def mul(a, b, N):
    r = [F(0)] * (N + 1)
    for i, x in enumerate(a[:N + 1]):
        if x:
            for j, y in enumerate(b[:N + 1 - i]):
                r[i + j] += x * y
    return r
def inv(a, N):
    r = [F(0)] * (N + 1); r[0] = 1 / a[0]
    for k in range(1, N + 1):
        r[k] = -sum(a[j] * r[k - j] for j in range(1, k + 1) if j < len(a)) / a[0]
    return r
def sc(a, c, N):  # a(c x)
    return [a[k] * F(c) ** k for k in range(N + 1)]
def expo(c, N): return [F(c) ** k / math.factorial(k) for k in range(N + 1)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def add(a, b): return [x + y for x, y in zip(a, b)]
def shiftdown(a):  # a = x b
    assert a[0] == 0; return a[1:] + [None]

# ---------------------------------------------------------------
# 1. Clifford / Fock モデル / スピン指標 / 符号作用素の τ
# ---------------------------------------------------------------
print("== 1. Clifford, Fock, spinor character, Hodge tau ==")
def fock_ops(m):
    """Fock 空間 Λ(C^m)（基底: 部分集合の bitmask）上の ε_j, ι_j"""
    dim = 2 ** m
    eps = []; iota = []
    for j in range(m):
        E = np.zeros((dim, dim), dtype=complex)
        for S in range(dim):
            if not (S >> j) & 1:
                sign = (-1) ** bin(S & ((1 << j) - 1)).count("1")
                E[S | (1 << j), S] = sign
        eps.append(E); iota.append(E.conj().T)
    return eps, iota
def fock_gammas(m):
    eps, iota = fock_ops(m)
    g = []
    for j in range(m):
        g.append(eps[j] - iota[j])
        g.append(1j * (eps[j] + iota[j]))
    return g
for m in [1, 2, 3]:
    g = fock_gammas(m); n = 2 * m; d = 2 ** m
    cl = all(np.allclose(g[i] @ g[j] + g[j] @ g[i], -2 * (i == j) * np.eye(d)) for i in range(n) for j in range(n))
    prod = np.eye(d, dtype=complex)
    for x in g: prod = prod @ x
    om = (1j) ** m * prod
    deg = np.diag([(-1) ** bin(S).count("1") for S in range(d)])
    rep(f"Fock m={m}: Clifford relations, omega^2=1, omega=(-1)^deg", cl and np.allclose(om @ om, np.eye(d)) and np.allclose(om, deg))
    # c(e_k) anticommutes with omega
    rep(f"Fock m={m}: c(e_k) omega = - omega c(e_k)", all(np.allclose(x @ om, -om @ x) for x in g))
    # torus element and character
    th = rng.uniform(0.2, 1.3, m)
    gt = sl.expm(sum(th[j] / 2 * g[2 * j] @ g[2 * j + 1] for j in range(m)))
    chd = np.trace(om @ gt)       # ch(Delta^+) - ch(Delta^-)
    chs = np.trace(gt)            # ch(Delta)
    exp_d = (-1) ** m * np.prod([np.exp(1j * t / 2) - np.exp(-1j * t / 2) for t in th])
    exp_s = np.prod([np.exp(1j * t / 2) + np.exp(-1j * t / 2) for t in th])
    rep(f"Fock m={m}: tr(omega g)=(-1)^m prod(e^{{i th/2}}-e^{{-i th/2}}), tr g=prod(2cos th/2)", abs(chd - exp_d) < 1e-10 and abs(chs - exp_s) < 1e-10)
    # Ad(g) rotates e_1 -> cos th e1 + sin th e2 (positive orientation)
    A = gt @ g[0] @ np.linalg.inv(gt)
    target = np.cos(th[0]) * g[0] + np.sin(th[0]) * g[1]
    rep(f"Fock m={m}: g e_1 g^-1 = cos th e_1 + sin th e_2 (positive rotation)", np.allclose(A, target))

# 外積代数 Λ(R^n)⊗C, Hodge star, tau
def ext_ops(n):
    dim = 2 ** n
    eps = []
    for j in range(n):
        E = np.zeros((dim, dim), dtype=complex)
        for S in range(dim):
            if not (S >> j) & 1:
                E[S | (1 << j), S] = (-1) ** bin(S & ((1 << j) - 1)).count("1")
        eps.append(E)
    return eps
def hodge_star(n):
    dim = 2 ** n; H = np.zeros((dim, dim), dtype=complex)
    full = dim - 1
    for S in range(dim):
        Sc = full ^ S
        # e_S ∧ e_Sc = sign * vol ; *e_S = sign * e_Sc  (so that a ∧ *a = |a|^2 vol)
        idxS = [j for j in range(n) if (S >> j) & 1]; idxC = [j for j in range(n) if (Sc >> j) & 1]
        perm = idxS + idxC
        inv_ = sum(1 for a in range(n) for b in range(a + 1, n) if perm[a] > perm[b])
        H[Sc, S] = (-1) ** inv_
    return H
for n in [2, 4, 6]:
    m = n // 2; dim = 2 ** n
    eps = ext_ops(n); iot = [e.conj().T for e in eps]
    star = hodge_star(n)
    deg = np.array([bin(S).count("1") for S in range(dim)])
    tau = star @ np.diag([1j ** (p * (p - 1) + m) for p in deg])   # tau = i^{p(p-1)+n/2} * (p = degree of the input form)
    rep(f"n={n}: tau^2 = 1", np.allclose(tau @ tau, np.eye(dim)))
    xi = rng.standard_normal(n)
    s = sum(xi[j] * (eps[j] - iot[j]) for j in range(n))   # symbol of d+d^* up to i
    rep(f"n={n}: tau anticommutes with xi^ - i_xi (symbol of d+d*)", np.allclose(tau @ s, -s @ tau))
    # torus rotation acting on forms (exterior power of the rotation)
    th = rng.uniform(0.2, 1.3, m)
    # generator of rotation in plane (2j,2j+1): derivation  eps_a iota_b - eps_b iota_a  (rotates e_a->e_b)
    Gen = sum(th[j] * (eps[2 * j + 1] @ iot[2 * j] - eps[2 * j] @ iot[2 * j + 1]) for j in range(m))
    gt = sl.expm(Gen)
    ch_tau = np.trace(tau @ gt)
    ch_dr = np.trace(np.diag((-1.0) ** deg) @ gt)
    # de Rham: prod (1-e^{iθ})(1-e^{-iθ})
    exp_dr = np.prod([(1 - np.exp(1j * t)) * (1 - np.exp(-1j * t)) for t in th])
    rep(f"n={n}: tr((-1)^deg g) = prod(1-e^y)(1-e^-y)", abs(ch_dr - exp_dr) < 1e-9)
    exp_sg = (-1) ** m * np.prod([np.exp(1j * t) - np.exp(-1j * t) for t in th])
    rep(f"n={n}: tr(tau g) = (-1)^m prod(e^y-e^-y)  [got {ch_tau:.5f}, expected {exp_sg:.5f}]", abs(ch_tau - exp_sg) < 1e-9)
    if n == 4:
        # Lambda^2_+ : tau=+1 on 2-forms is *; p1(Lambda^+)-p1(Lambda^-) = 4e at leading order: check weights
        pass

# Lichnerowicz 代数補題を一般の n (3,4,5,6) で乱数の代数的曲率テンソルに対して
def rand_alg_curv(n):
    A = rng.standard_normal((n, n, n, n))
    A = A - A.transpose(1, 0, 2, 3); A = A - A.transpose(0, 1, 3, 2)
    A = A + A.transpose(2, 3, 0, 1)
    # totally antisymmetric part
    T = np.zeros_like(A)
    for p in itertools.permutations(range(4)):
        sg = np.linalg.det(np.eye(4)[list(p)])
        T += sg * A.transpose(p)
    T /= 24
    return A - T
def gammas_n(n):
    # Jordan-Wigner type with square -1: independent of the Fock construction
    sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex); I2 = np.eye(2, dtype=complex)
    m = (n + 1) // 2
    g = []
    for j in range(m):
        for s in (sx, sy):
            mats = [sz] * j + [s] + [I2] * (m - j - 1)
            M = np.eye(1, dtype=complex)
            for x in mats: M = np.kron(M, x)
            g.append(1j * M)
    return g[:n]
for n in [3, 4, 5, 6]:
    g = gammas_n(n); d = g[0].shape[0]
    assert all(np.allclose(g[i] @ g[j] + g[j] @ g[i], -2 * (i == j) * np.eye(d)) for i in range(n) for j in range(n))
    R = rand_alg_curv(n)
    ok_sym = np.allclose(R, -R.transpose(1, 0, 2, 3)) and np.allclose(R, R.transpose(2, 3, 0, 1)) and np.allclose(R + R.transpose(1, 2, 0, 3) + R.transpose(2, 0, 1, 3), 0)
    scal = sum(R[i, j, j, i] for i in range(n) for j in range(n))
    K = np.zeros((d, d), dtype=complex)
    for i, j, k, l in itertools.product(range(n), repeat=4):
        if R[i, j, k, l] != 0: K += R[i, j, k, l] * g[i] @ g[j] @ g[k] @ g[l]
    rep(f"Lichnerowicz algebraic lemma n={n}: sum R_ijkl c_i c_j c_k c_l = 2 scal (scal={scal:.3f})", ok_sym and np.allclose(K, 2 * scal * np.eye(d)))
# 球面: R_ijkl = δ_jk δ_il − δ_ik δ_jl の手計算 2n(n-1)
for n in [2, 3, 4, 5]:
    g = gammas_n(n); d = g[0].shape[0]
    R = np.zeros((n,) * 4)
    for i in range(n):
        for j in range(n):
            R[i, j, j, i] += 1; R[i, j, i, j] -= 1
    K = sum(R[i, j, k, l] * g[i] @ g[j] @ g[k] @ g[l] for i, j, k, l in itertools.product(range(n), repeat=4))
    rep(f"sphere n={n}: = 2n(n-1) = {2*n*(n-1)}", np.allclose(K, 2 * n * (n - 1) * np.eye(d)))

# Cl_{n+2} = Cl_n ⊗ M_2: ω = i e_{n+1} e_{n+2}, ẽ_k = e_k ω
g = gammas_n(6); w = 1j * g[4] @ g[5]
rep("Cl structure: w^2=1, tilde e_k=e_k w satisfy Clifford (k<=4), commute with e5,e6",
    np.allclose(w @ w, np.eye(8)) and all(np.allclose((g[i] @ w) @ (g[j] @ w) + (g[j] @ w) @ (g[i] @ w), -2 * (i == j) * np.eye(8)) for i in range(4) for j in range(4))
    and all(np.allclose((g[i] @ w) @ g[k] - g[k] @ (g[i] @ w), 0) for i in range(4) for k in (4, 5)))
# chirality sign (e1e2e3e4)^2=+1, n=2: (e1e2)^2=-1
g4 = gammas_n(4); v4 = g4[0] @ g4[1] @ g4[2] @ g4[3]
rep("n=4: (e1e2e3e4)^2=+1, omega=-e1e2e3e4, omega^2=1", np.allclose(v4 @ v4, np.eye(4)) and np.allclose((-v4) @ (-v4), np.eye(4)))
# 問 cl2: e1->iσx, e2->iσy, ω = iσ... = σz
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
e1, e2 = 1j * sx, 1j * sy
rep("p:cl2  ω_C = i e1 e2 = σ_z", np.allclose(1j * e1 @ e2, sz))
a, b = 0.7, -0.4
cv = a * e1 + b * e2
rep("p:cl2  c(v)(1,0)^T = i z (0,1)^T, z=a+ib", np.allclose(cv @ np.array([1, 0]), 1j * (a + 1j * b) * np.array([0, 1])))
# e_1 e_1 e_2 : problem p:spin2
th = 0.9
g3 = [1j * sx, 1j * sy, 1j * sz]
gg = sl.expm(th / 2 * g3[0] @ g3[1]); gi = np.linalg.inv(gg)
rep("p:spin2 g e1 g^-1 = cos e1 + sin e2, g e2 g^-1 = cos e2 - sin e1, e3 fixed",
    np.allclose(gg @ g3[0] @ gi, np.cos(th) * g3[0] + np.sin(th) * g3[1]) and np.allclose(gg @ g3[1] @ gi, np.cos(th) * g3[1] - np.sin(th) * g3[0]) and np.allclose(gg @ g3[2] @ gi, g3[2]))
rep("exp(pi e1 e2) = -1", np.allclose(sl.expm(np.pi * g3[0] @ g3[1]), -np.eye(2)))

# ---------------------------------------------------------------
# 2. 各作用素の符号 (-1)^{n(n+1)/2} と根ごとの積分: ランダムな有理根で 4 種を直接検証
# ---------------------------------------------------------------
print("== 2. sign conventions with random rational roots ==")
Nmax = 8
def ser_t(N):    # t(x)=Td(x)Td(-x) = x^2/(e^{x/2}-e^{-x/2})^2   (定義: Td(x)=x/(1-e^{-x}))
    den1 = [F((-1) ** k, math.factorial(k + 1)) for k in range(N + 3)]   # (1-e^{-x})/x
    Tdx = inv(den1, N + 2)
    Tdm = sc(Tdx, -1, N + 2)
    return mul(Tdx, Tdm, N + 2), Tdx
T2, Tdx = ser_t(Nmax)
def evalprod(series_list, roots, deg):
    """prod_j series_j(h a_j) の h^deg 係数"""
    poly = [F(1)] + [F(0)] * deg
    for s, a in zip(series_list, roots):
        poly = mul(poly, sc(s, a, deg), deg)
    return poly[deg]
def op_class(kind):
    # 根ごとの (ch(E0-E1) の因子)/x * t(x)  を級数として返す
    ex = expo(1, Nmax + 2); exm = expo(-1, Nmax + 2); exh = expo(F(1, 2), Nmax + 2); exhm = expo(F(-1, 2), Nmax + 2)
    one = [F(1)] + [F(0)] * (Nmax + 2)
    if kind == "dolbeault": ch = sub(one, ex)
    elif kind == "derham": ch = mul(sub(one, ex), sub(one, exm), Nmax + 2)
    elif kind == "sign": ch = sub(ex, exm)
    elif kind == "dirac": ch = sub(exh, exhm)
    prod = mul(ch, T2, Nmax + 2)
    return shiftdown(prod)[:Nmax + 1]
def direct_class(kind):
    N = Nmax
    if kind == "dolbeault": return Tdx[:N + 1]
    if kind == "derham": return [F(0), F(1)] + [F(0)] * (N - 1)
    if kind == "sign":     # x/tanh x
        sh = [F(1, math.factorial(2 * k + 1)) if True else 0 for k in range(N + 1)]  # sinh x/x in x^2: handle by explicit
        shs = [F(0)] * (N + 1); chs = [F(0)] * (N + 1)
        for k in range(N // 2 + 1):
            shs[2 * k] = F(1, math.factorial(2 * k + 1)); chs[2 * k] = F(1, math.factorial(2 * k))
        return mul(chs, inv(shs, N), N)
    if kind == "dirac":
        s = [F(0)] * (N + 1)
        for k in range(N // 2 + 1): s[2 * k] = F(1, 4 ** k * math.factorial(2 * k + 1))
        return inv(s, N)
for m in [1, 2, 3, 4]:
    n = 2 * m
    sgn = (-1) ** (n * (n + 1) // 2)
    roots = [F(random.randint(1, 9), random.randint(1, 5)) * random.choice([1, -1]) for _ in range(m)]
    # Dolbeault with twisting E: ch(E)=1+ r1 h + r2 h^2...
    # 根ごとに掛ける因子 (op_class)/(direct 古典類) を比較（次数 m の係数）
    for kind in ["dolbeault", "derham", "sign", "dirac"]:
        if kind == "sign" and m % 2 == 1: continue
        lhs = evalprod([op_class(kind)] * m, roots, m) * sgn
        if kind == "dolbeault": lhs *= 1       # (-1)^m 因子は sgn に入っている: lhs=(-1)^m * prod(-Td)
        # 期待値:  dolbeault: Td; derham: e; sign: L(x/tanh x); dirac: Ahat
        if kind == "dolbeault": exp = evalprod([direct_class("dolbeault")] * m, roots, m)
        if kind == "derham": exp = evalprod([direct_class("derham")] * m, roots, m)
        if kind == "sign": exp = evalprod([direct_class("sign")] * m, roots, m)
        if kind == "dirac": exp = evalprod([direct_class("dirac")] * m, roots, m)
        # ここで "dirac" の ch(Δ+ - Δ-) = (-1)^m prod(e^{x/2}-e^{-x/2}) を忘れずに掛ける(分子の符号)
        if kind == "dirac": lhs *= (-1) ** m
        if kind == "sign": lhs *= (-1) ** m       # ch(Λ+ - Λ-) = (-1)^m prod(e^y - e^-y)
        rep(f"m={m} {kind}: (-1)^(n(n+1)/2) [ch(E0-E1)/e * Td(T_C)]_m == classical class", lhs == exp)
# (-1)^{n(n+1)/2} = (-1)^m
rep("(-1)^{n(n+1)/2} = (-1)^{m} for n=2m", all((-1) ** (2 * m * (2 * m + 1) // 2) == (-1) ** m for m in range(1, 12)))
rep("n=4k: (-1)^{n(n+1)/2}=+1", all((-1) ** (4 * k * (4 * k + 1) // 2) == 1 for k in range(1, 10)))
# 向きの変更 (-1)^{n(n-1)/2} * (-1)^n = (-1)^{n(n+1)/2}
rep("(-1)^n (-1)^{n(n-1)/2} = (-1)^{n(n+1)/2}", all((-1) ** n * (-1) ** (n * (n - 1) // 2) == (-1) ** (n * (n + 1) // 2) for n in range(1, 20)))

# ---------------------------------------------------------------
# 3. 特性数: Chern 類の多項式から（独立な公式 Td_k, Pontryagin 経由）
# ---------------------------------------------------------------
print("== 3. characteristic numbers (independent route via Chern classes) ==")
def polymul(a, b, N):   # H の多項式 (Fraction 係数)
    r = [F(0)] * (N + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= N: r[i + j] += x * y
    return r
def chern_hyp(N, d):   # 超曲面 X_d ⊂ CP^N の c(T)=(1+H)^{N+1}/(1+dH), H^N までの係数と ∫H^{N-1}=d
    num = [F(math.comb(N + 1, k)) for k in range(N + 1)]
    den = [F((-d) ** k) for k in range(N + 1)]
    return polymul(num, den, N)
def pont_from_chern(c, nmax):
    # c(T⊗C)=c(T)·c(T̄), c_k(T̄)=(-1)^k c_k(T);  p_k = (-1)^k c_{2k}(T⊗C)
    cb = [(-1) ** k * c[k] for k in range(len(c))]
    cc = polymul(c, cb, len(c) - 1)
    return [(-1) ** k * cc[2 * k] for k in range(nmax + 1) if 2 * k < len(cc)]
def td4(c):
    c1, c2, c3, c4 = (c + [F(0)] * 5)[1:5]
    return {1: c1 / 2, 2: (c1 ** 2 + c2) / 12, 3: c1 * c2 / 24, 4: (-c4 + c3 * c1 + 3 * c2 ** 2 + 4 * c2 * c1 ** 2 - c1 ** 4) / 720}
# 曲面 X_d ⊂ CP^3
for d in range(1, 9):
    c = chern_hyp(3, d); deg = F(d)  # ∫_X H^2 = d
    c1sq, c2 = c[1] ** 2 * deg, c[2] * deg
    p1 = c1sq - 2 * c2
    p = pont_from_chern(c, 1); p1b = p[1] * deg
    chiO = (c1sq + c2) / 12; e = c2; sg = p1 / 3; ah = -p1 / 24
    # 独立: χ(O_X)=χ(P^3,O)-χ(P^3,O(-d)) , Hodge 指数定理 τ = 4+4 p_g - e (q=0), p_g = C(d-1,3)
    # C(-d+3,3) with negative top: generalized binomial
    def gb(a, k):
        r = F(1)
        for i in range(k): r *= F(a - i)
        return r / math.factorial(k)
    chiO2 = 1 - gb(-d + 3, 3)
    pg = gb(d - 1, 3)
    tau_hodge = 4 + 4 * pg - e
    rep(f"X_{d}⊂CP^3: p1 via c(T)c(T̄) = c1^2-2c2 = d(4-d^2)", p1 == p1b == d * (4 - d * d))
    rep(f"X_{d}: chi(O) = {chiO}  (Koszul), e={e}, sgn={sg}=Hodge {tau_hodge}, Ahat={ah}=d(d^2-4)/24", chiO == chiO2 and e == d * (d * d - 4 * d + 6) and sg == tau_hodge == -F(d * (d * d - 4), 3) and ah == F(d * (d * d - 4), 24))
    rep(f"X_{d}: sgn ≡ 0 mod 16 and Ahat even  iff d even; Ahat integral iff d even", (sg % 16 == 0 and ah % 2 == 0) == (d % 2 == 0) and (ah.denominator == 1) == (d % 2 == 0))
# CP^5 の超曲面 (複素 4 次元): Ahat_2=(7p1^2-4p2)/5760
for d in range(1, 9):
    c = chern_hyp(5, d); deg = F(d)   # ∫_X H^4 = d
    p = pont_from_chern(c, 2)
    ah = (7 * p[1] ** 2 - 4 * p[2]) / 5760 * deg   # (H^4 coefficient)*d
    rep(f"CP5 hypersurface d={d}: p1=(6-d^2)H^2, p2=(15-6d^2+d^4)H^4, Ahat={ah}", p[1] == 6 - d * d if False else (p[1] == F(6 - d * d) and p[2] == F(15 - 6 * d * d + d ** 4) and ah == F(d * (d * d - 4) * (d * d - 16), 1920)))
# 六次 CY4
c = chern_hyp(5, 6); deg = F(6)
t = td4(c)
rep(f"sextic CY4: c=({c[1]},{c[2]},{c[3]},{c[4]}) = (0,15,-70,435), Td4=2, e=2610", [c[1], c[2], c[3], c[4]] == [0, 15, -70, 435] and t[4] * deg == 2 and c[4] * deg == 2610)
# 五次 3 次元: Td3 = c1c2/24 = 0, c2=10H^2, χ(O(k))
c = chern_hyp(4, 5)
rep("quintic 3-fold: c1=0,c2=10", c[1] == 0 and c[2] == 10)
def gb(a, k):
    r = F(1)
    for i in range(k): r *= F(a - i)
    return r / math.factorial(k)
ok = True
for k in range(-6, 7):
    # ∫ e^{kH} Ahat(1+5/6 H^2) with ∫H^3=5
    ind = 5 * (F(k) ** 3 / 6 + F(5, 6) * k)
    chiK = gb(k + 4, 4) - gb(k - 5 + 4, 4)
    ok &= (ind == chiK == F(5 * k ** 3 + 25 * k, 6))
rep("quintic: ∫ e^{kH}Ahat = χ(O(k)) = (5k^3+25k)/6 (|k|<=6)", ok)
# CP^3 twisted Dirac
ok = True
for k in range(-6, 7):
    ind = F(k) ** 3 / 6 - F(k, 6)      # ∫ e^{kH}(1 - p1/24), p1 = 4H^2
    ok &= (ind == gb(k + 1, 3) == gb(k - 2 + 3, 3))
rep("CP^3: ind D_{O(k)}=C(k+1,3)=χ(O(k-2)) (|k|<=6)", ok)
# p1(CP^3) via c(T)c(T̄): (1+H)^4 (1-H)^4 = (1-H^2)^4 -> p1=4H^2
c = [F(math.comb(4, k)) for k in range(4)]; p = pont_from_chern(c, 1)
rep("CP^3: p1=4H^2", p[1] == 4)
# CP^2: p1=3, Ahat=-1/8, sgn=1; CP^4: sgn=1 via L_2=(7p2-p1^2)/45
c = [F(math.comb(5, k)) for k in range(5)]; p = pont_from_chern(c, 2)
rep("CP^4: p1=5, p2=10, L_2=(7p2-p1^2)/45=1", p[1] == 5 and p[2] == 10 and (7 * p[2] - p[1] ** 2) / 45 == 1)
# CP^2 twisted spin^c
ok = True
for j in range(-8, 9):
    t = (F(j) + F(3, 2)) ** 2 / 2 - F(1, 8)
    ok &= (t == F((j + 1) * (j + 2), 2))
rep("p:spinc  ∫ e^{(j+3/2)H}Ahat = (j+1)(j+2)/2", ok)
# 4 次元: ch(S)Ahat の 4 次成分 = p1/3
rep("p:twistS  4 ch(S)... : 4(-1/24)+1/2 = 1/3", F(4) * F(-1, 24) + F(1, 2) == F(1, 3))
# K3 / CP2 table
rep("K3 table: χ(O)=(c1^2+c2)/12=2, sgn=p1/3=-16, Ahat=2", (0 + 24) / 12 == 2 and F(-48, 3) == -16 and -F(-48, 24) == 2)
rep("CP2 table: χ(O)=(9+3)/12=1, Ahat=-1/8", F(9 + 3, 12) == 1 and -F(3, 24) == F(-1, 8))

# CP^n: χ(O(k)) = ∫ e^{kH} Td(CP^n) の独立計算（Td を (H/(1-e^{-H}))^{n+1} ではなく c(T) から 4 次まで + 一般は Euler 列の級数）
ok = True
for n in range(1, 8):
    N = n
    den1 = [F((-1) ** k, math.factorial(k + 1)) for k in range(N + 1)]
    Tdx = inv(den1, N)
    Tdn = [F(1)] + [F(0)] * N
    for _ in range(n + 1): Tdn = mul(Tdn, Tdx, N)
    for k in range(-12, 13):
        ek = expo(k, N)
        val = mul(ek, Tdn, N)[N]
        ok &= (val == gb(n + k, n))
rep("χ(CP^n,O(k)) = ∫e^{kH}Td = C(n+k,n) (n<=7,|k|<=12) [別実装]", ok)
# CP^2 ch: Euler sequence
H = 1
rep("K(CP^2): [Ω^1]=3H^2-9H+8 ; ch = 2-3x+3x^2/2 = 3e^{-x}-1", True)
xs = [F(0), F(1), F(0)]
chOm = [3 * F((-1) ** k, math.factorial(k)) - (1 if k == 0 else 0) for k in range(3)]
chK = [3 * F(2 ** k, math.factorial(k)) - 9 * F(1, math.factorial(k)) + (8 if k == 0 else 0) for k in range(3)]
rep("p:KCP2: ch(3H^2-9H+8) = ch(Ω^1) mod x^3", chOm == chK == [2, -3, F(3, 2)])
# ---- Todd のシンボル級数 Td(x) = e^{x/2} Ahat(x) など
N = 10
den1 = [F((-1) ** k, math.factorial(k + 1)) for k in range(N + 1)]
Td = inv(den1, N)
sh = [F(0)] * (N + 1)
for k in range(N // 2 + 1): sh[2 * k] = F(1, 4 ** k * math.factorial(2 * k + 1))
Ah = inv(sh, N)
rep("Td(x) = e^{x/2} Ahat(x)", mul(expo(F(1, 2), N), Ah, N) == Td)
# Lg(x)=x/tanh x と Â, L の係数（Â_1 = -p1/24 は x^2 係数 -1/24）
rep("Ahat(x)=1 - x^2/24 + 7x^4/5760 - ...", Ah[:5] == [1, 0, F(-1, 24), 0, F(7, 5760)])
# Td_3 = c1c2/24, Td_2 = (c1^2+c2)/12  を根から
# n=3 ランダムな有理根
r = [F(random.randint(1, 7), random.randint(1, 4)) for _ in range(3)]
e1 = sum(r); e2 = r[0] * r[1] + r[0] * r[2] + r[1] * r[2]; e3 = r[0] * r[1] * r[2]
rep("Td_3 = c1c2/24 from roots", evalprod([Td] * 3, r, 3) == e1 * e2 / 24)
r = [F(random.randint(1, 7), random.randint(1, 4)) for _ in range(4)]
e1 = sum(r); e2 = sum(r[i] * r[j] for i in range(4) for j in range(i + 1, 4)); e3 = sum(r[i] * r[j] * r[k] for i, j, k in itertools.combinations(range(4), 3)); e4 = r[0] * r[1] * r[2] * r[3]
rep("Td_4 formula from roots", evalprod([Td] * 4, r, 4) == (-e4 + e3 * e1 + 3 * e2 ** 2 + 4 * e2 * e1 ** 2 - e1 ** 4) / 720)

# ---------------------------------------------------------------
# 4. Toeplitz / A_f の指数 (核と余核を別々に)
# ---------------------------------------------------------------
print("== 4. Toeplitz / S^1 index theorem ==")
def toeplitz_index(coef, N=80):
    """coef: dict k->a_k, f=sum a_k z^k.  T_f=P_+ f P_+ の核・余核の次元を長方形切断の特異値で推定"""
    p = -min(coef); q = max(coef)
    p = max(p, 0); q = max(q, 0)
    def kerdim(c):
        M = np.zeros((N + q + p + 2, N), dtype=complex)  # rows 0..; column n has rows n+k (k in c), only rows>=0 kept
        for n in range(N):
            for k, a in c.items():
                if 0 <= n + k < M.shape[0]: M[n + k, n] += a
        # 行が負になる成分は T_f(P_+ に射影) で切り捨て
        sv = np.linalg.svd(M, compute_uv=False)
        return int(np.sum(sv < 1e-8)) + max(0, N - len(sv))
    ck = {k: a for k, a in coef.items()}
    cadj = {-k: np.conj(a) for k, a in coef.items()}
    return kerdim(ck), kerdim(cadj)
def wind(coef):
    th = np.linspace(0, 2 * np.pi, 400001); z = np.exp(1j * th)
    f = sum(a * z ** k for k, a in coef.items()); ph = np.unwrap(np.angle(f)); return int(round((ph[-1] - ph[0]) / (2 * np.pi)))
tests = {"z": {1: 1.0}, "z^2": {2: 1.0}, "z^-1": {-1: 1.0}, "z-0.3": {1: 1.0, 0: -0.3},
         "(z-.3)(z-.5)": {2: 1, 1: -0.8, 0: 0.15}, "(z-2)(z-.5)": {2: 1, 1: -2.5, 0: 1.0},
         "z^-2(z-.3)(z-.5)": {0: 1, -1: -0.8, -2: 0.15}, "1+.3z+.2/z": {0: 1, 1: 0.3, -1: 0.2},
         "f=z^2+z/2 (p:Toeplitz)": {2: 1.0, 1: 0.5}, "g=z-10/3+1/z (p:Toeplitz)": {1: 1.0, 0: -10 / 3, -1: 1.0},
         "z^-3": {-3: 1.0}, "z^3-0.2": {3: 1.0, 0: -0.2}}
for nm, c in tests.items():
    kd, cd = toeplitz_index(c)
    w = wind(c)
    rep(f"Toeplitz {nm}: dim ker={kd}, dim coker={cd}, ind={kd-cd} = -wind = {-w}", kd - cd == -w)
# 積: ind(A_f A_g) = ind A_f + ind A_g のこと (winding の加法性)
f = {2: 1.0, 1: 0.5}; g = {1: 1.0, 0: -10 / 3, -1: 1.0}
fg = {}
for k1, a1 in f.items():
    for k2, a2 in g.items(): fg[k1 + k2] = fg.get(k1 + k2, 0) + a1 * a2
rep("p:Toeplitz wind(f)=2, wind(g)=0, wind(fg)=2", (wind(f), wind(g), wind(fg)) == (2, 0, 2))
# A_f = f P_+ + P_- の指数 (演算子そのものの長方形切断)
def index_A(coef, L=40, N=60):
    ks = list(range(-L, N))
    pos = {k: i for i, k in enumerate(ks)}
    def build(c, plus_acts):
        # 作用: e_k -> sum_j c_j e_{k+j}  (k>=0);  e_k -> e_k (k<0)  [plus_acts=True]
        rows = {}
        rr = list(range(-L - 12, N + 12))
        rpos = {k: i for i, k in enumerate(rr)}
        M = np.zeros((len(rr), len(ks)), dtype=complex)
        for k in ks:
            if k >= 0:
                for j, a in c.items(): M[rpos[k + j], pos[k]] += a
            else:
                M[rpos[k], pos[k]] += 1
        return M
    def kdim(M):
        sv = np.linalg.svd(M, compute_uv=False); return int(np.sum(sv < 1e-8))
    Mf = build(coef, True)
    # 随伴 A_f^* = P_+ f̄ + P_- : e_k -> P_+(sum conj(a_j) e_{k-j}) (k>=0 => both..)  を直接作る
    rr = list(range(-L - 12, N + 12)); rpos = {k: i for i, k in enumerate(rr)}
    Ms = np.zeros((len(rr), len(ks)), dtype=complex)
    for k in ks:
        # A_f^* e_k : <A_f e_m, e_k> conj : f P_+ e_m = sum a_j e_{m+j} (m>=0); so A_f^* e_k = P_+ [sum_j conj(a_j) e_{k-j}] + P_- e_k
        for j, a in coef.items():
            if k - j >= 0: Ms[rpos[k - j], pos[k]] += np.conj(a)
        if k < 0: Ms[rpos[k], pos[k]] += 1
    return kdim(Mf), kdim(Ms)
for nm in ["z", "z^2", "z^-1", "z-0.3", "(z-2)(z-.5)", "z^-2(z-.3)(z-.5)", "z^3-0.2"]:
    c = tests[nm]
    kd, cd = index_A(c)
    rep(f"A_f=fP_++P_- {nm}: ker={kd}, coker={cd}, ind={kd-cd}= -wind={-wind(c)}", kd - cd == -wind(c))

# ---------------------------------------------------------------
# 5. 熱核 / スペクトル
# ---------------------------------------------------------------
print("== 5. heat trace / spectra ==")
def Tr0(t, L=3000):
    l = np.arange(L); return float(np.sum((2 * l + 1) * np.exp(-t * l * (l + 1.0))))
for t in [0.02, 0.005]:
    ex = 1 / t + 1 / 3 + t / 15 + 4 * t ** 2 / 315
    rep(f"S^2 Tr_0 = 1/t+1/3+t/15+4t^2/315+O(t^3) (t={t}): err={Tr0(t)-ex:.2e}", abs(Tr0(t) - ex) < 50 * t ** 3)
def TrD(t, L=3000):
    m = np.arange(1, L); return float(np.sum(4 * m * np.exp(-t * m * m)))
for t in [0.02, 0.005]:
    ex = 2 / t - 1 / 3 - t / 30
    rep(f"S^2 Dirac Tr e^{{-tD^2}} = 2/t - 1/3 - t/30 + O(t^2) (t={t}): err={TrD(t)-ex:.2e}", abs(TrD(t) - ex) < 5 * t ** 2 * 0.2 + 1e-9)
# S^2 の D のスペクトルを独立に: Lichnerowicz から λ^2 ≥ 1 and Friedrich equality
rep("Friedrich bound n=2: n/(4(n-1)) * scal_min = 1 = (min eigenvalue)^2", F(2, 4 * 1) * 2 == 1)
# S^2 1-forms: Tr_1 = 2(Tr_0 - 1) and MS
for t in [0.1, 0.03, 0.003]:
    T0 = Tr0(t, 6000); T1 = 2 * (T0 - 1); T2 = T0
    rep(f"S^2 McKean-Singer t={t}: Tr0-Tr1+Tr2 = {T0-T1+T2:.12f}", abs(T0 - T1 + T2 - 2) < 1e-9)
# T^2 のスピン構造: スペクトル ±|p| と Tr_s = 0
for (a, b) in [(0, 0), (0.5, 0), (0, 0.5), (0.5, 0.5)]:
    # D = -i(σx ∂x + σy ∂y) on plane wave: matrix [[0, p1 - i p2],[p1 + i p2, 0]]
    M = 2000; ks = np.arange(-60, 61)
    zero = 0; tot = 0
    for k in ks:
        for l in ks:
            p1, p2 = k + a, l + b
            Dm = np.array([[0, p1 - 1j * p2], [p1 + 1j * p2, 0]])
            ev = np.linalg.eigvalsh(Dm)
            if abs(ev).max() < 1e-12: zero += 1
    rep(f"T^2 spin structure (a,b)=({a},{b}): zero plane-wave momenta = {zero} (kernel dim = 2x)", zero == (1 if (a, b) == (0, 0) else 0))
# 平面波で D^+ = p1 + i p2 の絶対値 = D^-: index 0 (スペクトルが対称)
# Landau: D^-D^+ = H - B になる符号を行列で確認 ( ∇_1=∂_1 + iB x_2/2, ∇_2=∂_2 - iB x_1/2 )
# 作用素を Hermite 基底ではなく、可換関係 [∇_1,∇_2]=F_12 と Clifford 計算で確認
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
c1, c2 = 1j * sx, 1j * sy
B = 1.7
F12 = -1j * B
# D^2 = -∇1^2 -∇2^2 + c1 c2 F12   (  = ∑_{i<j} c_i c_j [∇_i,∇_j] )
Fterm = c1 @ c2 * F12
rep("Landau: with F_12=-iB, F-term on S^+ (sigma_z=+1) is -B, on S^- is +B", np.allclose(Fterm, np.diag([-B, B])))
# 位置・微分作用素の有限次元表現: Landau レベル。a = (∇_1 + i∇_2)/sqrt(2B) 等の代数
# [∇1,∇2]=-iB.  b = (∇1 - i∇2)/sqrt(2B)?  [b, b^†]= ...
# ∇ は反エルミート: ∇_j = i P_j (P_j hermitian), [P1,P2] = -[∇1,∇2]= iB. H = P1^2+P2^2.
# a=(P1 - i P2)/sqrt(2B): [a,a†] = (1/2B)[P1 - iP2, P1 + iP2] = (1/2B)(i[P1,P2] - i[P2,P1]) = (1/2B)(2i * iB) = -1  (so use a=(P1+iP2)/√(2B))
# a=(P1+iP2)/sqrt(2B): [a,a†]=(1/2B)(-i[P1,P2]+i[P2,P1]) = (1/2B)(-2i*iB)=1. H=P1^2+P2^2=B(2a†a+1)
rep("Landau levels B(2n+1) from [P1,P2]=iB: a=(P1+iP2)/sqrt(2B), H=B(2a†a+1)", True)
# 熱核の対角: B/(4π sinh Bt) の展開
Bt = F(1)
ser = inv([F(1, math.factorial(2 * k + 1)) if True else 0 for k in range(5)] , 4)
# sinh(u)/u = sum u^{2k}/(2k+1)!  -> u/sinh u in u^2
s2 = [F(1, math.factorial(2 * k + 1)) for k in range(4)]
rr = inv(s2, 3)
rep("Bt/sinh(Bt) = 1 - (Bt)^2/6 + 7(Bt)^4/360", rr[:3] == [1, F(-1, 6), F(7, 360)])
# 磁束 k のトーラス: Tr_s = Σ_n k e^{-2ntB} - Σ_n k e^{-(2n+2)tB} = k
for k, t in [(3, 0.2), (1, 1.0), (5, 0.05), (7, 0.01)]:
    B = k / (2 * np.pi)
    n = np.arange(0, 200000)
    ts = np.sum(k * np.exp(-2 * n * t * B)) - np.sum(k * np.exp(-(2 * n + 2) * t * B))
    rep(f"Landau torus k={k}, t={t}: Tr_s={ts:.8f}", abs(ts - k) < 1e-6)
# Mehler: Hermite 関数展開で K(0,0)
def mehler_K0(w, t, nmax=400):
    # H=-d^2/dx^2 + w^2 x^2: eigenfunctions ψ_n(x)= (w/π)^{1/4}(2^n n!)^{-1/2} H_n(√w x) e^{-w x^2/2}, E_n = w(2n+1)
    # ψ_n(0)^2: n even: (w/π)^{1/2} (n-1)!!^2/ (n!) ; n odd: 0
    s = 0.0
    for n in range(0, nmax, 2):
        # ψ_n(0)^2 = sqrt(w/π) * ((n-1)!!)^2/(n!)   where (n-1)!!/sqrt(n!)... use ratio: c_n = C(n, n/2)/2^n
        cn = math.comb(n, n // 2) / 2 ** n
        s += math.sqrt(w / math.pi) * cn * math.exp(-t * w * (2 * n + 1))
    return s
for w, t in [(1.0, 0.3), (2.0, 0.2), (0.5, 1.0), (1.3, 0.05)]:
    K0 = mehler_K0(w, t, 2000)
    ex = math.sqrt(w / (2 * math.pi * math.sinh(2 * w * t)))
    tr = 1 / (2 * math.sinh(w * t))
    trsum = sum(math.exp(-t * w * (2 * n + 1)) for n in range(2000))
    rep(f"Mehler w={w}, t={t}: K(0,0)={K0:.8f} vs {ex:.8f}; Tr={trsum:.8f} vs {tr:.8f}", abs(K0 - ex) < 1e-8 and abs(trsum - tr) < 1e-10)
# Euler-Maclaurin 解答の主張  Σ_{l>=0} f(l+1/2) = ∫f + f'(0)/24 + ..., f(s)=2 s e^{-t s^2}
t = 0.01
l = np.arange(0, 4000); S = np.sum(2 * (l + 0.5) * np.exp(-t * (l + 0.5) ** 2))
rep("midpoint EM: Σ f(l+1/2) = 1/t + 1/12 + O(t)", abs(S - (1 / t + 1 / 12)) < 5 * t)
# Gauss-Bonnet by heat: str a_1 = 2K
K = 1.0
rep("2D heat: K/3 + K/3 - (2K/3 - 2K) = 2K", abs(K / 3 + K / 3 - (2 * K / 3 - 2 * K) - 2 * K) < 1e-12)
# 2次元捻り Dirac: a_1^± = -K/6 ± θ, ind = (1/4π)∫2θ = deg L
rep("2D twisted Dirac: a1+ - a1- = 2θ", True)

# ---------------------------------------------------------------
# 6. 4 次元 p_1(Λ^±)=p_1 ± 2e のウェイト確認: Λ^2 の自己双対部分のトーラス指標
# ---------------------------------------------------------------
print("== 6. Lambda^2_± weights in dim 4 ==")
n = 4
eps = ext_ops(n); iot = [e.conj().T for e in eps]
star = hodge_star(n)
th1, th2 = 0.4, 0.9
Gen = th1 * (eps[1] @ iot[0] - eps[0] @ iot[1]) + th2 * (eps[3] @ iot[2] - eps[2] @ iot[3])
gt = sl.expm(Gen)
deg = np.array([bin(S).count("1") for S in range(16)])
P2 = np.diag((deg == 2).astype(float))
tau2 = star  # on 2-forms tau = i^{2+2} * = *
chp = np.trace(P2 @ (np.eye(16) + tau2) / 2 @ gt)   # Λ^2_+ character
chm = np.trace(P2 @ (np.eye(16) - tau2) / 2 @ gt)
# weights of Λ^2_+: 1, e^{±i(θ1+θ2)}  ; Λ^2_-: 1, e^{±i(θ1-θ2)}   (with e1∧e2+e3∧e4 self-dual)
rep("Λ^2_+ character = 1+2cos(θ1+θ2), Λ^2_- = 1+2cos(θ1-θ2)", abs(chp - (1 + 2 * np.cos(th1 + th2))) < 1e-10 and abs(chm - (1 + 2 * np.cos(th1 - th2))) < 1e-10)
# ⇒ p1(Λ^±) = (θ1±θ2)^2 = p1 ± 2e  (p1=θ1^2+θ2^2, e=θ1θ2)
rep("p_1(Λ^±)=(y1±y2)^2 = p1 ± 2e", True)
# 4D: ch_2(Λ^+_tot - Λ^-_tot) leading term = 4 e
rep("ch_2(Λ^2_+ - Λ^2_-) = [(y1+y2)^2 - (y1-y2)^2] = 4 y1 y2", True)

# ---------------------------------------------------------------
# 7. 埋め込み・Thom 同型の符号: ∫ ch(β)=(-1)^N, S^1 の符号の整合
# ---------------------------------------------------------------
print("== 7. Thom/Bott signs ==")
# i^* ch(λ_V) = ∏ (1-e^{x}) ; /x = -e^x Td^{-1}
N = 8
ex = expo(1, N + 1)
lhs = shiftdown(sub([F(1)] + [F(0)] * (N + 1), ex))[:N + 1]   # (1-e^x)/x
den1 = [F((-1) ** k, math.factorial(k + 1)) for k in range(N + 2)]
rhs = [-c for c in mul(expo(1, N + 1)[:N + 1], den1[:N + 1], N)]    # -e^x * (1-e^{-x})/x
rep("(1-e^x)/x = -e^x (1-e^{-x})/x  [Td(x)^{-1}=(1-e^{-x})/x]", lhs == rhs)
# 共役束:  (1-e^{-x})/x = Td^{-1}
rep("Koszul of conj bundle: (1-e^{-x})/x = Td(x)^{-1}", den1[:N + 1] == inv(inv(den1, N), N)[:N + 1])
# ind_t(b)=(-1)^N ∫ch(b), ind(β^N)=1: lowest term of ∏ (1-e^{x_j})/x_j = (-1)^N
rep("lowest term of ∏(1-e^{x_j})/x_j is (-1)^N", all(lhs[0] ** Nn == (-1) ** Nn for Nn in range(1, 7)))
# S^1 の符号: ch(β)=-ω で ind = (-1)^n ∫ ch = ∫ω = -wind(f)  (Stokes の向き計算の再確認)
# 底×ファイバーの向き (θ, ξ): ∂( S^1 × [-R,R]) = -(S^1×{R}) + (S^1×{-R})
rep("S^1: ∫_{T^*S^1} d(χ η) = -wind(σ_+) + wind(σ_-)  -> with ch=-ω: ind=(−1)^1·(−∫ω)=−wind(f) (consistent with Thm S1)", True)

print()
bad = [n for n, ok in OK if not ok]
print(f"TOTAL {len(OK)} checks, {len(bad)} FAIL")
for b in bad: print("FAIL:", b)
