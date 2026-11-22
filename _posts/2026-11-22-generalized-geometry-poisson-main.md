---
layout: post
title: "一般化複素幾何の「三種の神器」へのアプローチ：正則 Poisson 構造の例から（総合版：Part I–V）"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Riemann-Roch, Serre消滅, Kodaira埋め込み, 総合版]
abstract: "複素幾何の三種の神器（Riemann–Roch、Serre 消滅、Kodaira 埋め込み）の一般化複素幾何版を、正則 Poisson 構造の $$\\beta$$-変換から得る型が跳ぶ一般化複素構造と一般化正則直線束の例から調べた Part I–V の総合版。80ページ。各主張に証明済・文献・計算・予想の区別と、仮定の役割の表を付けた。査読を受けていない。"
pdf: /assets/pdf/generalized-geometry-poisson-main-v1-ja.pdf
pdf_version: "v1"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-main-v1-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-main-v1-en.pdf' | relative_url }})（日本語版が原本です）。
本稿は [Part I]({{ '/2026/11/22/generalized-geometry-poisson/' | relative_url }})〜[Part V]({{ '/2026/11/22/generalized-geometry-poisson-part5/' | relative_url }}) を**1つの PDF にまとめた総合版**です。新しく書き下ろしたのは、冒頭の序論と読み方、番号の統一、末尾の整合性・未解決問題・検証範囲の節、および補遺（定理 V など）で、全体の約7〜8ページです。残りは Part I–V の本文を、番号を付け替えて収めたものです。短く書き直した論文ではありません。**査読を受けていない研究ノート**で、各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。
</div>

## 三種の神器の現状

| 神器 | 現状 |
|---|---|
| Serre 消滅 | 「横断次数での消滅」を任意次元で証明。双対性も任意次元で証明。 |
| Riemann–Roch | 全 Euler 標数は $$(-1)^n\mathrm{rk}(E)\chi(X)$$ で $$c_1$$ によらない（証明済）。曲面・トーリックでは Poincaré 多項式を留数で書き下した。一般次元は簡約定理（条件 (GEN′) つき）。指数定理は予想。 |
| Kodaira 埋め込み | 一般化正則断面による埋め込みは不可能であることを証明。正則型では葉空間版を証明。Poisson–Kodaira はトーリックで証明、一般は予想。 |

## 補遺：Part V の穴が埋まった

<div class="theorem" data-name="定理 V">
$$D$$ が単純正規交差で、$$U=X\setminus D$$ がアフィンであり、どの留数 $$r_i$$ も整数でないならば、任意の $$n\ge1$$ について、$$k\ne n$$ で $$H^k(U;L_U)=0$$ である。
</div>

これと簡約定理（Part IV の定理 R）から、$$r_i\notin\mathbb Z$$ のとき $$\mathbb H^*=\chi(X)\,t^n$$ が従います。Part V で未解決としていた $$n>2$$ の場合は、これで解決しました。

## 整合性についての注意

Part II–V の PDF に残っている記述のうち、次の点は総合版で整理しました。Part II の状態表では局所公式が観察・予想のままですが、Part V で $$s\ne1$$ の準斉次の場合は証明されています。Part III と Part V に別の「定理 K1」があります。Part IV・V で未解決とした $$H^k(U;L_U)$$ の消滅は、非整数留数の場合は定理 V が解決しました。Part II–V が引用する Part I の定理番号は、番号付け替えのとき機械的に書き換えており、すべてを確認したわけではありません。Hu の第2論文の題名は、Part 間で統一したが、題名自体は未確認です。

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
