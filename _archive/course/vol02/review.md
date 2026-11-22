# 第2巻 独立査読メモ

対象: vol02.tex（修正前は vol02_before_review.tex / vol02_before_review.pdf）。修正後は xelatex を2回通し、30ページ、未定義参照なし。修正箇所のページ（p.5 図と命題 2.2 の周辺、p.12、p.15 例 5.7、p.17 問 TP1、p.19 Kähler 恒等式）は画像で目視確認した。

結論: 本文の定理・命題・補題・例・注意の主張、および全40問の解答に、数学的な誤り（符号・係数・仮定の誤り）は見つからなかった。修正したのは、証明の穴 1 件、仮定の不足 1 件、規約の不整合 3 件、他巻との整合 1 件、出典の過剰な断定 3 件、図の重なり 1 件。

## 1. 発見した問題と修正

| # | 箇所 | 旧 | 新 | 理由 |
|---|---|---|---|---|
| 1 | 例 5.7（CP^n の正則切断）の逆の部分 | 「（概略）… $f_0$ の次数が $k$ 以下（増大度から）となり、斉次化して $P$ を得る」 | 引き戻しで $\mathbb C^{n+1}\setminus0$ 上の正則関数 $F$（$F(\lambda Z)=\lambda^kF(Z)$）を作り、Hartogs（注意 4.8、$K=\{0\}$）で $\mathbb C^{n+1}$ へ拡張、Taylor 展開と斉次性から $F=F_k$（$k<0$ なら $F=0$）。 | 概略では $n\ge2$ の主張が実質的に未証明だった。Hartogs を使う短い完全な証明に置換。結論 $\dim=\binom{n+k}{k}$ は正しい。 |
| 2 | 系（局所的な $\bar\partial$-完全性） | 「特に $H^{p,q}_{\bar\partial}(\Delta')=0$（$\Delta'$ が多重円板のとき）」 | 定理の主張（$\Delta'\Subset\Delta$）から直接は出ないので、「多重円板 $\Delta$ 自身の上でも消えるが、増大する縮小列上の解を修正して貼り合わせる近似の議論が要る（GH、Huybrechts §1.3）」と明記。 | 定理の仮定（$\Delta'\Subset\Delta$）と系の結論がずれていた。 |
| 3 | §2、命題 2.2 の直後 | （記述なし） | 複素 Jacobi 行列 $A$ の実 Jacobi 行列式は $\lvert\det A\rvert^2>0$ なので複素多様体は向きづけ可能、を1文追加。 | 第1巻（§1 向きの段落）が「複素多様体は常に向きづけ可能（第2巻）」と予告しているのに第2巻に記述がなかった。 |
| 4 | 注意（Kähler の特徴付け）§7 | $g_{j\bar k}=\delta_{jk}+O(\lvert z\rvert^2)$ | $g_{j\bar k}=\tfrac12\delta_{jk}+O(\lvert z\rvert^2)$（本巻の規約） | 本巻では $\mathbb C^n$ 標準計量で $g_{j\bar k}=\tfrac12\delta_{jk}$ なので規約と不整合（定数倍の違いだが）。 |
| 5 | 問 TP1(a) | $h(\partial_z,\partial_z)=\lambda$ | $h(\partial_z,\partial_z)=\lambda/2$（定数倍は Chern 接続と曲率を変えないので以下 $\lambda$ で計算してよい） | 冒頭の規約 $h(u,v)=g_{\mathbb C}(u,\bar v)$ だと $g_{\mathbb C}(\partial_z,\partial_{\bar z})=\lambda/2$。結果は不変。 |
| 6 | 例（Ricci 形式と $c_1(T\mathbb{CP}^n)$） | 計量行列を $H=(g_{j\bar k})$ と書き、同じ例の最後に超平面類 $H$ が現れる | $(g_{j\bar k})$ と書き改め | 記号 $H$ の二重使用。 |
| 7 | Kähler 恒等式の小節と記号表 | $L=\omega\wedge$、$\Lambda=L^*$ のみ | 「この小節に限り $L$ は $T^{0,1}$・直線束ではなく $\omega\wedge$、$\Lambda$ は格子ではなく $L$ の随伴」と注記。記号表も同様。 | $L=T^{0,1}$（§3, 5）、直線束 $L$（§6）、$L=\omega\wedge$、格子 $\Lambda$、演算子 $\Lambda$ が衝突していた。 |
| 8 | 命題 S2（$\mathbb R^4$ の直交複素構造）の証明 | 「軌道に含まれ、開かつ閉なので等しい」 | $aI+bJ+cK$ が誘導する向きは連続に変わる離散量なので $I$ と同じ、を追記 | 向きの一致が書かれておらず、軌道に含まれる理由が欠けていた。 |
| 9 | 理解チェック(10)の解答 | 「Courant 括弧で閉じた最大等方的部分束（Dirac 構造）」 | 「…（複素 Dirac 構造）で $L\cap\overline L=0$ をみたすもの」 | 一般化複素構造の定義に必要な条件 $L\cap\overline L=0$ が抜けていた。 |
| 10 | 橋渡しの節（第13巻） | 「Poisson 加群になり」と断定 | 末尾に【要確認】を付与 | 第13巻の内容に関する未確認の主張。 |
| 11 | Newlander--Nirenberg の出典、解析的な場合の方針 | 「Hörmander による $\bar\partial$ 方程式を使った証明や Malgrange の証明もある」「（Hörmander、Malgrange）が必要」 | 「Malgrange、Nijenhuis--Woolf、Webster などによる別証明もある【要確認】」。方針の段落は人名を削除。 | Hörmander の教科書に Newlander--Nirenberg の証明があるかを確認できなかったため、断定を避けた。 |
| 12 | 定理 Koszul--Malgrange の出典 | Donaldson--Kronheimer §2.2 | 第2章（節番号は未確認）【要確認】 | §2.2 の番号を確認できなかった（でっち上げの節番号を避ける）。 |
| 13 | 定理 Kähler 条件の出典 | 「Huybrechts §3.1（§3.1）」（重複） | 「Huybrechts 第3章（§3.1）」 | 誤植。 |
| 14 | §2 の CP^1 の図 | ラベルが球に重なっていた | ラベルを右へ移動 | 図の可読性。 |

## 2. 確認した項目（計算または文献で一致）

- Nijenhuis テンソル: 補題（$N(Z,W)=-4\pi^{1,0}[Z,W]$、混合型 $=0$）を手計算で再確認。積分可能性の同値 (a)–(d) の証明は正しい。非積分的な例（$W_2=\partial_{\bar z_2}+f\partial_{z_1}$）の $J_f$ の式、$N(W_1,W_2)=-4\partial_{z_1}$ も再計算して一致。verify.py の数値検算（有限差分）も再実行して一致。
- $J\leftrightarrow L$ の対応、$\mathbb R^2$ の Beltrami（$J_\mu=A^{-1}J_0A$ の行列と $\det=1$）、四元数の $J_J(z,w)=(-\bar w,\bar z)$ と正則座標 $\zeta_1,\zeta_2$、右乗法が逆向きであること。
- Dolbeault--Grothendieck の証明（帰納法、Cauchy 変換の符号 $\frac1{2\pi i}\int\frac{f}{w-z}dw\wedge d\bar w$、Stokes の向き）、楕円曲線・複素トーラスの Fourier 論法（$\partial_{\bar z}\chi_{m,n}=\pi i(m+in)\chi_{m,n}$）。
- 正則束と $\bar\partial_E$、直線束の Koszul--Malgrange（$D''(e^{-u}h)=e^{-u}\bar\partial h$）、$\mathcal O(k)$ の変換則 $f_1=z^{-k}f_0$、$K_{\mathbb{CP}^1}=\mathcal O(-2)$、$K_{\mathbb{CP}^2}=\mathcal O(-3)$（Jacobi 行列式の向きも確認）、第1巻の $e_0=-z^{-2}e_1$ と整合。
- Chern 接続: $\theta=\bar H^{-1}\partial\bar H$（$\nabla e_j=\sum\theta_{kj}e_k$ の規約と第1巻の規約が一致）、曲率 $\Theta=\bar\partial\theta$ が $(1,1)$、$\partial\theta+\theta\wedge\theta=0$、双対・テンソル・$\det$。
- Chern 形式の因子: $c_1=\frac i{2\pi}\Theta$、$\Theta=-\partial\bar\partial\log h$。$h'=e^{-\psi}h$ の差 $\frac i{2\pi}\partial\bar\partial\psi=d(\frac i{4\pi}(\bar\partial-\partial)\psi)$。$\deg\mathcal O(k)=k$、$\mathcal O(-1)$ の $-\omega_{FS}$、第1巻の $-\frac1\pi\frac{dx\wedge dy}{(1+r^2)^2}$ と一致。$\int\omega_{FS}^n=1$（$\mathrm{vol}(S^{2n-1})=2\pi^n/(n-1)!$）。Gauss 曲率との関係 $\frac i{2\pi}\Theta=\frac K{2\pi}dA$（$K=-\frac1{2\lambda}\Delta\log\lambda$）と、球面 $K=1$、円板 $K=-1$。
- Kähler 条件の同値 (a)(b)(c) の証明、トーション（Prop 7.4: $\Gamma^k_{lj}$、混合型 $=0$）。
- Kähler 恒等式の符号: 本巻の規約 $\omega=g(J\cdot,\cdot)$、$\Lambda=L^*$ で、独立に書いた数値検算（$n=2$、平面波の記号で $\partial,\bar\partial$、$L$、随伴をそのまま行列にして $\lvert dz\rvert^2=2$ の内積を使用）で $[\Lambda,\bar\partial]=-i\partial^*$、$[\Lambda,\partial]=i\bar\partial^*$、$[L,\bar\partial^*]=-i\partial$、$[L,\partial^*]=i\bar\partial$ の4式がすべて成立（誤差 0）。Huybrechts と同じ符号。問 kid1（1次元）も手計算で一致。
- Hodge 数の表: 複素トーラス（$h^{1,1}=4$ など）、$\mathbb{CP}^2$、K3（$h^{1,1}=20$、$h^{2,0}=1$、$b_2=22$、$\chi=24$）の整合（$b_k=\sum h^{p,q}$、Serre 双対）。
- Fermat/平面曲線の種数: $g=(d-1)(d-2)/2$、$d=1,\dots,6$ で $0,0,1,3,6,10$（$\chi=2,2,0,-4,-10,-18$）。四次曲面 $c_1=0$。
- Hopf 曲面（$H^2_{dR}=0$、$\omega^2=2\,dV$ の論法、$b_1=1$）。
- 全40問の解答: 問題と解答が1対1（各40）。すべて独立に解き直し、上の項目に含まれない問も含めて、答えは一致した（解答 wirt、count、decomp、cr、pn、compactconst、herm、torus1、Ntensor（(a)(b) の項ごとの確認）、Nexample、dim2、Ndim（$0,2,9,24$）、quat、beltrami、Lalg、dbarcalc、logg、solve、coordindep、fourier、torusfourier、Ok、gauge、integr、rank2（$\theta,\Theta$ の行列まで）、degk、TP1、indep、weight（$\frac1\pi\omega_{\rm std}$）、kahlercn、fsvol、kid1、cpt2k、sub、disc、fermat、hopf、torus2、Kcp、euler）。verify.py も再実行し、全項目 OK または期待どおりの値。
- 他巻との整合: 第1巻の記号（$\frac i{2\pi}$ の Chern 形式、$H_{ij}=h(e_i,e_j)$、Hermite 計量の線型性、$\mathcal O(-1)$ の $e_0=ze_1$、「Lie 亜代数」の訳語）は一致。第12巻の $\mathcal J_J=\mathrm{diag}(-J,J^*)$ と $L=T^{0,1}\oplus\Lambda^{1,0}$ は Gualtieri の記述と同じ符号。

## 3. 確認できなかった項目（【要確認】のまま）

- Borel--Serre（$S^{2n}$ の概複素構造は $n=1,3$ のみ）、$S^6$ の積分可能性が未解決であること、Atiyah--Hitchin--Singer / Salamon の記述（4次元の適合な概複素構造と $S^2$ 束）。
- Koszul--Malgrange（Arch. Math. 9 (1958)）と Atiyah--Bott §5 の節番号、Donaldson--Kronheimer の節番号（第2章のみ記載）。Kobayashi の第1章は、書名の目次で第I章が「Connections in Vector Bundles」であることだけ確認。
- Newlander--Nirenberg の別証明の帰属（Malgrange、Nijenhuis--Woolf、Webster）。
- Grothendieck の分裂定理を第4巻で扱う旨、第13巻の「Poisson 加群」との対応、Gualtieri の博士論文の章番号。
- 文献の定理番号は一切書かれておらず、書名・章のみ。Huybrechts・Griffiths--Harris・Hartshorne・Hörmander・Wells・Voisin・Kobayashi--Nomizu の章（Hörmander Hartogs の章を含む）は記憶に基づく一般的な位置づけで、頁・定理番号は未確認。

## 4. 残る懸念

- 表紙の「査読を受けていない教材」の注記は、独立査読後も著者側で更新が必要（私は変更していない）。
- Dolbeault--Grothendieck の証明は「方針」で、積分記号下の微分と切り捨て関数の扱いを省いている（標準的で本文でもそう明示）。
- 注意 4.8 の Hartogs は筋のみ（Hörmander の標準的な証明）。例 5.7 の逆はこの注意に依存するため、注意 4.8 が方針であることを承知しておく必要がある。
- $c_1$ に関する記述は微分形式の水準では検算済みだが、$c_1$ が整数類であること（第6巻）には本巻では触れていない（$\mathbb{CP}^1$ の $\int c_1=k$ のみ確認）。
- 記号 $K$（Gauss 曲率、標準束、添字集合）と $H$（超平面類、Hermite 行列）は節ごとの再利用が残る。同一の例内では解消したが、巻全体の統一は未実施。
