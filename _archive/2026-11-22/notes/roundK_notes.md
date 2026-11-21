# Round K notes (2026-11-22): Riemann–Roch-type formulation for GH line bundles

Script: cp2/roundK_check.py (padding bug fixed: predictions padded to 2n+1, r>=2 uses t^{2n}P(1/t)).
Results: (K1) 0/175 mismatches; (K2a) surface tables 0/188; (K2b) toric n=2,4 0/61.

## Theorem K1 (proved, given Deligne + log-symplectic)
L with flat log connection along SNC D, sigma log-symplectic: B = ∧T(-log D)⊗L ≅ DR_log(L).
chi(X; DR_log(L)) = ∫ c_n(T(-log D)) = chi(U)  (independent of L; rk-1 flat -> alternating sum of ranks of Omega^k(log D)).
Checked: P^2 with smooth degree-d curve, d=1..7, a=-12..12 (175 cases): S = c2 = 3-3d+d^2 ... = chi(U).

## Theorem K (proved under Thm R hypotheses; U affine, n even; checked)
P_HH(t) = chi(X) t^n + sum_{k<n} h^k(U;L_U) (t^k - (-1)^k t^n).
Surface case reproduces P_r(t). Toric n=2,4 consistent (h^k = C(n,k) iff rho in M, else 0).
Total Euler characteristic = chi(X)·(rank) stays m-independent => RR is "polynomial" only in the degree-0 part;
dimensions depend on m only through periodic residue-indicator conditions (contrast Cor L).

## Wall-crossing identity
chi_c(U;L) = chi(U;L) since chi(∂U)=0 (odd-dim closed manifold boundary).

## Index conjecture (not proved)
Weighted b-calculus on U with indicial roots r∈Z: generalized Dolbeault operator Fredholm iff r∉Z,
index = chi(U); at r∈Z jump by H^*(∂U;L) (APS-type wall-crossing triangle).
Hu's Lie groupoid RR does not apply (different complex).
