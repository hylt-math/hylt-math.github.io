# 学習コース「一般化幾何への道」シラバス（Claude 用、2026-11-22 作成）

読者は森（元博士課程学生、一般化複素幾何を学んだが忘れている。複素幾何の基礎は部分的に覚えている）。目標は統合論文
（_posts/2026-11-22-generalized-geometry-poisson-unified.md、PDF: assets/pdf/generalized-geometry-poisson-unified-v1-ja.pdf）を
1から理解し、指数定理（Atiyah–Singer、族、APS）まで到達すること。各巻は日本語 PDF（教科書＋問題集＋全問の解答）。

## 巻一覧（依存順）
| 巻 | 題 | 前提 | 主な内容 | 主な出典 |
|---|---|---|---|---|
| 1 | 多様体・ベクトル束・接続・微分形式 | 微積分、線形代数 | 多様体、接束、微分形式、de Rham、ベクトル束、接続・曲率、Chern–Weil の入口 | Lee; Bott–Tu; Milnor–Stasheff; Kobayashi–Nomizu |
| 2 | 複素多様体と Dolbeault 理論 | 1 | 概複素構造、Newlander–Nirenberg（主張）、(p,q) 分解、∂̄、正則ベクトル束、Hermite 計量・Chern 接続、Kähler | Huybrechts; Griffiths–Harris; Wells; Voisin |
| 3 | 層とコホモロジー | 2 | 前層・層、Čech コホモロジー、層コホモロジー（細分解/導来）、Dolbeault 定理、de Rham 定理、完全列、スペクトル系列の入口 | Hartshorne III; Griffiths–Harris 0.3; Voisin I; Bredon; Godement |
| 4 | Riemann 面と Riemann–Roch（曲線版） | 2,3 | 因子、直線束、Riemann–Roch、Serre 双対、Riemann–Hurwitz、種数、曲線の埋め込み、Jacobi 多様体の入口 | Forster; Miranda; Griffiths–Harris 2; Hartshorne IV |
| 5 | Hodge 理論と Kodaira 型定理 | 2,3,4 | Hodge の定理、Kähler 恒等式、Lefschetz、Serre 消滅・双対、Kodaira（Nakano）消滅、Kodaira 埋め込み、小平–Spencer | Huybrechts; Voisin I; Griffiths–Harris 0.6-1; Demailly |
| 6 | 特性類と Hirzebruch–Riemann–Roch | 1,2,3 | Chern 類、Chern 指標、Todd 類、splitting principle、HRR の主張と応用（曲面の Noether の公式、Riemann–Roch for surfaces） | Milnor–Stasheff; Hirzebruch; Griffiths–Harris 3; Huybrechts 5 |
| 7 | 楕円作用素と Fredholm 指数 | 1,2 | 微分作用素・シンボル、楕円性、Sobolev、楕円正則性、Fredholm、指数の不変性、Hodge/Dolbeault は楕円複体 | Lawson–Michelsohn III; Wells IV; Roe; Warner |
| 8 | Atiyah–Singer の指数定理 | 6,7 | Clifford 代数・スピン・Dirac 作用素、K 理論の入口、指数公式の主張、Dolbeault→HRR、符号定理、熱核による証明の概略 | Atiyah–Singer I,III; Lawson–Michelsohn; Berline–Getzler–Vergne; Roe |
| 9 | 族の指数定理 | 8 | 族と指数束（K 理論の元）、Atiyah–Singer IV、Bismut 超接続・Chern 指標、Gauss–Manin、Grothendieck–Riemann–Roch との関係 | Atiyah–Singer IV; BGV; Bismut; Lawson–Michelsohn |
| 10 | 境界つき多様体と APS・b-計算 | 8 | APS の境界条件と eta 不変量、APS 指数定理、b-計算（Melrose）、Lie 構造つき無限遠、Lie 亜群の指数への概観 | APS I–III; Melrose; Grieser; Ammann–Lauter–Nistor; Qiao–So; Braverman–Loizides–Song |
| 11 | Lie 亜代数と Poisson 幾何 | 1,2 | Lie 亜代数、Poisson 多様体、シンプレクティック葉、正則 Poisson、Poisson 加群、対数シンプレクティック | Mackenzie; Crainic–Fernandes; Dufour–Zung; Laurent-Gengoux–Pichereau–Vanhaecke |
| 12 | 一般化複素幾何 | 1,2,11 | T⊕T*、Courant 括弧、Dirac 構造、一般化複素構造、型、β 変換、Darboux、一般化 Dolbeault | Gualtieri（博士論文 math/0401221、Ann. 2011 math/0703298）; Hitchin math/0209099; Cavalcanti |
| 13 | 一般化正則束と Poisson 加群 | 3,11,12 | 一般化正則束、Poisson 加群、超コホモロジーによる一般化 Dolbeault、論文での設定 | Gualtieri 0710.2719; Laurent-Gengoux–Stiénon–Xu 0707.4253 |
| 14 | 統合論文への案内 | 全部 | 統合論文の各定理を、必要な巻と例で読み解く。残る問題の整理 | 統合論文 |

## 各巻の構成（必須）
1. 表紙：題、巻番号、日付、「執筆：Claude／企画：森」。2. 学習目標（goalbox）と前提。3. 目次。4. 本文：定義・定理・例。主要な定理には証明を付けるか、証明の方針と出典を明示。各節に「要点」（keybox）。5. 各節末に問題（prob 環境：[基本][標準][発展]、全体で 25〜40 問）。6. 解答の節：**全問**に解答（sol 環境）。計算問題は途中式を示す。7. この巻の理解チェック（10 問ほどの自己診断、正誤または短答）。8. 次巻への橋渡しと、統合論文との対応（どの定理にこの巻が効くか）。9. 参考文献（出典は書名・章節まで。**定理番号は確信がなければ書かず「第X章」までにする**）。

## 規則
- 標準的な結果は【文献】、本文で証明したものは【証明あり】、記憶に基づく出典・細部は【要確認】。捏造しない。分からなければ WebSearch で確認し、確認できなければ【要確認】。
- 解答は必ず独立に検算する（可能な計算は Python / sympy で）。数値や符号の誤りを避ける。
- 読者が復習しやすいよう、記号表（巻末）、定義の再掲、図解（tikz-cd / tikz）を適宜使う。1 巻あたり 40〜70 ページを目安にする。
- 日本語の PDF のみ（英語版は作らない）。xelatex、_archive/course/pre_course.tex を \input する。ネットワークからの pip/npm インストールは不可。
