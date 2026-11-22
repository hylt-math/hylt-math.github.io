---
layout: post
title: "一般化正則直線束のコホモロジーと Riemann–Roch 型公式（Part II）：トーリック多様体・Euler 標数・留数が不等な場合"
short_title: "Part II：トーリック多様体・Euler 標数・Riemann–Roch 型公式"
series: "一般化複素幾何の三種の神器（正則 Poisson 構造の例から）"
series_order: 2
series_label: "Part II"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, トーリック多様体, Riemann-Roch, 研究ノート]
abstract: "Part I の続編。任意次元で全複体の Euler 標数が $$(-1)^n\\,\\mathrm{rk}(E)\\chi(X)$$ になること、トーリック多様体での対数 de Rham 複体のコホモロジーの公式、留数が不等なトーリック曲面の閉公式、一般的な対数シンプレクティック構造をもつトーリック多様体での定理を与える。共鳴や特異点の局所公式は計算に基づく予想を含む。査読を受けていない。"
updated: 2026-11-22
pdf: /assets/pdf/generalized-geometry-poisson-part2-v2-ja.pdf
pdf_version: "v2"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-part2-v2-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-part2-v2-en.pdf' | relative_url }})（日本語版が原本です）。旧版：[v1（日本語）]({{ '/assets/pdf/generalized-geometry-poisson-part2-v1-ja.pdf' | relative_url }})、[v1（英語）]({{ '/assets/pdf/generalized-geometry-poisson-part2-v1-en.pdf' | relative_url }})。
本稿は [Part I]({{ '/2026/11/22/generalized-geometry-poisson/' | relative_url }}) の続きで、**査読を受けていない研究ノート**です。各主張に【証明済】【計算で確認】【予想】【要確認】の区別を付けています。
</div>

## 主な結果

<div class="theorem" data-name="Euler 標数（定理 E）">
$$X$$ をコンパクト複素多様体、$$\sigma$$ を任意の正則 Poisson 構造、$$E$$ を平坦 $$A$$-接続をもつベクトル束とすると
$$
\sum_k(-1)^k\dim\mathbb H^k(E)=(-1)^n\,\mathrm{rk}(E)\,\chi(X).
$$
</div>

全複体の Euler 標数は $$c_1(E)$$ にも留数にも依らず、$$m$$ 依存性は Poincaré 多項式にのみ現れます。

<div class="theorem" data-name="トーリック曲面・留数不等（定理 C2）">
完備なトーリック曲面で対数シンプレクティックな $$\sigma$$ をとり、すべての留数 $$r_i\ne1$$ とする。$$S=\{i: r_i\ge2\}$$、$$V_S$$ を $$S$$ で張られるファンの部分単体複体として、$$\rho\in M$$ のとき
$$
P_{\mathbb H}(t)=\chi(X)\,t^2+(1+t)^2\sum_q\tilde h^{q-1}(V_S)\,t^q
$$
（$$\rho\notin M$$ では $$\chi(X)t^2$$ のみ）。
</div>

<div class="theorem" data-name="トーリック多様体・一般の σ（定理 T）">
滑らかな射影トーリック多様体（偶数次元 $$n$$）上の一般的なトーラス不変な対数シンプレクティック構造で、$$L(D)$$ が ample、$$H^{>0}(\wedge^bT\otimes L)=0$$、すべての $$r_i\ne1$$ のとき
$$
P_{\mathbb H}(t)=[\text{すべての } r_i\in\mathbb Z_{\le0}]\,(1+t)^n+\chi(X)\,t^n.
$$
</div>

各定理には「仮定と、その役割」の表を付けています。246 例（定理 T）、1484 行（定理 C2）で厳密計算との食い違いはありませんでした。

そのほか PDF には、共鳴 $$r_i=1$$ の公式、準斉次な平面曲線特異点の局所公式、留数が不等な三重点の規則（以上は計算に基づく予想）、一般次元の予想、Part I への影響の確認（撤回すべき主張はなし）を含みます。

## 現状

<div class="remark">
Kodaira 埋め込みの一般化と、複素 Lie 亜群 $$L$$ に対する指数定理は得られていません。Cox–Little–Schenck の定理番号などの未確認事項は PDF 末尾に一覧しています。
</div>

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
- 2026-11-22：v2 公開。局所ストークの公式の閾値（$$s<\mathrm{lct}$$）が $$\mathrm{lct}<1/2$$ の特異点で誤っていたため、重みを考慮した規則に差し替えた（10種の特異点で確認、一部は予想）。Part I への影響はない。
- 2026-11-22：局所公式の準斉次な場合（$$s\ne1$$）は、[Part V]({{ '/2026/11/22/generalized-geometry-poisson-part5/' | relative_url }}) で証明された（本記事の PDF v2 では【計算で確認】のまま）。
