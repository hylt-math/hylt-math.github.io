# v1 論文の【要確認】引用の検証（2026-11-22, Task A）

検証方法：WebSearch で URL を出し、WebFetch で arXiv／出版社／索引ページを読んだ。「確認」は今回そのページで確認できたもの。取得できなかったものは「未確認」と明記。

## 要約表

| 項目 | v1 の記述 | 検証結果 | 修正の要否 |
|---|---|---|---|
| Pal–Poddar arXiv:2404.18113 | 題名・著者を【要確認】、「arXiv 上の著者表示と末尾の氏名に食い違い」 | arXiv abs: 題名 "Strong generalized holomorphic principal bundles"、著者 Debjit Pal, Mainak Poddar、2024-04-28。食い違いは再現せず。掲載：Ann. Sc. Norm. Super. Pisa Cl. Sci. 73 (2026)、doi:10.2422/2036-2145.202501_026（出版社ページ、forthcoming 表示で巻内頁・号は不明） | 要（題名・著者・掲載を確定、食い違いの記述を削除） |
| Pal–Poddar Thm 11.12 | 正則型・Kähler 軌道体・SGH で Kodaira／Serre 型消滅 | 存在確認（先頭10万字で）。主張：M コンパクト正則型 type k、M/S が Kähler 軌道体、E が正の SGH 直線束のとき (1) H^q(M,(G*M)^p⊗E)=0（p+q>k）、(2) 任意の SGH ベクトル束 E' に対し m≥m0 で H^q(M,E'⊗E^m)=0（q>0）。§11 の節名は 11.1 Generalized Serre duality and Hodge decomposition、11.2 Generalized Vanishing Theorems。序論に Thm 11.4, 11.6, 11.7 への言及。Thm 8.9, Cor 8.10, Prop 9.3, Ex 10.18, Def 11.10–11.11, Prop 11.2–11.8, Lemma 11.9, Ex 13.10 は取得範囲（先頭約10万字）に出ず未確認（Cor 8.10 は序論で SGH 束の Dolbeault コホモロジーとして言及）。「正」の定義は取得範囲で未確認 | 要（Thm 11.12 の主張を本文どおりに、他の番号は【要確認】のまま） |
| Gualtieri 2011（math/0703298）定義番号 | §3 の番号を【要確認】、型は Def？、Prop 3.16、Def 3.18（GH 束）、§4 Examples 4.1–4.2 | 型＝Def 3.5、標準束＝Def 3.7、一般化 CY＝Def 3.17、Pic＝Def 3.18（GH 束の定義ではない）、楕円性＝Prop 3.13、有限次元性＝Cor 3.14、GH 束は Thm 3.15 の後に散文で導入（番号付き定義なし）、複素構造の場合は Example 3.19。§4：Def 4.1 は正則点、Prop 4.2 は葉空間の複素構造、Thm 4.3 が一般化 Darboux（旧記録の "Thm 4.35" は誤り）。型跳びの例は §4.1 "Type jumping" の ρ = z1 + dz1∧dz2（式 (4.8)、R^4、z1=0 上で type 2、他で type 0）。「Examples 4.1–4.2」は存在しない | 要（Prop 3.16→3.13/Cor 3.14、Def 3.18 は Pic、Example 4.1–4.2 を削除） |
| Gualtieri "Branes on Poisson varieties" arXiv:0710.2719 | OUP 2010 掲載書誌を【要確認】、Prop 5, 8, 9 | 題名・著者確認。arXiv ページに掲載誌記載なし（v1 2007-10、v2 2010-07）。Prop 5：GC 構造が正則 Poisson 構造 σ=P+iQ（P=IQ）から得られる（generalized complex submanifold としての記述）、Prop 8：GH 束 = 正則 Poisson 加群、Prop 9：直線束の障害は Atiyah 類と σ から H^1(T_{1,0})、その次に二次の類 H^2_σ、存在するとき構造全体は H^1_σ 上のアフィン空間。§4.1 の節名は "Generalized holomorphic bundles" | 番号は正しい。書誌は【要確認】のまま（OUP 書誌は記憶） |
| arXiv:0905.3227 | 「M. Gualtieri, Poisson modules and generalized geometry」 | **著者の誤り**：N. Hitchin（Oxford）。題名 "Poisson modules and generalized geometry"、v1 2009-05-20、題名確認、アブストラクトなし。σ^{-1}=B+iω の B 場変換として記述、J_σ の記号なし、超コホモロジーの同定なし、Atiyah 類なし、CP^2 の例なし（本文取得による）。掲載誌は取得できず | 要（Gualtieri→Hitchin、本文の言及箇所すべて） |
| LGSX arXiv:0707.4253 | Thm 2.7, Rem 2.8, Def 4.17, Thm 4.19, Thm 4.21, Lemma 4.22 | すべて確認。Def 4.15（A-加群）、Lemma 4.16（A-加群 ⇔ T^{0,1}⋈A^{1,0} 上の加群）、Def 4.17（H^*(A,E) := H^*(X,Ω_A^•⊗E)）、Thm 4.19（H^*(A,E) ≅ Lie 亜群 T^{0,1}⋈A^{1,0} のコホモロジー、証明は Thm 4.11 と同様とだけ記載）、Thm 4.21（T^{0,1}⋈(T^{1,0})*_π ≅ L_{4π}、J_{4π} の −i 固有束）、Lemma 4.22（L_{4π} の明示形 (X^{0,1}+π^♯ξ^{1,0}, ξ^{1,0})、次元の数え上げで証明）。Rem 4.14 は Weinstein の問い（複素 Lie 亜群の積分）。Thm 2.7：(a) π=π_R+iπ_I 正則 Poisson ⇔ (b) (π_I,J) が Poisson Nijenhuis ⇔ (c) J_π が GC。IMRN 2008 の Art. ID は取得ページに記載なし | 番号は正しい。IMRN の書誌は未確認のまま。"Prop 3.7" は未確認 |
| Mokri | 記憶に基づく | 出版社ページ：T. Mokri, Matched pairs of Lie algebroids, Glasgow Math. J.、公開日 1997-10-06、doi:10.1017/S0017089500032055。巻・頁は取得ページに出ず（39, 167–181 は記憶と整合） | 軽微（DOI を追加、巻頁は【要確認】のまま） |
| Bailey–Gualtieri arXiv:1611.03850 | 題名を【要確認】、Thm 7.1 | 題名 "Integration of Generalized Complex Structures" 確認。Thm 7.1：GC 多様体 (M,I) が弱正則シンプレクティック亜群の微分として得られる ⇔ 下の実 Poisson 構造が（シンプレクティック亜群に）積分可能。Thm 7.1 自体は Hausdorff・s-連結性を述べない。構成 Thm 7.6 は s-連結かつ s-単連結な積分を要する。"only if" は Prop 4.4。Thm 1.1（微分は essential equivalence）、Thm 4.6（一意性）、Thm 2.8（局所標準形） | 要（題名の【要確認】を外す、Thm 7.6 の仮定を追記） |
| Gualtieri–Li arXiv:1206.3674 | IMRN 2014 | 題名・著者確認（Symplectic groupoids of log symplectic manifolds）。abs ページに掲載誌なし。滑らかな超曲面に接するベクトル場の Lie 亜群の構成と Hausdorff シンプレクティック亜群の分類（基本群のグラフ）を与える | 掲載誌は【要確認】のまま |
| Hitchin arXiv:1105.4775 | 掲載誌を【要確認】 | Moscow Math. J. 12 (2012), no. 3, 567–591（mathnet.ru mmj458）。題名確認、結果：コンパクト正則 Poisson 多様体の変形の非障害性定理。Hilbert scheme of P^2 を扱う | 要（掲載誌確定） |
| Goto | J. Math. Soc. Japan 68 (2016)、頁【要確認】 | arXiv:1501.03398 の題名・著者確認。掲載誌・巻・頁は取得できず未確認（JSTAGE の jmath/61 は別論文 "Poisson structures and generalized Kähler submanifolds"）。アブストラクト：滑らかな反標準因子をもつ複素曲面（del Pezzo, Hirzebruch）に適用、Poisson コホモロジーの計算あり | arXiv 番号を追加、掲載情報は【要確認】のまま |
| Pym | LMP 108 (2018)、頁【要確認】 | Lett. Math. Phys. 108 (2018), no. 3, 573–632、doi:10.1007/s11005-017-0984-5。arXiv:1701.08852 §2.2：P^2 の Poisson 構造はつねに 3 次曲線上で消え、曲線と重複度で定数倍を除き決まる。滑らかな場合は楕円曲線、modular residue は反標準因子上の非零ベクトル場 | 要（掲載情報確定） |
| Timmerscheidt | 「Math. Ann. 277 (1987) 247 または J. reine angew. Math. 379 (1987)」 | J. reine angew. Math. 379 (1987) 152–171、題名 "Mixed Hodge theory for unitary local systems"（Numdam/Mathdoc） | 要（確定） |
| Arapura | J. Algebraic Geom. 6 (1997) 563–597、頁【要確認】 | arXiv:alg-geom/9612006 の題名・著者確認、abs は "will appear in JAG" とあるのみ。巻頁は未確認 | arXiv 番号を追加、【要確認】のまま |
| Hausel–Hunsicker–Mazzeo | Duke Math. J. 122 (2004)、頁【要確認】 | Duke Math. J. 122 (2004), no. 3, 485–548、doi:10.1215/S0012-7094-04-12233-X | 要（確定） |
| Lang–Jia–Liu | 書誌【要確認】 | H. Lang, X. Jia, Z. Liu, The Atiyah class of generalized holomorphic vector bundles, arXiv:2102.07177（掲載誌は取得できず）。Thm 3.8（GH 束は L_- 接続 ∂̄_E, ∂̄_E²=0 をもつ）、Thm 4.5/4.7/4.8（Atiyah 類が GH 接続の障害、Čech/jet/Lie pair の3通り）、Prop 3.5・Cor 3.6（GH 束は誘導 Poisson 多様体上の Poisson 加群、正則 Poisson 多様体上では適切な Poisson 加群構造をもつ正則束について逆も成り立つ）。**注意**：この論文の GH 束は局所自明化で遷移関数が一般化正則という定義。Pal–Poddar の SGH 束とは別の文献で、本文の「Lang–Jia–Liu の強一般化正則束」という言い方は不正確の可能性。関連：D. Ni, arXiv:2508.10723（3通りの Atiyah 類の同値性。直線束の Pic の分類は扱わない） | 要（書誌と注意を置換） |
| Crainic–Fernandes | Thm 4.1, Cor 5.2 | **今回は未確認**（Task 内で fetch せず）。前回 (cp2_proof_notes) の引用のまま | 変更なし |
| Hu arXiv:2403.10876 | 先頭10万字のみ、付録は未読、BKN の符号に疑義 | 10万〜20万字（本文の続きと付録の一部、HTML 展開込みで全体は約50万字）を読んだ。付録は Lemma 6〜10（[∂̄_g, ι_ω] の計算、添字が乱れて検証困難）。Kähler の恒等式は [Λ, ∇^{0,1}] = √−1 ∇^{1,0*} と書かれ、符号は慣習により異なる。主定理 Thm 2・Cor 1：Kähler Lie 亜群 g と正の g-直線束 E に対し p+q>n で核が消える（正は Def 13：√−1R が正定値；負なら p+q<n）。base のコンパクト性は取得した主張に現れず。**符号の食い違いを本文で確認**：Lemma 5 は [L,Λ]=(p+q−n)id、証明は Δ_∂̄ = Δ^{1,0} − [L,Λ] = Δ^{1,0}+(p+q−n)id と書くが、後の等号は −(p+q−n)=(n−p−q) に反し誤り。さらに代入 ∇²=√−1L は √−1R=−L を意味し、正（√−1R>0）の定義と矛盾。つまり主張（p+q>n）は古典の Kodaira–Nakano と整合するが、印刷された証明に符号のずれがある。Cor 1 には M→g の矢印と s/t の混在の誤植。参考文献欄・掲載誌は取得範囲外で未確認 | 要（疑義を「確認した」に格上げし内容を書く。Hu の主張自体は否定しない） |
| Gualtieri math/0409093, 1007.3485, Cavalcanti | 定理番号を断言せず | 今回は検証対象外（未確認のまま） | 変更なし |
| Deligne LNM 163 の番号 | Ch. II §3 | 今回は未確認（原典の取得なし） | 変更なし |
| Deligne Bourbaki 543, Fulton Ann. Math. 111 | 記憶 | 今回は未確認 | 変更なし |

## 補足（本文の主張への影響）

1. **Hitchin の論文と Gualtieri の論文の混同**は、v1 の §8 台帳の「予備調査で『確認した』とした」の記述（Gualtieri の 0905.3227 に Pic や CP^2 が書かれていない）の主語を Hitchin に直せば本質的に変わらない。
2. **Pal–Poddar Thm 11.12 の (1) の次数 p+q>k と (2) の q のみ**という形は、v1 の「消滅は横断次数に対してのみ」という筆者の観察と整合する（k は型で、横断複素次元）。ただし (1) の群 H^q(M,(G*M)^p⊗E) は SGH 層の層コホモロジーであり、本文の HH^k との同一視は行っていない。
3. LGSX Thm 4.21 の因子 4 については v1 本文（sec2.tex 28 行目）がすでに触れている。
4. Hu の印刷された証明の符号の誤りは「主張の否定」ではなく「証明の記述の誤り」として書くべき。
5. Lang–Jia–Liu の GH 束は Gualtieri／Hitchin の「平坦な L-接続」とは定義が異なる（局所自明化による）。v1 の本文には「強一般化正則束の導入元」と読める箇所があり、Pal–Poddar の SGH とは別物として扱うこと。

## 未確認のまま残るもの

- Goto の掲載誌・巻・頁、Gualtieri–Li の IMRN 巻頁、Gualtieri "Branes" の OUP 書誌、LGSX の IMRN Art. ID、Mokri の巻頁、Arapura の巻頁、Lang–Jia–Liu の掲載誌。
- Pal–Poddar の Thm 8.9, Cor 8.10, Prop 9.3, Ex 10.18, Def 11.10–11.11, Prop 11.2–11.8, Lemma 11.9, Ex 13.10（先頭約10万字に未出現）。
- Hu 2403.10876 の Kähler 恒等式の証明（付録の主要部）と参考文献欄、本体 Lemma 4 の独立した記述。
- Gualtieri 2011 の §3.7 の節番号、Ex 3.19 以外の例示番号。
- Crainic–Fernandes、Deligne、Fulton、Esnault–Viehweg、Gualtieri math/0409093・1007.3485、Cavalcanti の番号・頁。
