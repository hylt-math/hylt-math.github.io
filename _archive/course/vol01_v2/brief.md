# 第1巻 v2（作り直し）執筆指示書 — 共通

## 読者と目的
読者は森（元博士課程学生。一般化複素幾何を学んだが多くを忘れている。数学的な成熟度は高いが、基礎を1から丁寧に学び直したい）。
この巻は学習コース「一般化幾何への道」（全18巻）の**土台**。以後の全巻（複素幾何、層、指数定理、Poisson・一般化複素幾何、ゲージ理論、Floer 理論）が依存する。
目標：**この1冊を読めば、多様体・微分形式・ベクトル束・接続・主束・Chern–Weil を自分の言葉で説明でき、計算でき、後の巻で詰まらない。** 教科書として「完璧」であること。

## 品質基準（最重要）
1. **動機→定義→例→定理→証明→例の計算→要点**の順。定義の前に「なぜこの概念が要るか」を1段落。抽象の前に必ず具体例（座標、$S^1,S^2,T^2,\R^3,\CP^1$ 等）。
2. 定理は、証明が短い（〜半ページ）ものは**完全に証明**する。長いものは「証明の骨格＋どこが難しいか＋出典（書名と章）」。標準的な結果は【文献】、本文で証明したものは【証明あり】、記憶に基づく出典・細部は【要確認】のタグ（\tC \tP \tQ）。**定理番号を捏造しない。確信がなければ「第X章」までにする。**
3. 計算は途中式を省略しない。符号・係数・規約（$\dd$ の規約、$\iota$、$\wedge$ の規約、曲率の符号、Chern 形式の $\frac{i}{2\pi}$）は冒頭で固定し、本文で一貫させる。規約を他書と比べて違う点には注意書き。
4. 図：tikz で**1節あたり少なくとも1〜2枚**（座標近傍の貼り合わせ、接ベクトル、流れ、Lie 括弧の閉じない四角形、Möbius 帯、遷移関数、平行移動、ホロノミー、Hopf、球面上の平行移動など）。図は PDF に描画して**重なり・はみ出しがないか目視確認**。
5. 各節の末尾：①「要点」（keybox）②「つまずきやすい点」③ 問題（**[基本][標準][発展]**）。問題はこの巻全体で**70〜90問**。難問にはヒント（\hint{...}）。**全問に完全な解答**（途中式つき、答えだけは不可）。
6. 後の巻・統合論文との接点を、該当箇所に短い注として書く（例：$V\oplus V^*$ の内積 → Courant 代数・一般化複素幾何；Frobenius → 分布・Dirac 構造・Poisson 葉；平坦接続・ホロノミー → 統合論文の対数接続と留数；接続・曲率・ゲージ変換 → Yang–Mills；Chern–Weil → HRR・指数定理；Hodge 星・Laplacian → 第5・7巻）。大げさな主張は避ける。
7. 長さの目安：自分の担当部分で 25〜35 ページ（11pt、a4、既存の pre_course.tex）。薄くせず、かつ冗長にしない。
8. 日本語。である調。専門用語は初出で（英語）を併記。

## 環境・体裁
- 作業ディレクトリ: /tmp/claude-0/-home-claude/3764233b-ffbe-5ebe-8574-810b73d47330/scratchpad/course/vol01v2/
- プリアンブル: `pre_vol01.tex`（pre_course.tex を読み込み、tikz/tikz-cd、マクロ \dd \Lie \tr \GL \U \SO \SU \X \Gam \pa \Ad \RP \CP \Ker \Ran \rank、環境 defn thm prop lem cor ex rem（section ごとの通し番号）、goalbox keybox、`probl{レベル}{キー}`・`soll{キー}`、\hint）。**必要なマクロを増やす場合は担当ファイルの冒頭で \providecommand を使い、他の担当と衝突させない。**
- 各担当は `partX.tex`（本文＋問題）と `solX.tex`（その部分の全問の解答）を作る。`\begin{document}` は書かない。節の番号は通し：全10節（下記）。partA は先頭で `\setcounter{section}{0}`、partB は `\setcounter{section}{3}`、partC は `\setcounter{section}{6}`。
- 問題は `\begin{probl}{基本}{キー}問題文\end{probl}`、解答は `\begin{soll}{キー}解答\end{soll}`（キーは担当ごとに接頭辞 A_ B_ C_ を付ける。例 A_chart1）。解答の節に出る番号は自動で一致する。
- ラベルも接頭辞（\label{A:...} 等）。他の担当の節への言及は「§5」のように節番号で書くか、\S\ref は使わない（未定義になるため）。
- ビルド確認用に `build_X.sh` を作る：`main_skeleton.tex` を元に自分の part/sol だけを入れた一時ファイル（例 tmpA.tex）を作り xelatex を2回。**エラー・Overfull hbox・未定義参照を0にする**。Underfull は許容。
- PDF を `pdftoppm -r 55 -png` で画像にして、図のあるページ・数式の多いページを目視確認（Read で画像を読む）。
- 検算：本文・解答に非自明な計算（外微分、括弧、曲率、Chern 形式、積分、行列式など）があれば、`check_X.py`（fractions / numpy のみ。sympy・ネットワーク・pip は使えない）で独立に検算し、出力を `check_X.out` に残す。既存の旧版の検算コード（有理係数多項式の微分形式の演算）は /home/claude/hylt-math.github.io/_archive/course/vol01/check*.py にあり、流用してよい。
- 旧版（v1）の本文 /home/claude/hylt-math.github.io/_archive/course/vol01/part*.tex は、良い部分を流用・拡張してよい（v1 は圧縮されすぎていた。v2 は教科書として**ゆっくり詳しく**）。旧版の誤り訂正（review.md）も参照。
- git の commit/push、_posts、assets には触らない。他の担当のファイルは読んでよいが書き換えない。
- 5時間の API 利用制限に当たったら、そこで止まって進捗を報告してよい。

## 規約（全担当共通。冒頭 §1 に載せる）
- 多様体は滑らか（$C^\infty$）、Hausdorff、第2可算。次元 $n$、座標 $(x^1,\dots,x^n)$、Einstein の和の規約。
- $[X,Y]f=X(Yf)-Y(Xf)$。$\dd(\alpha\wedge\beta)=\dd\alpha\wedge\beta+(-1)^k\alpha\wedge\dd\beta$。$\dd\alpha(X,Y)=X\alpha(Y)-Y\alpha(X)-\alpha([X,Y])$（$\dd x\wedge\dd y(\partial_x,\partial_y)=1$）。
- $(\alpha\wedge\beta)$ は「行列式」規約（$\dd x^1\wedge\dd x^2(\partial_1,\partial_2)=1$）。
- $\iota_X$、$\Lie_X=\dd\iota_X+\iota_X\dd$。
- 接続：$\nabla=\dd+A$（局所枠で）、曲率 $F=\dd A+A\wedge A$、ゲージ変換 $A\mapsto g^{-1}Ag+g^{-1}\dd g$（枠の変換 $e'=eg$ のとき）。
- Chern 形式：$c(F)=\det(I+\frac{i}{2\pi}F)$。$c_1(L)=\frac{i}{2\pi}F$。$\CP^1$ 上の $\mathcal O(-1)$（tautological 束）で $\int c_1=-1$。$TS^2=T\CP^1$ で $\int c_1=2$（Gauss–Bonnet と整合）。
- Hermite 計量は第1成分で線形（$h(\lambda u,v)=\lambda h(u,v)$）。

## 全体の節構成（全10節。担当の割り当て）
### 担当 A：§1〜§3
**§1 道具の復習（線形代数・解析・位相）**：双対空間、テンソル積、外積代数 $\Lambda^kV^*$（基底・次元・外積の結合律・行列式との関係）、内積による $V\cong V^*$、**$V\oplus V^*$ の自然な双線形形式 $\langle v+\xi,w+\eta\rangle=\frac12(\xi(w)+\eta(v))$ と符号 $(n,n)$**（一般化幾何への伏線）、複素構造 $J$ と $V\otimes\C=V^{1,0}\oplus V^{0,1}$（第2巻の伏線）、逆関数定理・陰関数定理、常微分方程式の存在・一意性・滑らかな依存、位相の最小限（Hausdorff、第2可算、コンパクト、連結）。**規約表**。読み方の地図。
**§2 多様体**：動機（曲面・配置空間・群）、位相多様体、アトラスと滑らかな構造、座標変換、例（$\R^n$、開集合、$S^n$ の2枚の座標、$T^n$、$\RP^n$、$\CP^n$ の座標、直積、$\GL(n,\R)$、$\SO(n)$ が多様体であること＝正則値定理、Grassmannian は例として軽く）、滑らかな写像・微分同相、**正則値定理（証明つき）と部分多様体**、はめ込み・埋め込み、はめ込みと埋め込みの違いの例、**1の分割（存在の証明）**、境界つき多様体、向き（定義・例・Möbius 帯・$\RP^2$）、コンパクト多様体の分類の言及（曲面）。
**§3 接空間・ベクトル場・Lie 括弧・Frobenius**：接ベクトルの3つの定義（導分／曲線の同値類／座標成分）とその同値、座標変換則、微分 $\dd F$ と連鎖律、接束 $TM$（それが多様体であること）、余接束、ベクトル場、流れ（ODE から）と完備性、**Lie 括弧**（定義・成分式・性質・Jacobi・流れによる定義 $[X,Y]=\frac{\dd}{\dd t}\phi_{-t*}Y$ の同値と証明）、可換な場は座標、押し出し・関連付け、**Lie 群と左不変ベクトル場・Lie 代数**（$\mathfrak{so}(3)$、$\mathfrak{gl}(n)$ の括弧＝行列の交換子の証明）、**分布と Frobenius の定理（証明つき）**、葉層（例：Kronecker 流、Reeb 風）、非可積分な例（接触構造 $\dd z-y\,\dd x$）。

### 担当 B：§4〜§6
**§4 微分形式・外微分・Cartan の公式・積分**：テンソル場、$k$ 形式（座標・$\R^3$ での対応表）、外積、引き戻し、**外微分（公理による特徴づけ、存在・一意性、座標独立性の証明）**、$\dd^2=0$、内部積、**Lie 微分と Cartan の公式（証明）**、不変公式、$\R^3$ のベクトル解析との対応（grad・curl・div）、**向きと積分、Stokes の定理（証明つき：1の分割＋半空間）**、Green・Gauss・古典 Stokes は系、完全形式・閉形式の例（$\dd\theta$ on $S^1$）、余接束の標準 1 形式とシンプレクティック形式（軽く、Darboux は主張のみ）、体積形式。
**§5 de Rham コホモロジー**：定義、最初の例（$\R$、$S^1$、$\R^2\setminus0$）、**Poincaré の補題（ホモトピー作用素の公式で証明）**、ホモトピー不変性、**Mayer–Vietoris（証明つき）**、計算：$S^n$、$T^n$、$\R^n\setminus\{0\}$、種数 $g$ 曲面（主張）、写像度とその $\int$ による定義、コンパクト台コホモロジー、**Poincaré 双対（主張・系：Euler 標数・$\dim$ の対称性）**、Künneth（主張）、Euler 標数、連結和（主張）、Čech–de Rham の予告（第3巻の層コホモロジーとの関係）。
**§6 Riemann 計量・Hodge 星・Laplacian**：計量、長さ・体積、Hodge 星（定義・性質・$\R^3$、$\R^4$ での表）、$\delta=\pm\ast\dd\ast$ と随伴性（証明）、Hodge Laplacian、調和形式、**Hodge の定理（コンパクト多様体：主張と出典）、トーラス上では Fourier 級数で完全に証明**、Hodge 分解、Poincaré 双対との関係、共形不変性（$\R^4$ の2形式の自己双対・反自己双対分解＝ゲージ理論への伏線）、Levi-Civita 接続は §8 へ予告。

### 担当 C：§7〜§10
**§7 ベクトル束**：動機、定義（局所自明化・遷移関数・コサイクル条件）、例（自明束、Möbius 束、$TS^2$、tautological 束 $\mathcal O(-1)$ on $\RP^n,\CP^n$、Hopf 束）、貼り合わせでベクトル束を作る定理（証明）、切断・枠・準同型・同型、構成（$\oplus,\otimes,\Hom,{}^*,\Lambda^k$、引き戻し）とその遷移関数、部分束・商束・完全列、ファイバー計量と Hermite 計量（存在：1の分割）、完全列が分裂すること（計量から）、直線束の群 $\mathrm{Pic}$ と $H^1(M,\underline{\C^*})$ 的な見方の予告、構造群の簡約、分類（$[M,BG]$）の主張のみ、自明かどうかの判定（大域枠）、$TM$ の自明性（$S^1,S^3,S^7$、$S^2$ は毛玉定理）の言及。
**§8 接続と曲率**：共変微分の定義（Leibniz）、局所表示 $\nabla=\dd+A$、ゲージ変換則、接続の存在（1の分割）、接続全体はアフィン空間、**平行移動（ODE）とホロノミー**、共変外微分 $\dd_\nabla$ と**曲率 $F=\dd_\nabla^2=\dd A+A\wedge A$（証明）**、**Bianchi 恒等式**、曲率は $\Om^2(\End E)$ の元（テンソル性の証明）、誘導接続（双対・テンソル積・$\End$・$\det$）、計量接続・Hermite 接続（$A$ が $\mathfrak u(n)$ 値）、**Levi-Civita 接続（存在・一意性）と Riemann 曲率**、$S^2$ の曲率の計算、**平坦接続・ホロノミー表現・局所定数係数**（$\pi_1\to\GL$）、例：$S^1$ 上の接続のホロノミー、トーラス上の Aharonov–Bohm、曲率の幾何的意味（共変微分の非可換性、平行移動で閉じない四角形）。
**§9 主束とゲージ変換（入口）**：Lie 群、主 $G$ 束（遷移関数、局所自明化）、例（枠束、Hopf: $S^3\to S^2$、$U(1)$ 束）、同伴ベクトル束、接続1形式 $\omega$（垂直射影・右作用で共変）、局所切断による引き戻し $A=s^*\omega$、曲率 $\Omega=\dd\omega+\frac12[\omega,\omega]$、ゲージ群・ゲージ変換、ベクトル束の接続との対応（主張）、第15巻（Yang–Mills）への橋渡し。長さは他の節より短くてよいが、定義と例は丁寧に。
**§10 Chern–Weil 理論の入口**：不変多項式、Chern 形式 $c_k(F)$、**閉性と接続によらないこと（超越公式 / 1パラメータ族による証明）**、Chern 数・整数性の例（$S^2$ 上の直線束、Hopf 束で $\int c_1=\mp1$、**符号を規約から確定**）、$T S^2$ の $c_1$ と Gauss–Bonnet、Whitney 和（形式レベルで $c(E\oplus F)=c(E)c(F)$ in cohomology）、Chern 指標・Todd 類・Pontryagin 類・Euler 類の予告（第6巻）、何が接続によらず何が依存するか、Chern–Simons の予告、$\R^3$ 上での $\mathfrak{u}(1)$ ゲージ（電磁気学）の読み替え。
（担当 C はさらに：参考文献節の自担当分、各節末の問題、解答。）

## 担当しない（統合担当が書く）
表紙・学習目標・目次・自己診断・橋渡し・全体の参考文献・記号表・索引的な記号表。

## 参考文献（出典は書名と章までを基本）
Lee『Introduction to Smooth Manifolds』(2nd)、Lee『Riemannian Manifolds』、Bott–Tu『Differential Forms in Algebraic Topology』、Warner『Foundations of Differentiable Manifolds and Lie Groups』、Spivak『Calculus on Manifolds』『Comprehensive Introduction to Differential Geometry』、Milnor–Stasheff『Characteristic Classes』、Kobayashi–Nomizu『Foundations of Differential Geometry』、Nakahara『Geometry, Topology and Physics』、Madsen–Tornehave『From Calculus to Cohomology』、Tu『Differential Geometry』、Morita『Geometry of Differential Forms』、Hatcher（位相）。章番号に確信がなければ【要確認】。WebSearch/WebFetch で確認できるものは確認してよい。

## 最後に
完成したら、(1) ファイル一覧、(2) 節ごとの量（ページ・問題数・図の数）、(3) 【要確認】にした箇所、(4) 検算した項目と検算していない項目、(5) 自信のない箇所、を簡潔に報告する。
