# 第5巻 独立査読報告

対象: vol05.tex（part0〜part11.tex を cat で連結して生成される。原稿の実体は part*.tex なので、修正は part*.tex に入れ、build.sh で vol05.tex を再生成した）。元の PDF は vol05_before_review.pdf、元の tex は vol05_before_review.tex に残してある。修正後は xelatex を 2 回通し 42 ページ（修正前 41）。未定義参照・エラーなし。

## 1. 発見した誤り・不適切な点と修正

| # | 箇所 | 旧 → 新 | 理由 |
|---|---|---|---|
| 1 | 例 K3（Hodge 指数の例） | 「$\mathrm{NS}_{\mathbb R}\subset H^{1,1}_{\mathbb R}$ には $\omega$ が入るので符号 $(1,\rho-1)$」→「$\rho\le20$。射影的なら豊富類が入るので $(1,\rho-1)$」 | 一般の（非射影的）K3 では $\mathrm{NS}_{\mathbb R}$ に Kähler 類は入らない。符号は $(1,\rho-1)$ か $(0,\rho)$ |
| 2 | 問 hodgeindex の解答 (b) | 「ある正の元（$\omega$ の有理近似…）を含む部分空間は…」→ 上と同じ修正 | 同上。$\omega$ の有理近似は $\mathrm{NS}$ に入る保証がない |
| 3 | 問 holclosed の問題文と解答 | 「$h^{p,0}$ が複素構造によらず…コホモロジー環の不変量」→「$H^0(\Omega^p)\to H^p(X,\mathbb C)$ は単射、$h^{p,0}\le b_p$」 | 元の主張は偽（部分空間 $H^{p,0}$ は複素構造に依る）。問題文として不適切 |
| 4 | 問 hirz の (b) と解答 | $h^1=a-1$ から「$F_0,F_1$ は剛的」と結論していた → $F_0$ は $h^0(T)=6$ から別に $h^1=0$ と書き足し、$h^1=a-1$ は $a\ge1$ と明記 | $h^0=a+5$ は $a\ge1$ でのみ成立。$a=0$ に公式を当てはめる誤読を防ぐ |
| 5 | 例 torusproj の $n=1$ | $E(1,\tau)=1$（$H=z\bar w/\mathrm{Im}\,\tau$）→ $E(\tau,1)=1$ | $\mathrm{Im}\,H(1,\tau)=\mathrm{Im}\bar\tau/\mathrm{Im}\tau=-1$ なので符号が逆だった |
| 6 | Kodaira 埋め込みの「一様性」の段落 | 「各 $x$ で $m(x)$、$m(x)+1$ の積 $s\cdot s'$ を使って…」の議論 → 爆発上の正値性・消滅の評価が $x,y$ について一様にとれる、という骨子に差し替え、【要確認】を付けた | 元の議論は、近傍が $m$ に依存するため論理が通らない（有限被覆で共通の $m$ が取れない） |
| 7 | 例 bochner | 「$H^0\ne0$ には曲率が少なくとも一部で正」→「$\mathrm{tr}_\omega(i\Theta)$ がどこかで正、または恒等的に $0$」 | 自明束（曲率 0）は $H^0\ne0$ で、元の言い方は反例を持つ |
| 8 | 定理 HR（Hodge–Riemann）と Weil の公式 | 【要確認】のまま「主張のみ」→ Weil の公式から符号を導く証明の骨子を追加（$\int\omega^{n-k}\alpha\bar\alpha=(n-k)!(-1)^{k(k+1)/2}i^{p-q}\|\alpha\|^2$）。係数と符号は数値確認済み（下記） | 係数の確認ができたので格上げ。Huybrechts の命題番号「3.3.17」は確認できなかったので削除 |
| 9 | 出典の番号 | Huybrechts「第3章 §3.2」（Lefschetz 分解）→ §3.3。Kodaira–Spencer の論文「Ann. 67, 68, 71」→ 67 (1958), 71 (1960)、Kodaira–Nirenberg–Spencer 68 (1958)、Kuranishi Ann. 75 (1962)。Wells の §4、Griffiths–Harris の §6・§7、Kodaira 本の「第1–3章」→ 節番号を削除し【要確認】 | Huybrechts の目次（§3.1 Kähler Identities、§3.2 Hodge Theory on Kähler Manifolds、§3.3 Lefschetz Theorems、§4.1 Hermitian Vector Bundles and Serre Duality、§5.1〜5.3、第6章）を確認。Ann. 68 は KNS の論文 |
| 10 | 定理 Serre 双対 | 出典なし → Huybrechts §4.1、Hartshorne III §7 を追加。注意 (iii)「第4巻では Mittag-Leffler 型の議論から出した」→ 第4巻は主張と、$\bar\partial_L$ の楕円性と留数による骨子を述べた、に訂正 | 第4巻の記述（thm:serre の骨子）と不整合 |
| 11 | §2 の「第4巻では有限性を Cartan–Serre（Banach 空間論）で示した」 | → 第3巻・第4巻は関数解析（Schwartz）と楕円型作用素論の 2 通りを挙げた、に訂正 | 第3巻 thm:CS、第4巻 thm:finite の記述と不整合 |
| 12 | §11 古典と統合論文の対比 | (a) 表と要点と橋渡しの「一般化正則切断による埋め込みは不可能」に、論文の仮定（$\sigma$ が稠密開集合で非退化＝命題 79、正則型で葉が正次元＝命題 81）を明記。$\sigma=0$ なら古典の Kodaira。(b) 「Serre 双対は項ごとに使う」→ $E_1$ 項の次元の整合だけがそれで、$d_E$ まで込めた定理 18 の証明は Dolbeault モデル（楕円型複体）の形式的転置（論文の証明 (0)–(4) による）。(c) Poisson 加群の定義を論文の定義 4・5 に合わせた（正則余接 Lie 亜代数上の平坦接続 $\nabla$、$\nabla_\beta e=\beta(V)e$）。(d) 命題 79 に「$X$ 連結」。(e) トーリックの定理 88 に「$\sigma$ がトーラス不変」。(f) Part VI（$m=2$ は存在、$m=3$ の非トーリックでは見つからない、予想の反証ではない）を追記し【要確認】。(g) 注意 17 は論文自身が【予想】と書いているので【要確認】を外して明記 | 論文の PDF（日本語版 v1）の定理・命題・注意 14, 15, 17, 18, 22, 79, 81, 82, 83, 88, 91 の本文と状態表を照合した。過大な主張を削った |
| 13 | 第6巻への橋渡し | 「Hirzebruch の元の証明は射影的な場合に Kodaira 型の消滅を使う【文献】」→ 削除し、第6・8巻で扱うと書いた | 出典なしで確認できない主張 |
| 14 | 例 ex:def (5)（Hirzebruch 曲面） | $h^0(T_{F_a})=a+5$ を導出付きの記述に（$0\to T_{F/\mathbb P^1}\to T_F\to\pi^*T_{\mathbb P^1}\to0$、$\pi_*T_{F/\mathbb P^1}=\mathrm{End}_0V=\mathcal O\oplus\mathcal O(a)\oplus\mathcal O(-a)$） | 【要確認】だった項目を、自分で導出して確認した（$a+5$、$h^1=a-1$） |
| 15 | 解答 holclosed の Iwasawa 多様体 | 【文献】だけ → 群の積、左移動での不変性、$d(dz_3-z_1dz_2)=-dz_1\wedge dz_2$ を明記 | 直接計算で確認した（左移動 $w\mapsto(a+w_1,b+w_2,c+w_3+aw_2)$ で $dw_3-w_1dw_2$ は不変） |
| 16 | 表紙の注記 | 依頼どおり「外部の査読は受けていない教材。執筆者とは別の AI による独立検査と、可能な範囲の計算での検算は行った。…」に変更 | 指示 |
| 17 | 目標欄 | 「一般化正則切断による埋め込みの不可能性」に仮定（$\sigma$ が稠密開集合で非退化など）を付記 | 上の 12(a) と同じ |
| 18 | 細部 | Kähler 正規座標の正規化（$\tfrac12\delta$ と $\delta$）の注記。曲面の $b_1=h^{1,0}+h^{0,1}$ の出典（BHPV 第IV章、節は【要確認】）。例 $\mathbb{CP}^n$ の Kodaira 消滅の日本語、例 $\mathbb{CP}^1\times\mathbb{CP}^1$ の表の注、Hodge ダイヤモンドの文、意味のない一文（Veronese の「Serre 消滅と同様…」）の削除 | 表現の修正 |

付録に独立検査で追加した検算の項目と、【要確認】の箇所の一覧の更新を入れた。

## 2. 確認した項目（誤りなし、または計算で一致）

- Hodge の星作用素（$**$、$d^*=(-1)^{m(k+1)+1}*d*$）、Hodge の定理の骨子、Dolbeault 版。
- Kähler 恒等式の 4 式の符号：平坦な場合の直接計算を再導出して一致。Huybrechts 命題 3.1.12 とも一致（外部で確認）。vol02 の記述とも一致。
- $\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}$ の導出（符号を含め展開し直して一致）、(a)(b)(c)。
- Hodge 分解、Hodge 対称性、$\partial\bar\partial$-補題の証明（Green 作用素の可換性、各段）。
- $[\mathsf L,\Lambda]=k-n$、$\mathfrak{sl}_2$ の関係、Hard Lefschetz、Lefschetz 分解、原始次元（$T^4$、K3、5 次超曲面）。
- Weil の公式 $*\alpha=(-1)^{k(k+1)/2}i^{p-q}\mathsf L^{n-k}\alpha/(n-k)!$ と Hodge–Riemann の符号 $i^{p-q}(-1)^{k(k-1)/2}\int\omega^{n-k}\alpha\bar\alpha>0$：平坦 $\mathbb C^n$（$n=2,3$）、$k\le n$ の全ての $(p,q)$ の原始形式を、実直交余枠で Hodge 星作用素を作って数値確認（weil_check.py）。Weil の公式から符号が出る計算も確認。
- Hodge の指数定理（符号 $(2p_g+1,h^{1,1}-1)$、$\tau=2p_g+2-h^{1,1}=\sum_{p\equiv q}(-1)^ph^{p,q}$）、K3 の $(3,19)$、Rokhlin、$\mathbb{CP}^1\times\mathbb{CP}^1$、3 次曲面。
- Serre 双対の証明（$\bar*_E$、$\bar\partial^*$ の表示の符号 $(-1)^{p+q}$、調和形式の対応、非退化）。
- $\mathbb{CP}^n$ 上の $\mathcal O(m)$ の Čech 計算（単体複体の議論の 3 場合）、表、系 (a)(b)(c)、$\mathbb{CP}^1$ の明示的コサイクル、曲面 $X_d\subset\mathbb{CP}^3$。
- Serre 消滅の骨子（0)〜(3)、下降帰納法の完全列の向き）、豊富・非常に豊富の定義と逆。
- BKN 恒等式の導出（展開して符号まで一致）、曲率項の補題、Nakano 形式の向き（$\langle\Theta_{j\bar k}\xi_j,\xi_k\rangle$、直線束 $\omega=i\Theta$ の場合に $q$ と一致）、Kodaira・Akizuki–Nakano の証明、仮定ごとの表、Nakano 消滅、Nakano を使った Serre 消滅の別証明、Kodaira–Serre 双対形。
- Kodaira 埋め込み：爆発の公式 $K_{\tilde X}=\sigma^*K_X\otimes\mathcal O((n-1)E)$、$B_m$ の計算（(J) は $-(n+1)E$、(S) は $-n(E_x+E_y)$）、曲線の場合の $\deg L>2g$、Lefschetz $(1,1)$、射影性の判定（$\Theta_h=\Theta_{h_0}+\partial\bar\partial\psi$ の符号）。
- Kodaira–Spencer、Hodge 数の不変性の証明（上半連続性と $b_k$ の一定性）、変形次元の例（$\mathbb P^n$、曲線、複素トーラス、K3 の 20、4 次曲面 19）、Hirzebruch 曲面 $h^0(T)=a+5$（導出）。
- K3 / 5 次 3 次元多様体の Hodge 数、$e=-200$、$b_3=204$、$h^{2,1}=101$、$e(X_d)$ の公式（$d=1,2,3$ の既知値 $4,4,-6$ とも一致）、Hodge ダイヤモンドの図。
- Iwasawa 多様体の正則 1 形式、Hopf 曲面（$h^{1,0}=0$ の議論）、複素トーラスの Hodge 数。
- 統合論文：定理 14、18、22、79、81、83、88、予想 91、注意 15、17、82 の番号と内容を PDF の本文と照合（HH の定義は定義 5：$(\wedge^\bullet T\otimes E,\ d_E=[\sigma,\cdot]+V\wedge)$ の超コホモロジー）。第1〜4巻との整合（記号 $\Gamma$/$\Lambda$、$\omega=g(J\cdot,\cdot)$、Chern 曲率 $\Theta=\bar\partial\partial\log h$、Kähler 恒等式、Hopf 曲面）。

## 3. 全 40 問の再検算

全 40 問の問題文と解答を読み直し、計算を含むものは別に書いたコード（indep_check.py）で再計算した。

- 一致を確認した問: 問 serrePn（$n=1..4$、$-14\le m\le13$）、tableP2、hypsurf（$d=1..7$、$-10\le k\le12$）、$p_g=0,0,0,1,4,10$、SerreFail (b)（$h^1=m+1$）、TP2（$h^1(T(-3))=1$、$h^2(T(m))=3,8,15,24,\dots$（$m=-5,-6,\dots$）、閾値 $m_0=-2$。Euler 完全列の写像の階数で計算し、$\chi$ とも整合）、quintic の $c_3=-40H^3$ と $e(X_d)$、K3 moduli（19）、$\chi(T)$（$8,6,-20$）、unifiedP1（$-2$ と $3$ が $m$ によらない。$\chi(\mathcal O(m))-\chi(T(m))+\chi(\mathcal O(m+3))\equiv3$ を一般の $m$ で代数的にも確認）、例 P1P1 の Künneth の表、Pfaffian $=1$、トーラスの $\mathrm{NS}$（問 torusNS の行列 $S$ で $J^2=-1$、階数 0、$J_0$ では 4。別実装の厳密計算 torus_check.py）。
- 手計算で再確認: LLam、starflat、hodgedecomp（$\gamma=-\frac1{2\pi}\sin(2\pi x)dx\wedge dy$ で $d^*\gamma=\cos(2\pi x)dy$）、minnorm、ddbar（$\varphi=\mathrm{Re}(-i\gamma)$）、torusH、K3、primP3、unimodal、chiSerre、hodgesym、KodairaPn、K3h0、semipos、fano、amplediv、veronese、curvejets、torusPolar、integralKahler、Pnrigid、toriDef、hodgeconst、assume。
- 修正した問: holclosed（問題文と解答）、hirz（$F_0$ の扱い）、hodgeindex（解答）。

## 4. 確認できなかった項目・残る懸念

- 参考文献の章・節の多く（記憶による）。確認できたのは Huybrechts の章立てと命題 3.1.12 のみ。Griffiths–Harris、Wells、Voisin、Kodaira の本、Birkenhake–Lange の節は未確認で、§ 番号を落として章までの記述にした。命題・定理番号は、確認できなかった Huybrechts 3.3.17 を削除した。Hartshorne III.5.1/III.5.2 は記憶による。
- BHPV 第IV章（$b_1=h^{1,0}+h^{0,1}$）の節番号。
- Kodaira 埋め込みの $m_0$ の一様性、爆発上の $B_m$ の正値性の詳細は骨子のみ（本文でも【要確認】）。
- Weil の公式の一般の証明（各点の線形代数）は本文では【文献】。数値確認は $n=2,3$ のみ。
- 統合論文の主張は本巻では再検証していない。Part VI の記述は公開済みの記事の要約による。論文の定理 18 の Koszul 符号の整合は論文自身が【要確認】。
- 例 ex:prodbl（爆発の Hodge 数）、Siu（K3 は Kähler）、Raynaud の反例、Kawamata–Viehweg などは標準的な事実として【文献】のまま、個別の出典の確認はしていない。
- 本巻は \sloppy で 1 か所の Overfull hbox（約 3pt、表）が残る。フォントの斜体の警告は元からのもの。
