# CP^2 with sigma = Pi_F for singular cubics F: hypercohomology of (wedge T(m), d_sigma)  (2026-11-21)
Scripts (cp2/): sing_table.py (computes), sing_out.txt (raw output), predict_sing.py (tests conjecture). Exact linear algebra mod 32003; m=-15..15.
Method [computed]: same code as before with other F (Pi_F is Poisson for ANY F; every O(m) is a Poisson module by the same construction).
E_1 terms do not depend on F, so for m>=-2 only d_1 (rank computations) and for m<=-4 local-cohomology computation (neg_check.run) are needed; m=-3: three 1-dim E_1 terms in total degree 2 => [0,0,3,0,0] for every F.
## Cubics tested
smooth(Fermat); nodal y^2z-x^3-x^2z; cuspidal y^2z-x^3; conic+secant x(yz-x^2); conic+tangent y(yz-x^2); triangle xyz; concurrent lines xy(x-y); double line+line x^2y; sigma=0.
## Results [computed]
- Total Euler characteristic = 3 for ALL nine, all m in -15..15 (assert in script).
- smooth, nodal, cuspidal give IDENTICAL tables (period 3): m in 3Z,m>=0: [1,0,2,0,0]; m in 3Z,m<=-6: [0,0,2,0,1]; other m: [0,0,3,0,0]; m=-3: [0,0,3,0,0].
- conic+secant and conic+tangent: identical to each other: m in 3Z,m>=0: [1,1,3,0,0]; m in 3Z,m<=-6: [0,0,3,1,1]; else [0,0,3,0,0].
- triangle: m in 3Z,m>=0: [1,2,4,0,0]; m in 3Z,m<=-6: [0,0,4,2,1]; else [0,0,3,0,0].
- concurrent lines (triple point, not normal crossing): m=0:[1,2,4]; m=3k: [1,2,4,0,0]; m=1,2,4,5..: [0,1,4,0,0]; but m=-2,-4: [0,0,3,0,0] (anomaly); negative side dual (m<->-m-6). Pattern depends on m beyond m mod 3 near the triple point.
- double line + line x^2y (non-reduced D): H^1,H^2 grow linearly in m (e.g. m=15: [1,18,20,0,0]); sigma vanishes to order 2 on a line, no log structure.
- sigma=0 control: = oplus H^a(wedge^b T(m)) (e.g. m=0 [1,8,10,0,0]); chi=3.
## Pattern (CONJECTURE, fits 6 cubics x 31 values of m, 0 mismatches; predict_sing.py)
Let U=P^2\D, c=#components, mu = sum of Milnor numbers of singular points (for a cubic chi(D)=mu, so chi(U)=3-mu), b0=1,b1=c-1,b2=chi(U)-1+b1.
 H^*(m) = [U-part] + C^{mu} in degree 2, where
   m=-3 : [0,0,3,0,0] (proved by E_1)
   m in 3Z, m>=0 : U-part = H^*(U;C)   (residue r=-m/3 <=0, Rj_*)
   m in 3Z, m<=-6: U-part = H^*_c(U;C) (j_!)
   m not in 3Z   : U-part = H^*(U;L_m) = [0,0,chi(U)] (rank-1 local system, monodromy e^{2 pi i m/3} around every component)
Interpretation: log-symplectic part gives the (Rj_*/j_!) topological term; each singular point p of D contributes a skyscraper of dimension mu_p in degree 2 (nc node: 1, cusp: 2, tacnode: 3) -- local Poisson cohomology of the singularity. For smooth D no local term.
Not covered: non-isolated/non-reduced D, triple point with m-dependent local term; H^1(U;L_m)=0 assumed for m not in 3Z (consistent with data).
## CP^1 x CP^1 [NOT DONE]
Reason: Pi on C^4 needs a verified Poisson-module structure; plan: line bundles O(a,b), T=O(2,0)+O(0,2), sigma in H^0(O(2,2)). Prediction (unverified): flat log connection exists only for O(m,m) (c_1(L) = -r[D], D=(2,2)), residue r=-m/2, so period 2 in m and H^*(U,L_m) with U=P^1xP^1\D; chi(P^1xP^1)=4 independent of m.
