# Dimension 4 (toric), arithmetic dependence on sigma, unequal residues (2026-11-21)
Legend: [P] proved here by hand (standard facts named) · [C] computed (exact arithmetic) · [V] verified vs independent computation · [K] cited · [?] conjectural.
Scripts (cp2/): toric_hh.py (linear-algebra model), toric_crit.py (closed weight criterion + fan list), toric_test2.py, toric_test4.py, toric_scan4*.py, toric_p2p2.py, toric_generic_check2.py (+ .out files), local_unequal.py, local_unequal_rule.py.
(toric_hh.py now works mod the 61-bit prime 2^61-1; earlier outputs in this file used 1000003 and are marked.)

## 1. Setting: toric log-symplectic structures
X smooth projective toric variety, N=Z^n (n=2k), rays u_i (i in I), D = toric boundary (SNC). A = skew nondegenerate n×n matrix (constant in the log frame E_j=z_j d_j): sigma = (1/2) sum A_ij E_i ^ E_j (torus-invariant, log-symplectic along D). L = O(sum a_i D_i), flat log connection d+rho with rho in M_C (any rho: closed constant log 1-form). Residues r_i = <rho,u_i> - a_i, c_1(L) = -sum r_i [D_i] (consistent: sum <rho,u_i>[D_i] ~ 0). All modules arise this way (H^0(Omega^1(log D)) = M_C) [P, Lemma 4 of ncd_theorem.md].
Generalized Dolbeault complex = C(A;L) = (wedge^b T (x) L, d), identification with J_sigma-GH cohomology: [K] LGSX arXiv:0707.4253 Thm 4.19 (not re-derived).

## 2. Weight criterion (exact formula, any n) [P]
Assume E_1^{a,b}=H^a(X, wedge^b T (x) L)=0 for a>0 (e.g. L ample enough; Bott/Kunneth for products of projective spaces with all m_i >= 1 or >= -dim). Then HH^* = cohomology of the global-section complex, which is T-graded by chi in M:
 G^b_chi = { w in wedge^b N_C : u_i ^ w = 0 for every i with c_i(chi) := <chi,u_i>+a_i = -1 }  (empty if some c_i(chi) < -1),   d = v_chi ^ ,  v_chi = A(chi+rho).
(derivation: z^chi w is a regular section of wedge^b T(x)L along D_i iff c_i >= -1, and if c_i = -1 iff u_i ^ w = 0; under wedge^b sigma^# the log de Rham differential (chi+rho)^ becomes v_chi ^ (Lemma 3 of ncd_theorem.md).)
Write C(chi) = {i : c_i(chi) = -1}, W = span(u_i : i in C(chi)), s = dim W. Then G^• ≅ wedge^{•-s}(N/W) (shifted) and v^ acts by v mod W. Hence
 **(Weight formula)** P_HH(t) = sum over chi in Lambda of t^{s(chi)} (1+t)^{n-s(chi)},  Lambda = { chi in M : c_i(chi) >= -1 for all i,  A(chi+rho) in W(chi) }.
Checks: closed formula == linear-algebra complex on 60 random cases (P2,P1xP1,P4,P2xP2,P1^4) [V]; reproduces all P^2 / P^1xP^1 toric surface tables of earlier notes (triangle: [1,2,4] for Rj_* case, 3 t^2 generic) [C].
Consequences [P]:
 (a) Euler characteristic = #{chi : s(chi)=n} = number of vertices (maximal cones) = chi(X) (one weight per vertex for ample L): the 'RR value' is topological, blind to rho and to L.
 (b) Where classes come from: x := chi+rho. [i] C=∅ (s=0): need A x = 0, i.e. chi = -rho, valid iff rho in M and all r_i <= 0 (c_i(-rho) = -r_i): contribution (1+t)^n = H^*(U) (Rj_* case). [ii] s=n: always satisfied ⇒ the vertex weights: t^n each. [iii] 0<s<n: need A x in W: x in A^{-1}W (dim s), and <x,u_i> = r_i - 1 for i in C (because chi has c_i=-1) -- an affine condition; solution exists/integral only for 'resonances'.
 (c) r_i = 1 resonance: for C with all r_i=1, rank s=n-1: Ann(W) is a rational line and A x in W holds automatically (x in Ann(W) ⇒ <x,Ax>=0). The lattice points on that line within the polytope give classes t^{n-1}(1+t) each: their number = deg(L|_curve)+1 for the toric curve of C. This is the n-dimensional version of the dim-2 resonance 'cohomology sheaves become coherent O_{D_i}-modules' (dims grow linearly in m), e.g. P^2, rho=(1,0): [0,m+2... ] table in section 4.

## 3. Generic sigma (no arithmetic coincidences) [C + P-reasoning]
Claim: for sigma with 'generic' (irrational) A,   Lambda_gen = Vert ∪ Res ∪ {-rho}, where Vert = vertex weights, Res = {chi : rank span(u_i, i in C(chi)) = n-1 and <chi+rho,u_i> = 0 for all i in C(chi)}, and -rho is included iff rho in M and all r_i <= 1.
Reasoning: for rank s<n-1 the condition A x in W cuts out an (irrational) s-dimensional subspace A^{-1}W of M_C; it meets the coset rho+M only at x=0 when A is generic (s even: unique irrational solution unless all pairings vanish; s odd: kernel of the skew s×s pairing is an irrational line). For s=n-1 the subspace condition is automatic (above).
Verified [C, mod 2^61-1, A with entries up to 1e9]: refined prediction == closed criterion on 3626 (fan, line bundle, rho) cases: P^4 (m=1,2), P^2xP^2 (1,2), (P^1)^4 (1,1,1,1),(1,2,1,3), P^1xP^3 (1,1), P^1xP^1xP^2 (1,1,1); rho in {-2..1}^4 and three non-integral rho: **0 mismatches**. (With small integer A, 11/3626 'accidents' appeared; each traced to an integer coincidence like -124 x1 -386 x2 +138(x3+x4)=0.)
Examples (generic A, m=1 on P^4, rho in M, all r_i <= 0):  P = (1+t)^4 + 5 t^4 = [1,4,6,4,6]; rho non-integral: 5 t^4; chi = 5 = chi(P^4). P^2xP^2: (1+t)^4+9t^4=[1,4,6,4,10]; rho=(-1,-1,0,0) (r=(-1,-1,1,0,0,-2): one branch r=1): t(1+t)^3+9t^4=[0,1,3,3,10] ✓.
**Statement for general (non-toric) SNC log-symplectic (X^{2k},D) [?]**: for generic sigma and residues with no r_i=1, HH^*(L) = H^*(X; F) ⊕ ⊕_{p in D_(n)} C[-n]  where D_(n) = points where n branches meet and F=j_{2!}Rj_{1*}L_U as in Thm 2 of ncd_theorem.md. Euler char consistent iff chi(D_k°)=0 for 1<=k<n (strata carry nowhere-vanishing log vector fields) -- true in toric case, not proved in general.

## 4. Dependence on sigma beyond residues (new phenomenon) [C]
Dim 2: nothing (nodes only). Dim 4: HH is NOT determined by (X,D,L,residues). Examples (toric, m=1 on P^4, rho=0, all r_i<=0):
 * sigma with small integer A (seed 1): [1,4,7,6,7]  vs generic [1,4,6,4,6]  (mod 1000003 run).
 * P^2xP^2 with sigma = product (block A): [1,4,12,16,16] = (1+2t+4t^2)^2 exactly the product of the surface results (Kunneth for C(A1;L1)⊗C(A2;L2)) [C: 6 cases match product formula]; generic A: [1,4,6,4,10]. Difference (0,0,6,12,6) = 6 t^2 (1+t)^2 = sum over the 6 codim-2 strata {node of one factor}×(C*)^2 of t^2 H^*(O_tau).
 Mechanism [P]: for |C|=2, Omega_C=(omega(u_i,u_j)) invertible gives a unique x_C(A,r) in A^{-1}W; it is a lattice shift of rho iff an arithmetic condition on A holds; if so the codim-2 stratum O_tau contributes t^2 H^*(O_tau; L|). So classes at strata whose normal log-pair (u_i,u_j) is symplectic for sigma ('nodal strata') appear exactly at arithmetic coincidences.
 Interpretation [?]: HH jumps upward on a countable union of proper analytic subsets of the space of log-symplectic structures (upper semicontinuity of generalized Dolbeault cohomology); the generic value is the minimal one: topological U-part + vertex classes + resonance classes. For P^2xP^2: generic [1,4,6,4,10] <= block [1,4,12,16,16] coefficientwise ✓.
 Resonance growth (dim 2, toric, A=[[0,1],[-1,0]], m=1..4, rho=(1,0)): r=(1,0,-1-m): P=[0,m+2,m+5] (linear in m).

## 5. Local theory at the triple point with unequal residues [C]
Module prod h_i^{s_i} (V = sum s_i X_{log h_i}), sigma=h dz^dw, h=z w (z-w) [local_unequal.py; reduces to local_stalk.py for equal s: sanity ✓]. Stalk of the twisted Lichnerowicz complex at 0, in degrees (h0,h1,h2):
 **Rule** (tested on 533 random triples s_i in (1/6)Z∩[-2,2], s_i != 1; all-integer-with-positive entries untested): stalk = C^4[-2] ⊕ R, R = H^*(U_loc;L_s) if s_1+s_2+s_3 < 2, else 0, where U_loc = C^2∖{three lines} ≃ C* × (P^1∖3 pts):
  all s_i in Z_{<=0}: H^*(U_loc)=(1,3,2) ⇒ stalk (1,3,6);   sum in Z, sum <=1, not all s_i integers: H^*(U_loc;L) = (0,1,1) ⇒ stalk (0,1,5);   otherwise (0,0,4).
 [(0,1,1): central monodromy e^{2 pi i sum} trivial, H^*(C*)=(1,1), H^*(P^1∖3pts;L')=(0,1).] 0 mismatches.
 Compare node: stalk Rj_* part nonzero iff each s_i in Z_{<=0} (torus (C*)^2, per-variable thresholds s_i<1) — for the triple point the threshold is on the *sum* sum s_i d_i < wz+ww=2 (single Euler field). [?] General principle: threshold = weight of the module under the symmetry torus of the germ relative to the log-canonical weight; equal residues: s< lct.
 Consequence [?]: the refined conjecture of cp2_second_notes.md section 4 holds with unequal residues if 'residue s' is replaced by the total residue at each singular point; at a triple point the resonance set is {sum s_i in {2,... } } — consistent with the anomaly at m=-2,-4 for equal s=-m/3 (sum = 2, 4... ) found earlier (sum=2 at s=2/3).
Not done: unequal residues globally (non-toric); cusps/tacnodes have a single branch (no residue freedom) -- see cp2_second_notes.md; two-branch tacnode with unequal residues untested.

## 6. Conjectural general formula for P_HH(t) [?]
For (X^{2k}, D SNC, sigma generic log-symplectic, L with constant residues r_i, none equal to 1, c_1(L)=-sum r_i D_i):
  P_HH(t) = P(H^*(X;F_r)) + #D_(n) t^n,   F_r = j_{2!}Rj_{1*}L_U (Rj_* across branches with r_i in Z_{<=0}, extension by zero across the others).
 Evidence: all toric examples above (3626 cases, but toric ⇒ H^*(X;F) only checked through the weight formula: the claim 'F-part = (1+t)^n if rho in M and all r_i<=0, else 0' i.e. H^*(X;F)=0 when some r_i>=2 or L_U nontrivial); surface Thm 2.
 Needed: independent computation of H^*(X;F) for mixed residues in the toric case (stratified Mayer–Vietoris) to confirm 'F-part = 0 when some r_i>=2': checked indirectly (weight formula gives 0 U-part, matches Euler char); not proved sheaf-theoretically.
 With special sigma: add t^{|tau|} H^*(O_tau; L|_{O_tau}) for each 'symplectic' stratum tau satisfying the integrality condition of section 4.
 With r_i=1 on a rank-(n-1) cone: add t^{n-1}(1+t)(deg(L|_C)+1) for the corresponding curve C (toric case) [P].
