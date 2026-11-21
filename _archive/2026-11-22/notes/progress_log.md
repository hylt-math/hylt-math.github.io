## 2026-11-21 (fork: Serre/RR statements)
- Wrote serre_rr_statements.md: Thm A1 (Serre-type: for projective X, any Poisson σ, ample Poisson-module L_0: E_1^{a>0}=0 for m≥m_0 ⇒ HH^* = cohomology of Γ-complex, HH^k=0 for k>n; proved, any dim; thresholds m_0=−2 on P², −1 on P¹×P¹ via Bott), Thm A2 (periodic stabilisation, log-symplectic nodal surfaces), Thm B (closed formula for Poincaré polynomial in residue r), A3/APS-type RR as conjectures.
- Checks: cp2/serre_rr_check.py (thresholds, periodicity m≥1 on 8 examples, 80 values of closed formula, duality r↔2−r on 73 rationals: 0 mismatches); ncd_global_check.py re-run: 196 values, 0 mismatches.
- New observation: total-degree vanishing already false for σ=0; the right statement is transversal degree a>0 plus total degree >n. A1 removes the "U affine" hypothesis of ncd Thm 2(v) for ample L_0.
- Open/flagged: Pal–Poddar §11 definition of the cohomology and of q not re-read (compare before citing); duality of HH itself; Hu's index not applicable; APS/weighted-b-calculus proposal is speculative.
- Next suggested: (1) prove duality via ELW modular-class pairing; (2) verify PP Thm 11.12 definitions; (3) test unequal residues / reducible D numerically; (4) attempt a weighted-index computation for the smooth-D surface case.
# Progress log
## 2026-11-21 (round 3: gap closing for the surface theorem)
- Proved log-Moser normal form at an ordinary node: sigma ~ c z1z2 d1^d2 with invariant c=u(0) (Prop 11); rewrote the connecting-morphism argument (Lemma 7') with a correct local-cohomology weight count (extra class of H^1_p(O_D)). G4 closed.
- Vanishing of H^0,H^1 of rank-one local systems on U: exact criterion (chi not in V^1), proof for the 8 examples (Prop 12: Fulton-Deligne abelian pi_1 for nodal plane curves; C*xC*; P^2\(conic+secant) model; Timmerscheidt+Arapura for smooth (2,2) and two (1,1) curves). G2 closed.
- Serre duality for HH of GH line bundles over beta-transformed complex surfaces: HH^k(L)^* = HH^{4-k}(L^v K^2), via ellipticity (checked directly) + transposition of d_L (checked by hand and by cp2/serre_dual_check.py) (Prop 13). G9 closed for surfaces.
- Open: n>=4 duality, non-nodal D, unequal residues, identification with GC complex (cited, LGSX Thm 4.19).
- Files: ncd_theorem.md (sections 6-9 appended), cp2/serre_dual_check.py.
## 2026-11-21 (round 4 fork: G1 + duality in all dimensions)
- Fetched LGSX 0707.4253 and Gualtieri 0710.2719 (Branes on Poisson varieties): exact cites. LGSX Thm 4.19 (H^*(A,E) = H^*(T^{0,1}|x A^{1,0},E), Def 4.17 sheaf-cohomology def), Thm 4.21/Lemma 4.22 (L_pi ≅ T^{0,1}|x(T^{1,0})^*_pi, uses J_{4π}), Def 4.15/Lemma 4.16 (module over A ⇔ module over T^{0,1}|xA^{1,0}); Gualtieri Branes Prop 5 (GC structure from σ), Prop 8 (GH bundle = Poisson module), Prop 9 (line bundles: obstructions σα∈H^1(T), f_α∈H^2_σ; structures an affine space over H^1_σ). Correction: Gualtieri 0905.3227 does not contain these; earlier note "confirmed by fetch" stays retracted.
- G1: wrote Prop 14 (identification of the GC generalized Dolbeault complex with total complex of Dolbeault resolution of (∧T⊗L,[σ,.]+V∧)), proof via matched pair (Mokri, cited from memory) + LGSX; flagged what is cited.
- Duality for every n: Lemma D ([σ,T]_top = −Σ∂_i(σ^{ij}u_j)+2M·u), Lemma E (⟨dP,Q⟩+(−1)^b⟨P,d'Q⟩ = −Σ∂_i(σ^{ij}u_j) with V'=−V−2M), Prop 15 (HH^k(L)^* ≅ HH^{2n−k}(L^∨⊗K²), any holomorphic Poisson σ on compact complex n-fold; modular-vector-field contribution = 2M, i.e. K² module). Exact script cp2/duality_ndim.py (finds c=−2, s=(−1)^b by solving, n=2,3,4) and cp2/duality_ndim_exact.py (exact identities; [σ,M]=0, d²=0 with V=M for Poisson σ).
- Cross-check: Gualtieri Prop 9 ⇒ module structures unique iff HH^1(O)=0 — consistent with tables (smooth cubic unique; reducible D affine family).
- Open: Koszul-sign compatibility of ∂̄- and d-parts of the transposition is by hand (not scripted); Mokri's theorem cited from memory; Lemma 4.22 not re-derived.
## 2026-11-21 (fork: index-theoretic route survey, priority 5)
- Wrote index_route_notes.md. Literature (titles/authors fetched): Gualtieri–Li 1206.3674; Lanius 1605.03854; Braverman–Loizides–Song 1910.10016 (b-index = ∫Td(^bTM)Ch(L), no boundary term); Pflaum–Posthuma–Tang 1308.0236; Qiao–So 2304.13345 (boundary groupoids, no eta term, codim≥2); Ammann–Lauter–Nistor math/0304044; Mazzeo–Melrose math/9812120; Hausel–Hunsicker–Mazzeo math/0207169. Not found: index theory for complex algebroid L or residue-as-weight b-Dolbeault index.
- Derived: indicial roots of the log complex are r∈ℤ (stalk factor (n−r)); the indicial kernel is H^*(∂U) (Gysin of D); χ(∂U)=0 ⇒ Euler characteristic blind to r (parallel to BLS).
- New fit (cp2/index_route_check.py, 196/196 values): P_r(t)=χ(X)t² + [r≤0]Δ(t) + [r≥2]t⁴Δ(1/t), Δ=(1+t)(1+(b1−1)t); μ and b2 drop out. Conjecture I3 recorded; not proved.

## 2026-11-21 (fork: higher dim / toric / unequal residues) -> higher_dim_notes.md
- Wrote cp2/toric_hh.py, toric_crit.py (+ tests): exact weight criterion for toric log-symplectic structures: P_HH(t)=sum_chi t^s(1+t)^(n-s) over weights with A(chi+rho) in span(u_i: c_i=-1). Validated vs linear algebra (60 cases).
- Generic (huge-entry) sigma: HH = U-part ((1+t)^n iff rho in M & all r_i<=0) + vertex classes t^n + r=1 resonance classes; 0 mismatches on 3626 cases in P^4,P^2xP^2,(P^1)^4,P^1xP^3,P^1xP^1xP^2.
- New phenomenon: for n>=4 HH depends on sigma beyond residues (arithmetic coincidences give extra t^2 H^*(O_tau) from symplectic codim-2 strata). Block-product sigma on P^2xP^2: [1,4,12,16,16] (=product of surface results) vs generic [1,4,6,4,10].
- Euler characteristic = #vertices = chi(X) proved in toric case.
- Local: triple point xy(x-y) with unequal residues: stalk = C^4[-2] + H^*(U_loc;L) iff s1+s2+s3<2 (533 random cases, 0 mismatches). Node: per-branch threshold; triple point: threshold on sum.
- Not done: cusp/tacnode families on other surfaces, unequal residues globally non-toric, sheaf-theoretic check of F-part for mixed residues, P^1xP^1 irreducible cases beyond earlier notes.

## 2026-11-22 ラウンド0 作業B（Pal–Poddar 再読）
- arXiv:2404.18113 の題名は "Strong generalized holomorphic principal bundles"（Debjit Pal, Mainak Poddar）、Ann. Sc. Norm. Super. Pisa Cl. Sci.（DOI 10.2422/2036-2145.202501_026）。著者の食い違いは再現せず。Lang–Jia–Liu は "The Atiyah class of generalized holomorphic vector bundles" (DGA 90, 2023)。
- Thm 11.12 の主張・証明・仮定の役割を確定。使う群は横断（葉に沿って定数）な形式の層コホモロジー。本ノートの「横断次数でのみ消滅」の読みと整合。群は別物（余接側 vs ∧^bT、葉方向 de Rham 因子の有無）。
- 番号訂正: Hodge/Serre 双対は Thm 11.2, 11.4, 11.6, 11.7（v1 は 8.9, 8.10 としていた）。
- 詳細: pp_recheck.md、v1 への訂正リストは pp_patch_list.md。v2 に反映予定（作業Aの結果と合わせる）。

## 2026-11-22 (Task A: 引用検証)
- 検証結果は verify_citations.md、修正案は verify_patch_list.md（tex は未編集）。
- 重要な訂正: arXiv:0905.3227 の著者は Hitchin（Gualtieri ではない）。Pal–Poddar の題名は "Strong generalized holomorphic principal bundles"（著者の食い違いは再現せず、Ann. SNS Pisa Cl. Sci. 73 (2026) forthcoming）。Gualtieri 2011: 楕円性は Prop 3.13/Cor 3.14、Def 3.18 は Pic、一般化 Darboux は Thm 4.3、「Example 4.1–4.2」は存在しない。Lang–Jia–Liu は arXiv:2102.07177。Timmerscheidt は J. reine angew. Math. 379 (1987) 152–171。Pym は LMP 108 (2018) 573–632。HHM は Duke 122 (2004) 485–548。Hitchin 1105.4775 は Moscow Math. J. 12 (2012) 567–591。
- Hu 2403.10876: 証明中の BKN の符号のずれを本文で確認（主張は古典と整合）。
- 未確認のまま: Goto・Gualtieri–Li・Mokri・Arapura・LJL の掲載巻頁、Pal–Poddar の Thm 8.9 他、Crainic–Fernandes 等。

## 2026-11-22 (v2 build)
- paper_v2/: citation corrections from verify_patch_list.md and pp_patch_list.md applied to ja/en sources (Hitchin 0905.3227; Gualtieri 2011 numbering; Pal–Poddar title/authors/numbers; Lang–Jia–Liu 2102.07177; Hu sign slip confirmed; bibliographic data). Added §Revision notes (sec9.tex). Built ron.pdf (ja, 32pp) and paper_en/ron-en.pdf (en, 33pp). Math statements unchanged. Fixed \mathscr -> \mathcal in sec5.tex (ja).
