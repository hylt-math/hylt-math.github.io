import sys
def rep(fn, old, new, count=1):
    s=open(fn,encoding='utf-8').read()
    n=s.count(old)
    if n!=count:
        print("FAIL",fn,n,old[:60]); sys.exit(1)
    s=s.replace(old,new)
    open(fn,'w',encoding='utf-8').write(s)
    print("ok",fn,old[:40].replace("\n"," "))
P0,P1,P2,P3,P4,P5,P6=[f"part{i}.tex" for i in range(7)]
# ---- part0
rep(P0,r"{\small （査読を受けていない教材。標準的な結果には出典を付け、確認できていないものは\tQ\ で示す。計算例は Python（fractions と自作の多項式・形式的べき級数コード）で検算した。）}",
 r"{\small （外部の査読は受けていない教材。執筆者とは別の AI による独立検査と、可能な範囲の計算での検算は行った。標準的な結果には出典を付け、確認できていないものは\tQ\ で示す。）}")
# ---- part1
rep(P1,r"$c_k(E)\in H^{2k}(X;\Q)$ が定まっていて",r"$c_k(E)\in H^{2k}(X;\R)$（$\Q$ 係数でも同様）が定まっていて")
rep(P1,r"本巻の計算には $\Q$ で十分である。",r"本巻の計算には実（または有理）係数で十分である。")
rep(P1,r"$H^2(\CP^N;\Q)\to H^2(\CP^1;\Q)$ は同型",r"$H^2(\CP^N;\R)\to H^2(\CP^1;\R)$ は同型")
rep(P1,r"つまり、Chern--Weil の定義（第1巻）と公理的な定義（Milnor--Stasheff §14 が Euler 類と Gysin 完全列から作るもの）は、一致する。以後 $c_k(E)$ はどちらでもよい。\tC\ （Milnor--Stasheff の定義が (C3) の符号と一致する正規化をとるかどうかは文献ごとに規約が異なる。本巻は $c_1(\Oc(1))$ が正、すなわちタウトロジー束 $\Oc(-1)$ の $c_1$ が負、という規約に固定する。）",
 r"つまり、Chern--Weil の定義（第1巻）と公理的な定義は（実係数の類として）一致する。以後 $c_k(E)$ はどちらでもよい。Milnor--Stasheff §14 が Euler 類と Gysin 完全列から作る整数係数の類も、符号規約を揃えれば同じものである\tC\ 。ただし符号規約は文献ごとに異なり、Milnor--Stasheff の公理が (C3) と同じ符号をとるかは未確認\tQ\ 。本巻は $c_1(\Oc(1))$ が正、すなわちタウトロジー束 $\Oc(-1)$ の $c_1$ が負、という規約に固定する。")
rep(P1,r"$L$ による捻りで $c_1$ を $0$ か $1$ に正規化できるのは、(b) の $c_1(E\otimes L)=c_1+2l$ による。",
 r"(b) の $c_1(E\otimes L)=c_1(E)+2l$ により、$L$ を取り替えて $c_1(E)$ を $2$ を法とする類だけに（曲線上なら次数を $0$ か $1$ に）正規化できる。")
rep(P1,r"（Griffiths--Harris, 第1章の第1 Chern 類の節、Poincaré--Lelong 公式）",r"（Griffiths--Harris の Poincaré--Lelong 公式の節。章・節番号は\tQ\ ）")
rep(P1,r"一般の四次曲面では $\rho=1$（$\Oc(1)$ の生成、Noether--Lefschetz\tC\ ）",r"非常に一般の四次曲面（$\CP^3$）では $\rho=1$（Picard 群は $\Oc(1)$ で生成される、Noether--Lefschetz\tC\ ）")
rep(P1,r"（Hartshorne, 付録 A；Fulton, \emph{Intersection Theory}, 第3章\tQ\ ）",r"（Hartshorne, 付録 A；Fulton, \emph{Intersection Theory}, 第3章）")
# ---- part2
rep(P2,r"つまり、「$X$ の HRR」から「$D$ の HRR」が、完全列",r"つまり、「$X$ の（連接層 $F\otimes\Oc_D$ に対する）HRR」から「$D$ の HRR」が、完全列")
# ---- part3
rep(P3,r"（Milnor--Stasheff §18）。Hirzebruch の HRR",r"（Milnor--Stasheff §17--§19。節の対応は未確認\tQ\ ）。Hirzebruch の HRR")
rep(P3,r"その指数は Hodge 理論（第5巻）と Dolbeault の定理（第3巻）により $\chi(X,E)$ に等しい。",r"その指数は $\dbar$ ラプラシアンの Hodge 理論（第5巻。Kähler 性は不要）と Dolbeault の定理（第3巻）により $\chi(X,E)$ に等しい。")
rep(P3,r"F.~Hirzebruch, \emph{Topological Methods in Algebraic Geometry}（第III章〜第IV章あたり\tQ\ ）。",r"F.~Hirzebruch, \emph{Topological Methods in Algebraic Geometry}（第3版の目次では第4章 The Todd genus と第5章 The Riemann--Roch theorem for algebraic manifolds。版により章番号が異なる）。")
rep(P3,r"Fulton, \emph{Intersection Theory}, 第15章\tQ\ ；Hartshorne, 付録 A。",r"Fulton, \emph{Intersection Theory}, 第15章（Riemann--Roch for Non-singular Varieties）；Hartshorne, 付録 A。")
rep(P3,r"（Fulton, \emph{Intersection Theory}, 第18章\tQ\ ）",r"（Fulton, \emph{Intersection Theory}, 第18章）")
# ---- part4
rep(P4,r"$F_a$ のすべては複素構造の変形で連結（$a$ の偶奇のみが微分同相型を決める）\tC\ という事実とも整合する。",
 r"$F_a$ は $F_{a-2}$ に変形する（同じ偶奇の $F_a$ は複素構造の変形でつながる）が、$F_0$ と $F_1$ は交叉形式の偶奇が違い変形でつながらない（$a$ の偶奇のみが微分同相型を決める）\tC\ という事実とも整合する。")
rep(P4,r"$m$ 個の点が $m$ 個の独立な 1 次条件を与える}という期待どおりの値で、$\chi(L)\le h^0(L)$ は条件の独立性が（$h^1(L)=0$ なら）成り立つことと同値である。（実際の $h^0$ は $h^1(L),h^2(L)$ に依る。",
 r"$m$ 個の点が $m$ 個の独立な 1 次条件を与える}という期待どおりの値である。$h^2(L)=h^0(K_X-L)=0$ なので $h^0(L)=\chi(L)+h^1(L)\ge\chi(L)$ で、等号は $h^1(L)=0$、すなわち点が独立な条件を与えることと同値である。（実際の $h^0$ は $h^1(L)$ に依る。")
rep(P4,r"$-\infty$ & $\CP^2$、線織曲面（$\CP^1$ 束、$F_a$） & 有理曲面：$K^2=9-m$（$m$ 点の爆発）、$\chi=1$\\",
 r"$-\infty$ & $\CP^2$、線織曲面（$\CP^1$ 束、$F_a$） & 底が種数 $g$ の線織曲面の $m$ 点爆発：$K^2=8(1-g)-m$、$\chi=1-g$（有理曲面は $g=0$。$\CP^2$ の $m$ 点爆発は $K^2=9-m$）\\")
rep(P4,r"から、$K_X$ は底の曲線の因子の引き戻しなので $K_X^2=0$。",r"から、$K_X$ は底の曲線の因子の引き戻し（重複ファイバーがあるときはさらにその成分の有理数倍）なので $K_X^2=0$。")
rep(P4,r"$H^2$ はそれぞれ $4,6,8$（Python：$e=24$、$c_1=0$）。",r"超平面類の自己交点 $H^2$ はそれぞれ $4,6,8$（Python：$e=24$、$c_1=0$）。")
# ---- part5
rep(P5,r"Dirac 作用素は（定数倍を除き）$\dbar+\dbar^*$ を $K^{1/2}$ で捻ったものになる\tC\ 。",r"Dirac 作用素は、Kähler なら（定数倍を除き）$\dbar+\dbar^*$ を $K^{1/2}$ で捻ったものに一致する（一般の Hermite 多様体では主シンボルが一致し、指数は等しい）\tC\ 。")
rep(P5,r"（「$\bar\partial$ または $d_\sigma$ の複体」という記述は不正確で、複体の微分は $d_E=[\sigma,\cdot]+V\wedge$、$\bar\partial$ は Dolbeault 分解で計算するときの方向である。第3巻。）",
 r"複体の微分は $d_E=[\sigma,\cdot]+V\wedge$ であって $\bar\partial$ ではない。$\bar\partial$ は、各項を Dolbeault 分解して超コホモロジーを計算するときの方向の微分である（Dolbeault モデル $D=\bar\partial+d_K$、論文の命題 6(b)、第3巻）。$\mathbb H^k(E)$ を「一般化 Dolbeault コホモロジー」と同一視する命題 6(b) は論文自身が Mokri の定理などに依存する【要確認】の部分とするが、本節の Euler 標数の計算は超コホモロジー $H^k(X;C(A;E))$ だけを使う。")
# ---- part6
rep(P6,r"第8巻で Atiyah--Singer の指数定理 $\ind D=\int\ch(\sigma(D))\Td(TM\otimes\C)/e(TM)$ を学ぶと",r"第8巻で Atiyah--Singer の指数定理 $\ind D=\pm\int\ch(\sigma(D))\Td(TM\otimes\C)/e(TM)$（符号・向きの規約は第8巻で正確に述べる。複素多様体では \S\ref{sec:hrr} のとおり $(-1)^n$ がつく）を学ぶと")
rep(P6,r"\item 論文の「Riemann--Roch 型公式」「指数予想」：HRR と Atiyah--Singer（第8巻）の枠組みで述べられる。\tQ\ （対応の細部は未確認。第13--14巻で扱う。）",
 r"\item 論文の「Riemann--Roch 型公式」「指数予想」：論文の一覧表では、Poincaré 多項式の公式（曲面：定理 34、一般次元：定理 92）が「Riemann--Roch 型」、指数定理による統一が予想 94（指数予想、未証明）、一般の一般化複素構造での全 Euler 標数は注意 24（予想）である。本巻はこれらを扱わず、HRR と Atiyah--Singer（第8巻）の枠組みとの関係は第13--14巻で扱う。\tQ\ （論文の一覧表を見ただけで、各主張の内容の再導出は未実施。）")
rep(P6,r"（通分：$-\frac{10}{720}+\frac{15}{720}-\frac6{720}\cdot$ ... $=-\frac{1}{720}$）",r"（通分：$-\frac{10}{720}+\frac{15}{720}-\frac6{720}=-\frac1{720}$）")
rep(P6,r"証明は手計算で書き、執筆者による再読のみで、独立の査読は受けていない。",r"証明は手計算で書いた。外部の査読は受けていないが、執筆者とは別の AI による独立検査を受け、別実装の Python（\texttt{fractions}、一変数形式的べき級数と乱数の Chern 根）で上記の数値・公式を再計算した。")
