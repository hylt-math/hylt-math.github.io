# 第4巻 独立査読メモ

対象: vol04.tex（修正前は vol04_before_review.tex / vol04_before_review.pdf）。修正後は xelatex を2回通し、43ページ（修正前42ページ）、未定義参照なし。修正箇所のページ（p.1 表紙、p.33 §10.4、p.41 統合論文との対応表と参考文献）は画像で目視確認し、定理 canonical (c) と参考文献の修正箇所は pdftotext で確認した。

結論: 本文の定理・命題・補題・例の主張と、全40問の解答に、数学的な誤り（符号・係数・仮定の誤り）は見つからなかった。修正したのは、証明の穴 1 件、仮定の不足 2 件、数学的に不正確な記述 3 件、統合論文に関する過大・不正確な記述 4 件、出典の誤り（節・章番号・叢書名）6 件、記号の不統一 1 件、問題文の不整合 1 件。

注意: vol04.tex は part0〜part12.tex を `cat` で連結したものなので、build.sh を再実行すると今回の修正が消える。part*.tex は修正していない（古いまま）。

## 1. 発見した問題と修正

| # | 箇所 | 旧 → 新 | 理由 |
|---|---|---|---|
| 1 | 表紙の注記 | 「査読を受けていない教材。…」→ 指示どおり「外部の査読は受けていない教材。執筆者とは別の AI による独立検査と、可能な範囲の計算での検算は行った。標準的な結果には出典を付け、確認できていないものは【要確認】で示す。」 | 指示。 |
| 2 | 定理（標準写像）(c) の証明 | $x^i dx/y$ $(0\le i\le g-1)$ が基底であることを問 Hodiv（$\deg f=2g+1$ のみ）だけで済ませていた → $\deg f=2g+2$ の場合を追記：$\infty_\pm$ で $\ord(x^i dx/y)=g-1-i\ge0$、有限点では零点・極なし。 | (c) は $\deg f\in\{2g+1,2g+2\}$ を主張するが、後者の計算が本文にも問にもなかった。結論は正しい（独立に再計算：$-i-2+(g+1)=g-1-i$、全次数 $2(g-1-i)+2i=2g-2$）。 |
| 3 | §4 Clifford の直前の文 | 「定理 RR は $\deg D\le0$ のときの Riemann の不等式と $H^1$ の消滅を併せて…」→「$\deg D<0$ での $h^0=0$ と $\deg D>2g-2$ での $h^1=0$（系 rr(b)）を併せて、次数が範囲外の因子の $h^0$ を完全に決める」 | 旧文は何の不等式を指すのか不正確（Riemann の不等式は $\deg D\ge g$ 側で効く）。 |
| 4 | Weierstrass 標準形の導出 | 「$y$ を $y+(a_1x+a_3)/2$ と平行移動、$x$ を平行移動してまとめると」→ 平方完成、$x^2$ の消去、$x\mapsto\lambda^2x,\ y\mapsto\lambda^3y$ の倍率で $x^3,y^2$ の係数をそろえる、と明記 | 係数 $a_0y^2+a_2x^3$ をそろえる倍率の操作が抜けていた。また記号 $a_3$ は直前の式に現れない。 |
| 5 | 例（周期格子）の $\varpi$ | 「レムニスケート定数（の 2 倍）$\varpi=\Gamma(1/4)^2/(2\sqrt{2\pi})$」→「レムニスケート定数 $\varpi=2\int_0^1dt/\sqrt{1-t^4}=\Gamma(1/4)^2/(2\sqrt{2\pi})$」と、変換 $x=u^{-2}$ による $\int_1^\infty dx/\sqrt{x^3-x}=2\int_0^1du/\sqrt{1-u^4}$ を追記 | $\varpi=2.62205755\ldots$ 自体がレムニスケート定数で「2 倍」は誤り。数値を再計算して一致。 |
| 6 | 例（標準曲線を含む 2 次曲面）$g=5$ | 「3 つの 2 次曲面の完全交叉」→「$X$ が 3 角（trigonal）でなければ 3 つの 2 次曲面の完全交叉」 | $g=5$ の 3 角曲線では標準曲線は 2 次曲面の完全交叉にならない（2 次曲面の個数 3 自体は Noether の定理で正しい）。 |
| 7 | 例（Brill--Noether の入口） | 「$W^r_d\ne\emptyset$ なら、特に $\rho\ge0$ のとき $\dim\ge\rho$」→「$\rho\ge0$ なら $W^r_d\ne\emptyset$ で、非空のときは常に $\dim W^r_d\ge\rho$」 | 条件の論理が混ざっていた。 |
| 8 | 例（$g=2$：$\mathrm{Sym}^2X\to\Jac$） | 「$h^0(p+q)=1$ で $p+q\ne K$ の類では単射」→「$p+q\not\sim K$ の類では $h^0(p+q)=1$ なので一意に決まり単射」 | $\ne K$（因子の等号）と $\not\sim K$（線形同値）の混同。 |
| 9 | 問 g2table | 「（例 g2 の表を訂正せよ）」→「例の表と一致することを確かめよ」 | 例 g2 の表は正しい（独立に再導出、下記）。訂正すべき誤りがないのに「訂正せよ」と書いてあった。 |
| 10 | 例（$g=0$、$g=1$ の gap） | 題に $g=0$ とあるが $g=1$ のみ → $g=0$（gap なし、$h^0(np)=n+1$）を 1 文追加 | 題と内容の不一致。 |
| 11 | 例（平面曲線）$h^0(\mathcal O_C(m))$ の式 | 二項係数 $\binom{m-d+2}2$ の約束（$m<d$ で後項 $0$）を明記 | 多項式として読むと $m-d+2<0$ で非零になる。 |
| 12 | §統合論文との対応 冒頭と 1/2/3 | 「記事冒頭の要旨のみ確認、PDF 本文は未読」→ 実際に PDF（日本語版 v1）の §1 要旨、§3 定理 18・注意 21、§4 定理 22・注意 23、§10 定理 92・予想 94 と照合した旨に更新。(1) は定理 22 の式 $\sum_b(-1)^b\chi(X,\wedge^bT\otimes E)=(-1)^n\mathrm{rk}\,\chi(X)$ と一致することを明記、$n=1$ では $\sigma=0$ になることを注記。(2) は「$K^2$ の捻りが現れる理由が見える」→「項の次元の対応として定理 18 と整合する。微分の双対・符号は未確認」。 | 照合の範囲を正確にし、断定を弱めた。 |
| 13 | §統合論文との対応 (3) の末尾（対数シンプレクティックとの対応） | 「…現象の、最も簡単な 1 次元の影である」→ 統合論文では $\wedge^nT=K^{-1}$ の切断 $\sigma^k$ が反標準因子 $D$ に 1 位で消え、留数が $\mathbb Z$ に入るかで cohomology が跳ぶこと、1 次元の例は「反標準因子に 1 位で消える切断」と「対数 de Rham 複体が $H^\bullet(X\setminus D)$」の点だけの形式的な類似で、留数による跳びの機構は再現しないことを明記。keybox の「σ が D で消えると cohomology が跳ぶ」も「類比」と明記。第11巻への橋渡しも「形式的な類似」に。 | 過大な主張。統合論文の跳びは留数 $r_i\in\mathbb Z_{\ge1}$ の共鳴で起きるもので、1 次元例（自明な局所系）にはその機構がない。 |
| 14 | 橋渡しの節の最後の段落 | 「一般化正則直線束の $\chi$ は Riemann--Roch 型の公式で $c_1$ だけで書ける」「…Riemann--Roch の一般化（σ が D 上で消える効果の補正項を含む形）である」→ 全面的に書き換え：統合論文の全 Euler 標数は $c_1(E)$ に\emph{依らず}（定理 22）、論文自身が古典 RR の一般化ではないと述べている（注意 23）。Poincaré 多項式の公式（定理 92）は RR 型と呼ばれるが本巻の RR の拡張として証明されたものではなく、指数定理による統一は予想（予想 94）。 | **統合論文と矛盾する記述**（論文は「$c_1(E)$ に依存する素朴な HRR は不成立」と明記）。 |
| 15 | 橋渡しの対応表 | 「Kodaira 型、埋め込み」の行に、統合論文は $\sigma$ が稠密な開集合で非退化なら一般化正則切断の空間は高々 1 次元で Kodaira 写像は定値（命題 79）と述べている旨を追記。「指数予想」の行に未証明の予想である旨を追記。表の前に「本巻から統合論文の定理が従うという意味ではない」を追記。 | 対応表が、統合論文の否定的結果（埋め込み不可能）と読み違えられる恐れがあった。 |
| 16 | 出典：Forster の節番号 | 有限性定理「第II章 §12」→ **§14**（A Finiteness Theorem）、Serre 双対「§14」→ **§17**（The Serre Duality Theorem）、g=1 の一意化の出典「第II章 §17」→ 削除して未確認と明記。Forster の目次を著者サイトで確認（§12 Cohomology Groups、§13 Dolbeault's Lemma、§14 A Finiteness Theorem、§15 The Exact Cohomology Sequence、§16 The Riemann–Roch Theorem、§17 The Serre Duality Theorem、§18 Functions and Differential Forms with Prescribed Principal Parts、§20 Abel's Theorem、§21 The Jacobi Inversion Problem）。参考文献欄も同様に更新。 | 節番号が実際の目次と食い違っていた。 |
| 17 | 出典：Miranda の章 | 参考文献「第IV--V章（因子、直線束）、第VIII章（Jacobi 多様体）」「Hurwitz は第III章」→ AMS の目次で確認した章題（I Basic Definitions, II Functions and maps, III More examples, IV Integration, V Divisors and meromorphic functions, VI Algebraic curves and the Riemann–Roch theorem, VII Applications of Riemann–Roch, VIII Abel's Theorem, IX–XI 層・Čech・直線束）に直し、RH や Weierstrass 点がどの章かは【要確認】に。第8節の Abel の定理の出典も「第VIII章（Abel's Theorem）」に。 | 章立ての記憶が誤っていた。 |
| 18 | 出典：その他 | Hartshorne III「第7章」→ **§7**。ACGH「第I--II章（Brill--Noether、Weierstrass 点）」→ 章の割り当ては未確認。Griffiths--Harris（Serre 双対、Weierstrass 点、g=1）に【要確認】（節番号）を付与。Huybrechts の章に【要確認】を付与。 | 確認できていない節番号を断定していた。 |
| 19 | 参考文献の Miranda | 「GTM 5 / AMS Graduate Studies 5」→「Graduate Studies in Mathematics 5, AMS, 1995」 | GTM 5 は別の本（Miranda の本は AMS の GSM 5）。 |
| 20 | 記号 | $\mathbb P^n$ → `\CP^n`（第2・3巻の記法）に統一。ただし $\mathbb P(V^*)$（ベクトル空間の射影化）は $\mathbb P$ のまま | 第2・3巻は `\CP` を使う。 |

## 2. 確認した項目（計算または文献で一致）

- **局所形と次数**：局所正規形の証明、$\deg f=\sum e_p$ が定数であること（証明の手順）、例の分岐数（$z^3-3z$：$\deg R=4$、$z+1/z$、$z^2(z-1)$）。
- **留数定理・主因子の次数 0**：Stokes の向き（$\partial X'=-\sum\partial D_i$）、$\mathrm{Res}_p(df/f)=\mathrm{ord}_pf$。
- **$\deg=c_1$ の Stokes による証明と符号**：$\Theta=-\partial\bar\partial\log|s|_h^2$（零点・極の外）、$\partial\bar\partial=d\bar\partial$、Stokes（領域の境界は円板の境界と逆向き）、$\oint_{ccw}d\bar z/\bar z=-2\pi i$ から各極の寄与が $+n_j$。第2巻の規約（$\Theta=\bar\partial\partial\log h$、$c_1=\frac i{2\pi}\Theta$、$c_1(\mathcal O(-1))=-\omega_{FS}$、$\deg\mathcal O(k)=k$）と整合することを再導出して確認。
- **Riemann--Roch の帰納証明**：補題（$\chi(D)-\chi(D-p)=1$）の長完全列、交代和 $h^0(D-p)-h^0(D)+1-h^1(D-p)+h^1(D)=0$、$\chi(0)=1-g$。起点は $D=0$ のみで $h^0(D)=0$（$\deg D<0$）は使わない。有限性は補題と長完全列の各項に使われている。補題 meromsec は $\chi(L(np))=\chi(L)+n$ と $h^0\ge\chi$ のみで Serre 双対に依存しない（循環なし）。
- **系**：$\deg K=2g-2$、$\deg D>2g-2\Rightarrow h^1=0$、Riemann の不等式、$\deg D\ge g\Rightarrow D\sim$ 有効、$g=0$ の特徴づけ。
- **Serre 双対の主張**：対合の well-definedness（$\alpha=\bar\partial\beta$）、$H^1(X,K)\cong\mathbb C$ の骨子、$h^1(D)=h^0(K-D)$。Čech 計算（$\mathbb P^1$、$k\ge2$）の $H^1=\mathrm{span}\{z^{-1},\dots,z^{-(k-1)}\}$、対合 $\delta_{m,j-1}$。Mittag-Leffler の完全列と留数対合（$D=0$）。
- **Clifford**：Hopf 型補題（位数が異なる基底の積）と $2h^0(D)\le\deg D+2$。等号の分類は文献。
- **Riemann--Hurwitz と種数**：$\mathrm{ord}_p(f^*\eta)=e\,\mathrm{ord}(\eta)+e-1$、系（$g_X\ge g_Y$ など）、解析的種数＝位相的種数の証明（三角形分割の Euler 標数との差が 0）。
- **種数の公式**：超楕円（$2g+2$ 個の分岐点）、Fermat（$d(d-1)$、$g=(d-1)(d-2)/2$）、$y^n=\prod_{i=1}^m(x-a_i)$（$g=((n-1)(m-1)-(\gcd(n,m)-1))/2$。$2\le n\le7$、$1\le m\le9$ で RH からの値と一致を再確認）、$(3,4)\to3$、$(3,5)\to4$。$y^2=x^6-1\to y^2=u^3-1$ の分岐数 2、固定点（$(0,\pm i)$）、$\tau=(-x,-y)$ の固定点が無限遠の 2 点であること。
- **Hurwitz $84(g-1)$**：$\mu=2h-2+\sum(1-1/m_i)>0$ の最小値 $1/42$（$(h;m_i)=(0;2,3,7)$）を独立に全探索（$h\le1$、$r\le5$、$m_i\le42$）で再確認。場合分け（$h\ge2$、$h=1$、$r=4$、$r\ge5$）も正しい。
- **Weierstrass 標準形・$\wp$**：$L(6O)$ の次元 6 と 7 個の元の従属。$\wp$ の Laurent 展開 $z^{-2}+3G_4z^2+5G_6z^4+\cdots$、$\wp'^2-4\wp^3+60G_4\wp+140G_6=O(z^2)$（係数 $-24-36=-60$、$-80-60=-140$）、$e_k$ の相異、$\Delta=g_2^3-27g_3^2=16\prod(e_j-e_k)^2$。楕円関数の定理 (c)（偏角の原理の辺ごとの計算、符号 $m\omega_1-n\omega_2$）。$g_2(\mathbb Z[i])=\Gamma(1/4)^8/(16\pi^2)=189.0727$、$c=(g_2/4)^{1/4}=2.6220$ と実周期 $\int_1^\infty dx/\sqrt{x^3-x}=2.62206$ の一致。
- **$g=0,1,2$ の分類**：$g=0$（次数 1 の写像）、$g=1$（$K\sim0$、群構造、$h^0(nO)=n$）、$g=2$（$|K|$ が基点なし、$x=\omega_2/\omega_1$ が 2 重被覆、関数体の 2 次拡大）、モジュライの次元 $3g-3$、$h^1(T_X)=3g-3$、$h^0(T_X)$ の表。
- **標準写像・埋め込み**：補題 criteria (i)(ii)(iii)、$\deg D\ge2g$ で基点なし、$\deg D\ge2g+1$ で埋め込み（$\deg(D-p-q)\ge2g-1>2g-2$）、$g=1$ で最良であること（$\deg2$ は 2 重被覆）。標準写像定理 (a)(b)(d)：$h^0(K-p-q)=g-3+h^0(p+q)$。$|4O|$ の 2 つの 2 次曲面（$u_1^2=u_0u_3$、$u_2^2=u_1u_3+au_0u_1+bu_0^2$）。2 次式の数 $(g-2)(g-3)/2$（$g=3,\dots,8$ で再計算）。平面曲線の $h^0-h^1=dm+1-g$（$d=3,\dots,7$、$m<3d$）。
- **Weierstrass gap・点**：gap 定理 (a)(b)(c) の証明（$h^0(np)-h^0((n-1)p)$ の差分）、超楕円の重み $g(g-1)/2$ と総和 $(2g+2)g(g-1)/2=g^3-g$（$g\le7$）、$g=2$ の 6 点。Fermat 4 次曲線：接線 $y=\zeta^3z$ との交点 $x^4$（接触位数 4）、gap $\{1,2,5\}$、重み 2、$xyz=0$ 上の 12 点、重みの和 $24=g^3-g=3d(d-2)$（Hessian $\propto xyz$ からも 12 点で一致）。
- **Abel の定理・Jacobi の主張**：$\Pic^0=H^1(\mathcal O)/H^1(\mathbb Z)$、格子であることの証明（実線形単射と次元）、Abel（$\Div^0$ が主因子 $\iff\mu=0$）、Jacobi の逆問題、Torelli の述べ方（点の単射）。$g=1$ で零点の和 $-$ 極の和 $\in\Lambda$ との整合。
- **指数としての Riemann--Roch**：$\mathrm{ind}\,\bar\partial_L=\deg L+1-g=\int\mathrm{ch}\,\mathrm{Td}$、Dirac 作用素（$K^{1/2}$）の指数 0、theta 関数の準周期性（$z\mapsto z+\tau$ の因子 $e^{-2\pi ikz-\pi ik\tau}$。$k=3$ で数値再確認、誤差 $10^{-11}$）。
- **全40問の解答**：問題と解答が 1 対 1（各 40）。すべて独立に解き直し（手計算、および上記の Python による再計算：$\wp$ の ODE、$z^2+1/z$ の臨界値 $1.8899,\,-0.9449\pm1.6367i$、$2P$ の公式が曲線上にあること、半群 $\langle2,2g+1\rangle$ の重み、2 次式の次元、平面曲線の RR）、答えは一致した。特に：問 local、divP1、residue、ell0、LD（基底 5 個）、eldim、pullback、Kp1、distinct、ses、cechP1（$k=4$ で $z^{-1},z^{-2},z^{-3}$ と $z^0,z^1,z^2dz$、$k=1$ で $H^1=0$）、Serredual、ellh0、P1h0（$h^1=4$）、g2table、Pnvect、conj、RHbasic（$z^2+1/z$ が単純分岐 4 個の例）、Rcount、fermat、quotient、gstar（$\Delta(y^2=x^3-x)=64$）、y5、chord、Hodiv、j、ratnormal、planequartic、g4（$h^0(2K)=9$）、pic0dim、abelell（$\ell/h$ の因子）、BN、gaps1、gapproof、weight、fermatW、index、landau、euler1（$-2,0,2$）、logdr（$(1,1,0)$）。解答の誤りはなし。
- **他巻との整合**：第2巻の $\Theta$、$c_1$ の規約、第3巻の Čech・層コホモロジー・Dolbeault 定理の使い方、第2・3巻が第4巻に予告した内容（Serre 双対、$\chi(\mathcal O(k))=k+1$、$H^1(X,K)\to\mathbb C$ のトレース、$\Pic^0$ が複素トーラス、Riemann--Roch）が本巻に実際にあることを確認。
- **統合論文との照合**（PDF 日本語版 v1）：全 Euler 標数 $(-1)^n\mathrm{rk}(E)\chi(X)$（定理 22）の $n=1$ 版が問 euler1 と一致。双対性 $\mathbb H^k(L)^*\cong\mathbb H^{2n-k}(L^\vee\otimes K^2)$（定理 18）の項ごとの対応（$\wedge^bT\otimes L$ の双対が $\wedge^{n-b}T\otimes L^\vee\otimes K^2$）が $n=1$ で本文の記述と一致。対数 de Rham の Euler 標数 $\chi(U)$（定理 25）と、本文の $\chi_{\rm top}(X)-\deg D=\chi_{\rm top}(X\setminus D)$ が一致。$D$ が反標準因子であること（定理 28 の証明）が、$g=0$ の $D=[0]+[\infty]$ と整合。
- **出典の確認（目次で確認できたもの）**：Forster の節題（上記 #16）、Miranda の章題（#17）。

## 3. 確認できなかった項目（【要確認】のまま）

- Griffiths--Harris、Huybrechts、Voisin、ACGH の章・節番号（本文・参考文献で【要確認】または章のみ）。Hartshorne IV 練習問題 2.5（Hurwitz）、Hartshorne IV §5（Clifford の等号の分類）、Miranda のどの章に Riemann--Hurwitz・自己同型・Weierstrass 点があるか。
- Forster の $H^1(X,\mathcal M)=0$ と g=1 の一意化の節。
- Picard 束の Chern 指標 $\mathrm{ch}=(d-g+1)-\theta$（ACGH 第VII章にあるはずだが未確認、本文で【要確認】のまま）。
- Deligne（対数 de Rham 複体と $H^\bullet(X\setminus D)$）の具体的な箇所。
- 統合論文の (1)(2)(3) で述べた複体の同定、微分の双対、符号（統合論文の定義の細部は読んでいない。本文で【要確認】のまま）。
- Serre 双対（定理）、有限性定理、Riemann の存在定理・GAGA、Torelli、Jacobi の逆問題、Brill--Noether の結果は【文献】として引用しており、本巻では証明していない。

## 4. 残る懸念

- Serre 双対の証明は骨子（楕円型正則性と Hodge 理論の引用）で、完全な証明ではない。本文もそう明示しており、Riemann--Roch 自体の証明はこの定理を入力とした条件つき。
- 定理 genus の証明は、閉曲面の分類（位相的種数）と三角形分割の存在を前提にしている（本文に明記）。
- 解答のうち「検算していない」とされた定性的な項目（証明問題）は、今回、手計算で論理を追った範囲で誤りは見つからなかったが、数値検算の対象ではない。
- 記号 $\mathcal A^{0,q}$（本巻は `\mathcal A`、第2・3巻は `\A` / `\sA`）、Čech の文字（`\Cech` の定義が第3巻と異なる）は巻ごとの差が残っている（表示上の問題はない）。
- 再現スクリプトは本巻の verify.py に加え、scratchpad の rev/chk.py（今回の独立検算）。なお rev ディレクトリは他の査読作業と共用で、chk.py と edit.py は私が作成した名前だが、同名の既存ファイルがあった場合は上書きした可能性がある。
