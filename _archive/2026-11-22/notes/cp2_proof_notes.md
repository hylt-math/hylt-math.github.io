# CP^2, Poisson cubic: proof of the hypercohomology table, and integrability (notes, 2026-11-21)
Legend: [P]=proved here (by hand, modulo the standard facts named), [C]=cited (fetched), [O]=open/unverified.
Setting: X=P^2, sigma=Pi_F in H^0(wedge^2 T)=H^0(O(3)), D={F=0} smooth cubic, sigma vanishes to order 1 on D. E=O(m).
Local: near D, coordinates (z,w), D={z=0}, sigma=h d_z^d_w, h=z*u, u unit.

## 1. Poisson modules on O(m)  <=>  flat log connections  [P]
Module over A=(T^*)_sigma: flat A-connection, nabla_xi(gs)=g nabla_xi s+(sigma^#xi)(g)s. Local frame e, nabla_{dz}e=a e, nabla_{dw}e=b e.
Flatness [nabla_dz,nabla_dw]=nabla_{[dz,dw]_sigma}, [dz,dw]_sigma=dh, gives  h(a_z+b_w)=h_z a+h_w b. At z=0: h=0,h_z=u,h_w=0 => u*a|_{z=0}=0 => a=z*alpha.
Hence nabla extends to Omega^1(log D)=:B (nabla_{dz/z}e=alpha e).  sigma^{-1}=omega in H^0(Omega^2(log D)) is nowhere degenerate (log-symplectic), closed for dimension reasons, so sigma^#: B -> T(-log D)=:T_D is an iso of Lie algebroids [standard: symplectic Poisson on Lie algebroid T_D, omega d_{T_D}-closed]. So A-module structures on a line bundle E <=> flat log connections nabla:E->Omega^1(log D)(x)E  (restriction to Omega^1 c B gives the converse).
Residue: Res_D nabla in H^0(O_D)=C is a constant r. Esnault-Viehweg/Deligne: c_1(E)=-r[D]. [D]=3H => r=-m/3.  (Sign check: O(D) with nabla s_D=0 has Res=-1, c_1=[D]. OK.)
Existence for every m: Atiyah class of E maps to 0 in H^1(Omega^1(log D)) iff c_1(E) in C*[D]  (sequence H^0(O_D)->H^1(Omega^1)->H^1(Omega^1(log D))); true for O(m). Curvature in H^0(Omega^2(log D))=C*omega has residue d r=0 => flat.
Uniqueness: difference of two log connections is in H^0(Omega^1(log D))=0 (connecting map 1 -> [D]=3H !=0). 
=> Poisson-module structures on O(m): exactly one for each m. (This re-derives and strengthens the earlier (i); Pic of GH line bundles = Z, GIVEN GH line bundle = Poisson module, which Gualtieri 0905.3227 only asserts and LGSX 0707.4253 Thm 4.19/4.21 set up.)
Local gauge: A=r dz/z+beta, beta closed holomorphic (f_w|_{z=0}=0 from dA=0) => frame with nabla e=r dz/z e; flat multivalued section z^{-r}=z^{m/3}.

## 2. Log subcomplex [P]
C_m=(wedge^b T (x) O(m), d_sigma) (Lichnerowicz/Chevalley-Eilenberg of A with coefficients in O(m)), C_log=(wedge^b T_D (x) O(m)) subcomplex (sigma in wedge^2 T_D, T_D Lie algebroid).
Via the iso sigma^#: C_log ≅ (Omega^•(log D)(x)O(m), nabla) = DR_log.
Stalks: at U: local system L_m=ker nabla. At D, frame nabla e=r dz/z e: z^n e -> (n+r) z^n (dz/z) e = (n-m/3) z^n dz/z e (times de Rham of C{w}: only H^0). So stalk cohomology of DR_log at D: [1,1] if m in 3Z_{>=0}, 0 otherwise.
 - m in 3Z_{>=0}: natural map DR_log -> DR(E(*D)) ≃ Rj_*L_m is a stalkwise quasi-iso => ℍ(C_log)=H^*(U,C).  
 - otherwise: j_!L_m -> DR_log (extension by zero is holomorphic) is a stalkwise quasi-iso => ℍ(C_log)=H_c^*(U,L_m).
Topology of U=P^2\D [P, Milnor]: pi_1=Z/3; Milnor fibre Ũ={F=1}⊂C^3 (cone over smooth cubic, mu=8) ≃ bouquet of 8 S^2, U=Ũ/mu_3, H^2(Ũ)=C^8 = 2 (trivial char)+3+3 (nontrivial; Euler char 3 each). U affine => H^k=0,k>2.
 H^*(U,C)=[1,0,2,0,0]; H^*(U,L)=[0,0,3,0,0] for nontrivial char; H_c^*(U,L)=dual of H^{4-*}(U,L^v): trivial -> [0,0,2,0,1]; nontrivial -> [0,0,3,0,0].
Monodromy of L_m around D = exp(2 pi i r)=exp(-2 pi i m/3): trivial iff m in 3Z.

## 3. Quotient complex [P]
Q=C_m/C_log is supported on D, only degrees 1,2: Q^1=N_D(m)=O_D(m+3), Q^2=wedge^2T(m)|_D=O_D(m+3).
d_sigma on Q: computed by the CE formula (d theta)(dz,dw)=nabla_dz theta(dw)-nabla_dw theta(dz)-theta([dz,dw]), theta=X(x)e, X=p d_z+q d_w:
 = h(p_z+q_w)-h_z p-h_w q+q a-p b. At z=0: = -p(u+b). Residue: nabla_{z d_z}e=-(b/u)e => b|_D=-r u. So d_Q = -u(1-r)p = -u(1+m/3) p.
 Invariantly d_Q=-(1+m/3)*(d sigma|_D : N_D -> wedge^2T|_D), and d sigma|_D is an iso (sigma=3F, dF!=0 on D). Hence Q acyclic iff m != -3.
 (Consistency: numerics earlier showed m=-3 exceptional; sign conventions agree with this.)
=> For m != -3: ℍ(C_m)=ℍ(C_log). Table:
 m in 3Z_{>=0}: [1,0,2,0,0];  m in 3Z_{<0}, m != -3: [0,0,2,0,1];  m not in 3Z: [0,0,3,0,0].  Matches direct computations m=-15..15.
## 4. m=-3 [P]
Directly: E_1^{a,b}=H^a(wedge^bT(-3)): O(-3): H^2=1 at (2,0); T(-3)=Omega^1: H^1=1 at (1,1); wedge^2T(-3)=O: H^0=1 at (0,2). All total degree 2 => every d_r (degree +1) is zero => [0,0,3,0,0]. (Rigorous, no sign issues.)
Compare: C_log ≃ j_!C: [0,0,2,0,1]; Q has d=0 (D elliptic): ℍ(Q)=H^{*-1}(O_D)+H^{*-2}(O_D)=[0,1,2,1,0]. Long exact sequence consistent iff connecting maps delta_1:C->C^2 injective, delta_3: C->C iso; Euler 3=3+0. 

## 5. Integrability [C]+[P]
(a) Literal question "does the complex Lie algebroid L integrate to a groupoid?" is not meaningful in the literature found: no notion of Lie groupoid for a complex (non-real) Lie algebroid L with L∩Lbar=0; Bailey-Gualtieri arXiv:1611.03850 do not construct one for L.
(b) What IS available: Bailey-Gualtieri Thm 7.1: GC manifold integrates to a weakly holomorphic symplectic groupoid (Morita-class notion) iff its underlying real Poisson structure P (= Im sigma in their convention, Example 2.6; Lemma 7.5) integrates. LGSX 0803.2031 Thm 3.22: holomorphic Poisson integrable iff Re or Im sigma integrable.
(c) Integrability of P=Im(sigma) on CP^2 [P, using Crainic-Fernandes, Ann.Math. 157 (2003), Cor. 5.2 'if all N_x(A) trivial then A integrable', and Thm 4.1 for arbitrary (non-regular) algebroids; fetched math/0105033v5]:
 Algebroid (T^*)_P. Leaves: U (open, rank 4, isotropy 0) and points of D (isotropy = linearization = aff(1,C) as real 4-dim Lie algebra, [dz,dw]=dz, CENTERLESS). N_x ⊂ Z(g_x)=0 for every x => N_x trivial => integrable. s-simply connected groupoid exists (maybe non-Hausdorff); symplectic groupoid by Mackenzie-Xu.
 => by Bailey-Gualtieri Thm 7.1, J_sigma admits a weakly holomorphic symplectic groupoid. (I did not re-derive their hypotheses beyond what the fetched summary states.)
(d) Gap: Hu (Tengzhou Hu, 'Lie groupoid Riemann-Roch-Hirzebruch theorem and applications', arXiv:2403.13424, Thm 4) works with a Lie algebroid g carrying an integrable almost complex structure J, Dolbeault operator on wedge g^{*(0,q)} (x)E, index in K_0 of the convolution algebra of G paired with a cocycle Omega_g, compact base; ellipticity is asserted without proof there. This is NOT the generalized-Dolbeault complex wedge L^*(x)E: relation not established here. [O] Whether Hu's framework contains the GC case is open; whether Hu's index sees m is open.
Note: the earlier notes called the Hu author 'S. Hu' — arXiv:2403.13424 lists Tengzhou Hu (2403.10876 author not re-checked).

## Remaining caveats
- Identification 'generalized Dolbeault complex of GH bundle O(m)' = hypercohomology of C_m: LGSX 0707.4253 Thm 4.19 (cited, not re-derived).
- Standard facts used w/o proof: Esnault-Viehweg residue formula; Deligne regularity local computation (done by hand above); Milnor fibre of homogeneous isolated singularity = bouquet of mu spheres; symplectic => sigma^# iso of Lie algebroids for log-symplectic.
- Smooth D only. Singular D, rank>1 not treated.
