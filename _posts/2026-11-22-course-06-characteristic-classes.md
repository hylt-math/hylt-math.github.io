---
layout: post
title: "学習コース 第6巻　特性類と Hirzebruch–Riemann–Roch の定理"
short_title: "第6巻：特性類と Hirzebruch–Riemann–Roch の定理"
series: "学習コース：一般化幾何への道"
series_order: 6
series_label: "第6巻"
status: textbook
tags: [学習コース, 教科書, 問題集]
abstract: "Chern 類、Chern 指標、Todd 類、Pontryagin 類・Euler 類、Hirzebruch–Riemann–Roch の定理とその応用（曲線・曲面・超曲面・K3・Calabi–Yau）、符号定理と Â 種数を、問題40問と全問の解答つきでまとめた第6巻。統合論文の Euler 標数の定理を HRR から再構成する節を含む。"
pdf: /assets/pdf/course-06-v1-ja.pdf
pdf_version: "v1"
---

企画：森　／　執筆：Claude

<div class="remark">
日本語の教科書と問題集です（40ページ）。各節の末尾に問題（[基本][標準][発展]）があり、**全問の解答**と自己診断10問、参考文献が付いています。外部の査読は受けていません。執筆とは別の AI による独立検査と、可能な範囲の計算での検算は行いました。確認できていない出典・記述は PDF 中で【要確認】と示しています。全体の計画は[学習地図]({{ '/2026/11/22/course-00-map/' | relative_url }})にあります。
</div>

## この巻の内容

- Chern 類（公理、Chern–Weil との一致、splitting principle）、Chern 指標、Todd 類
- Pontryagin 類・Euler 類、Chern–Gauss–Bonnet
- Hirzebruch–Riemann–Roch の定理（主張と証明の方針、P^n 上での完全な検証）
- 曲線・曲面への応用（Noether の公式、曲面の Riemann–Roch）、超曲面・K3・複素トーラス・Calabi–Yau 3次元
- χ_y 種数、符号定理、Â 種数と Dirac 作用素（第8巻への橋渡し）
- 統合論文の Euler 標数の定理（全 Euler 標数が c_1(E) に依らない）の再構成
- 問題40問、全問に解答、自己診断10問

## 検査の状況

- 全40問の解答を、別の AI が、元のコードを使わず乱数の Chern 根と Bernoulli 数から組んだ別実装の Python で解き直し、数値の誤りはありませんでした。直したのは次の点です：Chern 類の公理の係数（Q 係数と実係数の不整合）、「Hirzebruch 曲面は すべて変形でつながる」という誤り（同じ偶奇のものだけ）、「χ(L)≤h^0(L) が同値」という誤り（等号の場合のみ）、曲面の分類表の線織曲面の χ、楕円曲面の正準束公式の補正、問11の解答の組版。
- 統合論文との対応の節は、論文の定理22・注意23・定理25・定義5・命題6と照合し、過大な主張や番号の誤りはありませんでした。ただし命題6(b) は論文自身が【要確認】としています。
- 引用のみ（検算なし）：splitting principle、Leray–Hirsch、HRR 本体、符号定理、Hodge–Riemann、Rokhlin。
- 【要確認】のもの：Griffiths–Harris と Bott–Tu の章・節番号、Milnor–Stasheff の公理3の符号。

## 改訂履歴

- 2026-11-22：v1 公開。
