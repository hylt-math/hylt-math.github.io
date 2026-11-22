# 第1巻 独立査読報告

対象: part0〜part8.tex（build.sh が cat で vol01.tex を生成するので、元ファイルは part*.tex。vol01.tex は生成物）、vol01.pdf（37 頁）。
修正前の PDF は vol01_before_review.pdf、修正前の tex は vol01_before_review.tex。修正後 xelatex を2回通し 37 頁、エラーなし。修正箇所の PDF を目視確認した。

## 発見した誤り・不備と修正（最小限）
| # | 箇所 | 旧 → 新 | 理由 |
|---|---|---|---|
| 1 | §4 Poincaré 双対（定理 4.8、part3.tex） | 「向きづけられたコンパクト $n$ 次元多様体」→「向きづけられた**連結な**コンパクト…」。完全対は連結でなくても成り立つ旨を追記 | $\int_M:H^n(M)\cong\R$ は連結でなければ偽（成分の数だけ $\R$ が並ぶ） |
| 2 | §4 調和形式（part3.tex） | 「$M$ に Riemann 計量を入れると」→「コンパクト多様体 $M$ に…」 | Hodge の定理にはコンパクト性が必要 |
| 3 | §3 Stokes（part2.tex） | 境界の向きの記述なし → 「$\partial M$ には外向き法線を先頭にする誘導向き」を追記 | 例の $\int_{S^2}\omega=4\pi$ の符号が向きの規約に依存する |
| 4 | 解答 17(c)（part7.tex） | 行列 $\begin{pmatrix}0&-I\\I&0\end{pmatrix}$「符号は規約」→ $\omega(\partial_{\xi_i},\partial_{x^j})=\delta_{ij}$ より $\begin{pmatrix}0&I\\-I&0\end{pmatrix}$、$\dd\lambda$ の符号を逆にとる文献では逆、と明記 | 本巻の規約 $\omega=\dd\xi_i\wedge\dd x^i$、$\dd x\wedge\dd y(\partial_x,\partial_y)=1$ では旧記述の符号が逆 |
| 5 | 問 27（part4.tex、p:hermexist） | (a) が「任意の複素束に Hermite 計量があることを 1 の分割なしに $\CP^1$ のタウトロジー束で構成せよ」（一般論の主張と具体例の混同。1 の分割なしに一般の束には作れない）→ 「部分束には標準内積の制限が使える。$\mathcal O(-1)$ でこれが滑らかな Hermite 計量であることを示せ」 | 問題文が不適切 |
| 6 | 解答 3（part7.tex） | $TS^1$ の自明性を問題文の指示「ここから導け」に反して直接の切断だけで示していた → $TS^1\oplus\varepsilon^1\cong\varepsilon^2$ の $\Lambda^2$ から $TS^1\cong\varepsilon^1$ を導く議論を追加し、直接の切断は別解として残した | 問題文の要求を満たしていなかった |
| 7 | つまずきやすい点 2（part8.tex） | 「座標でない枠（極座標の $\partial_r/r$ など）では $0$ でないことがある」→ 正規直交枠 $\partial_r,\ \frac1r\partial_\theta$ で $[\partial_r,\frac1r\partial_\theta]=-\frac1{r^2}\partial_\theta\ne0$ | 旧例は誤り。問 9 で示したとおり $\partial_r=(x\partial_x+y\partial_y)/r$ は座標ベクトル場そのもので $\partial_\theta$ と可換 |
| 8 | 参考文献 Lee（part8.tex） | 「第1〜5章、第3章」の重複と【要確認】 → 章題を第2版の目次（著者サイトの front matter）で確認し、章対応を整理。【文献】に格上げ（章内の個々の主張の位置は未確認と明記） | 出典の確認 |
| 9 | 参考文献 Warner | 「微分形式、de Rham（第1・2・4章）」→ 第1章 Manifolds、第2章 Tensors and Differential Forms、第4章 Integration on Manifolds、第5章 Sheaves, Cohomology, and the de Rham Theorem、第6章 Hodge | 旧記述は de Rham の定理を第4章としており誤り。Springer の目次で確認 |
| 10 | 参考文献 Milnor–Stasheff | 「第2〜3章、第14章」→ 「§2〜§3、§14」（本書は章でなく § で区切られる。§1 Smooth manifolds、§2 Vector bundles、§14 Chern classes は目次で確認、§3 は記憶のまま【要確認】） | 章/§の取り違え |
| 11 | check.py（検算コード、part ではない） | $\beta$ の第2項を $(y^2,(0,2))$ としていたため $y^2\,\dd x\wedge\dd z$ になり、出力は $\dd\beta=(z-2y)\,\mathrm{vol}$ だった。$y^2\,\dd z\wedge\dd x=-y^2\,\dd x\wedge\dd z$ に直した | 本文・解答の $\dd\beta=(z+2y)\,\mathrm{vol}$ は正しいが、「検算：コードで $\dd\beta$」は本文の $\beta$ とは別の式を検算していた。修正後に $z+2y$ を確認（check3.py） |

## 確認した項目（誤りなし）
計算は自作の有理係数多項式コード（check.py、新規 check3.py/check4.py）、numpy による有限差分、手計算の三通りで確認した。

- 定義・定理（Part 0〜7 の全定義・定理・命題・補題・例・注意）を読み、符号・係数・仮定を確認：座標変換則、Lie 括弧の成分式と性質、Frobenius、$\dd$ の公理、不変公式、Cartan の公式（証明のスケッチと $\omega=f\,\dd x^1$ の確認例を含む）、$[\Lie_X,\iota_Y]=\iota_{[X,Y]}$、$\Lie_X\mathrm{vol}=\mathrm{div}X\,\mathrm{vol}$、ホモトピー作用素 $K$ の証明の符号（$\dd K+K\dd=\id-\pi^*s_0^*$）、Mayer–Vietoris の写像の向きと全射性の構成、$S^n$ の MV 帰納、$\chi$ の加法性、貼り合わせ関数のコサイクル条件と表（$\mathrm{Hom}$: $hXg^{-1}$、双対: $(g^{-1})^T$）、ゲージ変換 $A'=g^{-1}Ag+g^{-1}\dd g$、$F=\dd A+A\wedge A$、Bianchi の証明、ユニタリ条件 $A^*=-A$、Levi-Civita の構造方程式と $S^2$ の $\omega^1{}_2=-\cos\vartheta\,\dd\varphi$、$K=1$、Chern–Weil（閉性、transgression の公式と符号）、Chern 形式の演算、Gauss–Bonnet（$c_1(T\Sigma)=\frac1{2\pi}K\,\dd A$）、$\int c_1=-\mathrm{wind}(g)$ の Stokes の議論、$e_0=g\,e_1$ の向きの規約。
- **新規の独立検算（check3.py, check4.py）**：Poincaré の補題の公式 $K\omega=\int_0^1t^{k-1}\iota_x\omega(tx)\,\dd t$ が $\R^3$ のランダムな多項式 $k=1,2,3$ 形式で $\dd K+K\dd=\id$（厳密）。$\R^4$ で行列値形式のランダムな接続 $A_0,A_1$ について $\tr F_1^2-\tr F_0^2=\dd T$、$T=2\int_0^1\tr(aF_t)\,\dd t$（厳密に一致）、Bianchi、ゲージ共変性 $F'=g^{-1}Fg$、$\dd_\nabla^2s=Fs$。
- 既存の check.py/check2.py を再実行：$\dd\alpha$、引き戻し、Cartan（1・2 形式）、不変公式、括弧（Euler と回転、$\mathfrak{so}(3)$、接触）、$\dd\omega=3\,\mathrm{vol}$、原始関数 $xy+z^2$、問 29 の $F$ と Bianchi、$\int c_1=-k$（$k=1,2,-3$）、$\theta_0-\theta_1=1/z$、$\dd\theta$ の係数、立体射影の Jacobi 行列式。いずれも本文と一致。
- Witt 代数の括弧（問 11 の $[E,C]=-S$ など）を数値微分で確認。
- 全 40 問の解答を独立に解き直し（手計算＋上記コード）、解答はすべて正しいことを確認した（誤りがあったのは解答 17(c) の行列の符号のみ、および解答 3 の導出の不足）。確認した点の例：立体射影の行列式 $-1/\rho^4$、$\dd F$ の特異点、トーラスの接空間、MV での $T^2$ の Betti 数 $(1,2,1)$、$M_k=\R^2\setminus\{k\text{ 点}\}$ の帰納、$\dim\Lambda^2(E\oplus F)=10$、$\Lambda^{r-1}g=\det g\,(g^{-1})^T$、$F(1,1)=(0,2)$、$\iota_X\dd\omega=-\dd y$（Q2）、$c_2=\frac1{8\pi^2}\tr F\wedge F$ と $\ch_2=-c_2$、$T\CP^1$ の貼り合わせ関数 $-z^{-2}$ の巻き数 $-2$ から $+2$。
- 問題数：prob 40、sol 40。
- 後の巻との整合：第2巻（vol02.tex）と Hermite 計量の線形性の規約（第1成分で線形）、$\partial_{x}\leftrightarrow\partial_z$ の同一視が一致。$T\oplus T^*$ の内積 $\frac12(\xi(Y)+\eta(X))$ は Gualtieri の規約と同じで、Dorfman 括弧 $[X,Y]+\Lie_X\eta-\iota_Y\dd\xi$ は Courant 括弧 $+\ \dd\langle\ ,\rangle$ と計算で整合（Courant $=$ Dorfman $-\tfrac12\dd(\iota_X\eta+\iota_Y\xi)$）。第12巻の本文は未確認。
- 統合論文の記述（全 Euler 標数 $(-1)^n\mathrm{rk}(E)\chi(X)$、双対性 $\mathbb H^k(L)^*\cong\mathbb H^{2n-k}(L^\vee\otimes K^2)$、留数が定数の平坦な対数接続）は _posts の記事の冒頭の主張と一致。
- 出典の確認（WebFetch）：Lee 第2版の章題（第1〜19章）、Bott–Tu の節題（§1〜§7 が第I章、§8〜 が第II章。Poincaré の補題 §4、MV §2、積分 §3、双対・Künneth §5）、Warner の章題、Milnor–Stasheff の §1/§2/§14、Gualtieri の Ann. of Math. 174 (2011) と arXiv:math/0703298。

## 確認できなかった項目（【要確認】のまま）
- Kobayashi–Nomizu の章番号（第I巻 第II章 接続、第IV章 Riemann 接続、第II巻 第XII章 特性類）。第II巻 第XII章 が特性類であることは記憶と整合するが、目次を取得できなかった。
- Huybrechts の第4章（複素ベクトル束、Chern 接続）。
- Milnor–Stasheff の §3。
- Lee（Riemannian Manifolds）の Levi-Civita の章。
- 第12巻本文との Dorfman/Courant 括弧の記号（本巻は【要確認】のまま）。
- Chern 形式の因子（$\frac i{2\pi}$ と $-\frac1{2\pi i}$）の各文献での記号。

## 残る懸念（修正は不要と判断、または仕様の範囲外）
- 接空間の定義（$C^\infty(M)$ 上の点微分）で、基底 $\{\partial_i|_p\}$ の主張は局所化（bump 関数）を要する。本文は問 4 で $\R^n$ の場合だけ示す。標準事項として許容範囲。
- 平坦接続の局所平行枠の存在は【文献】で証明なし。
- 本巻の標題部の注記「査読を受けていない教材」は、この査読後は古くなる。公開時に「Claude による独立査読を 1 回受けた」等に直すかどうかは判断が必要（本査読では書き換えていない）。
- 図（球面上の三角形、流れの交換子）は模式図で、符号や厳密な式は規約によると本文が断っている。
- 手計算のみの解答（検算なし）は、本査読で解き直して全て一致したが、コードによる検算ではなく独立の手計算である（問 1〜3、9 などの手計算の項目）。
