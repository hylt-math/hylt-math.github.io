# v1 → v2 修正リスト（日本語 .tex。英語版 paper_en/ にも同じ箇所があるので対応する英訳を直す）

すべて scratchpad/paper/ 内。old は現行ファイルの文字列（そのまま検索可能）、new は置換後。根拠は verify_citations.md。

## 優先度A：誤りの訂正

### A1. arXiv:0905.3227 の著者は Hitchin（Gualtieri ではない）
- refs.tex 22 行目
  - old: `\bibitem{GuaPM} M.\ Gualtieri, Poisson modules and generalized geometry, arXiv:0905.3227 [題名\tQ].`
  - new: `\bibitem{GuaPM} N.\ Hitchin, Poisson modules and generalized geometry, arXiv:0905.3227 (2009)（題名・著者は arXiv ページで確認。掲載書誌は未確認\tQ）.`
  （bibitem のキー GuaPM は本文で \cite されていないのでキー名はそのままでよい。望むなら HitPM に変えて両方直す）
- sec8.tex 28 行目
  - old: `\item \textbf{Gualtieri, \emph{Poisson modules and generalized geometry}（arXiv:0905.3227、題名は\tQ）}：`
  - new: `\item \textbf{Hitchin, \emph{Poisson modules and generalized geometry}（arXiv:0905.3227、題名・著者は確認済み）}：`
  - 同じ行の文末 `（予備調査で「確認した」としていたのは誤り。）` はそのままでよい（予備調査で Gualtieri 論文と誤記し、かつ「確認した」と書いたため）。必要なら `（予備調査の「Gualtieri 0905.3227 で確認」は、著者名と内容の両面で誤りだった。）` に置換。
- 英語版 paper_en/refs.tex 22 行目、paper_en/sec8.tex 28 行目も同様（Gualtieri → Hitchin、title \tQ を外す）。

### A2. Gualtieri 2011 の番号
- sec2.tex 7 行目
  - old: `\S3（定義の番号は\tQ）`
  - new: `\S3（型 Def.\ 3.5、標準束 Def.\ 3.7、一般化 Calabi--Yau Def.\ 3.17、Picard 群 Def.\ 3.18。番号は原文で確認）`
- sec2.tex 11 行目
  - old: `\src{Gualtieri 2011, \S4（例 4.1--4.2 付近、番号は\tQ）。}`
  - new: `\src{Hitchin 2003（導入）；Gualtieri 2011, \S3（複素構造・シンプレクティック構造の例。具体的な例番号は確認できず。\S4 の Def.\ 4.1 は正則点の定義で、旧稿の「例 4.1--4.2」は存在しない）\tQ。}`
- sec2.tex 19 行目
  - old: `\src{Gualtieri 2011, \S3（Prop.\ 3.16 付近、番号は\tQ）。`
  - new: `\src{Gualtieri 2011, Prop.\ 3.13（$(\wedge L^*,d_L)$ は楕円型）、Cor.\ 3.14（コンパクトなら有限次元コホモロジー）。`
- sec2.tex 33 行目
  - old: `\src{Gualtieri 2011, \S3.7（Def.\ 3.18 付近、番号は\tQ）；`
  - new: `\src{Gualtieri 2011, \S3（一般化正則束は Thm.\ 3.15 の後に散文で導入され、番号付きの定義はない。複素構造の場合は Example 3.19。Def.\ 3.18 は Picard 群の定義）；`
- 型の跳びの例と Darboux（本文に引用があれば）：型跳びの例は Gualtieri 2011 \S4.1、$\rho=z_1+dz_1\wedge dz_2$（式 (4.8)、$\R^4$、$z_1=0$ で型 2、他で型 0）。一般化 Darboux は Thm.\ 4.3（正則点）、Prop.\ 4.2（葉空間の複素構造）、Def.\ 4.1（正則点）。台帳 sec8.tex 27 行目の「Darboux の定理など」は `Darboux の定理（Thm.\ 4.3）` に置換可。

### A3. Lang–Jia–Liu の書誌と位置づけ
- refs.tex 37 行目
  - old: `\bibitem{LJL} Lang--Jia--Liu, 強一般化正則束に関する論文（書誌は\tQ。本文では Pal--Poddar 経由で言及のみ）。`
  - new: `\bibitem{LJL} H.\ Lang, X.\ Jia, Z.\ Liu, The Atiyah class of generalized holomorphic vector bundles, arXiv:2102.07177（掲載誌は未確認\tQ）。（局所自明化と一般化正則な遷移関数で定義される GH 束の Atiyah 類。Pal--Poddar の SGH 束とは別の文献。）`
- sec2.tex の \ref{def:SGH} 付近 `Lang--Jia--Liu（定義の導入、題名・書誌\chk）` に当たる記述があれば、`Pal--Poddar（定義、arXiv:2404.18113 \S3--4）` に直す。（grep で "Lang" を検索したが現行 sec*.tex には本文の言及なし。refs のみ。）
- 追加してよい引用：LJL Cor.\ 3.6（GH 束は誘導 Poisson 多様体上の Poisson 加群、正則 Poisson 多様体上ではその逆も成り立つ）と Thm.\ 4.5（Atiyah 類が GH 接続の障害）。Ni, arXiv:2508.10723（3 通りの Atiyah 類が同値）。

### A4. Pal--Poddar の題名・著者
- refs.tex 41 行目
  - old: `\bibitem{PP} A.\ Pal, M.\ Poddar, et al., arXiv:2404.18113 [題名・著者\tQ].`
  - new: `\bibitem{PP} D.\ Pal, M.\ Poddar, Strong generalized holomorphic principal bundles, arXiv:2404.18113; Ann.\ Sc.\ Norm.\ Super.\ Pisa Cl.\ Sci.\ 73 (2026)（出版社ページ上は forthcoming、doi:10.2422/2036-2145.202501\_026）.`
- sec5.tex 66 行目
  - old: `\src{Pal--Poddar, arXiv:2404.18113（題名・著者表示は\tQ。arXiv 上の著者表示と末尾の氏名に食い違いがあった）, \S11, Thm.\ 11.12（正則型・葉空間が Kähler 軌道体・強一般化正則束）。}`
  - new: `\src{Pal--Poddar, \emph{Strong generalized holomorphic principal bundles}, arXiv:2404.18113, \S11.2, Thm.\ 11.12：$M$ がコンパクトな正則型（型 $k$）一般化複素多様体で $M/\mathscr S$ が Kähler 軌道体、$E$ が正の SGH 直線束のとき、(1) $p+q>k$ ならば $H^q(M,(\mathcal G^*M)^p\otimes E)=0$、(2) 任意の SGH ベクトル束 $E'$ に対し $m_0$ が存在して $m\ge m_0$、$q>0$ ならば $H^q(M,E'\otimes E^m)=0$。（取得した先頭約 10 万字で確認。「正」の定義は未確認\tQ。）}`
- sec7.tex 8 行目
  - old: `\tC\ Pal--Poddar, arXiv:2404.18113（題名・著者表示は\tQ）は、`
  - new: `\tC\ Pal--Poddar, \emph{Strong generalized holomorphic principal bundles}, arXiv:2404.18113 は、`
  - 同じ行の `（Thm.\ 8.9, Cor.\ 8.10）` と `（Thm.\ 11.12、準備 Prop.\ 11.2--11.8, Lemma 11.9）` の「準備 Prop.\ 11.2--11.8, Lemma 11.9」は未確認なので `（Thm.\ 11.12。準備の Prop.\ 11.2--11.8, Lemma 11.9 の番号は未確認\tQ）` に直す。Thm.\ 8.9 は未確認、Cor.\ 8.10 は序論で SGH 束の Dolbeault コホモロジーとして言及されることのみ確認。
- sec8.tex 26 行目（書誌の台帳）
  - old の末尾部分: `Pal--Poddar の題名・著者（arXiv 上の著者表示と末尾の氏名に食い違いがあった）、`
  - new: `Pal--Poddar の掲載巻・頁、`
  - old: `Bailey--Gualtieri の題名、`
  - new: （削除）
  - old: `Hitchin arXiv:1105.4775 の掲載誌、`
  - new: （削除。Moscow Math.\ J.\ 12 (2012) 567--591 を確認）
  - old: `Hausel--Hunsicker--Mazzeo の頁、`
  - new: （削除。Duke Math.\ J.\ 122 (2004) 485--548 を確認）
  - old: `Timmerscheidt の掲載誌、`
  - new: （削除。J.\ reine angew.\ Math.\ 379 (1987) 152--171 を確認）
  - old: `Pym (Lett.\ Math.\ Phys.\ 2018)、`
  - new: （削除。Lett.\ Math.\ Phys.\ 108 (2018) 573--632 を確認）
  - 残す：Goto の掲載誌・巻頁、Gualtieri--Li の IMRN 巻頁、Gualtieri "Branes" の OUP 書誌、Mokri の巻頁、Arapura の巻頁、LJL の掲載誌、LGSX の IMRN Art.\ ID。
  - 加える：`Pal--Poddar の Thm.\ 8.9, Prop.\ 9.3, Ex.\ 10.18, Def.\ 11.10--11.11, Prop.\ 11.2--11.8, Lemma 11.9, Ex.\ 13.10 の番号と内容（先頭約 10 万字には出現せず）`。

### A5. Timmerscheidt の書誌
- sec6.tex 41 行目
  - old: `Timmerscheidt（unitary 局所系の Hodge 理論、書誌は\tQ：Math.\ Ann.\ 277 (1987) 247 と記憶していたが J.\ reine angew.\ Math.\ 379 (1987) の可能性もあり未確認）`
  - new: `Timmerscheidt（\emph{Mixed Hodge theory for unitary local systems}, J.\ reine angew.\ Math.\ 379 (1987) 152--171）`
  - 同じ行の Arapura: old `Arapura（J.\ Algebraic Geom.\ 6 (1997) 563--597、トーション平行移動の定理）` → new `Arapura（\emph{Geometry of cohomology support loci for local systems I}, arXiv:alg-geom/9612006、J.\ Algebraic Geom.\ 6 (1997) 563--597（巻頁は記憶\tQ）、トーション平行移動の定理）`
- refs.tex 46 行目
  - old: `J.\ reine angew.\ Math.\ 379 (1987) [掲載誌・頁\tQ].`
  - new: `J.\ reine angew.\ Math.\ 379 (1987) 152--171.`
- refs.tex 5 行目（Arapura）
  - old: `J.\ Algebraic Geom.\ 6 (1997) 563--597 [頁\tQ].`
  - new: `arXiv:alg-geom/9612006; J.\ Algebraic Geom.\ 6 (1997) 563--597 [巻頁は記憶\tQ].`

## 優先度B：書誌の確定（\tQ を外す）

- refs.tex 28 行目（Hitchin）: old `arXiv:1105.4775 [掲載誌\tQ].` → new `Moscow Math.\ J.\ 12 (2012), no.\ 3, 567--591, arXiv:1105.4775.`
- sec3.tex 96 行目: old `（Moscow Math.\ J.\ 12 (2012)、書誌は\tQ）` → new `（Moscow Math.\ J.\ 12 (2012) 567--591）`
- refs.tex 25 行目（HHM）: old `Duke Math.\ J.\ 122 (2004), arXiv:math/0207169 [頁\tQ].` → new `Duke Math.\ J.\ 122 (2004) 485--548, arXiv:math/0207169.`
- refs.tex 43 行目（Pym）: old `Lett.\ Math.\ Phys.\ 108 (2018) [頁\tQ].` → new `Lett.\ Math.\ Phys.\ 108 (2018), no.\ 3, 573--632, doi:10.1007/s11005-017-0984-5.`
- sec3.tex 10 行目: old `Goto, \emph{Unobstructed deformations of generalized complex structures induced by $C^\infty$ logarithmic symplectic structures}, J.\ Math.\ Soc.\ Japan 68 (2016)；` → new `Goto, \emph{Unobstructed deformations of generalized complex structures induced by $C^\infty$ logarithmic symplectic structures and logarithmic Poisson structures}, arXiv:1501.03398（掲載誌・巻頁は未確認\tQ）；`; 同行の `Pym, ..., Lett.\ Math.\ Phys.\ 108 (2018)。書誌情報は記憶に基づく\tQ。` → `Pym, ..., Lett.\ Math.\ Phys.\ 108 (2018) 573--632（確認）。Gualtieri--Li の掲載誌と Goto の掲載情報は未確認\tQ。`
- refs.tex 15 行目（Goto）: old `J.\ Math.\ Soc.\ Japan 68 (2016) [頁\tQ].` → new `arXiv:1501.03398 [掲載誌・巻頁は未確認\tQ].`
- refs.tex 7 行目（Bailey–Gualtieri）: old `arXiv:1611.03850 [題名\tQ].` → new `arXiv:1611.03850.`
- sec7.tex 30 行目: old `（Thm.\ 7.1、題名は\tQ）` → new `（Thm.\ 7.1：下の実 Poisson 構造が積分可能であることが必要十分。Thm.\ 7.1 自体は Hausdorff・$s$-連結性を述べない。構成 Thm.\ 7.6 は $s$-連結かつ $s$-単連結な積分を用いる）`
- refs.tex 40 行目（Mokri）: old `Glasgow Math.\ J.\ 39 (1997) 167--181 [記憶に基づく\tQ].` → new `Glasgow Math.\ J.\ 39 (1997) 167--181, doi:10.1017/S0017089500032055 [年・DOI は出版社ページで確認、巻頁は記憶\tQ].`
- sec2.tex 46 行目: old `Glasgow Math.\ J.\ 39 (1997) 167--181、記憶に基づく引用\tQ）` → new `Glasgow Math.\ J.\ 39 (1997) 167--181, doi:10.1017/S0017089500032055。年・DOI は確認、巻頁は記憶\tQ）`。同じ行に追加：`（LGSX Lemma 4.16：複素ベクトル束が $A$-加群であることと $T^{0,1}X\bowtie A^{1,0}$-加群であることは同値。Thm.\ 4.19 の証明は Thm.\ 4.11 と同様とだけ記される。）`
- refs.tex 21 行目（Branes）: old `in: The Many Facets of Geometry, Oxford Univ.\ Press 2010, arXiv:0710.2719 [書誌\tQ].` → new `arXiv:0710.2719（v2, 2010-07；arXiv ページに掲載書誌の記載なし。The Many Facets of Geometry, Oxford Univ.\ Press 2010 は記憶\tQ）.`

## 優先度C：Hu 2403.10876 の記述
- sec7.tex 25 行目
  - old: `\item \emph{原典の不整合（要約を通して得たもの）}：Thm.\ 7 で $n$ が未定義、符号定数が Thm.\ 5, Prop.\ 1, Thm.\ 6 で異なる、「単模」の定義が二通り、BKN の符号（$[\nabla^2,\Lambda]$ 対 $[\sqrt{-1}R,\Lambda]$）に食い違いの疑い。2403.10876 は先頭約 10 万字のみ読み、付録（Kähler 恒等式の証明）は未読。\tQ`
  - new: `\item \emph{原典の不整合}：2403.13424（要約を通して得たもの）：Thm.\ 7 で $n$ が未定義、符号定数が Thm.\ 5, Prop.\ 1, Thm.\ 6 で異なる、「単模」の定義が二通り。2403.10876（本文の続きと付録の一部を読んで確認\tC）：Lemma 5 は $[L,\Lambda]=(p+q-n)\mathrm{id}$ だが、Thm.\ 2 の証明は $\Delta_{\bar\partial_{\mathfrak g}}=\Delta^{1,0}-[L,\Lambda]=\Delta^{1,0}+(p+q-n)\mathrm{id}$ と書き、後の等号の符号が合わない（$-(p+q-n)=n-p-q$）。さらに代入 $\nabla^2=\sqrt{-1}L$ は $\sqrt{-1}R=-L$ を意味し、「正」（$\sqrt{-1}R>0$、Def.\ 13）の定義と逆である。主張（正の $E$ で $p+q>n$ のとき核が消える）自体は古典の Kodaira--Nakano と整合する。つまり印刷された証明に符号のずれがある（主張の否定ではない）。Cor.\ 1 に矢印と記号 $s/t$ の誤植。付録（Lemma 6--10、$[\bar\partial_{\mathfrak g},\iota_\omega]$ の計算）は添字が読み取りにくく検証できていない。参考文献欄と掲載誌は未確認。\tQ`
- sec7.tex 14 行目「原典の記述について、本調査で気づいた疑義」は Pal--Poddar についてで、Hu ではない。変更なし。
- sec8.tex 29 行目付近「Hu の 2 論文」の台帳項目：`2403.10876 は先頭約 10 万字のみ` → `2403.10876 は先頭約 20 万字（HTML 展開後の全体は約 50 万字）まで`。

## 優先度D：確認できなかったため変更しない（v2 でも【要確認】のまま）
Goto の掲載誌、Gualtieri--Li の IMRN 巻頁、Gualtieri "Branes" OUP 書誌、LGSX の IMRN Art.\ ID と "Prop.\ 3.7"、Mokri の巻頁、Arapura の巻頁、LJL の掲載誌、Pal--Poddar の Thm 8.9 他の番号、Crainic--Fernandes・Deligne・Fulton・Esnault--Viehweg の番号、Gualtieri math/0409093・1007.3485・Cavalcanti の定理番号。
