# Log-symplectic surfaces with nodal anticanonical curve: generalized Dolbeault cohomology of GH line bundles
(notes, 2026-11-21; extends cp2_proof_notes.md and cp2_second_notes.md)

Legend: [P] = proved here (by hand; standard facts named), [C] = cited, [V] = verified by script (exact arithmetic) but not proved,
[G] = gap / open.  Scripts: cp2/ncd_cochain_check.py, cp2/ncd_local_weights.py, cp2/ncd_global_check.py.

## 0. Setting and notation

* X compact complex manifold, dim n (n = 2k necessarily). sigma in H^0(X, wedge^2 T) holomorphic Poisson.
* D = reduced divisor, simple-normal-crossings (SNC) or (surface case) with at most ordinary nodes; D_i = components (or branches).
  T_D := T_X(-log D) (a Lie algebroid, anchor = inclusion), B := Omega^1(log D) = T_D^*.
* **log-symplectic**: sigma in H^0(wedge^2 T_D) and sigma^#: B -> T_D is an isomorphism (equivalently omega := sigma^{-1} in H^0(Omega^2(log D))
  non-degenerate, d-closed automatically). Then div(sigma^k) = D, i.e. -K_X = O(D).
  *Surface case* (n = 2): this is just "sigma in H^0(-K_X) with reduced zero divisor D whose only singularities are ordinary nodes".
  Locally sigma = h d1^d2, h = z u (smooth point) or h = z1 z2 u (node), u a unit.
* A := (T^*_X)_sigma = Omega^1 with the Koszul bracket [a,b]_sigma = L_{sigma#a} b - L_{sigma#b} a - d sigma(a,b) and anchor sigma^#
  (a holomorphic Lie algebroid). A -> B (inclusion Omega^1 c Omega^1(log D)) is an injective morphism of Lie algebroids, iso off D.
* L = holomorphic line bundle with an A-module structure (flat A-connection)  =  generalized holomorphic (GH) line bundle for the
  beta-transformed GC structure J_sigma  [Gualtieri 0905.3227 (asserts the equivalence), Laurent-Gengoux--Stienon--Xu 0707.4253 Thms 4.19, 4.21].
* C(A;L) := (wedge^b T (x) L, d_L), d_L = [sigma,.] + V wedge  (Chevalley--Eilenberg complex of A with coefficients in L).
  "Generalized Dolbeault cohomology of (J_sigma, L)"  =  H^*(X; C(A;L)) =: HH^*(L)   [C: LGSX Thm 4.19; identification not re-derived].
  Computed by the spectral sequence E_1^{a,b} = H^a(X, wedge^b T (x) L) => HH^{a+b}.

## 1. Statements

**Theorem 1 (module = log connection; any even n, SNC D).**  Let (X,D,sigma) be log-symplectic and L an A-module (flat A-connection).
(a) In a local frame e, nabla_beta e = Theta(beta) e defines a holomorphic vector field V (Theta(beta) = beta(V)) with [sigma,V] = 0
    ("Poisson vector field"); a change of frame e -> g e changes V by the Hamiltonian field X_{log g}.
(b) V is automatically a *logarithmic* vector field: V in T_D. Hence the A-module structure extends uniquely to a B-module structure, i.e. (via the
    Lie algebroid isomorphism sigma^#: B ~ T_D) to a flat connection nabla^log: L -> Omega^1(log D) (x) L with logarithmic poles.
(c) The residue of nabla^log along each branch D_i is a constant r_i in C, and  c_1(L) = - sum_i r_i [D_i]  in H^2(X;C).
(d) Locally at a point of D (SNC; or node) there is a frame with nabla^log e = sum_{i} r_i dlog z_i e.
(e) Under (b) the complex C(B;L) = (wedge^b T_D (x) L, d_L) is a subcomplex of C(A;L), isomorphic via wedge^b(sigma^#) to the logarithmic
    de Rham complex DR_log(L) = (Omega^b(log D) (x) L, nabla^log).

**Theorem 2 (surface case; the Riemann--Roch/Serre-type theorem).** n = 2, D as above with mu = number of nodes (a node of an irreducible D counts too),
L a GH line bundle with residues r_i (constant along each branch). Assume r_i != 1 for every branch.  Put
I_* = {i : r_i in Z_{<=0}},  I_! = {i : r_i not in Z_{<=0}},  X' = X \ union_{i in I_!} D_i, j_1: U = X \ D -> X', j_2: X' -> X, L_U = local system of flat sections on U, and
   F := j_{2!} R j_{1*} L_U      ("Rj_* across D_i, i in I_*, and extension by zero across D_i, i in I_!").
Then
   HH^k(L)  =  H^k(X; F)  (+)  C^mu  [only for k = 2].
In particular
 (i) if all r_i not in Z_{>0} (e.g. all r_i in C \ Z, or in Z_{<=0}): HH^*(L) = H^*(U; L_U) + mu in degree 2;
 (ii) if all r_i not in Z_{<=0}: HH^*(L) = H^*_c(U; L_U) + mu in degree 2;
 (iii) (Euler characteristic) chi(HH^*(L)) = chi(U) + mu = chi(X) for every such L (equal to the Riemann--Roch value (-1)^n rk(L) chi(X) of the full complex);
 (iv) (duality symmetry of the dimensions) with L' = L^v (x) K_X^2, whose residues are r_i' = 2 - r_i: dim HH^k(L) = dim HH^{4-k}(L'),
      I_* <-> I_!  (Verdier/Poincare duality exchanges Rj_* and j_!);
 (v) (periodic stabilisation = "Serre vanishing" replacement) assume U affine (e.g. D ample) and L_0 a GH line bundle with residues rho_i = -a_i, a_i in Q_{>0}
      ("c_1(L_0) = sum a_i [D_i] is a positive rational combination of boundary classes"); let N = lcm of the denominators of a_i. For every m >= 1:
      HH^k(L_0^m) = 0 for k >= 3 and HH^*(L_0^m) = H^*(U; L_U^{(m)}) + mu[2] depends only on m mod N (when X is simply connected).
      (For D ample irreducible, P^2/cubic: m >= 1.)
 (vi) For L = K_X (all r_i = 1): if h^{p,q}(X) = 0 for p != q, then HH^k = 0 for k != 2 and dim HH^2 = chi(X).
      (This is the excluded value r_i = 1; the only L with r_i = 1 for all i and c_1 = c_1(K_X).)

**Resonance conditions (what is needed where).**
 R1: r_i != 1 for all branches  <=>  quotient complex Q := C(A;L)/C(B;L) has only the node contributions (otherwise Q has infinite-dimensional cohomology sheaves).
 R2: r_i not in Z_{>0} for all i  <=>  DR_log -> R j_* L_U is a quasi-isomorphism (Deligne);  r_i not in Z_{<=0} for all i <=> j_! L_U -> DR_log is a q.i.
 For all-equal residues r (the case in all computed tables) exactly one of R2's alternatives always holds: r in Z_{>0} gives j_!, otherwise Rj_*.
 (Mixed residues give F = j_{2!} R j_{1*} L_U, as in Theorem 2.)

## 2. Proofs

### Lemma 1 (flatness = Poisson vector field)  [P]
For the frame e put Theta(beta) = coefficient of nabla_beta e. Then nabla_a nabla_b e = (sigma#a)(Theta b) e + Theta(a)Theta(b) e, so flatness
[nabla_a,nabla_b] = nabla_{[a,b]_sigma} is equivalent to  sigma#a(Theta b) - sigma#b(Theta a) = Theta([a,b]_sigma),
i.e. Theta is a 1-cocycle of the Lichnerowicz complex: Theta(beta) = beta(V), [sigma,V] = 0 i.e. L_V sigma = 0.
Frame change e' = g e: Theta'(a) = Theta(a) + sigma#a(g)/g, i.e. V' = V - X_{log g}-type Hamiltonian term. In dim 2: with a = V^1, b = V^2, flatness for (dz1,dz2) reads
h (a_1 + b_2) = h_1 a + h_2 b, i.e. V(h) = h div V.
Differential: d_L(f e) = (-sigma#(df) + f V) e on C^0 and, for c = X (x) e,
  (d c)(dz1,dz2) = h(p_1+q_2) - h_1 p - h_2 q + q a - p b     (X = p d1 + q d2, a = Theta(dz1), b = Theta(dz2)).

### Lemma 2 (V is logarithmic; any n, SNC)  [P]
L_V sigma = 0 implies L_V sigma^k = 0 (n = 2k), sigma^k = f d_1 ^ ... ^ d_n with f = (unit) z_{1}...z_{s} (local equation of D, reduced). L_V(f d_1^...^d_n) = (V(f) - f div V) d_1^..^d_n = 0,
so V(f) in (f). For f = z_1 ... z_s: V(f)/f = sum_i V(z_i)/z_i is holomorphic; the summand i has poles only along {z_i = 0}, so each V(z_i)/z_i is holomorphic (restrict to the generic point of D_i).
Hence V(z_i) in (z_i), i.e. V in T_D = Der(-log D). So Theta extends from A = Omega^1 to B = Omega^1(log D): nabla_beta e := beta(V) e, beta in B. Flatness extends (identity between holomorphic sections, true on a dense open).
Together with the Lie algebroid isomorphism sigma^#: B -> T_D (below) this is Theorem 1(a),(b).

### Lemma 3 (sigma^# is an isomorphism of Lie algebroids B -> T_D)  [P, standard]
sigma is Poisson on the Lie algebroid T_D (sigma in wedge^2 T_D, [sigma,sigma] = 0) and non-degenerate; then B_sigma := (T_D^*)_sigma is a Lie algebroid, and
sigma^# is bracket preserving iff omega = sigma^{-1} is d_{T_D}-closed; on U, omega is a holomorphic 2-form with inverse Poisson, hence closed on U; closedness of a section of Omega^3(log D) on a dense open gives d omega = 0. Cf. Gualtieri--Li (IMRN 2014), Pym (2018), Goto (2016) [C; background].
Consequently a B-module = a T_D-module = a flat logarithmic connection.

### Lemma 4 (residues, local frame, c_1)  [P / C]
nabla^log e = theta e, theta in Omega^1(log D) closed (flatness). Near a smooth point or node write theta = sum_i theta_i dz_i/z_i + (holomorphic part). Closedness gives theta_i|_{D_i} constant r_i (restrict d theta to D_i: d_{z_j} theta_i must be holomorphic).
Then theta - sum r_i dlog z_i is a closed *holomorphic* 1-form, = dg; the frame e' = e^{-g} e satisfies nabla^log e' = sum r_i dlog z_i e' (Theorem 1(d)).
c_1(L) = - sum r_i [D_i]: Esnault--Viehweg (Invent. Math. 86 (1986), Sect. 2) / Deligne (LNM 163, Ch. II)  [C]. Sign check: O(D) with canonical section flat has residue -1, c_1 = [D].
Number of modules on a given L: torsor under H^0(Omega^1(log D)) = ker(C^c -> H^2(X)) (Deligne), dimension c - rank <[D_i]>. For irreducible D uniqueness; reducible D has an affine family of residue vectors.

### Lemma 5 (stalk cohomology of DR_log and Deligne's comparison)  [P]
In the frame of Lemma 4, DR_log at a point of D_I (|I| = s) is the Koszul complex of the commuting operators z_i d_{z_i} + r_i (i in I) tensored with the ordinary de Rham complex in the remaining variables.
On monomials z^a: z_i d_i + r_i = a_i + r_i (scalar). Division by a_i + r_i != 0 preserves convergence (|a_i + r_i| >= c > 0 for all but finitely many a, and the finitely many others are nonzero or give the cohomology).
Hence stalk cohomology = wedge^*(C^s) (dim 2^s, Euler characteristic 0) iff -r_i in N for all i in I (i.e. r_i in Z_{<=0}), and 0 otherwise.
The stalk of Rj_*L_U at the same point is H^*((C^*)^s; L) = wedge^*(C^s) iff all monodromies exp(2 pi i r_i) = 1 (all r_i in Z), else 0.
The natural map DR_log -> DR(L(*D)) ~ Rj_*L_U is therefore a q.i. iff no r_i is a positive integer (strata of single branches suffice)  [Deligne II.3.13; also P here].
j_! L_U -> DR_log (extension by zero of flat sections is holomorphic) is a q.i. iff every stalk of DR_log on D vanishes iff no r_i in Z_{<=0}.
Mixed case: restricted to X' the log complex is Rj_{1*} L_U (no positive integer residue among I_*); the cone of j_{2!}j_2^* DR_log -> DR_log has stalks 0 on union_{I_!} D_i
(stalk of DR_log is zero there because some r_i not in Z_{<=0}); hence DR_log ~ j_{2!} R j_{1*} L_U = F.

### Lemma 6 (the quotient complex Q; surface case)  [P, verified: ncd_cochain_check.py]
Q := C(A;L)/C(B;L) is supported on D: Q^1 = (T/T_D)(x)L, Q^2 = (wedge^2 T/wedge^2 T_D)(x)L, Q^0 = 0.
 * Smooth point, h = z u: Q^1 = d_z (x) O_D, Q^2 = d_z^d_w (x) O_D and  d_Q(p) = -u (1 - r) p|_D   (from the formula of Lemma 1 with a = theta_2 h, b = -theta_1 u, theta_1|_D = r).
   So Q is acyclic at smooth points iff r != 1.
 * Node, h = z1 z2 u: Q^1 = O_{D_1} d_1 (+) O_{D_2} d_2, Q^2 = O_D = O/(z1 z2), and
        d_Q(p,q) = -u [ (1 - r_1) z_2 p + (1 - r_2) z_1 q ]  mod z_1 z_2.
   For r_1, r_2 != 1 this is injective with image u m_D = m_D (m_D = functions on the node vanishing at p), so H^1(Q)_p = 0 and H^2(Q)_p = O_D / m_D = C.
 Hence for r_i != 1: Q ~ (+)_{nodes p} C_p[-2] in the derived category of sheaves of C-vector spaces.
 Check: ncd_cochain_check.py verifies d_1 d_0 = 0 and the formula for d_Q with random polynomial u, g, p, q, r_i (20 trials each, smooth and node): all pass.
 If some r_i = 1: Q has cohomology sheaves O_{D_i}-modules (infinite dimensional stalks): reduction fails (only handled for L = K_X, Prop 8).

### Lemma 7 (the connecting morphism vanishes)  [P modulo log-Moser normal form; V local computation by script]
The distinguished triangle  C(B;L) -> C(A;L) -> Q -> C(B;L)[1]  has connecting morphism in Hom(Q, DR_log[1]) = (+)_p H^3_p(DR_log) (local cohomology at the nodes, computed in the derived category of sheaves of C-vector spaces).
Claim: each component e_p = 0.
Normal form: near a node, sigma can be put in the form z_1 z_2 d_1^d_2 (and nabla^log e = r_1 dlog z_1 + r_2 dlog z_2): omega = (1/u) dlog z_1 ^ dlog z_2 and
omega_t = (1-t) omega_0 + t omega_1 (omega_0 = standard) are log-symplectic near p when u(0) = 1; omega_1 - omega_0 = d alpha, alpha in Omega^1(log D) (log Poincare lemma: H^2(Omega^*(log D))_p = C dlog z_1 ^ dlog z_2);
the time dependent log vector field X_t, i_{X_t} omega_t = -alpha, is tangent to D and vanishes at p, so its flow preserves D and gives phi^* omega_1 = omega_0 (log Moser; cf. Pym, Gualtieri--Li)  [C-sketch, not written out in full].
Weight argument in the model: all complexes are Z^2-graded by gamma (monomial z^gamma times E_I, E_i = z_i d_i) and the differentials are
   d_0 z^gamma = lam_2 z^gamma E_1 - lam_1 z^gamma E_2,   d_1(x E_1 + y E_2) z^gamma = (lam_1 x + lam_2 y) z^gamma E_12,   lam_i = gamma_i + r_i.
RGamma_p of a complex of free O-modules is computed by H^2_p(O) = span{z^-a : a >= 1} termwise (Laurent tails). Local cohomology of C(A;L): present elements  1: gamma <= -1;  E_1: (gamma_1 <= -2, gamma_2 <= -1);
E_2: (-1,-2 swapped); E_12: gamma <= -2.  Local cohomology of C(B;L): all four elements for gamma <= -1.
H^2_p(Q) = C sits at the single weight gamma = (-1,-1) (class of z^{-1} e = z_1^{-1} z_2^{-1} ... ); H^3_p(DR_log) lives only at weights gamma = (-r_1,-r_2) (where lam = 0), which equal (-1,-1) iff r_1 = r_2 = 1.
Weight preservation of the connecting map => e_p = 0 whenever (r_1,r_2) != (1,1). Convergence is harmless: all maps are diagonal on monomials.
Script ncd_local_weights.py (exact arithmetic, weights |gamma_i| <= 8, 78 residue pairs (r_1,r_2) with entries in {-3..3, +-1/2, 1/3, -2/3, 5/2}, all with r_i != 1):
  stalk cohomology of Q = [0,0,1]; local-cohomology cone = H^2_p (one class); and the map H(LOG) -> H(FULL) is injective on cohomology (equivalently all connecting maps vanish): 0 violations.
  (For r = (1, anything) the stalks are infinite dimensional: window truncation shows growth; for r = (1,1) the map is not injective: connecting map non-zero. This is the resonance.)
Splitting: Q ~ (+)_p C_p[-2] (Lemma 6) and e = (e_p) = 0 give  C(A;L) ~ DR_log (+) (+)_p C_p[-2]  in D^b(C_X); take RGamma(X;.).

### Proof of Theorem 2  [P modulo the items flagged above]
Lemmas 1-4 reduce to the log complex; Lemma 5 identifies DR_log ~ F; Lemmas 6-7 give the splitting, hence HH^k = H^k(X;F) + (C^mu if k = 2).
(i),(ii): F = Rj_*L_U or j_!L_U, RGamma(X;j_!L_U) = RGamma_c(U;L_U) (X compact).
(iii): chi(X;F) = sum over strata chi_c(S) chi(F_x): stalks on D have Euler characteristic 0 (wedge^*(C^s) or 0), so chi(X;F) = chi_c(U) = chi(U) = chi(X) - chi(D).
     For D anticanonical with at most nodes: omega_D = (K_X + D)|_D = O_D, so chi(O_D) = 0 = chi(O_{D~}) - mu, hence sum (2-2g~_j) = 2 mu and chi_top(D) = sum(2 - 2 g~_j) - mu = mu.  So chi(U) + mu = chi(X).
     (Check: for SNC D: chi(U) = integral c_2(T_X(-log D)) = chi(X) - sum_{i<j} D_i.D_j = chi(X) - mu, using c_1(T_D) = 0.)
     Also equals the Riemann--Roch value (-1)^n rk chi(X) = chi(X) of the full complex (Section 4 of the earlier notes: sum_b (-1)^b chi(wedge^b T (x) L) = integral ch(L) Td(T) prod(1 - e^{x_i}) = (-1)^n rk(L) c_n(T)[X]).
(iv): Serre duality for the E_1-terms: (wedge^b T (x) L)^v (x) K = Omega^b (x) L^v (x) K = wedge^{2-b}T (x) L^v K^2, so the dual complex is C(A; L^v K^2) shifted; K_X is an A-module with residues 1 (c_1(K_X) = -[D]), so r' = -r + 2.
     We do not prove duality of HH itself; we verify that the closed formula is symmetric: Verdier duality D(j_{2!}Rj_{1*}L_U) = Rj_{2*} j_{1!} L_U^v [4] (swap I_* <-> I_!), L_U^v (x) K_U^2 = L_U^v (K|_U carries the trivial flat structure: flat section omega = sigma^{-1}), and r in Z_{<=0} <-> 2-r in Z_{>=2} (r = 1 excluded).
     Hence dim HH^k(L) = dim HH^{4-k}(L') follows from the formula and Poincare duality H^k_c(U;L) ~ H^{4-k}(U;L^v)^*.  [P given the formula; independent proof of duality: G]
(v): m >= 1 gives r_i = -m a_i < 0, so r_i != 1 and no r_i in Z_{>0}: F = Rj_*L_U^{(m)}. L_U^{(m)} = L_0|_U^{(m)} has monodromy exp(-2 pi i m a_i) around D_i, depends only on m mod N; for X simply connected pi_1(U) is generated by meridians (abelianisation), so the whole local system depends on m mod N. U affine => H^k(U; L) = 0 for k > 2 (Artin vanishing).
(vi) = Prop 8 below.

### Proposition 8 (r_i = 1: L = K_X)  [P]
For L = K_X, wedge^b T (x) K_X = Omega^{2-b}, so E_1^{a,b} = H^{2-b,a}(X) in total degree a + b = 2 + (a - p), p = 2 - b. If h^{p,q} = 0 for p != q, then E_1 is concentrated in total degree 2; d_r changes total degree by 1, so the spectral sequence degenerates:
HH^k = 0 for k != 2 and dim HH^2 = sum_p h^{p,p} = chi(X). (P^2: 3, P^1 x P^1: 4: matches the m = -3 and (-2,-2) tables.)

## 3. Verification against all computed data  [V]
cp2/ncd_global_check.py compares Theorem 2 (for equal residues r = -m/k, k = 3 on P^2, k = 2 on P^1 x P^1, plus Prop 8 at r = 1) with the exact-linear-algebra tables of
cp2/sing_out.txt and cp2/p1p1_out.txt. Inputs b_1(U) = c - rank<[D_i]> (Gysin), chi(U) = chi(X) - mu, b_2 = chi(U) - 1 + b_1, b_3 = b_4 = 0 (U affine).
Result: **196 values of m over 8 examples, 0 mismatches**:
  P^2, m = -15..15: smooth cubic, nodal cubic (mu = 1, irreducible), conic + secant line (2 nodes), triangle (3 nodes);
  P^1 x P^1, m = -9..8: smooth (2,2)-curve, two transverse (1,1)-curves (2 nodes), four lines (4 nodes), (1,1)+(1,0)+(0,1) (3 nodes).
Local checks: ncd_cochain_check.py (formulas of Lemma 1, 6) and ncd_local_weights.py (Lemma 7) as above.
Not covered by the theorem (and visible in the data): cuspidal cubic, conic + tangent line (tacnode), concurrent lines (triple point) and non-reduced D (see cp2_second_notes.md for the conjectural local theory with spectral numbers).

## 4. Gaps and caveats  [G]
 G1. The identification "generalized Dolbeault complex of (J_sigma, L) = C(A;L)" is cited (LGSX 0707.4253 Thm 4.19; Gualtieri 0905.3227 only asserts GH = Poisson module), not re-derived.
 G2. H^1(U; L_chi) = 0 for non-trivial rank one L_chi was assumed in the "r not in Z" rows of the check. Justified for P^2 with nodal D: pi_1(U) is abelian (Fulton, Ann. Math. 111 (1980); Deligne, Sem. Bourbaki 543), and H^*(abelian group; non-trivial character) = 0 for finitely generated abelian groups of this type. For P^1 x P^1 it is only consistent with the data.
 G3. Vanishing in degrees > 2 uses "U affine" (D ample) — true in all examples, not in general (then up to degree 4).
 G4. Log-Moser normal form at nodes is sketched, not written out; also holomorphic vs. formal: weight arguments use that all operators are diagonal on monomials (fine for the sheaf-level statements, convergence of Laurent tails in local cohomology).
 G5. Higher dimension (n >= 4): Lemmas 1-5 hold (SNC, any n); Q analysis needs the log-Darboux normal forms at deeper strata; for strata of 'Darboux type' (sigma = sum z_i d_{z_i}^d_{w_i} + symplectic) the same filtration (tensor product of one-pair complexes) shows Q_J acyclic when some r_i != 1 in J; strata with non-isotropic kernel of the anchor (toric type z_i z_j d_i^d_j, as the node here) contribute skyscraper-type terms. Not carried out.
 G6. r_i = 1 on only some branches (unequal residues; possible only for reducible D with relations among the [D_i]): not treated. Equal residues with r = 1 is Prop 8 (needs L = K_X).
 G7. Non-nodal singular points of D (cusp, tacnode, triple point), non-reduced D: only conjectures (cp2_second_notes.md).
 G8. Unequal residues for reducible D were not tested numerically (the tables use the symmetric member of the affine family).
 G9. Serre duality of HH itself (not only of the closed formula) is not proved.
 G10. Pic(J_sigma) = H^1(L_log): not used here. The theorem only needs: GH line bundle = Poisson module (Gualtieri).

## 5. Summary of the Riemann--Roch / Serre-vanishing content (what the theorem says in words)
 * "Riemann--Roch": the total Euler characteristic is chi(X) (topological, blind to c_1(L)); the c_1(L)-dependence is in the Poincare polynomial and is governed by the residues r_i = coefficient of -c_1(L) in the boundary classes through the dichotomy Rj_* (r_i in Z_{<=0} or non-integer) / j_! (r_i in Z_{>=2}), with each node adding one class in degree 2.
 * "Serre vanishing": for boundary-positive L_0 the groups HH^k(L_0^m), m >= 1, vanish for k >= 3 (U affine) and are periodic in m; no vanishing in degree 2 (H^2 >= chi(X) - ...): vanishing holds only for degrees above the complex dimension.
 * "Kodaira embedding": not addressed here (GH sections of L_0^m are the Casimir sections of the Poisson module: HH^0 = H^0(U;L_U) = flat sections on U that are holomorphic at D: nonzero iff trivial monodromy and r_i in Z_{<=0}).

## References
 Deligne, Equations differentielles a points singuliers reguliers, LNM 163 (1970), Ch. II (Prop. 3.13, Thm 3.?; numbering to be checked).
 Esnault--Viehweg, Logarithmic de Rham complexes and vanishing theorems, Invent. Math. 86 (1986) 161-194.
 Gualtieri, Generalized complex geometry, Ann. Math. 174 (2011); Gualtieri, Branes on Poisson varieties / 'Poisson modules' arXiv:0905.3227 (GH bundles = Poisson modules, as asserted in its introduction).
 Laurent-Gengoux--Stienon--Xu, Holomorphic Poisson manifolds and holomorphic Lie algebroids, IMRN 2008, arXiv:0707.4253 (Thms 4.11, 4.19, 4.21).
 Gualtieri--Li, Symplectic groupoids of log symplectic manifolds, IMRN 2014; Pym, Constructions and classifications of projective Poisson varieties, Lett. Math. Phys. 108 (2018); Goto, Unobstructed deformations of generalized complex structures induced by C^infty logarithmic symplectic structures, J. Math. Soc. Japan (2016).
 Fulton, On the fundamental group of the complement of a node curve, Ann. Math. 111 (1980); Deligne, Le groupe fondamental du complement d'une courbe plane n'ayant que des points doubles ordinaires est abelien, Sem. Bourbaki 543 (1979/80).
 (Bibliographic details of Gualtieri--Li, Pym, Goto, Deligne numbering: from memory — to be checked before use.)


---
# Round 3 (2026-11-21): closing gaps G2, G4, G9 (appendix; earlier text kept unchanged)

Legend as above. Script: cp2/serre_dual_check.py (exact, pure Python).

## 6. Local normal form at a node and a rigorous version of Lemma 7  (closes G4)

**Correction to Lemma 7's sketch.** The invariant u(0)=:c need not be 1 (the coordinate scalings z_i -> lambda z_i do not change c; c is a local invariant of
the log-symplectic structure: Res Res omega = 1/c). The normal form is sigma = c z1 z2 d1^d2 with c a non-zero constant.

**Proposition 11 (holomorphic log-Moser at a node)  [P].**  Let omega = sigma^{-1} = (1/u) dlog z1 ^ dlog z2 near p (u unit, u(0)=c). Then there is a biholomorphism phi,
phi(p)=p, preserving each branch {z_i=0}, with phi^* omega = (1/c) dlog z1^dlog z2.
Proof. omega_0 := dlog z1^dlog z2, omega_t := (1/c + t k) omega_0, k := 1/u - 1/c, k(0)=0, so omega_t = g_t omega_0 with g_t a unit near p for all t in [0,1];
d omega_t = t dk^omega_0 = 0 (dz_i ^ dlog z_i = 0). Write k = sum k_{ab} z1^a z2^b; put
 alpha := sum_{a>=1,b>=0} (k_{ab}/a) z1^a z2^b dlog z2  -  sum_{b>=1} (k_{0b}/b) z2^b dlog z1  (holomorphic log 1-form; coefficients |1/a|<=1 so it converges).
Since d(z^{ab} dlog z2) = a z^{ab} omega_0 and d(z2^b dlog z1) = -b z2^b omega_0, we get d alpha = k omega_0.
The map  T_D -> Omega^1(log D), X -> i_X omega_t  is an isomorphism (i_{z1 d1} omega_t = g_t dlog z2, i_{z2 d2} omega_t = -g_t dlog z1);
let X_t := -(i_. omega_t)^{-1} alpha  in T_D = z1 A d1 + z2 B d2 (holomorphic in (t,z)). X_t is tangent to both branches and vanishes at p, so its flow
phi_t exists on a smaller neighbourhood for t in [0,1], preserves D, and  d/dt phi_t^* omega_t = phi_t^*( d i_{X_t} omega_t + k omega_0 ) = phi_t^*(-d alpha + k omega_0) = 0.
Hence phi_1^* omega_1 = omega_c. QED.
[cf. Pym 2018, Gualtieri-Li 2014 for log-Darboux/Moser in general; the above is self-contained in the surface/node case.]
Combined with Lemma 4 (applied in the new coordinates w: Lemma 4 only used that D = {w1 w2 = 0}), we may assume
  sigma = c z1 z2 d1^d2,  nabla^log e = r1 dlog z1 + r2 dlog z2   (r_i the constant residues).
Then, with lambda_i = gamma_i + r_i, the complexes C(B;L) (= DR_log) and C(A;L) are exactly the weight-graded models of Lemma 7 with all differentials multiplied by the constant c.

**Lemma 7' (the connecting morphism vanishes)  [P].**  Let e_p in Hom_{D(C_X)}(C_p[-2], DR_log[1]) = H^3_p(X; DR_log) be the p-component of the connecting morphism Q -> DR_log[1]
(Q ~ (+)_p C_p[-2] by Lemma 6). Then e_p = 0 whenever (r1,r2) != (1,1).
Proof. e_p = delta(1), delta: H^2_p(Q) -> H^3_p(DR_log) the connecting map of the triangle RGamma_p(B) -> RGamma_p(A) -> RGamma_p(Q) -> .
Compute everything termwise with local cohomology (analytic = algebraic local cohomology for coherent sheaves; differential operators act on the Laurent-tail modules).
 (a) H^i_p of a free O-module O.eps is H^2_p(O) = (+)_{gamma<=-1} C z^gamma eps (i=2 only). Torus weights: wt(z^beta d_I) = beta - sum_{i in I} e_i, wt(z^gamma E_I)=gamma, E_i = z_i d_i.
     All differentials preserve weight (sigma = c z1 z2 d1^d2 has weight 0).
 (b) H^*_p(DR_log) = the Koszul complexes of (c lambda_1, c lambda_2) on span{z^gamma E_I}, gamma<=-1, shifted by 2. A weight-gamma Koszul complex is acyclic unless
     lambda_1 = lambda_2 = 0, i.e. gamma = -r, which is allowed only if r1, r2 are positive integers; then its cohomology has dims 1,2,1 in total degrees 2,3,4.
     So  H^3_p(DR_log) is concentrated in weight -r (r1,r2 in Z_{>=1}) and is zero otherwise.
 (c) H^2_p(Q): Q^1 = O_{D1} d1 (+) O_{D2} d2, Q^2 = O_D d12, d_Q(p d1 + q d2) = -c[(1-r1) z2 p + (1-r2) z1 q] d12.
     H^1_p(O_{D1}) = span{z2^{-k}}_{k>=1}, similarly for D2, and H^1_p(O_D) = span{z1^{-k}, z2^{-k}}_{k>=1} (+) C.[class of (c1,c2) with c1 != c2]  (from 0->O_D->O_{D1}+O_{D2}->C_p->0; this extra class has beta = (0,0)).
     (Q^j are depth-one, so only H^1_p occurs; total degrees 2 (from Q^1) and 3 (from Q^2).)
     In weight (-1,-1): Q^1 has the two classes z2^{-1} d1 and z1^{-1} d2, Q^2 has the extra class; d_Q maps (x,y) -> -c[(1-r1)x - (1-r2)y]; for (r1,r2) != (1,1) it is onto, kernel is 1-dim.
     In all other weights d_Q is an isomorphism Q^1 -> Q^2 (weights (-1,-k) / (-k,-1), k>=2: z2^{-k}d1 -> -c(1-r1) z2^{-k+1}d12, with 1-r1 != 0).
     Hence H^2_p(Q) = C, located in weight (-1,-1), and H^3_p(Q)=0 (consistent with Q ~ C_p[-2]).
 (d) delta preserves weights; weight(-1,-1) does not occur in H^3_p(DR_log) unless -r = (-1,-1). Hence delta = 0 for (r1,r2) != (1,1), e_p = 0. QED
 Remark: for r in Z_{>=2}^2, H^3_p(DR_log) = C^2 != 0 (the j_! case), so e_p = 0 is a genuinely non-topological statement there; it holds only because of the torus grading.
 Consequence: C(A;L) ~ DR_log (+) (+)_p C_p[-2] in D^b(C_X); this closes G4 (the weight argument no longer relies on a "sketched" normal form; the script ncd_local_weights.py remains a consistency check).
 [Sanity: the weight bookkeeping in (c) differs from the sketch in Lemma 7 in that the extra class of H^1_p(O_D) is needed.]

## 7. Vanishing of H^0, H^1 of rank-one local systems on U  (closes G2 for all 8 examples)

**Proposition 12  [P/C].** X smooth projective surface, D reduced normal-crossings divisor, U = X \ D, chi: pi_1(U) -> C*, L_chi the rank-one local system.
 (a) H^0(U;L_chi) = 0  iff  chi != 1.  [P: flat sections = invariants]
 (b) If pi_1(U) is abelian and chi != 1 then H^*(U;L_chi) vanishes in degrees 0 and 1; in fact H^1(U;L) = H^1(pi_1;L) = 0.  [P: for G = Z^r x F finite, chi nontrivial: either chi|_F != 1 (then H^*(G;C_chi)=0 by LHS since F-invariants vanish and H^{>0}(F;C)=0), or chi|_{Z^r} != 1 (Kunneth, H^*(Z;C_t)=0 for t != 1).]
 (c) [C/P] Unitary criterion: let chi be unitary, Lbar the Deligne extension (residues r_i' in [0,1), c_1(Lbar) = -sum r_i' [D_i] torsion-free class), then (Timmerscheidt, Math. Ann. 277 (1987) 247; Esnault-Viehweg 1986)
       H^1(U;L_chi) = H^0(X, Omega^1(log D) (x) Lbar)  (+)  H^1(X, Lbar).
     Via 0 -> Omega^1_X -> Omega^1(log D) -> (+) nu_* O_{D~_i} -> 0 one gets vanishing if  H^1(X,Lbar)=0,  H^0(Omega^1_X (x) Lbar)=0  and  deg(Lbar|_{D~_i}) < 0 for all components.
 (d) [C] (Arapura, J. Alg. Geom. 6 (1997) 563, Thm 1.2) The loci {chi : H^i(U;L_chi) != 0} are finite unions of torsion-translated subtori. Hence if H^1(U;L_chi)=0 for every torsion chi != 1, then H^1(U;L_chi) = 0 for all chi != 1.
 Applicability to the 8 examples (all verified in this round, hand arguments):
   P^2, D nodal curve (smooth cubic, nodal cubic, conic+secant, triangle): pi_1(P^2 \ D) abelian (Fulton, Ann. Math. 111 (1980); Deligne, Sem. Bourbaki 543) => (b).  [C]
   P^1xP^1, four lines: U = C* x C*, pi_1 = Z^2 abelian.  [P]
   P^1xP^1, (1,1)+(1,0)+(0,1): U = C^2 \ {xy=1} = P^2 \ (conic u secant)  [coordinates (x,y), lines at infinity] => abelian by Fulton-Deligne.  [P/C]
   P^1xP^1, smooth (2,2): H_1(U)=Z/2, characters {1, sign}; r'=1/2, Lbar = O(-1,-1): H^1(X,Lbar)=0, Omega^1_X(x)Lbar = O(-3,-1)+O(-1,-3) no sections, deg(Lbar|_D) = -4 < 0 => (c).  [P]
   P^1xP^1, two transverse (1,1)-curves: H_1(U) = Z^2/(1,1) = Z; unitary torsion characters have r_1'+r_2' = 1, Lbar = O(-1,-1), degrees on C_i = -2 < 0, as before => H^1=0 for torsion chi != 1; by (d) for all chi != 1.  [P/C]
 Remark (the exact condition in general): H^1(U;L_chi) = 0 iff chi is not in the first characteristic variety V^1(U) = {chi : H^1(U;L_chi) != 0}. V^1 may contain nontrivial points when D has non-nodal singularities
 (e.g. three concurrent lines; Libgober, Arapura), which is exactly where the closed formula of Theorem 2 stops being valid (cp2_second_notes.md).
 Also: H^3(U;L)=H^4(U;L)=0 if U affine (Artin); for D ample this holds in all examples. For the formula one needs b_2 = chi(U) - 1 + b_1 (chi(U;L) = chi(U) for rank one).

## 8. Duality for HH itself  (closes G9; independent of the closed formula)

**Proposition 13 (Serre duality for generalized holomorphic line bundles over a beta-transformed complex surface)  [P].**
Let X be a compact complex surface (no Kahler or log-symplectic assumption), sigma a holomorphic Poisson structure, L a Poisson module (GH line bundle) with Theta(dz_i) = (a,b), i.e. V = a d1 + b d2 in a local frame.
Let K_X carry its canonical Poisson module structure (flat A-connection nabla_{df} omega = L_{sigma#df} omega), in the frame dz1^dz2: V_K = (h_2, -h_1) where sigma = h d1^d2, and put
   L' := L^v (x) K_X^2,  V' = -V + 2 V_K.
Then  dim HH^k(L) = dim HH^{4-k}(L')  and  HH^k(L)^* = HH^{4-k}(L')  canonically.
Proof.
 (1) Dolbeault model: HH^k(L) = H^k(Tot), Tot^k = (+)_{a+b=k} A^{0,a}(wedge^b T (x) L), D = dbar + (-1)^a d_L (d_L is a holomorphic differential operator, extended to A^{0,*}(.) by acting on the smooth coefficient functions; it commutes with dbar).
 (2) Ellipticity [P]: the principal symbol of D at xi in T^*_C is wedge with  v(xi) = (xi^{0,1}, sigma#(xi^{1,0})) in L^* = T^{*0,1} (+) T^{1,0}, acting on wedge L^*; (wedge L^*, v wedge) is exact iff v != 0; v = 0 forces xi^{0,1}=0, hence xi = 0 for real xi.
     So Tot is an elliptic complex at EVERY point (also where sigma degenerates). (This is Gualtieri's ellipticity of (wedge L^*, d_L), verified here directly in this setting.)
 (3) Pairing: <.,.>: E^b(L) x E^{2-b}(L') -> wedge^2 T (x) K^2 = K, and A^{0,a} x A^{0,2-a} -> A^{0,2}(K) = A^{2,2}, integrate over X: perfect pairing Tot^k(L) x Tot^{4-k}(L') -> C.
 (4) Transposition: with the frame formulas  d_0 f = (h f_2 + f a, -h f_1 + f b),  d_1(p d1 + q d2) = h(p_1+q_2) - h_1 p - h_2 q + q a - p b,  one checks (hand integration by parts, and exactly by cp2/serre_dual_check.py with random polynomial data, 20 trials)
        <d_L f, beta>  = - <f, d_{L'} beta> + div(h f p' d1 + h f q' d2 ...),    <d_L X, g'> = + <X, d_{L'} g'> + div(...)
     precisely: (b=0): <d0 f,(p',q')> + <f, d1' (p',q')> = d1(h f p') + d2(h f q');  (b=1): <d1 (p,q), g'> - <(p,q), d0' g'> = d1(h g' p) + d2(h g' q);
     where d' is the operator built from V'. The solution of the matching conditions is forced: a' = -a + 2h_2, b' = -b - 2h_1, i.e. V' = -V + 2 V_K.
     V' satisfies the Poisson-module relation V'(h) = h div V' (V_K(h)=0, div V_K = 0), so L' is a module (this is just L^v (x) K^2 with K the Lie-derivative module).
     Stokes: for smooth data the divergence terms are (1,2)/(2,1)-exact total derivatives (dbar(A^{2,1}) = d(A^{2,1}) since A^{3,1}=0) so integrate to 0; the dbar-parts are transposed by the classical Serre duality computation.
     Hence <D alpha, beta> = +- <alpha, D' beta>.
 (5) Duality: D, D' elliptic on a compact manifold => closed ranges and finite-dimensional cohomology; the dual of H^k of an elliptic complex with closed ranges is H^k of the transposed (distributional) complex, and distributional cohomology = smooth cohomology by elliptic regularity.
     So H^k(Tot(L))^* = H^{4-k}(Tot(L')). QED
 Consequences:
 * Verifies Theorem 2(iv) without using the closed formula (and shows the formula's r <-> 2-r symmetry is not an accident).
 * Check against P^2/smooth cubic: K_X^2 = O(-6): L = O(m) -> L' = O(-m-6): the observed duality m <-> -m-6 (cp2_notes.md); and P^1xP^1, K^2 = O(-4,-4): O(m,m) -> O(-m-4,-m-4): m <-> -m-4 (cp2_second_notes.md).
 * Valid for all dimensions n? The same transposition identity should hold for the Chevalley-Eilenberg differential of a rank-n holomorphic Lie algebroid with A^* = T, giving L' = L^v (x) K_X^2 again (E^b dual = wedge^{n-b} T (x) L^v K^2); only n = 2 is checked here.  [G for n >= 3]
 * Gualtieri/Pal-Poddar (SGH) Serre duality is the analogue in the regular type-k setting; the present statement is for the beta-transform family (all types). Not compared term by term.

## 9. Updated gap list (supersedes G2, G4, G9 above)
 G2 closed for the 8 examples (Prop 12); general X, D: exact condition = chi not in V^1(U); sufficient conditions Prop 12(b),(c).
 G4 closed (Prop 11, Lemma 7'); correction: c = u(0) is an invariant, not necessarily 1; weight of H^2_p(Q) is (-1,-1) and the extra class of H^1_p(O_D) is essential.
 G9 closed for surfaces (Prop 13). Remaining: n >= 4 duality (expected same proof), G1 (identification with the GC generalized Dolbeault complex is cited, not re-derived; but note that Prop 13 and the entire Dolbeault-model argument only use the complex C(A;L)), G3, G5-G8 unchanged.
 New caveats: (i) Prop 12(c) needs unitary characters + Timmerscheidt's degeneration (D normal crossings, X compact Kahler), (ii) Arapura's torsion-translate theorem is cited, (iii) I did not re-derive Fulton/Deligne, (iv) Lemma 7' uses that local cohomology of coherent sheaves can be computed on Laurent tails and that differential operators act on them (standard, not written out).

---
# Round 4 (2026-11-21): G1 (identification with the GC generalized Dolbeault complex) and duality in every dimension

Conventions for this round. X complex manifold, dim_C X = n, coordinates z_1..z_n, omega = dz_1^...^dz_n. sigma = (1/2) sigma^{ij} d_i ^ d_j holomorphic bivector with [sigma,sigma]=0.
sigma^#(xi)^i = sigma^{ij} xi_j ... (i.e. sigma^#(dz^k) = sum_i sigma^{ki} d_i).  A := (T^*)_sigma, anchor sigma^#.  Polyvector fields graded by wedge-degree, Schouten bracket [ , ] in the "odd coordinates"
convention  [A,B] = sum_i ( A<-d/dtheta_i  d_{z_i}B  -(-1)^{(a-1)(b-1)} B<-d/dtheta_i d_{z_i} A )  (implemented in cp2/duality_ndim.py).
Modular vector field w.r.t. omega:  M^j := sum_i d_i sigma^{ij}.   Poisson module (L,V): frame e, flat A-connection  nabla_{dz^k}(f e) = (sigma^#(dz^k) f) e + f V^k e, i.e. d_L(P e) = ([sigma,P] + V^P) e.

## 10. G1: the generalized Dolbeault complex of J_sigma  (identification)

**Proposition 14.**  Let sigma be a holomorphic Poisson structure on X and J_sigma the generalized complex structure whose (-i)-eigenbundle (Gualtieri's convention in "Branes on Poisson varieties"; the +i eigenbundle of the conjugate structure in Gualtieri 2011 conventions)
 is  L_sigma = T^{0,1} (+) graph(sigma|_{T^{*1,0}}) = { Xbar + sigma^# xi + xi : Xbar in T^{0,1}, xi in T^{*1,0} } .
 (a) [C] L_sigma is involutive iff dbar sigma = 0 and [sigma,sigma] = 0.  (Gualtieri, Branes on Poisson varieties arXiv:0710.2719, Prop. 5 (§4.2); LGSX arXiv:0707.4253 Thm 2.7 and Rem. 2.8, where the structure is called J_pi with pi=pi_R+i pi_I.)
 (b) [C] phi(Xbar,xi) = (Xbar + sigma^# xi, xi) is an isomorphism of complex Lie algebroids  T^{0,1} |x (T^{1,0})^*_sigma  -> L_sigma (LGSX Thm 4.21 and Lemma 4.22, eq. (27); their J_{4 pi} carries the factor 4 only because of the normalisation pi=pi_R+i pi_I, Prop 3.7 there).
     Here T^{0,1} |x A^{1,0} is the matched pair: T^{0,1} acts on A^{1,0} = (T^{1,0})^* by the holomorphic structure (nabla_{Xbar} xi = pr^{1,0} L_{Xbar} xi) and A^{1,0} acts on T^{0,1} by nabla_xi Xbar = pr^{0,1}[sigma^# xi, Xbar] (LGSX §4.4, Lemma 4.16 and Def. 4.15 there).
 (c) [C + P] A bundle E with a flat L-connection (= generalized holomorphic bundle in the sense of Gualtieri 2011 Def. 3.18 / Branes §4.1) is the same thing as a holomorphic vector bundle with an A-module structure (= holomorphic Poisson module {f,s}).
     [C] Gualtieri Branes Prop. 8 (eqs. (18),(19)); LGSX Lemma 4.16.  [P] direct proof (below).  For line bundles Gualtieri Prop. 9: structures exist iff the classes sigma.alpha in H^1(T^{1,0}) and f_alpha in H^2_sigma(M) vanish, and then form an affine space over H^1_sigma(M).
 (d) [C + P] (Dolbeault model) with  L^* = T^{*0,1} (+) T^{1,0},  Gamma(wedge^k L^* (x) E) = (+)_{a+b=k} A^{0,a}(wedge^b T^{1,0} (x) E), and
        d_L = dbar + (-1)^a d_A  on A^{0,a}(wedge^b T (x) E),
     where d_A = [sigma,.] + V^. acts on the holomorphic-frame coefficients (commutes with dbar).  Consequently the generalized Dolbeault cohomology
        H^k_{GC}(E) := H^k(Gamma(wedge^. L^* (x) E), d_L)  =  H^k(X, (wedge^. T (x) E, [sigma,.]+V^.))   (hypercohomology)  =: HH^k(E).
     [C] LGSX Thm 4.19 (H^*(A,E) = H^*(T^{0,1} |x A^{1,0}, E)), with H^*(A,E) := H^*(X, Omega_A^. (x) E) (Def. 4.17), finite-dimensional on compact X (Lemma 4.18); proof there is "similar to Thm 4.11".
     [P, modulo Mokri's matched-pair theorem] proof given below.

*Proof of (c).* (<=) Given an A-module structure and a holomorphic frame {e_s}, define for smooth sections s = sum f_s e_s : nabla_{Xbar} s = sum (Xbar f_s) e_s (the holomorphic structure), nabla_xi s = sum ((sigma^# xi) f_s) e_s + f_s nabla_xi e_s  (xi in A^{1,0}, C^infty-linear in xi); the second formula is the only possible extension (Leibniz), well defined because nabla_xi e_s is holomorphic. Flatness in the three types of pairs: (Xbar,Ybar): integrability of the holomorphic structure; (Xbar, xi): [nabla_Xbar, nabla_xi] = nabla_{[Xbar,xi]_L}, equivalent to nabla_xi (holomorphic sections) being holomorphic -- true by construction; (xi,eta): Def. 4.15(iii) for holomorphic xi,eta, then extended C^infty-linearly (curvature is tensorial).  (=>) a flat L-connection restricted to T^{0,1} is a holomorphic structure (Koszul-Malgrange, integrability), and by the mixed flatness condition nabla_xi maps holomorphic sections to holomorphic sections for holomorphic xi; Leibniz gives (18); flatness gives (19).  QED
   Cross-check with Lemma 1 of §2 (direct computation: flatness <=> Theta(beta)=beta(V), L_V sigma = 0, i.e. [sigma,V]=0).

*Proof of (d).* L^* = (T^{0,1})^* (+) (A^{1,0})^* = T^{*0,1} (+) T^{1,0}, so wedge^k L^* = (+) wedge^a T^{*0,1} (x) wedge^b T^{1,0}. For a matched pair of Lie algebroids g |x h the Chevalley--Eilenberg complex of g |x h with coefficients in a module E is the total complex of the bicomplex C(g; C(h;E)) with the induced actions (Mokri, Matched pairs of Lie algebroids, Glasgow Math. J. 39 (1997) 167--181 -- cited from memory [C?]; see also Mackenzie GTM-213 / LMS 124 for the Lie-groupoid version). Here g = T^{0,1} with the module M = Gamma(wedge A^{1,0 *} (x) E): the T^{0,1}-module structure on the C^infty-module of holomorphic-polyvector-valued sections is the Dolbeault operator, so C(T^{0,1}; M) = (A^{0,.}(wedge^b T (x) E), dbar) is the Dolbeault resolution of the holomorphic bundle wedge^b T (x) E, and the A^{1,0}-direction is d_A (the CE complex of the holomorphic Lie algebroid A with coefficients in E, which on polyvectors is [sigma,.]+V^.).  The two differentials anticommute after the Koszul sign (-1)^a.  Hence Tot is a fine resolution of the complex of sheaves (wedge^. T (x) E, d_A) and its cohomology is hypercohomology.  QED
   What is *not* re-derived here: Mokri's theorem itself; the check that the Dorfman bracket restricted to L_sigma coincides with the matched-pair bracket (cited from LGSX Lemma 4.22, where it is a direct computation).  Convention caveat: Gualtieri's papers differ (Branes §4.1 uses ker(J-i) in one place and ker(J+i) in the proof of Prop 8); the complex Lie algebroid L and the complex conjugate give isomorphic cohomologies by conjugation, so statements (c),(d) are insensitive to this.

**Consistency checks with earlier results (P/V).**
 * Gualtieri Prop. 9 says module structures on a line bundle form an affine space over H^1_sigma(M) = HH^1(O) (trivial coefficients).  For the smooth cubic on P^2 our table (m=0) gives HH^1 = 0: uniqueness (earlier derivation).  For reducible D, H^1(U) != 0 (e.g. conic+secant: [1,1,3,0,0]): non-uniqueness, an affine family -- this is exactly the correction noted for the reducible tables (the residues along components form an affine family).
 * Existence: the obstruction classes sigma.alpha in H^1(T) (zero for P^2 since H^1(T)=0) and f_alpha in H^2_sigma (here 2- or 3-dimensional): vanishing was shown by the explicit Casimir/log-connection construction (Lemma 4), consistent.

## 11. Duality for HH in every dimension

**Setting.** X compact complex manifold of any dimension n (n need not be even; sigma need not be log-symplectic or non-degenerate anywhere), sigma holomorphic Poisson, (L,V) a Poisson module.

**Notation.** K = K_X with its canonical module structure (frame omega, nabla_{df} omega := L_{sigma^# df} omega = div_omega(sigma^# df) omega, i.e. V_K^k = sum_i d_i sigma^{ki} = -M^k); L^v the dual module (V -> -V); tensor products add V's.
Set  L' := L^v (x) K^2  with  V' = -V + 2 V_K = -V - 2M  in frames e' with e e' = omega^2.  [For log-symplectic D: K^{-1} = O(D) and the residue of K as a module is 1 (Prop. 8, r=1), so res(L') = 2 - res(L): the symmetry r <-> 2-r of the closed formula, now in every dimension.]

**Lemma D (P; hand derivation + exact script check for n=2,3,4: cp2/duality_ndim_exact.py).**  For T in wedge^{n-1}T with T = sum_j (-1)^j u_j d_1^..^hat{d_j}^..^d_n (u_j smooth functions):
    [sigma, T]_top  =  - sum_{i,j} d_i( sigma^{ij} u_j )  +  2 sum_j M^j u_j ,      and      (M ^ T)_top = sum_j M^j u_j .
 Hand derivation: first term of the Schouten bracket: sum_i sigma<-d_theta_i d_i T gives sum sigma^{ji} d_i u_j = - sum sigma^{ij} d_i u_j; second term gives + sum_{i,j} (d_i sigma^{ij}) u_j; and -sum sigma^{ij} d_i u_j + sum (d_i sigma^{ij}) u_j = -sum d_i(sigma^{ij}u_j) + 2 sum (d_i sigma^{ij}) u_j.  (The sign bookkeeping of the right derivatives was checked by machine.)  Equivalent invariant form: under wedge^{n-1}T = Omega^1 (T -> iota_T omega) the Schouten bracket with sigma corresponds to the Koszul--Brylinski operator [iota_sigma, d] minus the modular term, [sigma,.] = [iota_sigma,d] - M^ (up to sign), which is the classical statement that [sigma,.] differs from the BV-differential [iota_sigma, d] by the modular vector field.

**Lemma E (transposition identity; P + exact script check).**  Let P in wedge^b T, Q in wedge^{n-b-1}T (smooth coefficients, 0 <= b <= n-1), d = [sigma,.] + V^ and d' = [sigma,.] + V'^ with V' = -V-2M.  With <P,Q> := (P^Q)_top,
    <dP, Q> + (-1)^b <P, d'Q>  =  - sum_{i} d_i( sum_j sigma^{ij} u_j ),     T = P^Q = sum (-1)^j u_j d_{hat j}.
 Proof: Leibniz [sigma, P^Q] = [sigma,P]^Q + (-1)^b P^[sigma,Q] (sigma has even degree 2); the V-terms: V^P^Q + (-1)^b P^(-V)^Q = V^P^Q - V^P^Q = 0; the M-term: (-1)^b P^(-2M)^Q = -2 M^P^Q = -2 M^T.  Hence LHS = [sigma,T]_top - 2 (M^T)_top = - sum d_i(sigma^{ij}u_j) by Lemma D.  QED  [Checked exactly (not just by residues) for n=2,3,4 with random polynomial/Laurent data, arbitrary bivector sigma (Poisson not needed for this identity): duality_ndim_exact.py (I),(II); the constants c=-2, s=(-1)^b were *found* by solving, independently of the derivation: duality_ndim.py.]
 Note that sigma need not be Poisson and L' need not be a module for the identity itself; Poisson-ness of sigma and the module property of L' are needed for D'^2 = 0.

**Proposition 15 (Serre duality for generalized Dolbeault cohomology of GH line bundles over beta-transformed complex manifolds).**
 Let X be a compact complex manifold, dim n, sigma holomorphic Poisson, L a GH line bundle. Then for all k
        HH^k(L)^*  ~=  HH^{2n-k}(L^v (x) K_X^2)      (in particular dim HH^k(L) = dim HH^{2n-k}(L^v (x) K^2)),
 where L^v (x) K^2 carries the tensor-product module structure (V' = -V + 2 V_K = -V - 2M in frames with e e' = omega^2).  No Kahler, projective, log-symplectic or non-degeneracy hypothesis; any holomorphic Poisson structure including sigma = 0 (for which it is classical Serre duality: HH^k(L)=(+)_{a+b=k} H^a(wedge^b T (x) L), dual of H^{n-a}(wedge^{n-b} T^* ... ) = H^{n-a}(Omega^b (x) L^v ...): check: wedge^b T (x) L ~= Omega^{n-b}(x)K^{-1}(x)L, Serre dual H^{n-a}(Omega^b (x) K (x) L^v (x) K^{-1}... ) which is H^{n-a}(wedge^{n-b} T (x) K^{-1} ... ) consistent -- verified below by P^1 example).
 *Proof.*  Tot^k(L) = (+)_{a+b=k} A^{0,a}(wedge^b T (x) L), D = dbar + d_K  where d_K (phi (x) P e) = (-1)^a phi (x) d(P e) (Koszul sign; d acts on the coefficients in holomorphic frames, commutes with dbar), D^2=0 because dbar^2=0, d^2=0 (needs [sigma,sigma]=0 and [sigma,V]=0), dbar d_K + d_K dbar = 0.
   (1) Ellipticity [P]: principal symbol of D at real xi != 0 is wedge with v(xi) = (xi^{0,1}, sigma^#(xi^{1,0})) in L^* = T^{*0,1} (+) T^{1,0} on wedge L^*; exact iff v(xi) != 0, and v(xi)=0 forces xi^{0,1}=0 hence xi=0 (xi real).  (= Gualtieri's ellipticity of (wedge L^*, d_L) 2011 Prop. 3.16 (number to be checked); here verified directly.)  The same holds for D' (L' is a module).
   (2) Pairing: for alpha = phi P e (phi in A^{0,a}, P in wedge^b T), beta = psi Q e' (psi in A^{0,a'}, Q in wedge^{b'}T),
          <alpha,beta> := int_X (-1)^{b a'} phi ^ psi  (P^Q)_top omega   if b+b' = n, a+a' = n  (else 0),
       using e e' = omega^2 and wedge^n T = K^{-1}.  It is a perfect pairing Tot^k(L) x Tot^{2n-k}(L') -> C (pointwise perfect).
   (3) Transposition [P]: (i) dbar-part: Stokes for the (n,n-1) form  c omega ^ phi ^ psi, c=(P^Q)_top, gives  <dbar alpha, beta> = -(-1)^{a+b} <alpha, dbar beta>.  (ii) d-part: <d_K alpha, beta> + (-1)^{k} ... : by Lemma E the integrand of <d_K alpha, beta> + (-1)^{a+b}<alpha, d'_K beta>-type combination is  - sum_i d_i(F^i) omega ^ (antiholomorphic top form), and  d_i F omega ^ dzbar^{1..n} = pm d( F iota_{d_i} omega ^ dzbar^{1..n} ) (the dzbar^{1..n} factor kills the dbar-part of dF, and dz^j ^ iota_{d_i}omega = 0 for j != i).  This is a *local* statement about the formal transpose D^t of D with respect to the perfect pairing: D^t is a differential operator defined by <D alpha, beta> = <alpha, D^t beta> for compactly supported data; it is local, hence defined globally by its local expressions; Lemma E + Stokes show D^t = -(-1)^{k} D' on each coordinate chart (the signs of the dbar- and d-parts agree: both come out as  <D alpha, beta> = -(-1)^{deg alpha} <alpha, D' beta>), hence globally.  (So no global primitive of the divergence is needed.)     Sign computation for (ii) (by hand): alpha = phi P e (deg phi = a, deg P = b), beta = psi Q e' (deg psi = a', deg Q = n-b-1, a+a'=n). Then <d_K alpha,beta> = (-1)^{a+(b+1)a'} int phi^psi (dP^Q) omega and <alpha, d'_K beta> = (-1)^{a'+b a'} int phi^psi (P^d'Q) omega.  Lemma E: dP^Q = -(-1)^b P^d'Q + divergence, and the divergence integrates to 0.  Hence <d_K alpha,beta> = -(-1)^{a+b} <alpha, d'_K beta>, the same sign -(-1)^{deg alpha} as in (i).  So D^t = -(-1)^{deg} D' componentwise and <D alpha,beta> = -(-1)^{deg alpha}<alpha, D' beta>.
   Then for global smooth alpha, beta (compact X, no boundary), partition of unity gives <D alpha,beta> = -(-1)^{deg alpha}<alpha, D' beta>.
   (4) Conclusion: D, D' elliptic complexes on a closed manifold, perfectly paired with D^t = pm D'; H^k(Tot L) finite-dimensional, ranges closed (Hodge theory for elliptic complexes), and the dual of H^k(Tot L) is the cohomology H^{2n-k} of the transposed complex = Tot(L') (distributional cohomology equals smooth cohomology by ellipticity).  QED  
 *What was machine-checked vs. by hand:*  Lemma D, Lemma E: exact polynomial identities for n = 2,3,4; the Koszul signs in step (3) (the relative sign of the dbar- and d-parts) were derived by hand (explicit computation above, both parts give -(-1)^{deg alpha}) and *not* machine-checked.  The scheme "formal transpose is local" removes the global-primitive issue.

**Sanity checks.**
 * n=2: reproduces Prop. 13 (V' = -V+2V_K, V_K=(h_2,-h_1) = -M; M=(−h_2,h_1)).  Exact script serre_dual_check.py agrees with the sign convention d_0 f = (h f_2 + f a, -h f_1+ f b).
 * sigma=0: HH^k(L) = (+)_{a+b=k} H^a(X, wedge^b T (x) L), and the claimed dual is HH^{2n-k}(L^v K^2) = (+) H^{n-a}(wedge^{n-b}T (x) L^v (x) K^2).  Classical Serre duality gives H^a(F)^* = H^{n-a}(F^v (x) K) with F = wedge^b T (x) L; since wedge^b T^* = wedge^{n-b}T (x) K one gets F^v (x) K = wedge^{n-b}T (x) K (x) L^v (x) K = wedge^{n-b}T (x) L^v (x) K^2. OK.
 * P^2, smooth cubic, K^2 = O(-6): m <-> -m-6; P^1 x P^1: K^2 = O(-4,-4): m <-> -m-4 (both observed earlier, cp2_notes.md, cp2_second_notes.md).
 * Log-symplectic SNC D in any even dimension: L=L_r (residues r_i) gives L' with residues 2 - r_i, HH^k(L_r) dual to HH^{2n-k}(L_{2-r}); in the closed formula (surface) the r <-> 2-r symmetry (Thm 2).  Consistent with Serre duality H^k(U;L) <-> H_c^{2n-k}(U;L^v) after the shift r -> -r on U... (residue of L' on U: monodromy exp(-2 pi i r)*exp(4 pi i)=exp(2 pi i(2-r))=exp(-2pi i r): L'|_U = L^v|_U ✓ since K^2|_U trivialised by omega_sigma^{...}).

## 12. Updated gap list (Round 4)
 * G1: structure of the identification proved modulo (i) Mokri's matched-pair theorem (cited from memory, publication data to be checked), (ii) LGSX Lemma 4.22 (cited; direct computation not re-done), (iii) sign conventions between Gualtieri's papers (harmless by conjugation).  LGSX Thm 4.19 itself is cited; Gualtieri 0905.3227 asserts less than assumed (see cp2_proof_notes / earlier correction): use Branes (0710.2719) Prop 5, 8, 9 and LGSX instead.
 * Duality in all n: proved (Prop 15) modulo the hand-derived Koszul-sign compatibility of the dbar- and d-parts (not machine-checked) and the standard Hodge theory of elliptic complexes.  Lemma D/E exact for n=2,3,4 (script).
 * Unchanged: non-nodal singularities, unequal residues, higher-dimensional normal-crossings quotient analysis (G3, G5--G8).
 * Corrections to earlier text: Gualtieri Prop 9 (Branes) says Poisson-module structures on a line bundle form an affine space over H^1_sigma, so uniqueness on P^2/smooth cubic is *equivalent* to HH^1(O)=0 (true by our table), while for reducible D the module structures are a family (matches the earlier reducible-D correction).
