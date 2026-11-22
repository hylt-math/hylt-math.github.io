import sys
src=open('rev/apply.py').read().split("# ---- part0")[0]
exec(src)
rep(P5,r"複体の微分は $d_E=[\sigma,\cdot]+V\wedge$ であって $\bar\partial$ ではない。$\bar\partial$ は、各項を Dolbeault 分解して超コホモロジーを計算するときの方向の微分である（Dolbeault モデル $D=\bar\partial+d_K$、論文の命題 6(b)、第3巻）。$\mathbb H^k(E)$ を「一般化 Dolbeault コホモロジー」と同一視する命題 6(b) は論文自身が Mokri の定理などに依存する【要確認】の部分とするが、本節の Euler 標数の計算は超コホモロジー $H^k(X;C(A;E))$ だけを使う。",
 r"$\bar\partial$ は複体の微分ではなく、各項を Dolbeault 分解して超コホモロジーを計算するときの方向の微分である（Dolbeault モデル $D=\bar\partial+d_K$、論文の命題 6(b)、第3巻）。$\mathbb H^k(E)$ を一般化 Dolbeault コホモロジーと同一視する命題 6(b) は、論文自身が Mokri の定理などに依存する部分として\tQ\ としているが、本節の Euler 標数の計算は超コホモロジー $H^k(X;C(A;E))$ だけを使う。")
# references
rep(P6,r"コボルディズム（§17--§18）、符号定理（§19）。節番号は目次の記憶による\tQ\ 。",r"Chern 数・Pontryagin 数（§16）、コボルディズム（§17--§18）、符号定理（§19）。節番号は出版社の目次で確認した（細部の対応は未確認）。")
rep(P6,r"Euler 類（§9、§11）",r"Euler 類（§9、§11）")
rep(P6,r"HRR、Todd 類、$\chi_y$ 種数。章番号\tQ\ 。",r"HRR、Todd 類、$\chi_y$ 種数。第3版の目次では第4章（Todd genus）、第5章（HRR）。$\chi_y$ 種数の章は\tQ\ 。")
rep(P6,r"第3章（Chern 類、Riemann--Roch）、第0章（Poincaré--Lelong）。\tQ\ （節番号）",r"Chern 類、Poincaré--Lelong 公式、Riemann--Roch を含む。\tQ\ （章・節番号）")
rep(P6,r"第5章（HRR と応用）。\tQ\ （章題）",r"第5章（Applications of Cohomology）の HRR の節。Chern 類の章は\tQ\ 。")
rep(P6,r"Chern 類、Riemann--Roch。\tQ\ （章番号）",r"第3章（Chern 類）、第15章（非特異多様体の Riemann--Roch）、第18章（特異多様体）。出版社の目次で確認した。")
rep(P6,r"第IV章あたり（Leray--Hirsch、splitting principle、Chern 類）\tQ\ 。",r"§5（Leray--Hirsch）、第IV章（Chern 類、splitting principle）。\tQ\ （節・章番号は記憶による）")
