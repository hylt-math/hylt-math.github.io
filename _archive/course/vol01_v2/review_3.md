# 査読者3（N=3）ノート：§7〜§10（partC.tex, solC.tex）、front.tex、back.tex

ビルド: rv3_build/（xelatex 2 回、エラー 0、Overfull 0、142 頁。残る警告はイタリック CJK フォントのみ）。
修正はすべて rv3_build/ 内のコピー（partC.tex, back.tex）。**メインの partC.tex / back.tex には未反映**（統合担当が下表を反映するか rv3_build のファイルをコピーすること）。

## 修正一覧
| 箇所 | 旧 | 新 | 理由 |
|---|---|---|---|
| partC 例 8.x（トーラス上の平坦接続） | 「第3・5巻の Fourier--Mukai や Hodge 理論の土台」 | 「Jacobi 多様体・Picard 多様体（第4巻）の実数版のモデル」 | シラバスに Fourier--Mukai はなく、後の巻の内容の過大な主張 |
| partC 例（対数接続の入り口）、§8 keybox | 「第3巻・第13巻」「第3・13巻」 | 「第11・13・14巻」 | 第3巻（層）に対数接続・留数は無い。対数シンプレクティックは第11巻、論文対応は第13・14巻 |
| partC 命題（ホロノミー表現）の出典 | Lee ISM「平坦束・局所系に関する節」 | Kobayashi--Nomizu 第I巻 第II章のみ（節番号は書かない\tQ） | Lee ISM にその節があることを確認できず、捏造のおそれ |
| back Q11 答 | 「$F\ne0$ なら枠をどうとっても消せない」 | 「その点の近傍で $A$ を恒等的に $0$ にできない」と明確化 | 点での $A=0$ は常に可能なので曖昧 |
| back 参考文献 [BT] | 第 I 章の § の並びが不順（Poincaré の補題が MV の後、MV が 2 回） | §1--§7 を実際の順（複体、Poincaré の補題、MV、向きと積分、Poincaré 双対、Thom 同型）に | Bott--Tu 目次（§3 Poincaré 補題、§4 MV）に合わせた |
| back 参考文献 [Wa] | 「第2章 微分形式」\tQ | 「第2章 テンソルと微分形式」、章題を Springer 目次で確認し \tQ を外した | WebFetch（Springer）で確認 |
| back 橋渡し冒頭 | 「状態表に載っている定理・命題の番号だけ」 | 「本文・状態表で実在を確認した定理・命題・定義の番号だけ」 | 実際は命題 3、定義 4・5 も引用（実在は確認済）。記述と実態の不一致 |
| back 橋渡し（定理 9(c)） | 符号照合を第 13 巻に先送りのみ | 最も単純な例（$\CP^1$、$D=\{0\}$、$e_0=z^re_1$）で $\int c_1=-r$ と統合論文の $c_1=-\sum r_i[D_i]$ が整合することを追記。一般の場合は\tQ のまま | 手計算で確認できた範囲のみ |

## 確認した項目（誤りなし）
- §7 全体：貼り合わせ定理の証明（構成・位相・Hausdorff・一意性）、$e_\beta=e_\alpha g_{\alpha\beta}$ / $\sigma_\alpha=g_{\alpha\beta}\sigma_\beta$ の整合、Möbius 束の貼り合わせ関数、$\mathcal O(-1)$ の $g_{ij}=z_i/z_j$、$g_{01}=z^{-1}$、双対・$\Hom$ の貼り合わせ関数、Gram--Schmidt と $g^*g=I$、完全列の分裂、$TS^3$ の枠（$\langle ip,jp\rangle=0$）、Bott--Milnor--Kervaire の出典、$\mathcal O(-1)$ の Hermite 計量の整合。
- §8：ゲージ変換則（順方向・逆方向）、他書の規約の注意書き（$e'=g^{-1}e$ のとき $gAg^{-1}-\dd g\,g^{-1}$）、$S^1$ のホロノミー $e^{-2\pi i\lambda}$、射影接続 $\theta=\partial\log(1+|z|^2)$、接続のアフィン構造と $A_\beta=\sum\rho_\alpha g_{\alpha\beta}^{-1}\dd g_{\alpha\beta}$、平行移動の定理と (25)、$\dd_\nabla$ の well-definedness、$F=\dd A+A\wedge A$ の証明、(c)(d)、**小ループのホロノミー**（4 因子の $\varepsilon^2$ 展開の全係数を手で再計算、かつ別実装の RK4 で非可換 $A$ に対し誤差が $\varepsilon^3$ で減ることを確認：$0.031,0.0038,0.00047$）、Bianchi 恒等式（2 通りの証明）、誘導接続の表、ユニタリ接続（$A^*=-A$、$F^*=-F$）、Koszul の公式（符号を再導出）、Christoffel 記号の存在証明、構造方程式、$S^2$ で $\omega^1{}_2=-\cos\vartheta\,\dd\varphi$、$K=1$、緯線ホロノミー（回転角 $-2\pi\cos\vartheta_0\equiv2\pi(1-\cos\vartheta_0)$、向きも一致）、測地三角形の回転角 $\alpha$、平坦接続の局所自明性（$[X_i,X_j]=-(F_{ij}g)\partial_g$ を再導出）、ホロノミー表現（$\rho=P^{-1}$ で準同型）、AB・トーラス・対数接続の例。
- §9：Hopf 束の遷移関数 $s_1=s_0\,|z|/z$（$g_{10}=z/|z|$、巻き数 1）、同伴束 $\varepsilon_\beta=\varepsilon_\alpha\rho(g_{\alpha\beta})$、命題 9.6（$A_\beta=g^{-1}A_\alpha g+g^{-1}\dd g$ の微分の導出）、曲率の水平性と Bianchi（括弧の符号・Jacobi）、$s_0^*\omega=\frac{\bar z\dd z-z\dd\bar z}{2H}$、$F=\dd\bar z\wedge\dd z/H^2$（手計算で再確認）、ゲージ群の記述。
- §10：超越公式の証明（$\dot F_t=\dd_{\nabla_t}a$、トレースの巡回性、Bianchi）、$\int c_1(\mathcal O(-1))=-1$（極座標積分まで）、$L_k$ の $-k$、巻き数定理（$e_0=ge_1$、境界の向き）、$T\Sigma$ で $c_1=\frac K{2\pi}\dd A$、$T\CP^1$ の $g=-z^{-2}$、$\int c_1=2$、$c_2=\frac1{8\pi^2}\tr F^2$、$\ch_2=-c_2$、Todd 級数、$\chi(\CP^1,\mathcal O(m))=m+1$（$\mathcal O(m)=L_{-m}$）、CS 形式の $d\mathrm{CS}=\tr F^2$、EM の符号（$\nabla=\dd-ia$、$c_1=\frac1{2\pi}\dd a$）。
- solC 全 36 問を通読。独立再計算：C_gauge（$A'$ 全成分、$g^{-1}Fg$）、C_curvcalc（$F$ の全成分と $\dd F+A\wedge F-F\wedge A=0$ を有限差分で数値確認：$F$ 一致、Bianchi 残差 $6\times10^{-12}$、$\dd F$ 各成分 $z,2y,2x,-z$ 一致）、C_hopf(c)（$A_0-A_1=i\,\dd\varphi$）、C_winding(c)、C_Dirac、C_CS(a)、C_c2、C_Euler、C_LC (b)（$K=-1$）、C_clutch、C_flat、C_smallloop。誤りなし。
- 問題のレベル表示：妥当（C_curvcalc は基本だが 4 成分の Bianchi 確認がやや長い。[標準] に近い）。
- front.tex：各節への要約・節番号・「88 問」「15 問」は一致。
- back.tex：自己診断 15 問の答えをすべて検算（Q2 の $[\partial_y,\partial_x+y\partial_z]=\partial_z$、Q3 の $2\,\dd x\wedge\dd y$、Q7 の $(-1)^{n+1}$、Q8 の $\star^2=+1$ 等）。節参照（§3.6, §8.5, §10.3--10.4 など）はすべて目次と一致。巻の対応はシラバス（_archive/course/syllabus.md）の巻名・内容と一致。
- **統合論文との対応**（PDF unified-v1-ja を全文抽出して照合）：§2.2 命題 3（β 変換）、定義 4・5、命題 6、§2.3 定理 9（(c) の $c_1=-\sum r_i[D_i]$ も実在）、定理 18（双対性）、定理 22（全 Euler 標数）、定理 25、§1.3 状態表、§1.5 (i)(ii)、§2.1 HRR、§8、§10（予想 94）はすべて実在し内容も記述と合致。捏造番号・過大な主張は上記 Fourier--Mukai 以外に見つからず。
- 参考文献：Lee ISM（22 章・付録）、Bott--Tu 4 章の構成、Warner の章題、Gualtieri・Hitchin・Bott--Milnor・Kervaire・Kervaire--Milnor の書誌は記憶と Springer 目次で一致。

## 確認できなかった項目
- Lee Riemannian Manifolds、Milnor--Stasheff 付録 C、Hirzebruch 第I章、Husemoller、Petersen、KN の章番号（\tQ のまま）。
- 「Euler 類 $=\mathrm{Pf}(\frac1{2\pi}F)$」の符号規約（予告の範囲）。
- 命題 8.x（ホロノミー表現）の証明は概略のまま。

## 残る懸念（範囲外を含む）
1. partA §1.1 の依存関係図は §9→§10 を実線で結ぶが、§10 の本文の前提は §4・§8（§10 の goalbox も同じ）で §9 は本質的でない（Hopf 接続への言及程度）。図か goalbox のどちらかに合わせるとよい（partA 担当）。
2. §8.1 の `\ref{C:ss:PT}` 等が「節」として出る箇所は読めるが、「§8.4 節」の形になっていないか目視で一部のみ確認（問題なし）。
3. §7 の「$H^1(M,\underline{GL})$ と Pic」の記述は予告で、$\Pic\cong H^2(M;\Z)$ の出典は\tQ のまま。
4. 論点としては、§9 の「接続の存在（主束）」は述べられず、ベクトル束経由で足りるとされている点（入口として許容）。
