# Round C notes (2026-11-22): log-symplectic surfaces beyond equal residues

Scripts (cp2/): roundC_toric_cech.py (weight-graded Cech hypercohomology, kinds A=C(A;L), B=DR_log),
roundC_p2_sweep*.py/analyze.py, roundC_p1p1_sweepA.py, roundC_p1p1_analyze.py, roundC_local_verify.py.

## (1) Unequal / mixed residues at ordinary nodes
[proved, toric weight/CLS argument] For DR_log: weight-chi Cech complex = K_chi (x) (wedge N, v^); acyclic unless chi=-rho
(needs rho in M, i.e. all r_i integral). So H^*(X;F) = sum_q htilde^{q-1}(V_S) t^q (1+t)^n, S={i: r_i>=2}, V_S full
subcomplex of the boundary complex of the fan on S (htilde^{-1}(empty)=C).
[computed, = Theorem 2 extended] All r_i != 1 on toric surface:
  HH = (#vertices) t^2 + sum_q htilde^{q-1}(V_S) t^q(1+t)^2 if rho in M, else (#vertices) t^2.
 P^2 triangle: 755 rows (m in -9..6, residues in {-2..3,+-1/2}), 0 mismatches (S proper nonempty -> 0; S empty: (1+t)^2 only if all r_i<=0 ... as in P_r; all r_i>=2: t^2(1+t)^2).
 P^1xP^1 four lines: 729 rows, 0 mismatches, including S = two opposite rays (nonzero t(1+t)^2 term: new prediction confirmed).
 So unequal residues: no new phenomenon beyond the V_S combinatorics; resonance only at r_i=1.
## Resonance r_i=1 (R = resonant branches, N=N_{D_i}(x)L, K=K_X^{-1}(x)L|_{D_R})
[computed + derived heuristically, not fully proved]
 HH = t h^0(N) + t^2(h^1(N)+h^0(K_R)+nu) + t^3 h^1(K_R), nu=#nodes with no resonant branch.
 Checked: P^2 single/double resonance (L_U nontrivial); P^1xP^1: 108 rows with some r_i=1, non-integral residues, 0 mismatches.
 Fails (needs connecting maps from DR / H_c of torus): all residues integral (L_U trivial) with m<<0, and all-resonant (L=K), cf. Prop 8.
 Example failures: P^2 double resonance m=-5 integral: observed [0,0,5,2] vs naive [0,0,6,3]; triple (1,1,1): [0,0,3] vs 4t^2+t^3.
## (2) Quasi-homogeneous plane curve germs (cusp, tacnode, D,E, T_{2,3,6})
[computed, formula] stalk(C_s)=C^mu[-2] (+) R(s), s!=1, R(s)=[s<lct]([s in Z](1+t)+(t+t^2)#{alpha in Spec: s+alpha in Z});
 at s=lct count c-1 (c=#{alpha: s+alpha in Z}); c-1=0 for A_k,D_k,E6,E8; =1 for T_{2,3,6} at s=1/2.
 Verified A1-A6, D4, D5, D6, E6, E8, T236 (s=1 excluded: infinite-dim). Not proved (sketch: Wang sequence on Milnor fibration, Jacobian algebra computation of Q).
 CORRECTION: D5 = z^2 w - w^4 has weights (3,2,8), spectrum {5/8,7/8,1,9/8,11/8}; earlier D5 values in cp2_second_notes.md (weights (3,1,7)) are wrong.
## (3) Theorem statements
 T-C1 (proved, toric, rho in M criterion) V_S formula for H(X;F).
 T-C2 (computed on P^2, P^1xP^1) full HH for r_i != 1.
 C-C3 (conjecture) resonance sheaf formula when L_U nontrivial.
 C-C4 (conjecture) local stalk formula above for quasi-homogeneous germs.
