# CP^2 with Poisson cubic: GH line bundles O(m) and generalized Dolbeault cohomology (notes, 2026-11-21)
Code: scratchpad/cp2/poisson.py, table.py (exact linear algebra mod 32003; Fermat and Hesse cubics give identical dims).

## Setup (derived/assumed)
- sigma = Pi_F reduced: Pi^{ij}=eps_{ijk} dF/dx_k on C^3, Euler weight 0, descends to P^2; as section of wedge^2 T=O(3) it is E.grad F = 3F (vanishes exactly on D={F=0}). [derived; standard Bondal-type construction]
- GH bundle for J_sigma <-> Poisson module (Gualtieri 0905.3227: Poisson module defined in Sec 2.1, GH bundle in Sec 4.2; the equivalence is only ASSERTED in its Introduction -- see Update 2). Generalized Dolbeault complex of GH bundle O(m) = hypercohomology of (wedge^b T (x) O(m), dbar + [sigma,.]) [Gualtieri; the identification for O(m) is assumed, not re-derived].

## (i) Which O(m) are GH?  ALL m in Z.  [derived]
- Obstruction class lives in H^0(wedge^2 T)/[sigma,H^0(T)] (+ ker of H^1(T)->H^1(wedge^2T)). Here H^1(T)=0, H^0(T)=sl3 injects (smooth cubic has finite stabilizer), coker dim = 10-8 = 2 (sigma-scaling and j-direction). So obstruction space is C^2; the map Pic(P^2)=Z -> C^2 is a homomorphism, hence O(m) GH for all m or only m=0.
- Explicit Poisson-module structure: {f,s} = Pi(df,ds) for f weight 0, s homogeneous of degree m. Leibniz+Jacobi inherited from Pi on C^3. So obstruction vanishes: every O(m) is a Poisson module / GH. Structure unique up to iso (psi in H^0(T) with [sigma,psi]=0 forces psi=0).
- Hence Pic(J_sigma) = Z (given Gualtieri's H^1-description; not text-verified).
- Literature check: Hitchin arXiv:1105.4775 (eq. 11) 0->T^*->^sigma T->T|_D->0, Prop.8 (variation of L|_D); neither states this result for P^2. Gualtieri 0905.3227 has no Atiyah-class obstruction or P^2 example (fetch says so).

## (ii) Hypercohomology H^k(m) of (wedge T(m), d_sigma)
E_1^{a,b}=H^a(wedge^b T(m)), Bott: T(m)=Omega^1(m+3), wedge^2T(m)=O(m+3).
For m>=-2 all E_1 terms have a=0, so complex is 0->H^0(O(m))->H^0(T(m))->H^0(O(m+3))->0, d_1 = module action / Schouten [Pi,.] (computed explicitly). No higher d_r. [derived+computed]
m=-3: E_1 has three 1-dim terms (2,0),(1,1),(0,2), all total degree 2 => H^2=3. [derived]
m<=-4: by Serre duality H^k(m) = H^{4-k}(-m-6)^* [ASSUMED: delta dual to delta; E_1-level dimensions match].
Result [H0..H4]:
 m=0: [1,0,2,0,0]  (= H^*(P^2 minus D), consistent with log de Rham)
 m=3k, k>=0: [1,0,2,0,0]; other m>=-3: [0,0,3,0,0]
 m<=-6, m in 3Z: [0,0,2,0,1]; other m<=-4: [0,0,3,0,0]
Total Euler characteristic = 3 = chi(P^2) for all m (checked m=-12..12): matches (-1)^n rk(E) chi(M).
H^0 = Casimir sections = C*F^{m/3}: jumps exactly when O(m)=K^{-k}.
Ranks e.g. m=1: d1 ranks (3,12) ; m=3: (9,26); m=6: (27,53).
## Open
- Duality assumption for m<=-4; independent Cech check not done.
- Relation of jump set 3Z to Serre vanishing: for large m, H^0=H^1=0, H^2 = 3 or 2-> NOT vanishing of H^2; GH "Serre vanishing" fails in total degree (E_1 d_1 coker of H^0(T)->H^0(O(m+3)) survives). Need the right (transversal) notion.
- Which refined invariant sees m? chi_b = chi(wedge^b T(m)) does; the jump pattern is mod 3 and not captured by chi.

# UPDATE 2 (verification + explanation of period 3), 2026-11-21
Scripts: cp2/neg_check.py (direct, no duality), cp2/predict.py (compares everything).

## (a1) m<=-4 verified directly [computed]
H^2(P^2,O(k)) = span of Laurent monomials with all exponents <=-1 (Cech); H^2(T(m)) = H^2(O(m+1))^3/E.H^2(O(m)); d_0,d_1 = same sigma-formulas on Laurent monomials projected to all-negative ones. For m=-4..-15, Fermat and Hesse cubic: d1d0=0, d1 kills E-image, and [H0..H4] = [0,0,3,0,0] except m=-6,-9,-12,-15 -> [0,0,2,0,1]. This agrees exactly with the Serre-duality-based table (m<=-4 no longer assumed). m=-3 by hand: all three E_1 terms (2,0),(1,1),(0,2) are 1-dim, total degree 2, no d_1,d_2 possible -> [0,0,3,0,0].

## (a2) What Gualtieri 0905.3227 actually says [cited, fetched]
Poisson module (Sec 2.1), GH bundle = operator dbar_V:C^inf(V)->C^inf(V⊗Lbar) with Leibniz, dbar^2=0 (Sec 4.2); equivalence with Poisson modules for holomorphic Poisson case only asserted in the Introduction. NOT in the paper: J_sigma notation, hypercohomology identification, d_sigma, Pic group/Atiyah-class obstruction, CP^2 example, Lie algebroid L. So earlier statement "confirmed by fetch" was too strong.
The identification I need IS in Laurent-Gengoux--Stienon--Xu, "Holomorphic Poisson manifolds and holomorphic Lie algebroids", arXiv:0707.4253: L = T^{0,1} ⋈ (T^{1,0})^*_pi is the Dirac structure L_{4pi} = -i eigenbundle of the GC structure (Thm 4.21, Lemma 4.22); H^*(A,C) = H^*(T^{0,1}⋈A^{1,0},C) (Thm 4.11) and with coefficients in an A-module E (Thm 4.19), where holomorphic Lie algebroid cohomology = H^*(X,Omega_A^•) (Def 4.10); Remark 4.27 (Stein: Lichnerowicz complex), Lemma 4.18 (finite dim for compact X). Their Remark 4.14 only RAISES the integrability question for T^{0,1}⋈A^{1,0}. Pic(J)=H^1(L_log) claim: NOT text-verified anywhere; only the existence/uniqueness of Poisson-module structure on each O(m) is derived (above).

## (a3) Integrability [cited, partial]
LGSX, "Integration of holomorphic Lie algebroids", arXiv:0803.2031: Thm 3.17 (A holomorphic Lie algebroid integrable iff A_R integrable; s-connected s-simply connected Gamma gets holomorphic structure), Thm 3.22 (holomorphic Poisson manifold integrable iff Re(pi) or Im(pi) integrable as real Poisson), Ex 3.30 (non-integrable holomorphic Poisson structure on C^3). They do NOT treat the complex algebroid T^{0,1}⋈A^{1,0}. For the cubic sigma on CP^2 I found no statement. Derived side remark: at p in D the isotropy of (T^*)_sigma is the 2-dim non-abelian complex Lie algebra [dz,dw]=dw (sigma=z d_z∧d_w locally). Integrability of A=(T^*)_sigma not decided; integrability of L (needed by Hu) open.

## (b) Explanation of the period-3 jumps [derived sketch + numerically verified m=-15..15]
Facts: (1) sigma is log-symplectic: sigma^#:T^*->T has image T(-D)=T(-3); sigma^{-1} in H^0(Omega^2(log D)) is nowhere degenerate, so sigma^#: Omega^1(log D) ≅ T(-log D) and Lichnerowicz subcomplex wedge T(-log D)⊗O(m) ≅ log de Rham complex Omega^•(log D)⊗(O(m),nabla).
(2) F is a Casimir for Pi on C^3 so F^{m/3} is a (multivalued) flat section of O(m)|_U, U=P^2\D. Hence O(m)|_U = rank-1 local system L_m with monodromy exp(2 pi i m/3) around D (pi_1(U)=Z/3 for a smooth cubic) -- period 3. Locally nabla e = -(m/3) dz/z e (residue -m/3), flat section z^{m/3} e.
(3) Local analysis: complex O e -> (dz/z) O e, g e -> (z g' - (m/3) g) dz/z e: on z^n multiplication by (n - m/3). So stalk cohomology on D: (1,1) if m in 3Z_{>=0} (=> Rj_*C), 0 if m<0 or m not in 3Z (=> j_!L_m = Rj_*L_m when monodromy nontrivial).
(4) Quotient Q = wedge T(m)/wedge T(-log D)(m) lives on D: N_D(m)=O_D(m+3) -> O_D(m+3), differential = -(1+m/3)·id (hand computation, sign conventions unchecked), an isomorphism iff m != -3. So for m != -3 full complex ≃ log complex; at m=-3 (the self-dual point under m <-> -m-6) Q has zero differential and contributes H^*(D,O_D)[-1]+H^*(D,O_D)[-2]; exact sequence consistent with [0,0,3,0,0] (checked).
Result (predict.py, 0 mismatches for m=-15..15 vs direct computation):
 m in 3Z, m>=0 : H^*(U,C)   = [1,0,2,0,0]
 m in 3Z, m<=-6: H^*_c(U,C) = [0,0,2,0,1]
 m not in 3Z   : H^*(U,L_m)=H^*_c(U,L_m) = [0,0,3,0,0]  (H^0=H^1=0 since pi_1 finite; Artin vanishing: U affine; chi=3)
 m=-3          : [0,0,3,0,0] (exceptional)
Serre duality m <-> -m-6 exchanges H^*(U,.) and H^*_c(U,.) (Verdier duality).

## Conjectural refined statement [CONJECTURE, not proved]
(C1) Total Euler characteristic is blind to m (= chi(U) = 3); the m-dependence sits in the *Poincare polynomial*, which is governed by the residue r=-m/3 of the induced flat log connection along the type-jumping divisor D: H^*(M,E) = H^*(M, Rj_*L) for r in Z_{<=0}, = H^*(M, j_!L) for r in Z_{>0} (r>=2 plus the self-dual r=1 anomaly), and = H^*(U,L) for r not in Z. I.e. 'Riemann-Roch' for GC structures with log-symplectic type-change locus = a Riemann-Hilbert/Deligne-type statement; only the Euler characteristic chi(U,L)=rk*chi(U) is a numerical formula.
(C2) Serre 'vanishing' in total degree is false here (H^2 stays 2 or 3 for all m>>0); the right statement is *periodic stabilization*: for m>>0, H^*(m) depends only on m mod 3 (equal to H^*(U,L_{m mod 3})).
(C3) Generalization guess: for a log-symplectic holomorphic Poisson surface (X,sigma) with smooth anticanonical D and a line bundle with Casimir-type flat structure, the same dichotomy holds with residue r determined by c_1(E)/c_1(K^{-1}).
Not yet done: rigorous proof of quasi-isomorphism (needs care at points where sign conventions/quotient Q matter), singular D, rank >1.
