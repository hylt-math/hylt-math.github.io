# Part I (v2) corrections check after Part II v2 (local formula fix)
- Part I v2: no statement invalidated. Local rule [s<lct] in v1/Part II v1 is wrong only for lct<1/2; all types in Part I §6.6 (A_k, D_k, E_6, E_8, T_{2,3,6}) have lct>=1/2 where old and new rules agree.
- Triple-point sum rule (s1+s2+s3<2) is consistent with the new rule at equal residues for D_4 (checked s in (1/3)Z, -10<=3s<=10, s!=1: 0 mismatches).
- Only recommended wording change in Part I at next revision: Obs. 6.7 clarity (already noted); mention that the local formula is verified for listed types only.

# Part II v2: status upgrade for the local formula (added by Part V writer)
Part V (Thm local, paper5/body_ja.tex §5) proves R(s) for quasi-homogeneous isolated plane-curve germs, s≠1 (weight-k0 piece; K via df∧dh=0 and Euler contraction; dim Cok via Hilbert series). Recommended for next revision of Part II (obs:stalk, ledger row ~line 243 of paper2_v2/body_ja.tex):
- Replace tags 【計算で確認】【予想】 by 【証明済】 for "quasi-homogeneous, s≠1", with the caveat 【要確認】 on (i) sign convention of s in B_s≅(Ω(log D), d+s dlog h), (ii) formal vs convergent weight decomposition.
- Proposed text: 「$h$ が準斉次な孤立特異点で $s\ne1$ のとき、この公式は Part V 定理 \ref{thm:local} で証明された\tP（$s$ の符号規約と収束の扱いは\tQ）。準斉次でない場合と $s=1$ は未証明\tK。」
- Delete the "未証明：Wang 完全列との一致" bullet for quasi-homogeneous germs (still open for non-q.h.). Part I v2 needs no change.
