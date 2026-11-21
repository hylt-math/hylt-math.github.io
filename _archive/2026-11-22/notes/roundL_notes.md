# Round L (2026-11-22): regular type (Pal–Poddar setting) vs. our results
Tags: [P] proved here (hand proof) · [C] cited · [V] verified by script cp2/roundL_check.py · [?] conjectural/heuristic · [G] gap.

## 0. Setting S (flat symplectic bundles)
M = (Y × X̃)/Γ, Γ = π_1(X) acting on X̃ by deck transformations and on Y by symplectomorphisms ρ: Γ→Symp(Y,ω_Y).
X compact complex (dim k), Y compact connected symplectic (dim 2m). J = J_Y × J_X descends: a *regular GC structure of type k*,
leaves = fibres Y_x, leaf space X (smooth, or Kähler orbifold if Γ acts with fixed points: allowed in Pal–Poddar Thm 7.3).
SGH line bundle (module) E = π^*G, G holomorphic on X (leafwise-trivial case). V^j := local system H^j(Y_x;C) on X (Gauss–Manin), with its flat holomorphic bundle V^j⊗O_X.
(Leafwise-flat E with non-trivial holonomy χ: on a *compact* base the holonomy character is a holomorphic section of a flat torus bundle, hence locally constant [P, max. principle]; if Y is a torus and χ≠1, H^*(Y;L_χ)=0 so HH=0 [P].)

## 1. Structure of the L-complex  [P]
Prop L1. ω̃ := descent of pr_Y^*ω_Y is a closed 2-form on M; e^{iω̃} is a Courant automorphism (dω̃=0) with L = e^{iω̃} L_0, L_0 = T_{F,C} ⊕ T^{0,1}_{hor} ⊕ N^*, N^* = π^*T^{*1,0}_X.
Hence L ≅ L_0 as Lie algebroids (anchor-preserving): **the cohomology does not see ω** (only the foliated complex structure):
 C(L;E) = Ω^•_{F_C}(M; E⊗∧^•T^{1,0}_X),  F_C = T_{F,C}⊕T^{0,1}_{hor} (involutive), N acts trivially on SGH E.
Proof: locally this is the product statement; all objects are Γ-invariant. □
Consequence (compare Pal–Poddar Thm 8.9, Cor 8.10): the transversal-only groups H^{p,q}_{d_L} do NOT contain the leafwise factor H^j_dR(Y); our HH does.

## 2. Theorem L (Leray + Lefschetz)  [P]
Hypotheses: (S) setting above; (HL) hard Lefschetz holds for (Y,ω_Y); E = π^*G.
Claim: HH^k(M,E) = ⊕_{a+b+j=k} H^a(X, ∧^bT_X ⊗ V^j ⊗ G),   (dim over C), no X Kähler/projective needed.
Proof. (i) double complex (leafwise de Rham) × (Dolbeault on X with coefficients ∧^bT_X⊗G); fibres compact, Ehresmann ⇒ leafwise cohomology sheaf = C^∞-sections of V^j; ∂̄ on it = (0,1)-part of Gauss–Manin [independent of the choice of lift since changes are leafwise Lie derivatives of closed forms = exact] ⇒ E_2^{a,j}=⊕_b H^a(X,∧^bT⊗V^j⊗G).
(ii) ρ^*ω̃ = ω_F (mixed components vanish because ω̃ is locally pr_Y^*ω_Y), so Λ=ω_F∧ is a chain map of the double complex (commutes with d_F and ∂̄), acts on E_r commuting with d_r, and on E_2 is fibrewise Lefschetz V^j→V^{j+2}, an isomorphism V^{m−i}→V^{m+i} of flat bundles by (HL).
(iii) Deligne's lemma (Deligne 1968, "Théorème de Lefschetz et critères de dégénérescence de suites spectrales", Publ. IHES 35): d_2 x has L^{s+1}d_2x=0 for x primitive of weight s, and d_2x lives in fibre degree n−s−1 where L^{s+1} is injective ⇒ d_2=0; induction ⇒ d_r=0 (r≥2). Dimensions add. □
 Role of hypotheses: (S) gives the splitting L≅L_0 and Ehresmann/local systems; compact Y and (HL) give finite-dimensional E_2 and degeneration; X compact gives finite dimensions; N acting trivially (SGH) is why the T_X-grading b is a direct summand (no Poisson d_1). Without (HL) d_2 may be ≠0 (no example computed).

## 3. Examples (all [V] where marked)
(a) Product Y×X, X=P^1, G=O(m): P(t)=P_Y(t)·((m+1)+(m+3)t) for m≥−1. Y=T²: m=0: 1,5,7,3; Y=S²: m=0: 1,3,1,3. Euler char = −2χ(Y) = (−1)^1χ(M)-type (Theorem E) [V].
(b) **Kodaira–Thurston** T²→M→E (monodromy shear ψ=[[1,1],[0,1]] around one cycle). V^0=V^2=O, V^1 = Atiyah bundle F_2 (flat unipotent with nonzero (0,1)-class; h^0=h^1=1 for G=O) [C Atiyah 1957 for F_2]. G=O: P(t)=(1+t)(1+t)(1+t+t²)=1+3t+4t²+3t³+t⁴. **[V]** independently from the invariant model: L_0-complex of the Lie algebra F=⟨X1,X2,W⟩, [X2,W]=−½X1 (Heisenberg h_3) ⊗ ∧N: Betti (1,3,4,3,1) — equal, so d_r=0 consistent (note: invariant-form model assumed to compute HH, Nomizu-type; not proved).
   deg G=d>0: P(t)=d(1+t)³ (h^0(F_2⊗G)=2d, h^1=0); deg G=0, G≠O: P=0.
(c) Flat Bieberbach quotient (T²×E)/Z_2, (y,x)→(−y,x+τ/2): V^1=L_{−1}⊕L_{−1}, acyclic for G=O ⇒ P=(1+t)²(1+t²) **[V]** (equals Z_2-invariants of Künneth).
(d) S²-bundles with flat SO(3) holonomy: V^j trivial ⇒ same numbers as the product (a).

## 4. Corollary L (graded Riemann–Roch + Serre in regular type)  [P] (given Thm L)
X projective, G ample (π^*G = positive SGH line bundle in the sense of Pal–Poddar Def 11.11 when X is Kähler), m≥m_0:
 H^a(X,∧^bT_X⊗V^j⊗G^m)=0 (a>0) (classical Serre: ∧^bT_X⊗V^j locally free), hence
 HH^k(M,E^m) = ⊕_{b+j=k} H^0(X,∧^bT_X⊗V^j⊗G^m),
 dim HH^k(M,E^m) = Σ_{b+j=k} b_j(Y)·∫_X ch(∧^bT_X) e^{m c_1(G)} Td(X)   (flat ⇒ ch(V^j)=rk V^j).
So in regular type there IS a Riemann–Roch *polynomial in m for each total degree k*, and the total Euler characteristic χ(Y)(−1)^kχ(X) is consistent with Theorem E (Part II). 
Comparison with the type-jumping log-symplectic case (Parts I–III): there E_1^{0,b}=H^0(∧^bT⊗L^m) also grows polynomially but d_1=[σ,·] is almost exact ⇒ dims bounded/periodic in m. The difference between "polynomial graded RR" and "periodic stabilisation" is exactly whether the Poisson differential d_1 on the T_X-graded pieces vanishes (SGH, regular) or not.

## 5. Pal–Poddar Thm 11.12 in Setting S  (reading from pp_recheck.md; [C])
Hyp.: M compact regular GC type k, M/S Kähler orbifold, E positive SGH line bundle. (1) H^q(M,(𝒢^*M)^p⊗E)=0 for p+q>k; (2) ∀ SGH E', ∃m_0: H^q(M,E'⊗E^m)=0, q>0, m≥m_0.
In Setting S these groups are H^q(X,Ω^p_X⊗G) (transversal / leafwise-constant forms): (1) is classical Kodaira–Nakano on X; (2) for E'=π^*(∧^bT_X⊗V^j) (SGH: transition functions locally constant along leaves, holomorphic transversally) is classical Serre on X. [P] So **our transversal-degree vanishing is exactly P–P (2) applied to E' = ∧^bT_X⊗V^j**, and Corollary L is "P–P Serre + Leray/Lefschetz".
CAVEAT [?/要確認]: literally, the sheaf cohomology of the sheaf of locally leafwise-constant sections on M picks up extra H^j(Y) (Leray, R^jπ_*π^{-1}≠0); P–P's Thm 8.9/Cor 8.10 identify H^q(M,(𝒢^*M)^p) with leafwise-constant (transversal) Dolbeault cohomology, so their H^q must be read on the leaf space (H^q(M/S, π_*·)). We did not find this spelled out; check the definition of 𝓖 sheaf cohomology in Section 8.
Also: what vanishing gives for HH^k = ⊕H^0(∧^bT_X⊗V^j⊗G^m): only transversal degree a>0 vanishes; the H^j_dR(Y) factor survives in every degree j.

## 6. Common framework (heuristic) [?]
Both settings: HH(E)=H^*(M;C(L;E)), L Lie algebroid with ideal N=ker(anchor) (rank k at regular points, jumps at type-jump points), filtration by N-degree b with E_1^{a,b}=H^a(∧^bT-type; E) (for β-transforms N^*=T^{1,0} twisted by σ). d_1 = N-action ("Higgs/Poisson"): 0 for SGH on a regular structure; [σ,·]+V∧ for β-transforms.
 Regular type:   HH = ⊕ H^*(X; ∧T ⊗ [leafwise de Rham of compact leaves]) (Thm L) — leaf space cohomology, local system V^j.
 Type jump (log-symplectic): open leaf U (type 0), leafwise de Rham of the NON-compact leaf ⇒ H^*(U;L_U); the type-2 stratum D contributes (extension Rj_*/j_! by residues, C^μ[−2] at nodes, …). In both: HH ≈ "leafwise de Rham × transversal Dolbeault", with boundary conditions at lower strata governed by the module's indicial data (residues).
Dictionary: fibre Y compact ↔ leaf U with 'boundary' D; V^j (Gauss–Manin) ↔ H^j(U;L_χ) with Rj_*/j_! choice; flat-bundle monodromy ↔ monodromy e^{2πi r} around D; Lefschetz degeneration (needs compact Y) ↔ no analogue (U non-compact: d_1≠0 genuinely).
Conjecture U (stratified, imprecise): for a compact GC manifold with finitely many type-strata S and E with N-trivial module along regular strata, HH^*(E) has a filtration with pieces H^*_{(c)}(leaf-space-fibration over S; leafwise de Rham ⊗ transversal Dolbeault) with (c)/non-(c) decided by indicial roots. NOT formulated precisely; no test beyond the two families above.

## 7. Gaps
G1: the invariant-form computation for KT assumes Nomizu-type theorem for L_0-cohomology (only a consistency check; Thm L itself does not use it).
G2: Atiyah's F_2 cohomology and the identification V^1≅F_2 (unipotent, nonzero (0,1)-class) are standard but cited/derived quickly.
G3: Orbifold base / non-flat bundles (Ehresmann connection not flat; coupling form ω̃) not treated; Thm L is for flat symplectic fibre bundles only.
G4: nontrivial leafwise holonomy with Y non-torus (e.g. HL for twisted coefficients) not treated.
G5: P–P sheaf-cohomology reading (§5 caveat) unverified in the source.
