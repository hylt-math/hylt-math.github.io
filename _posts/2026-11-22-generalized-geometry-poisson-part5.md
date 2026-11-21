---
layout: post
title: "一般化正則直線束のコホモロジー（Part V）：Riemann–Roch 型公式と指数定理の予想、準斉次特異点の局所公式の証明"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Riemann-Roch, 指数定理, 研究ノート]
abstract: "対数シンプレクティックな場合の Riemann–Roch 型の公式として、Euler 標数が $$\\chi(U)$$ に等しいこと、Poincaré 多項式を $$H^*(U;L_U)$$ で書く公式を示し、次元が $$m$$ の多項式にならない理由を説明する。準斉次な特異点の局所公式も証明した。留数を重みとする指数定理を予想として述べる。査読を受けていない。"
pdf: /assets/pdf/generalized-geometry-poisson-part5-v1-ja.pdf
pdf_version: "v1"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-part5-v1-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-part5-v1-en.pdf' | relative_url }})（日本語版が原本です）。
[Part I]({{ '/2026/11/22/generalized-geometry-poisson/' | relative_url }})、[II]({{ '/2026/11/22/generalized-geometry-poisson-part2/' | relative_url }})、[III]({{ '/2026/11/22/generalized-geometry-poisson-part3/' | relative_url }})、[IV]({{ '/2026/11/22/generalized-geometry-poisson-part4/' | relative_url }}) の続編です。本稿は**査読を受けていない研究ノート**で、各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。
</div>

## 主な結果

<div class="theorem" data-name="定理 K1">
対数シンプレクティックな $$\sigma$$ をもつ $$X$$ について、対数 de Rham 複体の Euler 標数は $$\chi(X;\mathrm{DR}_{\log}(L))=\int_X c_n\bigl(T(-\log D)\bigr)=\chi(U)$$ であり、$$L$$ によらない。さらに $$\chi_c(U;L)=\chi(U;L)$$（壁越えの恒等式）が成り立つ。
</div>

<div class="theorem" data-name="定理 K（Poincaré 多項式）">
$$U$$ がアフィンで $$n$$ が偶数、定理 R（Part IV）の仮定のもとで、
$$
P_{\mathbb H}(t)=\chi(X)\,t^n+\sum_{k<n}h^k(U;L_U)\bigl(t^k-(-1)^kt^n\bigr).
$$
</div>

次元の $$m$$ への依存は、次数0の部分を除いて、留数の条件（周期的なもの）だけです。次の3つの振る舞いが対比されます。

| 設定 | 次元の $$m$$ 依存 |
|---|---|
| 正則型（Part IV） | 各次数 $$k$$ で $$m$$ の多項式 |
| 対数シンプレクティック型 | 周期的（留数の条件） |
| 全 Euler 標数 | $$m$$ によらない |

<div class="theorem" data-name="局所公式（準斉次な特異点）">
準斉次な孤立平面曲線の特異点で、$$s\ne1$$ のとき、局所ストークの多項式は $$R(s)+\mu t^2$$ で、
$$
R(s)=[s\in\mathbb Z,\,s\le0](1+t)+(t+t^2)\cdot\#\{\alpha\in\mathrm{Spec}:\ s+\alpha\in\mathbb Z,\ s+\alpha\le1\}.
$$
</div>

重みの部分に分解し、Hilbert 級数の恒等式で次元を数えて証明しました（Part II v2 の計算での確認を、証明に格上げしたものです）。14種類の特異点で、正確な有理数計算と食い違い0です。

## 指数定理の予想

重み付き $$b$$-計算で、一般化 Dolbeault 作用素が Fredholm になるのは留数 $$r\notin\mathbb Z$$ のときで、指数は $$\chi(U)$$ であり、$$r\in\mathbb Z$$ では指数が $$H^*(\partial U;L)$$ だけ跳ぶ、と予想します（APS の壁越えの三角形と同じ構造）。Hu の Lie 亜群版の Riemann–Roch は、この複体には適用できません。証明には、対数接 Lie 亜群上の指数理論が必要で、これは存在しません。

<div class="remark">
**未確認・未証明の点**：$$s$$ の符号の規約と、形式的な重み分解から収束する複体への移行は、データでのみ確認しています。定理 K は、$$n>2$$ では定理 R の【要確認】を引き継ぎます。$$r\notin\mathbb Z$$ かつ $$n>2$$ のとき、定理 K は $$\chi(X)t^n$$ をまだ再現せず（$$k<n$$ で $$H^k(U;L_U)=0$$ を示していないため）、この点は未解決です。
</div>

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
