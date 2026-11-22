---
layout: post
title: "一般化複素幾何の「三種の神器」へのアプローチ：正則 Poisson 構造の例から（統合論文）"
short_title: "統合論文：全体を主題別に書き直した1本（49ページ）"
series: "一般化複素幾何の三種の神器（正則 Poisson 構造の例から）"
series_order: 0
series_label: "統合論文"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Riemann-Roch, Serre消滅, Kodaira埋め込み, 統合論文]
abstract: "Part I–V の結果を、Part ごとの並びではなく主題別（Serre 型消滅と双対性、Euler 標数、対数シンプレクティック曲面、トーリックと局所項、一般次元の簡約定理、正則型との比較、Kodaira 型、Riemann–Roch 型公式と指数予想）に書き直した1本の論文。重複を整理し、番号を通し番号にし、状態表と記号表を1つにまとめた。査読を受けていない。"
pdf: /assets/pdf/generalized-geometry-poisson-unified-v1-ja.pdf
pdf_version: "v1"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-unified-v1-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-unified-v1-en.pdf' | relative_url }})（日本語版が原本で、英語版は翻訳です）。
本稿は**査読を受けていない研究ノート**です。各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。
</div>

## この論文について

先に公開した[総合版]({{ '/2026/11/22/generalized-geometry-poisson-main/' | relative_url }})（80ページ）は Part I–V を1冊にまとめた合本でした。本稿はそれを主題別に1本の論文として書き直したものです（日本語49ページ、英語51ページ）。証明を載せた主張は本文で証明し、省いたものは根拠のスクリプト名を明記して【計算で確認】にとどめています。状態タグは、本文の証明の範囲を超えて格上げしていません。

## 主な結果

- 一般化正則直線束は Poisson 加群であり、対数シンプレクティックなら留数が定数の平坦な対数接続になる。
- Serre 型の消滅は横断次数でのみ成り立つ。双対性 $$\mathbb H^k(L)^*\cong\mathbb H^{2n-k}(L^\vee\otimes K^2)$$ は任意次元で成り立つ。
- 全 Euler 標数は $$(-1)^n\mathrm{rk}(E)\chi(X)$$ で、$$c_1$$ に依らない。
- 対数シンプレクティック曲面・トーリック多様体では Poincaré 多項式が留数で書ける。準斉次な孤立特異点の局所公式を $$s\ne1$$ で証明した。
- 一般次元は、商複体の条件 (GEN$$_Q$$) のもとで簡約定理に帰着する。全留数が非整数で $$U$$ がアフィンなら $$H^k(U;L_U)=0\ (k\ne n)$$（定理 V）。
- Kodaira 型：一般化正則切断による埋め込みは不可能。葉空間版の Kodaira とトーリックでの Poisson–Kodaira を示した。

<div class="remark">
**未確認・未証明の点**：(GEN$$'$$) から (GEN$$_Q$$) を導く段（命題 55）は【要確認】のままです。簡約定理（定理 59）は (GEN$$_Q$$) を直接の仮定とするので、この命題には依存しませんが、仮定の言い換えとして残っています。ほかに、LGSX・Mokri に依存する Poisson 加群の同定、双対性の Koszul 符号の整合（手計算のみ）、Gauss–Manin との同定が【要確認】です。一般の Poisson–Kodaira 予想と指数予想は未証明です。大規模な表（トーリック、三重点など）の計算は、総合版の記録の転記で、今回は再実行していません。文献の多くは原典での適用範囲を確認していません。PDF の目視確認は一部のページのみです。
</div>

## 総合版からの変更

- 局所公式の証明を $$(e,\chi_h)$$ 基底による短い証明に書き換え、旧版の規則 $$[s<\mathrm{lct}]$$ が $$\mathrm{lct}<1/2$$ で誤りであることを明記した。大域の精密化予想は $$\mathrm{lct}\ge1/2$$ に限定した。
- 簡約定理の証明を、濾過に依らない形（連鎖写像が擬同型という仮定 (GEN$$_Q$$)）に書き直した。
- 記号の衝突（$$\rho$$）と、2つの「定理 K1」の名前の重複を解消した。
- 変更の全体は PDF 付録 A に載せている。

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
- 2026-11-22：予想 91 の「$$\mathbb P^2$$、$$m\ge3$$ は未計算」は、[Part VI]({{ '/2026/11/22/generalized-geometry-poisson-part6/' | relative_url }})で $$m=3$$ を計算した結果（非トーリックで拡張は数値的に見つからない）に更新される。PDF は未改訂。
