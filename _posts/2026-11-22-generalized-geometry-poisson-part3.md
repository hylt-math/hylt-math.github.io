---
layout: post
title: "一般化正則直線束のコホモロジーと Kodaira 型定理（Part III）：断面による埋め込みの不可能性、葉空間版 Kodaira、Poisson–Kodaira 予想"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Kodaira埋め込み, 研究ノート]
abstract: "三種の神器の残り、Kodaira の埋め込み定理の一般化を考える。一般化正則断面による埋め込みは一般には不可能であることを示し、正則型では葉空間への Kodaira 埋め込みに帰着する定理を得た。代わりの定式化として Poisson–Kodaira 予想を提案し、トーリックの場合を証明した。非被約な境界の例も計算した。査読を受けていない。"
pdf: /assets/pdf/generalized-geometry-poisson-part3-v1-ja.pdf
pdf_version: "v1"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-part3-v1-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-part3-v1-en.pdf' | relative_url }})（日本語版が原本です）。
[Part I]({{ '/2026/11/22/generalized-geometry-poisson/' | relative_url }})、[Part II]({{ '/2026/11/22/generalized-geometry-poisson-part2/' | relative_url }}) の続編です。本稿は**査読を受けていない研究ノート**で、各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。Mumford の二次式定理と Baily の軌道体の埋め込み定理は記憶からの引用で、未確認です。
</div>

## 主な結果

古典の Kodaira の埋め込み定理は、正の直線束 $$L$$ の正則断面で $$X\to\mathbb P^N$$ を作ります。一般化複素幾何では、一般化正則（GH）断面の空間が小さすぎて、同じ手順は通りません。

<div class="proposition" data-name="断面による埋め込みの不可能性">
$$\sigma$$ が稠密な開集合で非退化なら、一般化正則断面の空間 $$\mathrm{HH}^0(L)$$ の次元は高々 1 である。したがって、GH 断面が定める写像は定数であり、埋め込みにはならない。正則型で型 $$k<n$$ の場合も、GH 断面は葉に沿って定数なので、写像は埋め込みにならない。
</div>

例：$$\mathbb{CP}^2$$ の3次曲線に沿って消える $$\sigma$$ では、Casimir $$F^k$$ が現れるのは $$m=3k$$ のときだけです。

<div class="theorem" data-name="葉空間版 Kodaira">
正則型の一般化複素多様体 $$M$$ の葉がコンパクトで連結なファイバーをなし、葉方向のホロノミーが自明で、葉空間 $$X$$ 上の直線束 $$L_X$$ が豊富であるとする。このとき、GH 断面が定める写像は、古典の Kodaira 埋め込み $$X\hookrightarrow\mathbb P^N$$ と射影 $$M\to X$$ の合成である。
</div>

これは古典の定理への簡単な帰着で、文献には見つかりませんでした。

## Poisson–Kodaira 予想

代わりの定式化として、$$(X,\sigma)$$ を Kodaira 埋め込みで $$\mathbb P^N$$ に入れたとき、$$\sigma$$ が $$\mathbb P^N$$ 上の Poisson 構造の制限になるか、という問題を考えます。

- **証明済み**：トーラス不変な $$\sigma$$ に対して、非常に豊富な $$\mathcal O(m)$$ はすべて、対角的な2次 Poisson 構造への Poisson 埋め込みになる。
- **計算で確認**：$$\mathbb P^2$$（Veronese $$m=2$$、$$F=xyz$$、Fermat、Hesse、尖点）で、$$\mathbb P^5$$ への2次の Poisson 拡張が存在する。
- **予想**：$$m\gg0$$ なら、任意の $$(X,\sigma)$$ の Kodaira 埋め込みは Poisson 埋め込みになる。

## 非被約な境界と局所項

$$\mathbb P^2$$ で $$D=\{x^2y=0\}$$ のとき、$$m\ge-2$$ で Poincaré 多項式は $$[3\mid m](1+t)+3t^2+(m+2)(t+t^2)$$ となり、31個の値と一致します（計算で確認）。一般の形は予想です。また、準斉次な特異点の局所ストークについて、Part II の閾値の規則（$$\mathrm{lct}<1/2$$ で誤り）を重みを考慮した規則に訂正しました（Part II v2 も参照）。

<div class="remark">
Pal–Poddar の定理 11.12 は、正の強一般化正則束に対する消滅定理で、埋め込みの主張は含みません。一般の一般化複素構造に対する Kodaira 埋め込みの結果は、調査した範囲では見つかっていません。
</div>

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
