# 第3巻「層とコホモロジー」独立査読報告（2026-11-22）

対象: `parts/p0.tex`〜`p7.tex`（`build.sh vol03` で `vol03.tex` に連結してビルド。`vol03.tex` は parts の連結と同一であることを確認）。編集は parts に対して行い、再ビルド（xelatex 2 回、46 ページ、未定義参照・欠字なし）。修正前の PDF は `vol03_before_review.pdf`。
独立検算コード: `verify_review.py` / `verify_review.log`（執筆者の `verify.py` とは別実装）。

## 1. 発見した誤りと修正

| # | 箇所 | 旧 → 新 | 理由 |
|---|---|---|---|
| 1 | §8.3「統合論文との接点」、問題文、§10 Q10、§11.4 対応表、要点 | HH は「複体 $(\Lambda^\bullet T\otimes L,\ \bar\partial$ または $d_\sigma)$ の超コホモロジー」→ 複体 $(\Lambda^\bullet T\otimes L,\ d_E)$、$d_E=[\sigma,\cdot]+V\wedge$（Poisson 加群の Chevalley–Eilenberg 複体）の超コホモロジー。$\bar\partial$ は複体の微分ではなく Dolbeault 分解の方向 | 統合論文 v1 の定義 5・命題 6(b) による。論文では $d_L=\bar\partial+(-1)^a d_A$ が全複体の微分で、層の複体の微分は $d_E$ |
| 2 | 例 8.10（$\CP^1$、$\sigma=0$）と、HH の表を作る問（HHP1）の問題文と解答 | 「$\sigma=0$ なので $d_\sigma=0$」→ $\sigma=0$ かつ加群構造が自明（$V=0$）のとき $d_E=0$。$V\in H^0(T_X)\neq0$ なら $d_E=V\wedge$ は零でなく表は変わる、と明記 | $\sigma=0$ でも $V$ は任意（$\CP^1$ なら $H^0(\mathcal O(2))$）。論文の注意 15（$\sigma=0$＝複素構造）は $V=0$ の場合 |
| 3 | 定義 6.11（$c_1$）の符号注記【要確認】 | 「$c_1(\mathcal O(1))$ が正になるよう選ぶ。厳密な一致は第6巻」→ 連結準同型は「持ち上げて $\delta$」で定義し、備考 6.12 で Čech–de Rham の計算（Bott–Tu $D=\delta+(-1)^p d$）により、本巻の規約（$e_j=g_{ij}e_i$、$(\delta h)_{ij}=h_j-h_i$）では $c_1[g]=[\tfrac{i}{2\pi}\Theta]$ と一致することを示した。$\mathcal O(k)$ で $\int c_1=k$、第1巻の「$e_0=ge_1\Rightarrow\int c_1=-\mathrm{wind}(g)$」（第1巻の $g$ は本巻の $g_{01}^{-1}$）とも整合 | 符号を「選ぶ」のではなく規約から決まる。規約依存であることも明記 |
| 4 | 例 6.15（楕円曲線の平坦直線束） | 「$E$ は 1 次元なので曲率は常に 0」→「正則 1 形式は閉なので $d\omega=0$、曲率は変わらない。一般の接続の曲率は 2 形式で 0 とは限らない」 | 元の理由は誤り（結論の $\nabla+\omega$ が平坦は正しい） |
| 5 | 例 6.14（楕円曲線の $\mathrm{Pic}$）と例 6.15 の【要確認】、問 PicTorus の解答 | $H^1(E,\mathbb C)\to H^1(E,\mathcal O)$ が Hodge 分解の射影であることの証明を追加：de Rham 分解から Dolbeault 分解への複体の射 $\alpha\mapsto\alpha^{0,\bullet}$（$(d\alpha)^{0,k+1}=\bar\partial\alpha^{0,k}$）、核が $H^{1,0}$、$\mathbb R$-線形同型の理由。例 6.15 の見出しを【証明あり】に変更（例 6.14 にも同じ証明を追加） | 標準的で本文中の議論で完結する |
| 6 | 図 例 3.3（$S^1$ の 2 枚の弧） | 弧 $U_1$ を $200^\circ\to380^\circ$ から $200^\circ\to400^\circ$ に、ラベル $B$ を $10^\circ$ から $30^\circ$ に | 旧図では $U_0$ の始点 $20^\circ$ と $U_1$ の終点 $20^\circ$ が接するだけで、交わり $B$ が存在しない（本文 $U_0\cap U_1=A\sqcup B$ と矛盾） |
| 7 | 例 6.7（Čech 類から Dolbeault 類）$s_1=\rho_0 c$ の延長 | 「$U_1$ の $z=0$ の近傍へ 0 で延ばす」→「$U_1=\mathbb{CP}^1\setminus\{0\}$ なので $z=\infty$ の近傍へ 0 で延ばす」。$s_0$ の延長も明記 | $z=0\notin U_1$。誤った点を延長先に挙げていた |
| 8 | Leray の定理（定理 6.2）の証明の式 | $\check H^p(\mathcal U)\xleftarrow{\cong}H^p(\mathrm{Tot}K)$ → $\xrightarrow{\cong}$（右側の写像は $\xleftarrow{\cong}$）。一般の被覆の主張も合わせて修正 | 写像の向きが逆。列が完全なら $C^\bullet(\mathcal U,\mathcal F)\to\mathrm{Tot}K$ が擬同型 |
| 9 | 系 7.10(b)（Leray スペクトル系列の帰結） | 「$p+q<m$ で $H^p(Y,f_*\mathcal F)\to H^p(X,\mathcal F)$ が同型」→「$p<m$ で同型、$p=m$ で単射」 | 写像は $H^p$ 間なので条件は $p$ のみ（$R^qf_*=0$、$0<q<m$） |
| 10 | 命題 6.13(c) の証明 | 式の途中の「$\cdots$、正確には」を削除し $g h_1/h_0=z^m$ のみを残す | 書きかけの式が残っていた |
| 11 | 問 17 の問題文（flasque） | 「軟弱でも非輪状でもよい層の例」→「軟弱ではないが非輪状な層の例」、(d) の $H^k(\mathbb C,\mathcal O)=0$ を追加 | 解答側（「非輪状だが軟弱でない例が (a)(b)(d)」）と問題文が食い違い、日本語としても意味不明 |
| 12 | 出典 | (i) Hartshorne 細分「補題 Čech の細分」→ 第III章 演習 4.4(a)(b)。$H^1$ の一致 → 演習 4.4(c)（WebFetch で内容確認）。(ii) $\mathbb{CP}^n$ の $\mathcal O(k)$ の Griffiths–Harris 第0章 §5 を削除（0.5 はベクトル束・Chern 類の節で、記憶に基づく誤引用の疑い）。(iii) 「Hartshorne は導来圏の言葉（第III章の演習）」（超コホモロジー）を削除。(iv) fine 層の「Hartshorne 参照」→ Bredon 第II章（節は【要確認】）、Hartshorne 本文には fine 層がない旨。(v) Stein 多様体の出典（Hörmander 第5章、Gunning–Rossi 第VII章）の章番号を【要確認】に。(vi) Bredon 第IV章を「スペクトル系列の応用」に（章題を確認）。(vii) 正則 Poincaré 補題などの章節を【要確認】に | 確認できない番号・節の断定を除去 |
| 13 | §11.1 第4巻への橋渡し | 「Riemann–Hurwitz は直像 $f_*$ とその完全列から」→ 分岐被覆の完全列 $0\to f^*K_Y\to K_X\to(\text{分岐点の skyscraper})\to0$ の次数比較 | 元の記述は不正確 |
| 14 | 備考 7.7（$\chi(\Lambda^\bullet T\otimes L)$） | 「統合論文の主張と同型の構造」→ 論文の定理 22 の証明（HRR、Chern 根、Gauss–Bonnet）と同じ計算、と具体化 | 論文を確認 |
| 15 | §11.4 対応表 | 論文の Serre 型消滅は横断次数 $a>0$ のみで全次数では偽（注意 15、$\mathbb{CP}^2$・$\sigma=0$・$m=0$ で $[1,8,10,0,0]$）を追記。双対性の行に論文定理 18（任意のコンパクト複素多様体・任意の $\sigma$）と加群構造 $V'=-V+2V_K$ を追記 | 論文確認 |
| 16 | 表紙の注記、末尾の「検算について」 | 指示どおり「外部の査読は受けていない教材。執筆者とは別の AI による独立検査と、可能な範囲の計算での検算は行った。…」に変更。「検算していないもの」から Hodge 分解の射影を削除し、$c_1$ の符号を確認済と追記 | 指示 |

軽微な表記: 参考文献の Hörmander の章、Bredon の章題の記述を調整。記号表に $d_E$ を追加。

## 2. 確認した項目（数学的に問題なし）

- 前層・層・茎・層化の普遍性（命題 1.5(b) の証明：$\tilde\varphi$ の定義、一意性）、核・像・余核、完全性の茎判定、$\Gamma$ の左完全性。
- Godement 分解の定義、補題（軟弱層の短完全列で $\Gamma$ が完全。Zorn の補題の議論）、基本性質 (a)–(d)（$3\times3$ のスネーク補題の議論）、非輪状分解定理、fine 層（1 の分割）の非輪状性。軟弱層は非輪状、$\Omega^p\otimes E$ の Dolbeault 分解が非輪状分解であること。
- Čech: 低次の公式、$\check H^0=\Gamma$、細分の単射性（問題 refinj のヒントを実際に計算して確認）、任意位相空間で $\check H^1(X,\mathcal F)=H^1(X,\mathcal F)$（Hartshorne III 演習 4.4(c)）、$H^2$ 以上は一般に不一致・paracompact で一致。Leray の定理の仮定（交叉で $H^q=0$、$q\ge1$）と二重複体の証明。
- $\mathrm{Pic}=\check H^1(X,\mathcal O^*)$（コサイクル・コボーダリーの向きを全て計算し直した）、$\mathcal O(k)$ のコサイクル $g_{01}=z^k$、$K\cong\mathcal O(-2)$（$-z^{-2}$ と $z^{-2}$ は定数 $-1$ で同値）、$\mathcal O(k)\not\cong\mathcal O(l)$（巻き数）。第2巻の $\mathcal O(k)$ の規約（$f_1=z^{-k}f_0$）、第1巻の貼り合わせ関数の向きとの関係。
- 指数完全列（茎での完全性）、長完全列、$H^1(\mathcal O)=0,H^2(\mathbb Z)=0\Rightarrow\mathrm{Pic}=0$、コンパクト連結で $H^1(\mathbb Z)\hookrightarrow H^1(\mathcal O)$、$\mathrm{Pic}(\mathbb{CP}^1)=\mathbb Z$、平坦直線束との可換図式。
- de Rham 定理・Dolbeault 定理の証明（局所補題＋1 の分割）。第2巻の Dolbeault–Grothendieck の補題の述べ方（多重円板 $\Delta'\Subset\Delta$）と整合。
- $\mathbb{CP}^1$ の $\mathcal O(k)$ の $h^0,h^1$ と基底、Euler 完全列の整合、留数 $H^1(\Omega^1)\cong\mathbb C$、Čech→Dolbeault の対応（$\int\beta=-2\pi i\,\mathrm{Res}$ を Stokes で再計算）、$\mathbb C^2\setminus\{0\}$ の $H^1(\mathcal O)$ が無限次元（Laurent 単項式 $z_1^{-a}z_2^{-b}$）、$\mathbb{CP}^n$ の公式。
- Cartan–Serre の仮定（コンパクト複素多様体・連接層）、$\chi$ の加法性、$\chi(\mathcal O(k))=k+1$ の 3 通り、HRR の計算 $(1-e^x)/(1-e^{-x})=-e^x$ など。
- 超コホモロジー: 定義、短完全列の長完全列、2 項の複体の長完全列（連結準同型が $\pm\varphi_*$）、$\chi$ は項だけで決まる。Hodge–de Rham スペクトル系列の主張（$E_1^{p,q}=H^q(\Omega^p)\Rightarrow H^{p+q}(X,\mathbb C)$、コンパクト Kähler で退化）。閉埋め込みの直像（$i_*$ は完全で軟弱層を保つ）。
- 統合論文: 定義 5（HH）、命題 6、定理 9(c) の $c_1(E)=-\sum r_i[D_i]$（本巻では使っていない）、定理 18（双対性）、定理 22（Euler 標数 $(-1)^n\mathrm{rk}(E)\chi(X)$）を v1 PDF のテキストで確認。
- 全 40 問の解答を独立に検算（下記）。問題文の不備は 1 件（#11）。解答の数値・論証に誤りは見つからなかった。

### 独立検算（`verify_review.py`）
- $\mathbb{CP}^n$ ($n=1,2,3$)、$k=-6,\dots,4$: 単項式ごとの単体コチェイン複体を numpy の階数で計算し、Bott の公式 $(h^0,h^n)$ と一致（問 P1dims、Pnh、定理 Pn）。
- $\mathbb{CP}^1$、$d_E=0$ の HH 表（問 HHP1）が $k=-4,\dots,2$ で解答と一致、Euler 標数 $-2$。項ごとの Serre 双対による次元一致（$k=-9,\dots,9$）。
- $\mathbb{CP}^2$: $\chi(\mathcal O)-\chi(T(k))+\chi(\mathcal O(k+3))=3$（$k=-6,\dots,6$）。$\mathbb{CP}^3$: $\sum(-1)^p\chi(\Lambda^pT(k))=-4$（K 理論で $\Lambda_t T=\Lambda_t(\mathcal O(1))^4/\Lambda_t(\mathcal O)$ から計算）。
- $S^1$ の 3 枚被覆の階数 2。他の問（$\mathbb Z/2$、$S^2$ 被覆、$\mathbb C^2\setminus0$ の窓 $7^2=49$、$6^2=36$、$\chi$ の算術）は手計算で再確認。手計算で解き直した問: 全 40 問（記号的な問は論証を追い直した）。

## 3. 確認できなかった項目（【要確認】のまま）

- Godement, Bredon, Gunning–Rossi, Hörmander（Stein・連接層の章）、Griffiths–Harris（第3章スペクトル系列・超コホモロジー、第0章の正則 Poincaré の補題、第1章 $c_1$ の節）、Voisin 第4章以外、Huybrechts の節番号。章題レベルは確認できたもの（Bredon の章題、Hartshorne 演習 4.4）以外は記憶に基づく。
- Cartan–Serre の C. R. 誌の掲載情報（237, 1953, 128–130 とあるが、eudml で確認できたのは Séminaire Cartan 6 (1953–54) の講演のみ）、Serre FAC。
- 連接層に対する $H^q=0$（$q>\dim X$）の出典（Reiffen–Siu 型の結果で、Cartan–Serre 本体ではない可能性）。
- 統合論文の命題 6 の証明は Mokri・LGSX に依存し、論文自身が【要確認】。双対性の符号（Koszul 符号）の整合も論文では手計算のみ。
- $c_1$ の符号の文献照合（Griffiths–Harris の符号規約と本巻の規約の関係）。本巻内（第1・2巻との整合）は計算で確認。

## 4. 残る懸念

- 備考 6.12 の Čech–de Rham による符号の導出は概略。Čech の $\delta$ の符号・連結準同型の符号・Čech–de Rham 同型の符号の 3 つに依存するため、別の規約の文献を読むときは注意（本文にも明記）。
- Theorem B・Cartan–Serre・Leray スペクトル系列・HRR は主張として使用（証明なし）。出典の節番号は上のとおり未確認。
- 一般化正則束・Poisson 加群の記述（$d_E$ の符号、$V$ の取り方）は論文 v1 の記号に合わせたが、第11–13巻で詳細を確認する必要がある。
- 論文は v1 の PDF で確認した。論文の本文は §2.1–2.2、§3.2、§4.1、注意 15、例 38 付近のみ読み、全体の整合は確認していない。
