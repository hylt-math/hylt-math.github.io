# 独立検算（査読者による別実装）。verify.py / verify2.py のコードは流用していない。
import numpy as np, itertools, math
from math import comb, pi
rng = np.random.default_rng(7)

# ---------- A. 外積代数（bitmask と明示的な符号規則）----------
def wedge_vec(v, form, n):
    """form: dict{bitmask: coeff}。v ∧ form"""
    out = {}
    for m, c in form.items():
        for j in range(n):
            if m >> j & 1: continue
            sign = (-1) ** bin(m & ((1 << j) - 1)).count("1")
            out[m | (1 << j)] = out.get(m | (1 << j), 0) + sign * v[j] * c
    return out

def contr_vec(v, form, n):
    """iota_v (v は実または複素。ここでは内積 <v,.> = sum v_j conj? ではなく双線形)。 反微分として定義"""
    out = {}
    for m, c in form.items():
        for j in range(n):
            if not (m >> j & 1): continue
            sign = (-1) ** bin(m & ((1 << j) - 1)).count("1")
            out[m ^ (1 << j)] = out.get(m ^ (1 << j), 0) + sign * v[j] * c
    return out

def add(a, b, ca=1, cb=1):
    out = {}
    for k, c in a.items(): out[k] = out.get(k, 0) + ca * c
    for k, c in b.items(): out[k] = out.get(k, 0) + cb * c
    return out

for n in [2, 3, 4, 5, 6]:
    xi = rng.normal(size=n)
    err = 0
    for m in range(1 << n):
        f = {m: 1.0}
        t = add(wedge_vec(xi, contr_vec(xi, f, n), n), contr_vec(xi, wedge_vec(xi, f, n), n))
        for k in range(1 << n):
            err = max(err, abs(t.get(k, 0) - (xi @ xi if k == m else 0)))
    print("A: xi^iota + iota xi^ = |xi|^2, n=%d, err=%.1e" % (n, err))

# ---------- B. シンボル複体の完全性（Koszul）を階数でなく H=0 で確認 ----------
def koszul_homology_dims(vec, n):
    """複素 vec による v∧ の複体 Λ^0 -> ... -> Λ^n のコホモロジー次元（SVD で）"""
    idx = [[m for m in range(1 << n) if bin(m).count("1") == k] for k in range(n + 1)]
    mats = []
    for k in range(n):
        M = np.zeros((len(idx[k + 1]), len(idx[k])), dtype=complex)
        for ci, m in enumerate(idx[k]):
            r = wedge_vec(vec, {m: 1.0}, n)
            for mm, c in r.items():
                M[idx[k + 1].index(mm), ci] = c
        mats.append(M)
    dims = []
    for k in range(n + 1):
        dimk = len(idx[k])
        rin = np.linalg.matrix_rank(mats[k - 1], tol=1e-10) if k > 0 else 0
        rout = np.linalg.matrix_rank(mats[k], tol=1e-10) if k < n else 0
        dims.append(dimk - rin - rout)
    return dims

for n in [1, 2, 3, 4]:
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    print("B: Koszul cohomology dims (v != 0), n=%d:" % n, koszul_homology_dims(v, n))
print("B: v = 0, n=2 (完全でない):", koszul_homology_dims(np.zeros(2, dtype=complex), 2))

# ---------- C. 統合論文の全複体のシンボル: Λ^{0,a} ⊗ Λ^b T、s0=v∧(a 因子)、s1=(-1)^a w∧(b 因子) ----------
def total_symbol_ranks(n, v, w, t=1.0):
    # 基底 (ma, mb) ビットマスクの組
    basis = [(ma, mb) for ma in range(1 << n) for mb in range(1 << n)]
    deg = lambda b: bin(b[0]).count("1") + bin(b[1]).count("1")
    byk = {k: [b for b in basis if deg(b) == k] for k in range(2 * n + 1)}
    mats = {}
    for k in range(2 * n):
        M = np.zeros((len(byk[k + 1]), len(byk[k])), dtype=complex)
        for ci, (ma, mb) in enumerate(byk[k]):
            a = bin(ma).count("1")
            for m2, c in wedge_vec(v, {ma: 1.0}, n).items():
                M[byk[k + 1].index((m2, mb)), ci] += c
            for m2, c in wedge_vec(w, {mb: 1.0}, n).items():
                M[byk[k + 1].index((ma, m2)), ci] += t * (-1) ** a * c
        mats[k] = M
    for k in range(2 * n - 1):
        assert np.abs(mats[k + 1] @ mats[k]).max() < 1e-10
    out = []
    for k in range(2 * n + 1):
        rin = np.linalg.matrix_rank(mats[k - 1], tol=1e-10) if k > 0 else 0
        rout = np.linalg.matrix_rank(mats[k], tol=1e-10) if k < 2 * n else 0
        out.append(len(byk[k]) - rin - rout)
    return out

for n in [1, 2, 3]:
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    w = rng.normal(size=n) + 1j * rng.normal(size=n)
    print("C: total symbol cohomology n=%d (v!=0):" % n, total_symbol_ranks(n, v, w))
# v=0 のとき(ξ^{0,1}=0 は実 ξ≠0 では起きない)完全にならない
print("C: v=0, n=2, w!=0:", total_symbol_ranks(2, np.zeros(2, dtype=complex), rng.normal(size=2) + 0j))

# ---------- D. Weyl 型の格子点数 ----------
def N2(lam):
    r = int(math.isqrt(int(lam)))
    return sum(1 for a in range(-r, r + 1) for b in range(-r, r + 1) if a * a + b * b <= lam)
def N3(lam):
    r = int(math.isqrt(int(lam)))
    return sum(1 for a in range(-r, r + 1) for b in range(-r, r + 1) for c in range(-r, r + 1) if a * a + b * b + c * c <= lam)
print("D: N2:", [N2(l) for l in (100, 1000, 10000)], "pi*lam:", [round(pi * l, 1) for l in (100, 1000, 10000)])
print("D: N3:", [N3(l) for l in (100, 1000)], [round(4 / 3 * pi * l ** 1.5, 1) for l in (100, 1000)])
print("D: r2:", {mu: sum(1 for a in range(-30, 31) for b in range(-30, 31) if a * a + b * b == mu) for mu in (1, 2, 3, 5, 25)})

# ---------- E. Landau 準位の等間隔性: A = d/ds + w s - rho、(1/4) A^*A の固有値 ----------
def landau_levels(k, rho, L=14.0, n=2000):
    w = k / (2 * pi)
    s = np.linspace(-L, L, n); h = s[1] - s[0]
    # A^*A = -d^2/ds^2 + (w s - rho)^2 - w   （A^* = -d/ds + w s - rho、[A,A^*]=2w）
    main = 2 / h ** 2 + (w * s - rho) ** 2 - w
    off = -np.ones(n - 1) / h ** 2
    Hm = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    ev = np.linalg.eigvalsh(Hm)[:6]
    return ev / 4  # ∂̄_L = A/2
for k, rho in [(1, 0), (3, 1), (2, 0)]:
    ev = landau_levels(k, rho)
    print("E: k=%d rho=%d  eig(dbar^*dbar)=" % (k, rho), np.round(ev, 5), " expected n*k/(4pi) =", np.round(np.arange(6) * k / (4 * pi), 5))

# ---------- F. P^n 上の sum_b (-1)^b chi(P^n, ∧^b T(m)) = (-1)^n (n+1)  （Euler 完全列の K 群計算）----------
def chiO(n, a):  # chi(P^n, O(a)) = C(n+a, n) の多項式拡張
    p = 1.0
    for i in range(1, n + 1): p *= (a + i) / i
    return round(p)
def chi_wedgeT(n, b, m):
    # [∧^b T] = sum_{j=0}^b (-1)^j C(n+1, b-j) [O(b-j)]
    return sum((-1) ** j * comb(n + 1, b - j) * chiO(n, b - j + m) for j in range(b + 1))
ok = True
for n in range(1, 7):
    for m in range(-8, 9):
        val = sum((-1) ** b * chi_wedgeT(n, b, m) for b in range(n + 1))
        if val != (-1) ** n * (n + 1): ok = False; print("mismatch", n, m, val)
print("F: sum_b (-1)^b chi(P^n, ∧^bT(m)) = (-1)^n (n+1) for n<=6, |m|<=8:", ok)
print("F: CP^2, E=O: chi(∧^b T) =", [chi_wedgeT(2, b, 0) for b in range(3)])

# ---------- G. Toeplitz/A_f の指数 = -(f の単位円内の零点数) ----------
def winding(coeffs_dict):
    th = np.linspace(0, 2 * pi, 20001)
    z = np.exp(1j * th); f = sum(c * z ** k for k, c in coeffs_dict.items())
    ang = np.unwrap(np.angle(f)); return round((ang[-1] - ang[0]) / (2 * pi))
for name, f in [("z^2+0.3", {2: 1, 0: .3}), ("z^3+0.5z", {3: 1, 1: .5}), ("z^-1+0.3", {-1: 1, 0: .3}), ("1+0.3z", {0: 1, 1: .3})]:
    print("G: f=%s winding = %d  -> ind T_f = %d" % (name, winding(f), -winding(f)))
# T_f = S^2 + 0.3 の余核: ker (S^*^2 + 0.3) を有限切断で数える
N = 60
S = np.diag(np.ones(N - 1), -1)  # (Sx)_j = x_{j-1}
Tf = S @ S + 0.3 * np.eye(N)
sv = np.linalg.svd(Tf, compute_uv=False)
print("G: T_f 切断の最小特異値(上位3):", np.round(np.sort(sv)[:4], 4), "(切断では末尾の境界効果で小さい特異値が出る)")
# 直接: 零ベクトル
a = 1j * np.sqrt(.3)
x1 = np.array([np.conj(a) ** j for j in range(300)]); x2 = np.array([(-np.conj(a)) ** j for j in range(300)])
Sst = lambda x: np.append(x[1:], 0)
print("G: coker vectors residual:", abs(Sst(Sst(x1)) + .3 * x1)[:290].max(), abs(Sst(Sst(x2)) + .3 * x2)[:290].max())

# ---------- H. T^2 の 1 形式 sin(x+y)dx の Hodge 分解（Fourier 乗数で）----------
M = 32
xs = 2 * pi * np.arange(M) / M
X, Y = np.meshgrid(xs, xs, indexing="ij")
f = np.sin(X + Y); g = np.zeros_like(f)
kx = np.fft.fftfreq(M, 1 / M)[:, None] * np.ones((1, M)); ky = np.ones((M, 1)) * np.fft.fftfreq(M, 1 / M)[None, :]
F = np.fft.fft2(f); G = np.fft.fft2(g)
dstar = -(1j * kx * F + 1j * ky * G)   # d^*(f dx + g dy) = -(f_x + g_y)
lap = kx ** 2 + ky ** 2
phi_hat = np.where(lap > 0, dstar / np.where(lap > 0, lap, 1), 0)   # Δφ = d^*α
phi = np.fft.ifft2(phi_hat).real
dphi_x = np.fft.ifft2(1j * kx * phi_hat).real; dphi_y = np.fft.ifft2(1j * ky * phi_hat).real
print("H: phi vs -cos(x+y)/2:", abs(phi + .5 * np.cos(X + Y)).max())
rx = f - dphi_x; ry = g - dphi_y  # = d^*ψ の成分
print("H: remainder vs (1/2) sin(x+y)(dx - dy):", abs(rx - .5 * np.sin(X + Y)).max(), abs(ry + .5 * np.sin(X + Y)).max())
# ψ = h dx∧dy, d^*ψ = h_y dx - h_x dy
h = -.5 * np.cos(X + Y); Hh = np.fft.fft2(h)
hy = np.fft.ifft2(1j * ky * Hh).real; hx = np.fft.ifft2(1j * kx * Hh).real
print("H: d^*psi vs remainder:", abs(hy - rx).max(), abs(-hx - ry).max())
# 3 成分が互いに直交（L2）
print("H: <dφ, d^*ψ>_L2 =", np.mean(dphi_x * hy + dphi_y * (-hx)))

# ---------- I. T^2 上の P_a = ∂̄ + a の固有値 ----------
for a in [0.5, 1j, -0.5 + 1.5j, 0.3, 0.5 + 0.1j]:
    ks = [(k1, k2) for k1 in range(-6, 7) for k2 in range(-6, 7) if abs(0.5j * (k1 + 1j * k2) + a) < 1e-12]
    print("I: a=%s kernel modes:" % a, ks)

# ---------- J. S^1 上の A_f と ∂/∂θ - b: 余核の次元 = 核の次元 ----------
def Pmat(c0, b1, M=80):
    ks = np.arange(-M, M + 1); n = len(ks)
    P = np.diag(1j * ks - c0).astype(complex)
    for i in range(n - 1): P[i, i + 1] = -b1 / 2; P[i + 1, i] = -b1 / 2
    return P
for c0 in [0, 1j, 0.5, 0.3 + 1j, -2j]:
    s = np.linalg.svd(Pmat(c0, 1.5), compute_uv=False)
    print("J: c0=%s, smallest sv=%.3e" % (c0, s[-1]))

# ---------- K. 1 階 Pauli-Dirac のシンボル ----------
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]])
xi, eta = rng.normal(size=2)
S1 = sx * xi + sy * eta
print("K: sigma_1(D)^2 - |xi|^2 =", np.abs(S1 @ S1 - (xi ** 2 + eta ** 2) * np.eye(2)).max())

# ---------- L. 補間不等式・Peetre・交換子の簡単な数値チェック ----------
kk = rng.normal(size=(2000, 3)) * 5; ll = rng.normal(size=(2000, 3)) * 5
br = lambda x: np.sqrt(1 + (x ** 2).sum(-1))
worst = 0
for t in [-3.0, -1.5, 0.7, 2.0]:
    lhs = br(kk) ** t; rhs = 2 ** (abs(t) / 2) * br(kk - ll) ** abs(t) * br(ll) ** t
    worst = max(worst, (lhs / rhs).max())
print("L: Peetre max ratio (<=1):", worst)
# 補間: <k>^{2(s+m-1)} <= eta <k>^{2(s+m)} + eta^{-(m-1)} <k>^{2s}
w2 = 0
for s_, m_, et in [(0.3, 2, .2), (-1, 3, .05), (1.1, 1, 3.0), (0, 4, 10.0)]:
    kv = np.linspace(0, 200, 4001); b2 = 1 + kv ** 2
    w2 = max(w2, (b2 ** (s_ + m_ - 1) / (et * b2 ** (s_ + m_) + et ** (-(m_ - 1)) * b2 ** s_)).max())
print("L: interpolation max ratio (<=1):", w2)
# 交換子補題の係数 mu_eps = exp(-eps|xi|^2): |grad mu| <= 3 <xi>^{-1}
z = np.linspace(0, 400, 400001); worst = 0
for eps in [1, .3, .01, 1e-4]:
    g_ = 2 * eps * z * np.exp(-eps * z ** 2) * np.sqrt(1 + z ** 2)
    worst = max(worst, g_.max())
print("L: sup |grad mu_eps| <xi> over eps in (0,1] (<=3):", worst)
