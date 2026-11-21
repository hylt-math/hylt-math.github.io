# v1 への訂正リスト（Pal–Poddar 関連）。ファイルは paper/*.tex、paper_en/*.tex（英訳側も同様に直す）

1. refs.tex:41
 旧: \bibitem{PP} A.\ Pal, M.\ Poddar, et al., arXiv:2404.18113 [題名・著者\tQ].
 新: \bibitem{PP} D.\ Pal, M.\ Poddar, Strong generalized holomorphic principal bundles, arXiv:2404.18113; Ann.\ Sc.\ Norm.\ Super.\ Pisa Cl.\ Sci., DOI 10.2422/2036-2145.202501\_026（掲載巻号は\tQ）。
2. refs.tex:37
 旧: \bibitem{LJL} Lang--Jia--Liu, 強一般化正則束に関する論文（書誌は\tQ。…）
 新: \bibitem{LJL} H.\ Lang, X.\ Jia, Z.\ J.\ Liu, The Atiyah class of generalized holomorphic vector bundles, Differential Geom.\ Appl.\ 90 (2023) 102031, doi:10.1016/j.difgeo.2023.102031（Pal--Poddar の参考文献 [26] による）。SGH の定義は Pal--Poddar Def.\ 3.1。
3. sec5.tex:66（\src）と sec7.tex:8: 「（題名・著者表示は\tQ。arXiv 上の著者表示と末尾の氏名に食い違いがあった）」→ 削除。
 sec7.tex:8 の定理番号: 旧「Serre 双対性（Thm.\ 8.9, Cor.\ 8.10）、…（Thm.\ 11.12、準備 Prop.\ 11.2--11.8, Lemma 11.9）」
 新「横断 Dolbeault 同型（Thm.\ 8.9, Cor.\ 8.10）、Hodge 分解と Serre 双対性（Thm.\ 11.2, 11.4, 11.6, 11.7）、Kähler の恒等式（Prop.\ 11.8, Lemma 11.9）、正の SGH 直線束（Def.\ 11.10, 11.11）に対する消滅（Thm.\ 11.12）」。
4. sec5.tex:68 の注意（「各群の定義と『q』が何の次数を指すかを筆者は読み直していない」）を置換:
 新: 「Pal--Poddar の H^q(M,(𝒢*M)^p⊗E)（Cor.\ 8.10 により H^{p,q}_{d_L}(M,E)）は、葉に沿って定数な横断形式の層コホモロジーで、q は横断（複素）次数である。したがって上の命題の読み（横断次数 a についてのみ消滅）は Thm.\ 11.12 と整合する。ただし群は同じではない：Pal--Poddar は 𝒢*M の外冪、本ノートは ∧^bT（接側）をテンソルし、さらに本ノートの HH は葉方向の de Rham 因子を含む全複体である。」
5. sec7.tex:12（旧「定理 11.12 との直接の比較はしていない\tQ」）→ 「定理 11.12 の主張・証明の構造は §11 を再読して確認した（正確な主張：H^q(M,(𝒢*M)^p⊗E)=0 (p+q>k)、および H^q(M,E'⊗E^m)=0 (m≥m_0, q>0)。仮定の役割は…）。」と差し替え、役割を2〜3行で追記。
6. 疑義リスト (sec7.tex:13) を更新: (i) 1/2π: 主張は (i/2π)、証明は 1/2π なし（無害）; (ii) 符号: 原因は特性多項式 (9.9) と §10.1 の det(I±tA/2πi); (iii) 正のクラス⇒正曲率計量は Def 11.11 の定義から証明には出ず、Thm 11.12 の証明が仮定; 追加 (iv) Def 11.11 にコンパクト・Kähler 仮定の明記なし; (v) Lemma 11.9(1) の証明は点ごとの局所枠での計算; (vi) Thm 13.4(2),(3) の T^{1,0} vs T^{1,0*}、Example 13.10 の q=n の二項係数。
7. sec8.tex:32（精読範囲）: 旧「各群の定義を読み直していない」→ 「§§5–11, 13 を再読した（2026-11-22）。抽出は要約を介しており式の細部は未確認」。sec8 の【要確認】台帳から「Pal--Poddar §11 の再読」を除き、「巻号（Ann. Sc. Norm. Super. Pisa）」を加える。
8. sec7.tex:41 と sec7.tex:37: 「Pal--Poddar §11 の再読」「Thm.\ 11.12 との正確な比較」→ 完了済みに更新。
9. 英語版（paper_en）の対応箇所（Section "Relation to Pal–Poddar"、references、status ledger）にも同様に反映。
