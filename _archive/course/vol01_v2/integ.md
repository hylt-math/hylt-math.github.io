# 第1巻 v2 統合ノート（integ.md）

作業: 2026-11-28。ビルド: `./build.sh` → `vol01.tex`（\input 展開済み 1 本）→ `vol01.pdf`。補助: `check_integ.py`（問題と解答の機械的照合）、`mkspreads.sh`（見開き画像）。

## 規模
- 全 142 ページ（表紙 1、学習目標 1、前提と読み方 1、目次 2、§1〜§3 p6–39、§4〜§6 p40–76、§7〜§10 p77–112、問題の解答 p113–131、自己診断 p132–133、橋渡し p134–136、参考文献 p137–139、記号表 p140–141）。
- 図（tikz）39 枚、問題 88 問（基本 18、標準 53、発展 17）、解答 88（番号・順序一致、check_integ.out）。
- 節ごとの問題数: §1:8 §2:11 §3:10 §4:11 §5:12 §6:9 §7:6 §8:10 §9:3 §10:8。

## 統合時に見つけて直したこと
1. **partB.tex の問題の位置の誤り**: build_B.sh が `ls` で断片を並べるため、§5・§6 の問題（p5, p6）が §5・§6 本文の前（§4 の直後）に入っていた。B_src から正しい順（s4a-d, p4, s5a-c, p5, s6a-c, p6）で partB.tex を作り直し、以後 partB.tex を正本とした（B_src は参照のみ。build_B.sh は廃止）。
2. **問題数 103 → 88**（目標 70〜90）。未参照・重複の問題 15 問を part/sol の両方から削除: A_wedge1, A_axb, A_two, A_liederiv, A_top, A_related, B_line, B_star3, B_fixed, C_holS1, C_pgauge, C_constr, C_trivial, C_herm, C_pullback。解答側に残っていた削除問への参照（solC の `pr:C_trivial` 2 か所）は文言に置換。
3. **相互参照の誤り**: partA の「§§7--9 で学ぶ接束」→「§3 で学ぶ」。partC §7.6 の「Γ が分布（§3）」→「D が分布（§3.9）」（記号の取り違えも修正）。
4. **後の巻の指示の誤り**（シラバスと照合）: partC の「Floer 理論（第16〜18巻）」→「Donaldson 理論・Seiberg–Witten 理論（第16・17巻）」（3 か所）、「指数定理の局所公式（第8〜9巻、HRR）」→「第8巻、族は第9巻、HRR は第6巻」。
5. **出典の誤り**: partB「Bott–Tu 第II章 §14」（de Rham の定理）は §14 が第III章（スペクトル系列）なので誤り → 「第II章（§8 以降）」＋【要確認】。Cartan の公式の出典から「Bott–Tu 第I章 §4」を削除（§4 は Poincaré の補題）。Hatcher の節番号に【要確認】を付加。Bott–Tu と Lee の章構成は目次で確認した。
6. **「本巻の内部資料」への言及の除去**: partC/solC 中の `check_C.py` への言及（読者は持っていない）を「計算機でも確認した」に置換。
7. **規約表の文言**: partA §1.1 の「$A$ を $\mathfrak u(n)$ 値の実形式として…本書の標準」を、歪 Hermite 行列値の 1 形式、物理では Hermite 行列値で $\nabla=d-iA$、と明確化。
8. **図**: partA の 8 の字（例 2.24）で $t\to\pm\pi$ の矢印ラベルが曲線・原点ラベルと重なっていたのを修正。
9. **節の冒頭**: partC §7〜§10 に（partA/B にあった）goalbox「この節のねらい」を追加。
10. **解答側**: solB に節見出し（§4〜§6 の解答）を追加。
11. **重複**: 毛玉定理は §5.4（写像度で偶数次元球面）と §10.4（$c_1$ で $S^2$）に別証があり、片方に寄せず相互参照を付けた。$\R^3$ のベクトル解析は §4.5（$\dd$ による grad/curl/div）と §6.2（$\star$ による表現）で役割が違い、Hodge 星の表は §6 のみ（§4 は形式の対応表のみ）で、実質的な重複はない。

## 記号・規約・符号の点検結果（矛盾は見つからなかったもの）
全 part・sol を grep で通し確認:
- $[X,Y]f=X(Yf)-Y(Xf)$、$\dd\alpha(X,Y)=X\alpha(Y)-Y\alpha(X)-\alpha([X,Y])$（§3, §4, §8 の $R(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$）: 一致。
- $\iota_X$（第1引数）、$\Lie_X=\dd\iota_X+\iota_X\dd$: §1, §4, §9 で一致。
- $\nabla=\dd+A$、$F=\dd A+A\wedge A$、$e'=eg\Rightarrow A'=g^{-1}Ag+g^{-1}\dd g$、$F'=g^{-1}Fg$: §8（受動的）、§9（能動的・主束 $s_\beta=s_\alpha g$）、§10 で一致。§7 の貼り合わせ関数も $e_\beta=e_\alpha g_{\alpha\beta}$、$\sigma_\alpha=g_{\alpha\beta}\sigma_\beta$、$g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}$ で §8–§10 と一致。
- Chern 形式 $c=\det(I+\frac i{2\pi}F)$: §1 表、§10 で一致。$\int_{\CP^1}c_1(\mathcal O(-1))=-1$（Hopf 接続 $A_0$ から $-\frac1\pi\int\frac{dxdy}{(1+r^2)^2}=-1$ を手で再確認）、$L_k$ で $-k$、$T\CP^1=\mathcal O(2)$ で $+2$（$\mathrm{wind}(-z^{-2})=-2$）: 一致。
- Hermite 計量は第1成分で線形: §1.5（$h(Ju,v)=ih(u,v)$）、§7.6、§8.8、§10 で一致。
- $\omega=\dd\lambda$（§4.9、Hamilton $\iota_{X_H}\omega=-\dd H$）と §9 の接続 1 形式 $\omega$ は同じ記号の別用法。記号表に注記。
- Euler 標数・Betti 数・$H^k_{\rm dR}$ の記号は B のみ、C は $\Om^k(M;E)$ で統一。

## 検算
- check_A.out / check_B.out / check_C.out（各担当の検算。全 PASS/OK）は担当ファイルのまま。統合で削除した問題の検算は残るが、本文・他の問題には影響しない。
- 統合担当の追加検算: check_integ.py（問題数・解答数・キー順・番号連続・未定義 `pr:` 参照 0）。$\int c_1(\mathcal O(-1))=-1$ は手計算で再確認。自己診断 Q3, Q8, Q12 の値は本文の例（§4.4, §6.6/例 6.7, §8.4）と照合した。

## 残る懸念
- 本文全体を通読して証明の正否を再検査してはいない（担当 3 名の検算と、grep による規約の通し点検、全ページの目視によるレイアウト確認のみ）。独立査読は別途。
- 【要確認】の出典（Warner・Kobayashi–Nomizu・Milnor–Stasheff・Husemoller・Hirzebruch・Petersen・Lee Riemannian Manifolds の章節）は未確認のまま。Lee ISM と Bott–Tu の章構成のみ目次で確認。
- hyperref の PDF しおり: 節題に数式があるため「Token not allowed in a PDF string」の警告が 23 件（表示には影響せず、しおりの数式部分が欠ける）。
- 基本問題が 18 問と少なめ（削除した 15 問のうち 9 が基本）。
- 橋渡しの対応表は読み方の目安。統合論文の定理番号は状態表に載っているものだけを引いた。符号（統合論文 定理 9(c) の $c_1=-\sum r_i[D_i]$）の照合は第13巻に先送りし【要確認】とした。
- 日本語の強調（\emph）はイタリック体が無いため立体のまま（見た目の区別がない）。
