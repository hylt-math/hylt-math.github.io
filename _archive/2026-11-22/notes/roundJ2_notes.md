# Round J2 (2026-11-22) — vanishing H^k(U;L_U)=0 (k<n) for no-integer residues; Poisson–Kodaira tests
Legend: [P] proved here · [V] verified by script · [C] cited · [?] conjectural.
Scripts (cp2/): roundJ2_vanish_check.py (exact toric HH), roundJ2_sklyanin_segre.py (exact rational Sklyanin check).

## 1. Theorem V (vanishing) [P]
Hyp.: X compact complex manifold dim n≥1; D⊂X reduced SNC divisor with components D_1..D_s; U=X∖D **affine**; L_U a rank-one local system on U whose monodromy around D_i is e^{-2πi r_i}, with **every r_i∉Z**. (No condition on sums Σ_{i∈I} r_i, no condition on n>2; log-symplectic structure not used.)
Concl.: H^k(U;L_U)=0 for all k≠n; hence dim H^n(U;L_U)=(-1)^n χ(U).
Proof. (a) Stalk of Rj_*L_U at p∈D_I (|I|=k≥1): small polydisc B, U∩B≃(Δ*)^k×Δ^{n-k}≃(S^1)^k, L_U|=⊠ of rank-one local systems on circles with monodromy μ_i=e^{-2πi r_i}≠1. Künneth: H^*((S^1)^k;L)=⊗ H^*(S^1;L_{μ_i}) and H^*(S^1;L_μ)=0 for μ≠1 (H^0=ker(μ-1), H^1=coker(μ-1)). So (Rj_*L_U)_p=0, i.e. Rj_*L_U=j_!L_U (canonical map j_!→Rj_* is iso on stalks over U and both vanish over D).
(b) H^k(U;L_U)=H^k(X;Rj_*L_U)=H^k(X;j_!L_U)=H^k_c(U;L_U) (X compact).
(c) Artin/Andreotti–Frankel: U affine of dim n ⇒ H^q(U;F)=0 for q>n for every local system F (constructible sheaf). Poincaré duality on the oriented 2n-manifold U: H^k_c(U;L)≅H^{2n-k}(U;L^∨)^*, L^∨ again a local system, which vanishes when 2n-k>n, i.e. k<n. With (b): H^k(U;L)=0 for k<n; and k>n by (c) directly. ∎
Role of hypotheses: r_i∉Z for every i is used only in (a); at a stratum with all r_i∈Z the stalk is H^*(T^k) ≠ 0 (this is the source of the jump in Parts II/V). Affineness is used in (c) (fails e.g. if D is empty). The Σ r_i condition that the task allowed for is irrelevant for SNC D (it matters only for non-SNC/non-normal-crossing points, where the local fundamental group is not Z^k — e.g. the triple-point stalk rule of Part II, where Σ over the local Spec enters).
Consequence [P, given Theorem R of Part V]: under Theorem R hypotheses with all r_i∉Z, HH^k=0 for k≠n and dim HH^n = (-1)^nχ(U)+#D_(n) = χ(X)  (n even, χ(U)=χ(X)-χ(D) etc. — this uses χ(X)=χ(U)+χ(D) and the point terms; consistent with Theorem K: P_HH(t)=χ(X)t^n).
Mixed case [?]: if some residues are integers, stalks of Rj_*L_U along D_I vanish unless all r_i (i∈I) ∈Z, so Rj_*L_U is j_! on the open part plus contributions from the "integer strata" only; the vanishing below degree n then depends on those strata (not claimed).

## 2. Exact toric verification [V]  (roundJ2_vanish_check.py; exact arithmetic mod 2^61-1, random nondegenerate A)
Weights ρ non-integer ⇒ r_i=<ρ,u_i>-a_i; Poincaré polynomial of HH (n=4):
- P^4, O(1), r=(1/2,1/3,1/5,1/7,-457/210) all non-integer: (0,0,0,0,5) = χ(P^4)t^4 ✓.
- P^4, O(2), r=(1/3,1/3,1/3,1/3,-10/3): any three of the first four sum to 1∈Z (3-fold point-like intersections with Σr∈Z) ✓ (0,0,0,0,5).
- P^2×P^2, (1,2), r=(1/2,1/3,-11/6,1/2,1/3,-17/6): (0,0,0,0,9) ✓ (r_1+r_2+r_3=0∈Z).
- P^1^4, r=(1/2,-3/2,…): all non-integer, r_1+r_2=-1∈Z: (0,0,0,0,16) ✓.
- P^1×P^3, (1,1), r=(1/2,-3/2,1/3,1/3,1/3,-2) (one integer residue -2 at the last divisor, mixed case): (0,0,0,0,8) ✓ ; P^2×P^2 (1,1) with r_3=-1 integer: (0,0,0,0,9).
All equal χ(X)t^n, as predicted by Theorem V + Theorem R. (Mixed cases also concentrated here — an observation, not a theorem.) Scope: toric, constant-in-log-frame σ, L sufficiently ample (the script's validity condition); not a check of Theorem V for non-toric U.

## 3. Poisson–Kodaira tests
### 3a. P^1×P^1 Segre (m=1, ambient P^3) [V for the pencil statement; ?: covers all (2,2)-curves]
Classical Sklyanin–Feigin–Odesskii quadratic Poisson structure on C^4: {x_0,x_i}=(J_j-J_k)x_jx_k, {x_j,x_k}=x_0x_i ((i,j,k) cyclic in 1,2,3), J=(2,3,7). Exact rational check [V]: Jacobi identity holds (4/4 triples); exactly 2 independent quadratic Casimirs (Q1=-x0²/4+5x1²/4+x2², Q2=x0²/4-x1²/4+x3²), generic rank of π = 2. (My first attempt with J_{jk}=(J_j-J_k)/J_i failed Jacobi: wrong convention; corrected form is the standard one.) Hence every quadric of the pencil Q_λ=Q1-λQ2 is a Poisson subvariety of P^3 (a leaf closure); smooth ones are Segre P^1×P^1, on which the structure is symplectic off the base locus E=Q1∩Q2, which is a smooth elliptic quartic here (diagonal pencil with all 2×2 minors of the coefficient matrix nonzero [V]). So (P^1×P^1, σ_E) embeds Poisson-ly by O(1,1) into a quadratic Poisson structure on P^3 for these J [V: Jacobi/Casimirs exact; the identification "σ|_Q has simple zero exactly along E" is by the rank/leaf argument, not computed]. [?] that every smooth (2,2) curve arises (J has 2 ratios, moduli of E is 1-dim: expected yes, not checked). This is classical (Feigin–Odesskii, Odesskii; also Hua–Polishchuk); not new. Note it is a strongly special σ (log-symplectic along smooth elliptic E); non-generic (2,2) σ (nodal/singular E) not tested.
### 3b. P^2, m=3 (P^9) [not computed]
Setup (as roundE_veronese_poisson.py): 10 coordinates, 45 pairs, dim I_2=55-28=27 ⇒ 1215 unknowns ε, 120 Jacobiator triples × 220 cubic monomials. The dict-based Levenberg–Marquardt of Round E was already judged too heavy at 1215 unknowns; not attempted in this round. Not run ⇒ no evidence for or against PK at m=3 for Fermat; xyz at m=3 is covered by Theorem PK-toric [P] (diagonal quadratic Poisson structure), so xyz is not an independent test. Possible reductions for a future round: use the symmetry group of Fermat (diag (Z/3)^2 acting on ε reduces unknowns ≈1215/9≈135+ invariants), or a pencil/Feigin–Odesskii construction (E⊂P^8 hyperplane section of Veronese; q_{9,1}(E)=Poisson structure on P^8 but the ambient here is P^9 — mismatch, so no immediate classical shortcut).

## 4. Status summary
Proved: Theorem V (all n≥1, no Σr condition, SNC, U affine). Verified: toric exact checks incl. Σr_i∈Z cases; Sklyanin structure ⇒ PK for P^1×P^1 Segre with smooth elliptic E. Conjectural/undone: PK at m=3, non-smooth (2,2) σ, mixed integer residues in general.
