---
layout: post
title: "一般化正則直線束のコホモロジー（Part IV）：正則型（Gauss–Manin）と対数シンプレクティック型の比較、一般次元の簡約定理"
short_title: "Part IV：正則型と対数シンプレクティック型の比較・簡約定理"
series: "一般化複素幾何の三種の神器（正則 Poisson 構造の例から）"
series_order: 4
series_label: "Part IV"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Gauss–Manin, Riemann-Roch, 研究ノート]
abstract: "正則型（葉がシンプレクティック）では各次数のコホモロジーの次元が $$m$$ の多項式になり、対数シンプレクティック型では周期的になることを対比する。一般次元の対数シンプレクティックな場合に、局所条件のもとでコホモロジーを $$H^*(U;L_U)$$ と境界の角の項に簡約する定理を証明した。査読を受けていない。"
pdf: /assets/pdf/generalized-geometry-poisson-part4-v1-ja.pdf
pdf_version: "v1"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-part4-v1-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-part4-v1-en.pdf' | relative_url }})（日本語版が原本です）。
[Part I]({{ '/2026/11/22/generalized-geometry-poisson/' | relative_url }})、[Part II]({{ '/2026/11/22/generalized-geometry-poisson-part2/' | relative_url }})、[Part III]({{ '/2026/11/22/generalized-geometry-poisson-part3/' | relative_url }}) の続編です。本稿は**査読を受けていない研究ノート**で、各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。
</div>

## 主な結果

<div class="theorem" data-name="正則型の分解（定理 L）">
$$Y\to M\to X$$ を、コンパクトで連結な、hard Lefschetz をみたすシンプレクティックファイバーをもつ平坦束、$$E=\pi^*G$$ とする。このとき
$$
\mathrm{HH}^k(M,E)=\bigoplus_{a+b+j=k}H^a\bigl(X,\ \wedge^bT_X\otimes V^j\otimes G\bigr)
$$
である。ここで $$V^j$$ は Gauss–Manin の平坦束である。
</div>

Leray の二重複体が $$E_2$$ で退化することは、Deligne の Lefschetz の補題から従います。

<div class="corollary" data-name="次数別の Riemann–Roch">
$$G$$ が豊富で $$m\ge m_0$$ ならば、
$$
\dim\mathrm{HH}^k=\sum_{b+j=k}b_j(Y)\int_X\mathrm{ch}(\wedge^bT_X)\,e^{m c_1(G)}\,\mathrm{Td}(X).
$$
</div>

正則型では、各次数 $$k$$ で $$m$$ の多項式です。対数シンプレクティックの場合は、$$d_1=[\sigma,\cdot]$$ がほぼ完全なので、多項式ではなく周期的になります。これが Part I で見た周期3の跳びの本質のようです。Pal–Poddar の定理 11.12(2) を $$E'=\wedge^bT_X\otimes V^j$$ に適用すると、横断次数での消滅が得られ、本稿の読みと一致します。

<div class="theorem" data-name="簡約定理（定理 R）">
一般次元の、単純正規交差の境界 $$D$$ に沿って対数シンプレクティックな $$\sigma$$ と、留数がどれも $$\mathbb Z_{\ge1}$$ に入らない Poisson 加群 $$L$$ を考える。$$0<|T|<n$$ のすべての層で商複体 $$Q_T$$ が完全ならば、
$$
\mathbb H^*\cong H^*(U;L_U)\oplus\mathbb C^{\#D_{(n)}}[-n]
$$
である。ここで $$D_{(n)}$$ は $$D$$ の $$n$$ 重点の集合である。
</div>

追加の仮定（豊富性や消滅）は不要です。$$Q_T$$ の完全性が破れる場合は、予想からずれます（$$\mathbb P^2\times\mathbb P^2$$ のブロック積の場合、ずれはちょうど $$6t^2(1+t)^2$$）。

## 計算による確認

- Kodaira–Thurston 多様体：Poincaré 多項式 $$(1,3,4,3,1)$$（Nomizu 型の定理を仮定）。
- Bieberbach 商：$$(1,2,2,2,1)$$。
- $$\mathbb P^2\times\mathbb P^2$$、$$(\mathbb P^1)^4$$、$$\mathbb P^4$$ などで、定理 R の条件を満たす48個の場合がすべて一致。

<div class="remark">
正則な範疇での対数 Darboux の標準形は、実の場合の文献しか引用できておらず、【要確認】です。$$Q_T$$ の完全性が、$$\nu_T$$ がどこでも 0 にならないことから従うかは、線形化できない $$\sigma$$ では未証明です。
</div>

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
- 2026-11-22：定理 R の追加条件に関する $$H^k(U;L_U)$$ の消滅は、非整数留数の場合に [総合版]({{ '/2026/11/22/generalized-geometry-poisson-main/' | relative_url }})の定理 V で証明された。
