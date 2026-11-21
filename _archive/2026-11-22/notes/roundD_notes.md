# Round D: Riemann–Roch-type statements for log-symplectic GH line bundles (2026-11-22)
Legend: [P] proved here (hand proof; standard facts named) · [C] cited · [V] verified by script · [?] conjectural.
Script: cp2/roundD_check.py (Euler char via Bott recursion n<=6, m=-12..12: all pass; Theorem T vs closed weight criterion: 246 cases, 0 mismatches).
Uses: ncd_theorem.md (weight formula Lemma 3, Thm 2), higher_dim_notes.md §2–3, serre_rr_statements.md.

## 1. Total Euler characteristic [P] (any dimension, any holomorphic Poisson σ, any E)
**Theorem E.** X compact complex manifold, dim n; σ holomorphic Poisson; E holomorphic vector bundle with a flat A-connection (A=(T*_X)_σ), so that K^•=(∧^•T_X⊗E, d_E) is a complex of sheaves of C-vector spaces with coherent terms K^b. Then HH^k:=H^k(X;K^•) are finite-dimensional and
 Σ_k (−1)^k dim HH^k = (−1)^n · rk(E) · χ(X).
Proof. (i) The differentials are C-linear (not O-linear); only coherence of the terms and boundedness are used. Brutal truncations give triangles K^{≥b+1} → K^{≥b} → K^b[−b] →. Each H^*(X;K^b) is finite-dimensional (coherent, X compact), so by downward induction on b all hypercohomology groups are finite-dimensional and χ(K^{≥b}) = χ(K^{≥b+1}) + (−1)^b χ(X,K^b). Hence χ(HH) = Σ_b (−1)^b χ(X,∧^bT⊗E).
(ii) HRR: χ(X,∧^bT⊗E)=∫ch(E)ch(∧^bT)Td(T). With Chern roots x_i of T: Σ_b(−1)^b ch(∧^bT)=Π(1−e^{x_i}); Td=Π x_i/(1−e^{−x_i}); and (1−e^{x})/(1−e^{−x}) = −e^{x}. So the integrand is ch(E)·Π(−x_i e^{x_i}) = (−1)^n ch(E) e^{c_1(T)} c_n(T). Since c_n(T) already has degree n, only the degree-0 part of ch(E)e^{c_1} (=rk E) survives: χ(HH) = (−1)^n rk(E) ∫c_n(T) = (−1)^n rk(E) χ(X) (Gauss–Bonnet). ∎
Checks [V]: P^2: 1−0+2 = 3 (n=2: +χ). P^1, E=O(m): (m+1)−(m+3) = −2 = (−1)^1·2 ✓. roundD_check.py (1): Σ_b(−1)^bχ(P^n,∧^bT(m)) = (−1)^n(n+1), n=1..6, m=−12..12.
Consequences/roles: compactness ⇒ finiteness; holomorphic structure ⇒ coherent terms; GH structure ⇒ d²=0 (complex). Nothing about σ (non-degeneracy, log) or E's positivity is used: the Euler characteristic is blind to c_1(E), i.e. the "Riemann–Roch polynomial in m" is the constant (−1)^n rk E χ(X).
**Remark (general GC) [?].** For an arbitrary GC structure and flat L-connection E, ind(∧L*⊗E) = ∫ ch(E)·S (A–S, S = class of the symbol complex of (∧L*,d_L): Koszul complex of T*→L̄, ξ↦pr_{L̄}ξ, injective on real ξ≠0 since L∩L̄=0). Heuristic: flatness of E along L means ch_j(E) ∈ ker(H^{2j}_{dR}(M)→H^{2j}(L)) (Chern–Weil for L-connections), so one expects only rk E to contribute; not proved (needs the class S to be dual to the Lie-algebroid cohomology image).

## 2. The refined invariant: unified statement
Surfaces [P modulo gaps G1,G2,G4 of ncd_theorem.md] (Theorem B, serre_rr_statements.md):
 P_L(t) = χ(X)t² + [r∈Z_{≤0}]Δ(t) + [r∈Z_{≥2}]t⁴Δ(1/t),  Δ(t)=(1+t)(1+(b_1−1)t),  b_1=b_1(U).
Equivalent form [P]: P_L(t) = P(H^*(U;L_U)) + μ t² for r∈Z_{≤0} or r∉Z (note H^*(U;L)=[0,0,χ_U] for r∉Z), and P(H^*_c(U;L_U))+μt² for r∈Z_{≥2}. The "Riemann–Roch part" is χ(X)t² (value at t=−1: χ(X)); the residue-dependent "defect" Δ(t) is divisible by (1+t) (=cohomology of the boundary torus bundle ∂U, whose Euler characteristic is 0), hence invisible to any Euler characteristic.
**General-n conjecture (C), generic σ [?; proved in the toric case = Theorem T below].**
 X smooth projective, D SNC, σ log-symplectic (n=2k), L a GH line bundle with constant residues r_i on D_i, c_1(L)=−Σr_i[D_i], satisfying (V): H^a(X,∧^bT⊗L)=0 for a>0; σ generic (no arithmetic coincidences); no r_i ∈ Z_{≥1}. Then
 HH^*(L) ≅ H^*(U;L_U) ⊕ C^{#D_(n)}[−n],  D_(n)=points where n branches meet,
 i.e. P_{HH}(t) = P(H^*(U;L_U)) + #D_(n)·t^n. At t=−1: χ(U)+#D_(n) = χ(X) ⇔ Σ_{0<k<n}χ(D_k°)=0 (Euler-consistency, equivalent to Theorem E for this family).
 Euler-consistency check: surfaces: χ(D°)=0 by adjunction (K_D̃ = −(nodes)); toric: all strata are tori; general n [?]: strata S of codim k carry the nowhere-vanishing log vector fields σ^♯(dz_i/z_i) (i∈J) tangent to S̄ (sketch, nondegeneracy of the residue pairing Ω_J needed) ⇒ c_top(T_S̄(−log ∂S̄))=χ(S°)=0.
 Dictionary: ∫c_n(T_X(−log D)) = χ(U) (bulk term, the b-/log-algebroid Euler class) and #D_(n) = corner term; c_n(T)−c_n(T(−log D)) = Σ_{k≥1}χ(D_k°) = χ(D).
 For r_i∈Z_{≥2}: j_!-type, H_c^*(U;L)+#D_(n)t^n [?].
 Reduction of (C) to the quotient complex: Deligne ⇒ DR_log(L) ≃ Rj_*L_U iff no r_i∈Z_{≥1} [C]; HH = H^*(X;DR_log) ⊕ (stalks of quotient complex Q along strata). Surface: Q contributes C^μ[−2] (ncd Lemma 6, Prop 11) [P]. Missing for n≥4: the analogue of the log-Moser normal form at n-fold points and vanishing of Q along lower strata (weight/torus argument, verified numerically in the toric case).

## 3. Toric case: proof [P]
**Theorem T.** X smooth projective toric, dim n≥2 even, rays u_i, D=toric boundary, σ torus-invariant log-symplectic given by a nondegenerate skew matrix A in the log frame; L=O(Σa_iD_i) with GH structure d+ρ, ρ∈M_C, residues r_i=⟨ρ,u_i⟩−a_i. Assume
 (V) H^a(X,∧^bT⊗L)=0 for a>0 (all b);
 (A) L(D):=L⊗O(ΣD_i) is ample;
 (GEN) Pf(A)≠0 and the numbers A_ij (i<j) are linearly independent over K=Q(ρ_1,…,ρ_n);
 (R) r_i≠1 for all i.
Then P_HH(t) = [ρ∈M and r_i≤0 ∀i]·(1+t)^n + χ(X)·t^n.
Equivalently HH^* = H^*(U;L_U) ⊕ C^{χ(X)}[−n] when L has no residue in Z_{≥1}: indeed if ρ∈M all r_i∈Z, and then "r_i≤0 ∀i" ⇔ no r_i∈Z_{≥1} given (R); if ρ∉M then L_U is a nontrivial rank-one local system on (C*)^n so H^*(U;L_U)=0 — and Theorem T's first term is 0. (Statement (C) holds in the toric case for such L.)
Proof. Start from the weight formula [P] (ncd_theorem.md Lemma 3; higher_dim_notes.md §2), valid under (V): P_HH=Σ_{χ∈Λ}t^{s(χ)}(1+t)^{n−s(χ)}, Λ={χ∈M: c_i(χ):=⟨χ,u_i⟩+a_i ≥−1 ∀i, A(χ+ρ)∈W(χ)}, W(χ)=span{u_i: c_i(χ)=−1}, s=dim W.
Put x=χ+ρ∈M_C, C=C(χ)={i:c_i=−1}; for i∈C, ⟨x,u_i⟩=r_i−1. The condition Ax∈W is equivalent to ω(x,m):=⟨m,Ax⟩=0 for all m∈Ann_M(W), where ⟨m,Ax⟩=Σ_{i<j}A_ij(m_ix_j−m_jx_i).
* s=n: W=N, condition void; these χ are the lattice points with C(χ) of full rank, i.e. vertices of the polytope {c_i≥−1} of the ample L(D) (A): simple, normal fan = Σ, vertex lattice since X smooth; exactly one per maximal cone: χ(X)=V of them, each contributes t^n.
* s≤n−1: m_i,x_j∈K, so by (GEN) ω(x,m)=0 iff m_ix_j=m_jx_i for all i<j, i.e. x∥m over K. If rk Ann(W)=n−s≥2 (s≤n−2) pick independent m,m′∈Ann(W): x∥m and x∥m′ force x=0, i.e. χ=−ρ. If s=n−1: Ann(W)=Zm_0, and x=τm_0 gives ⟨x,u_i⟩=0 for i∈C, i.e. r_i=1 for i∈C≠∅ — excluded by (R) (here C≠∅ since s≥1 when n≥2).
* The weight χ=−ρ (possible iff ρ∈M) has c_i=−r_i, so C(−ρ)={i: r_i=1}=∅ by (R), s=0, and the condition c_i≥−1 reads r_i≤1, i.e. r_i≤0 (r_i∈Z). It contributes (1+t)^n.
Collecting: P=[ρ∈M, r_i≤0 ∀i](1+t)^n+χ(X)t^n. ∎
Role of hypotheses: (V) ⇒ computation by global sections (weight formula); (A) ⇒ #vertex weights = χ(X) (simple polytope, one weight per maximal cone, no degenerate vertices); (GEN) ⇒ vanishing of the skew pairing forces x∥m (kills all intermediate strata classes); (R) ⇒ removes the "resonance" curves (classes t^{n−1}(1+t)); Pf(A)≠0 ⇒ log-symplectic (iso σ^♯, so DR_log≅Lichnerowicz complex). For n=2 (GEN) is just A_12≠0, so Theorem T holds for every log-symplectic toric surface: e.g. P^2 triangle, m=1..: [1,2,4] ✓ (matches Theorem B with b_1=2,μ=3).
(V) holds for L=L_0^m, m≫0, L_0 ample: the sequence 0→O⊗N→T_X→⊕N_{D_i}→0 (T_X(−log D)=O⊗N) gives a filtration of ∧^bT with graded pieces ∧^{b−|J|}N⊗O_{D_J}(D_J), |J|≤b; Demazure vanishing (nef line bundles on complete toric varieties have no higher cohomology) applies to L(D_J)|_{D_J} for m≫0 [C: Cox–Little–Schenck, Toric Varieties, Thm 9.2.3].
Verification [V]: roundD_check.py (2): P^2 (m=1,2,3), P^1×P^1 (1,1),(1,2),(2,3), P^4 (1), P^2×P^2 (1,1), (P^1)^4 (1,1,1,1); ρ over a grid incl. rho=(1/3,0,…); random A mod 2^61−1; 246 cases with all r_i≠1: 0 mismatches. Earlier refined-prediction check (higher_dim_notes §3, includes r_i=1 resonances) 0/3626 with the big prime.
Non-generic σ: additional classes t^{|τ|}H^*(O_τ;L|_τ) on symplectic strata at arithmetic coincidences (higher_dim_notes §4): (GEN) is genuinely needed.

## 4. Index-theoretic outlook [?]
 1. Bulk term. The Lie algebroid T_X(−log D) (rank n, Euler class e) has de Rham complex DR_log; its index/Euler class is ∫c_n(T_X(−log D))=χ(U) [C: e.g. Aluffi, or Deligne]. This is the b-/log "Riemann–Roch" term, residue-independent.
 2. Corner term. #D_(n)·t^n: located at the deepest strata; the quotient complex Q=C(A;L)/C(B;L) is supported on D with differential −(1−r)·(unit)·p on smooth points (ncd Lemma 6), i.e. acyclic except at points where the residue pairing degenerates (resonance) and at n-fold points.
 3. Residue-dependent defect. In the weighted b-calculus picture the residue r is a weight; DR_log(L) ≃ Rj_*L (r∉Z_{≥1}) vs j_!L (r∉Z_{≤0}) differ by H^*(∂U;L)=cohomology of the boundary torus bundle (APS-type boundary term: cohomology of the boundary operator at the indicial root r∈Z). Its Euler characteristic is 0 (χ(torus bundle)=0), which explains why the Euler characteristic is blind to r and why a refined RR must be a graded/Poincaré-polynomial statement P_r(t)=χ(X)t^n+defect_r(t), defect divisible by (1+t) [P for surfaces].
 4. What a theorem would need: (a) index theory for the complex Lie algebroid L=T^{0,1}⋈A^{1,0} or Morita-equivalent real algebroid T(−log D)≅(T*(log D))_σ (integrability: Crainic–Fernandes with trivial monodromy via leaves, Bailey–Gualtieri Thm 7.1, see cp2_proof_notes.md); Hu's theorem does not apply (hu_notes.md); (b) a weighted/b-Sobolev Fredholm theory in which "r∈Z" = non-Fredholm weights; (c) an APS-type formula whose boundary contribution reproduces the polynomial Δ_r(t) from H^*(∂U).
