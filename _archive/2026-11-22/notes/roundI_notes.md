# Round I (2026-11-22): Conjecture C — reduction theorem, intrinsic (GEN'), checks
Legend: [P] proved here · [C] cited · [V] verified by script · [?] conjectural / gap.
Script: cp2/roundI_check.py (output summary cp2/roundI_out.txt).  Uses ncd_theorem.md (Lemma 3: B ≅ DR_log), roundD_notes.md (Thm E, Thm T), higher_dim_notes.md.

## 0. Setting and notation
X compact, dim n=2k, D=ΣD_i SNC, σ log-symplectic (σ^♯: Ω^1(log D)≅T(−log D)), L a Poisson module = flat log connection, residues r_i (constants on D_i, c_1(L)=−Σr_i[D_i]).
C=(∧^•T⊗L, d_σ+V∧) generalized Dolbeault complex of sheaves of C-vector spaces (HH^k=H^k(X;C)); B=∧^•T(−log D)⊗L ⊂ C subcomplex ≅ DR_log(L) via ∧σ^♯ [P, ncd Lemma 3]; Q=C/B.

## 1. Structure of Q [P modulo the coordinate computation in 1.3]
1.1 Filtration. In log coordinates (z_I,w): ∧T has O-basis ∂_{z_S}∧∂_w^Y, ∧T(−log D) has basis E_S∧∂_w^Y=z^S ∂_{z_S}∧∂_w^Y. Hence Q is spanned by 'multivectors with a pole': pole set T(s)=set of branches along which s has a pole (of order exactly 1). Since σ∈∧²T(−log D) and the module vector field V=σ^♯(Σ r_i dlog z_i)∈T(−log D), d never creates poles: F_k={|T(s)|≤k} (F_0=0) is an increasing filtration of Q by subcomplexes, F_n=Q.
1.2 Graded pieces. gr_k Q=⊕_{|T|=k} Q_T, T running over (connected components of) strata D_T=∩_{i∈T}D_i, and
  Q_T ≅ (z^{−T}E_T) ⊗ (∧^•T_{D_T}(−log D'_T) ⊗ L|_{D_T}),  D'_T = the other branches restricted to D_T,
 with differential d_T = [σ_T,·] + ν_T∧ , where
  σ_T = image of σ in ∧²(T(−log D)|_{D_T}/⟨E_i: i∈T⟩)=∧²T_{D_T}(−log D'_T)  (a Poisson structure: D_T is a Poisson submanifold),
  ν_T = Σ_{i∈T}(r_i−1)[H_i] ∈ T_{D_T}(−log D'_T),  H_i=σ^♯(dlog z_i)∈T(−log D), [·]=class mod ⟨E_j:j∈T⟩.
 ([σ_T,ν_T]=0 and (d_T)²=0.)  The '−1' comes from [σ,z_i^{−1}]=−z_i^{−1}H_i, the 'r_i' from the module structure.
1.3 Checks of the formula [P for n=2; general n computation sketched]: n=2, T={i}, smooth point: d_Q=(r−1)∂_{w}∧ up to unit/sign (ncd Lemma 6); node T={1,2}: gr_2=C_p[−2]. Product example below confirms the general formula numerically (§4). The general-n derivation is the same Schouten-bracket computation in the frame (E_i, ∂_w): [E_i∧Y,z^{−T}E_T f β] for i∈T contributes only the −∂-term (E_i∧E_T=0), for i∉T it is part of σ_T. [? not written line by line]
1.4 Top piece. |T|=n: D_T=point p, ∧^•T_{D_T}=C, so gr_n Q=⊕_{p∈D_(n)} C_p[−n] with zero differential. [P]

## 2. Intrinsic genericity (GEN') [definition]
(GEN') for every stratum T with 1≤|T|≤n−1 the complex of sheaves Q_T=(∧^•T_{D_T}(−log D'_T)⊗L|_{D_T}, [σ_T,·]+ν_T∧) on D_T is acyclic (stalkwise).
Necessary conditions [P]: ν_T≠0 on D_T (if ν_T≡0, Q_T is the twisted Lichnerowicz complex of σ_T, whose H^0 contains the locally constant Casimirs); in particular for |T|=1 one needs r_i≠1 (R) — so (GEN') contains (R). ν_T(p)=0 at a point can still be compatible with acyclicity only if cancelled by [σ_T,·]; the simplest sufficient condition is: ν_T nowhere vanishing and the operator 1+L_{X_θ} invertible on germs, θ a 1-form with θ(ν_T)=1 (homotopy h=ι_θ: (δ+ν∧)h+h(δ+ν∧)=1+[δ,ι_θ]) [?, only checked in models]. 
Models [P]: (a) |T|=1, smooth point of D, n arbitrary: σ=E_z∧∂_{w_1}+Σ∂_{w_{2j}}∧∂_{w_{2j+1}} (log-Darboux at smooth points of D: cited for b-symplectic real case, Guillemin–Miranda–Pires Adv.Math.264 (2014), holomorphic analogue by the same Moser argument — 【要確認】). Then ν=(r−1)∂_{w_1}, and Q is the cone of (r−1)·id on the Lichnerowicz complex of the symplectic part, hence acyclic iff r≠1. (b) toric/linear model with constant A (below).

## 3. Main reduction theorem [P]
**Theorem R.** Let X,D,σ,L as in §0, n even, and assume (i) no residue r_i lies in Z_{≥1}; (ii) (GEN'). Then
   HH^*(L) ≅ H^*(U;L_U) ⊕ ⊕_{p∈D_(n)} C[−n],   U=X∖D, L_U=flat local system,
and in particular χ(X)=χ(U)+#D_(n) i.e. Σ_{0<k<n}χ(D_k°)=0 (D_k°: open k-fold strata) [using Theorem E].
Proof. (1) B≃Rj_*L_U by Deligne (nonresonance (i)) [C: Deligne, Équations différentielles à points singuliers réguliers, LNM 163, II.3.13; see also Esnault–Viehweg]. (2) By §1 and (ii), F_{n−1}Q has all graded pieces acyclic, hence is acyclic; so Q→Q/F_{n−1}=gr_n Q=⊕_pC_p[−n] is a quasi-isomorphism. (3) The triangle B→C→Q→B[1] has connecting morphism in Hom_{D(X)}(⊕i_{p*}C[−n], Rj_*L_U[1]) = ⊕Hom(j^*i_{p*}C[−n],L_U[1])=0, since j^*i_{p*}=0 (p∈D). So C≃B⊕Q in D(X). (4) Take H^*(X;·); H^*(X;Rj_*L_U)=H^*(U;L_U). The Euler statement: Theorem E gives χ(HH)=(−1)^nχ(X)=χ(X) (n even), the right side has χ(U)+#D_(n)·(−1)^n; χ(X)=Σ_kχ(D_k°) (D_0°=U, D_n°=D_(n)). ∎
Roles of hypotheses: (i) identifies B with Rj_*; (ii) kills all lower strata of Q; n even only because log-symplectic; compactness only for finiteness/Theorem E; NO vanishing hypothesis (V) and NO ampleness is used — those only entered the earlier toric weight computation of global sections.
Corollary [P]: this proves Conjecture C in the form: C holds for (X,D,σ,L) iff Q's lower graded pieces contribute nothing; so Conjecture C ⇔ (GEN') (⇐ proved; ⇒ in the toric case since extra classes are exactly non-acyclic Q_T, §4).

## 4. Toric/linear model [P + V]
X toric, σ=½ΣA_ijE_iE_j constant in log frame (A skew nondegenerate), ρ∈M_C, r_i=⟨ρ,u_i⟩−a_i. The weight-χ part of Q_T (T={i:χ_i=−1}) is the Koszul complex ∧(N_C/W_T) with differential v_χ∧, v_χ=A(χ+ρ) (this is the toric form of d_T: ν_T acts through the r_i−1 on W_T coordinates, the derivative part through χ). It is acyclic iff v_χ∉W_T.
 • Q_T acyclic for all weights ⇔ no solution x∈ρ+χ-coset of 〈x,u_i〉=r_i−1 (i∈T), Ax∈W_T. 
 • (GEN)+(R) (A_ij linearly independent over Q(ρ), r_i≠1) ⇒ no solution for any T with 1≤|T|≤n−1 (proof as in Theorem T: ω(x,m)=0 for m∈Ann(W_T) ⇒ x∥m ⇒ r_i=1). Hence (GEN') holds and Theorem R gives HH=H^*(U;L_U)⊕C^{χ(X)}[−n]: this REPROVES Theorem T WITHOUT (V) and (A) [P].
 • Necessary-direction test [V]: cp2/roundI_check.py: for subsets S of rays (rank s, 1≤s≤n−1) test solvability of 〈x,u_i〉=r_i−1 (i∈S), Ax∈W_S mod 2^61−1; over P^2,P^1×P^1,P^4,P^2×P^2,(P^1)^4 with generic A, block A, small-integer A and 5 residue vectors: 48 cases with no solvable S all give HH=generic prediction (0 violations); 25 cases with solvable S and HH≠generic; 92 solvable-but-unrealised (false alarms). Output: cp2/roundI_out.txt.
 • Mechanism of cross terms [P+V]: P^2×P^2, block A=A_X⊕A_Y, ρ=0,m=1: ν_T=0 for T=(node of X)×Y because the mixed block A_{XY}=0, so Q_T=∧T_Y(−log D_Y)⊗… with the Lichnerowicz differential of σ_Y, i.e. ≃DR_log(Y)≃Rj_*C_{U_Y}, contributing t²(1+t)² per T; 3+3=6 such T: 6t²(1+t)²=[0,0,6,12,6] = actual−generic = [1,4,12,16,16]−[1,4,6,4,10] ✓ (exactly). Also explains roundF: 'cross terms μ_X·H_Y·t²' with H_Y= H^*(U_Y;L_Y).
 General prediction [?]: without (GEN'), E_1^{T}=H^*(D_T;Q_T) ⇒ H^*(X;Q); if all Q_T with ν_T=0 are of 'product type' the extra part is Σ_T t^{|T|}H^*(U_T;L_T).

## 5. Intrinsic reading of (GEN') in terms of the residue matrix [P/?]
At p∈D_T (|T|=c) in log frame (E_1..E_c,∂_w): A(p)=[[A_TT,A_{TW}],[−A_{TW}^t,A_WW]] with A_TT=σ(dlog z_i,dlog z_j)(p) the intrinsic 'residue pairing' (c×c skew), ν_T(p)=(A_{TW})^t(r_T−1) the vector in T_pD_T. In the constant-coefficient model the stalk of Q_T at p has cohomology iff the vector ν_T(p) lies in the image of the Poisson structure A_WW up to the Koszul lattice weights; (GEN') thus asks: (r_T−1)^tA_{TW}∉ (image of A_WW + lattice), i.e. residues r_T−1 are not annihilated by the 'transversal part' of σ along D_T. Special cases: c=1: A_{TW} is the row (σ(dlog z_i,·)) ≠0 by nondegeneracy; ν≠0 iff r_i≠1. c≥2: needs A_{TW}^t(r_T−1)≠0 — fails e.g. for products (A_{TW}=0).
 Not proved in general: (a) that ν_T≠0 (nowhere) implies acyclicity of Q_T for non-linearizable σ (homotopy argument needs invertibility of 1+L_{X_θ}); (b) log-Darboux/linearization of σ at crossing points of codimension ≥2 (n=2: node normal form c·z_1z_2∂_1∧∂_2 proved in ncd §6–9).

## 6. Statement summary
Proved: Theorem R (reduction), its consequence Σ_{0<k<n}χ(D_k°)=0 under (GEN'), toric reproof of Theorem T without (V),(A), the necessary form of (GEN') (ν_T≠0, hence (R)), smooth-point acyclicity iff r≠1 (given log-Darboux at smooth points).
Computed [V]: roundI_check.py (see §4).
Conjectural/gaps: sufficiency of 'ν_T nowhere vanishing' for non-linear σ; log-Darboux in holomorphic category at smooth/crossing points (GMP real b-Darboux only cited); general-n derivation of the gr_T formula written only in sketch; product-type prediction for non-acyclic strata.
