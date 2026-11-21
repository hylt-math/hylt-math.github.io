# Hu's papers vs. the generalized Dolbeault complex (notes)

Legend: [CITED] = from fetched text (WebFetch summaries of arXiv PDFs; first 100k chars of 2403.10876 only; I did not see the appendices);
[DERIVED] = my reasoning, not checked against a source; [CONJ] = conjecture.

## 1. Bibliographic corrections for gc3.tex
- arXiv:2403.10876: author **Tengzhou Hu** (WashU), title **"Kodaira vanishing theorems for Kähler Lie algebroids"** (v1, 19 Mar 2024). gc3.tex wrote "S. Hu" and an invented title -> wrong.
- arXiv:2403.13424: author **Tengzhou Hu**, title **"Lie groupoid Riemann–Roch–Hirzebruch theorem and applications"** (21 Mar 2024). gc3.tex wrote "S. Hu, Riemann–Roch for Lie algebroids" -> wrong.
- gc3.tex §5 cites "Thm 2, Def 12,13" for vanishing. Actual numbering: in 2403.10876 the Kähler Lie algebroid is Def 2, Kähler identities Thm 1 / Prop 4, BKN = Lemma 4, main vanishing theorem is stated in the Introduction (kernel of Laplacian). In 2403.13424: Kähler Lie algebroid Def 11, positive/negative bundle Def 12, vanishing = Thm 7 (+Cor 1), RR = Thm 4.
- Note: "positive" in 10876 is not defined in the part I read; defined in 2403.13424 Def 12 (some Hermitian metric with sqrt(-1)R positive definite).
- gc3.tex remark that BKN has "sign slip": 10876 Lemma 4 reads Delta_dbar = Delta^{1,0} + sqrt(-1)[nabla^2, Lambda]; still unverified against proof.

## 2. Setting of 2403.13424 [CITED]
- Lie groupoid G ⇉ M (Def 1, no properness/source-connectedness stated); associated Lie algebroid g = ker(s_*)|_M, anchor dt.
- "Complex Lie algebroid" (Def 2): vector bundle g with bracket, anchor rho: g -> TM^C, Leibniz, and a fibrewise complex structure J on g with vanishing Nijenhuis tensor; g^C = g^{1,0} ⊕ g^{0,1}. (Reading: g is a REAL Lie algebroid with an integrable J; this is NOT the same as "complex Lie algebroid L ⊂ (T⊕T^*)_C".)
- Unimodular (Def 5): global nonvanishing section Omega of L_g = ∧^top T^*M ⊗ ∧^top g (needs to be g-invariant to be a cocycle in H^0(g;L_g)).
- Index Ind_Omega(D) for G-invariant elliptic D (ellipticity = principal symbol invertible on g^*-nonzero covectors).
- Thm 3 (simplified index formula, M compact): Ind_beta(D) = (2πi)^{-k} ∫_M beta ∧ Td^g(g⊗C) ∧ (ch^g(E)-ch^g(F)) / eu^g(g^*). (Theorem 2 = Pflaum–Posthuma–Tang.)
- **Thm 4 (RR for Lie algebroids)**: Ind_Omega(dbar_g + dbar_g^*) = (2πi)^{-k} ∫_M (-1)^{rk g} < ch^g(g^{*p,0}) ch^g(E) Td^g_C(g), Omega_g >. Hypotheses: M compact, elliptic, Omega_g exists (a cocycle). Proof: apply Thm 3 with beta = Phi_g(v), simplify via splitting principle (classical Lawson–Michelsohn identity cannot be quoted directly).
- Thm 5/6: Connes' index theorem and RR for regular complex foliations; Prop 1: Lie algebroid of the holonomy groupoid of a foliation gives same Dolbeault operator, topological indices agree up to (2π)^{-k}.
- Thm 7 (vanishing): kernel of the g-Dolbeault Laplacian on A^{p,q}_g(M,E) vanishes if E positive and p+q>n; E negative and p+q<n.
- Source inconsistencies noted by the fetch: n undefined in Thm 7; sign constants differ ((-1)^{k(k+1)/2} Thm 5, (-1)^{k/2} Prop 1, (-1)^k Thm 6); "unimodular" described two ways. Ellipticity of the Dolbeault operator seems asserted; not checked.

## 3. Does the GC complex fit? [DERIVED unless marked]
GC complex: (∧L^*⊗E, dbar_E), L = +i eigenbundle of J in (T⊕T^*)_C, a COMPLEX Lie algebroid with L ∩ Lbar = 0 and L ⊕ Lbar = (T⊕T^*)_C.
1. Hu needs a real Lie algebroid g with integrable fibrewise J, and complex d_g = ∂_g + dbar_g on ∧ g^{*p,q}. L has no such J: L is already a complex Lie algebroid and ∧L^* is NOT bigraded (p,q) by (g^{1,0}, g^{0,1}) in general (that bigrading, in the complex case, is T^{*0,1} ⊕ T^{1,0}, whose differential mixes only via Higgs field). So (∧L^*, d_L) is not a special case of Hu's (∧g^{*0,q}, dbar_g) in general. -> No direct fit.
2. Where something close does fit: holomorphic Poisson structure sigma on complex X gives holomorphic Lie algebroid A = (T^*X)_sigma. Its underlying real algebroid A_R has an integrable J (Laurent-Gengoux–Stiénon–Xu). Then g := A_R is an object in Hu's setting, with anchor Re(sigma^sharp)-type. But its Dolbeault complex ∧ g^{*0,q} (uses anchor of g^{0,1} = Abar, i.e. sigma-bar) is a DIFFERENT complex from L = T^{0,1} ⋈ A^{1,0} (the GC complex, whose cohomology is holomorphic Poisson cohomology). The GC complex contains T^{0,1} (base antiholomorphic directions) and A (holomorphic algebroid directions); Hu's g-Dolbeault complex uses only g^{0,1} = Abar. [DERIVED; my identification of the two complexes is from the structure of L in LGSX Thm 4.21 only, not rechecked.]
3. The groupoid/ellipticity hypotheses: for g = A_R on CP^2 with the cubic sigma, the real Poisson structure Re/Im sigma has an open symplectic leaf U and D as zero-dim leaves; per cp2_proof_notes.md, Crainic–Fernandes Cor 5.2 gives integrability of Im sigma (isotropy aff(1,C), trivial centre) [CITED via agent, unverified by me]. Ellipticity of dbar_g + dbar_g^* is claimed in Hu without proof; since anchor drops rank along D, g-symbol ellipticity is in terms of g^* (not T^*), so Fredholmness is replaced by groupoid-index (K-theory of C^*(G)), not dim ker.
4. Unimodularity: need a g-invariant Omega in L_g. L_g is trivial here (orientable, ∧^4 g ≅ ∧^4 T^*), but invariance <=> vanishing of the modular class of the real Poisson structure; for log-symplectic structures this class is generally nonzero -> **unknown/likely obstruction** [CONJ, to compute].

## 4. Could the Hu index see c_1(E) or residue data? [DERIVED sketch]
- Hu's index is a number ∫_M <ch^g(g^{*p,0}) ch^g(E) Td^g(g), Omega>, built from Lie-algebroid Chern classes; for E holomorphic (in Hu's sense: ∂bar_g-holomorphic = ordinary holomorphic here) with ordinary connection, ch^g(E) = rho^* ch(E), so it depends on c_1(E)=m·c_1(O(1)) polynomially via rho^*. It need not be constant in m. At degree top (rank_R g = 4) only the degree-2 Chern character pieces enter; pairing rho^*(beta) with an invariant Omega on the symplectic leaf U gives roughly ∫_U beta (up to normalisation) where beta is the top part of ch(E)·(Td^g, ch(g^{*p,0}) classes of g = T^*_C): so one gets a classical-looking integral ∫ ch(E) Td(T^*) ch(∧^p T) with T^* replacing T, i.e. an m-dependent polynomial. [CONJ: heuristic, not computed]
- This index is an index in K_0(C^*(G)) paired with Omega, NOT dim H^even − dim H^odd of the GC complex. In particular it does not coincide with our computed GC invariants, whose total Euler characteristic is 3 for all m (cp2_notes.md, cp2_singular_notes.md). Hence Hu's theorem is not "the" RR for generalized Dolbeault cohomology.
- Residues: the Poisson module structure of O(m) (flat log connection, residue -m/3) is NOT part of Hu's data (E only needs to be g-holomorphic); so residue data does not appear in Hu's formula directly. The GC cohomology dependence on m mod 3 (Casimir sections F^k, monodromy e^{2πim/3}) is invisible to a formula polynomial in m. [DERIVED]

## 5. Conclusions
- Hu's RR is a RR for the real Lie algebroid with complex structure (foliation-like case: Connes), with the groupoid-dependent Ind_Omega. It does not directly apply to the GC complex (∧L^*, d_L), and where it applies (g = A_R) it computes a different operator, with an extra unimodularity hypothesis (modular class).
- Candidate route for a true GC statement: use L ⋈ structure (T^{0,1} ⋈ A^{1,0}) as a complex Lie algebroid and an index theory for complex Lie algebroids (Pflaum–Posthuma–Tang style but without J), or use the real Poisson algebroid and Morita-equivalence from Bailey–Gualtieri (weakly holomorphic symplectic groupoid). Both need work.
- To-do: read the appendices of 2403.10876 (not seen) and the proof of ellipticity in 2403.13424; compute the modular class of the cubic-sigma Poisson structure.
