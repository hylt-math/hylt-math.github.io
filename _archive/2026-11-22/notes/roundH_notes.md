# Round H (2026-11-22): proof of local stalk rule R(s) for quasi-homogeneous isolated plane-curve germs

Setting: h quasi-homogeneous, weights (wz,ww), degree N, delta=N-wz-ww, isolated singularity, mu=dim T (T=O/J, J=(h_z,h_w)).
sigma = h dz^dw (log-symplectic-type, D={h=0}), rank-1 module with residue s: nabla = d + s dlog h on Omega^*(log D).
chi = h_w d_z - h_z d_w (Hamiltonian field), e = Euler field (wz z d_z + ww w d_w), e h = N h.

## Weight-k0 piece (k0 = -sN-type weight index; s=-k0/N)
Basis omega_e = (dz.. contracted with e)/h, omega_chi (log forms dual to e, chi). Computation:
 nabla_s f = (e f + sN f) omega_e + chi(f) omega_chi
 nabla(a omega_e + b omega_chi) = (nu/N)[chi(a) - (e + sN - delta) b]
On weight-k0 piece (e acts as scalar k0 on O_{k0}):
 C0=O_{k0}, C1=O_{k0}+O_{k0+delta}, C2=O_{k0+delta}; d0 f=(0,chi f) [first comp. vanishes since k0+sN=0], d1(a,b)=chi(a)/N [second comp. term (k0+sN-delta... ) ] 
 => H0=K=ker chi, H1=K+Cok, H2=Cok, Cok=coker(chi:O_{k0}->O_{k0+delta}).
 K = C h^{k0/N} iff k0 in N Z>=0 (chi f=0 <=> f function of h, quasi-homog; isolated => f in C{h}).
 Hilbert series identity (x^{-delta}-x^b-x^a+x^N)=(x^{-delta}-1)(1-x^N)+(1-x^a)(1-x^b)
   => dim Cok = sum_{r>=0} dim T_{k0+delta-rN} = #{alpha in Spec : s+alpha in Z, s+alpha<=1}.
 Stalk polynomial: R(s) + mu t^2 (s != 1), R(s)=[s in Z,s<=0](1+t)+(t+t^2)#{alpha in Spec: s+alpha in Z, s+alpha<=1}.
 (Spec: alpha=(weight(m)+wz+ww)/N for monomial basis m of T.)

## Computed (cp2/roundH_proof_check.py, exact Fractions)
 - polynomial identities for d0,d1 verified with random polynomials/s on all 14 types.
 - K and Cok dims vs R(s) predictions for ~700 values of k0 across A1,A2,A3,A6,D4,D5,E6,E8,z3+w6,z4+w5,z5+w5,z4+w4,z3+w7,z5+w6: 0 mismatches.
## Gaps
 - Needs weight decomposition to be complete: holds for convergent germs by quasi-homogeneity (graded pieces, formal=analytic by Artin/standard); sum over k0 gives full complex (completion fine).
 - Only s != 1 (s=1 separate). Non-quasi-homogeneous isolated germs: not covered (semicontinuity only).
 - The "chi f=0 => f in C{h}" step: standard for isolated sing. (Saito-type); cite/check.
