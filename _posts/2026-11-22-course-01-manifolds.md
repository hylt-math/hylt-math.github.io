---
layout: post
title: "学習コース 第1巻　多様体・ベクトル束・接続・微分形式"
short_title: "第1巻：多様体・ベクトル束・接続・微分形式"
series: "学習コース：一般化幾何への道"
series_order: 1
series_label: "第1巻"
status: textbook
tags: [学習コース, 教科書, 問題集]
abstract: "多様体と微分形式、de Rham コホモロジー、ベクトル束、接続と曲率、Chern–Weil の入口までを、問題40問と全問の解答つきでまとめた第1巻。第2巻（複素多様体）、第12巻（T⊕T*, Courant 括弧）への橋渡しを含む。"
pdf: /assets/pdf/course-01-v1-ja.pdf
pdf_version: "v1"
---

企画：森　／　執筆：Claude

<div class="remark">
日本語の教科書と問題集です（37ページ）。各節の末尾に問題（[基本][標準][発展]）があり、**全問の解答**と自己診断10問、参考文献が付いています。外部の査読は受けていません。執筆とは別の AI による独立検査と、可能な範囲の計算での検算は行いました。確認できていない出典・記述は PDF 中で【要確認】と示しています。全体の計画は[学習地図]({{ '/2026/11/22/course-00-map/' | relative_url }})にあります。
</div>

## この巻の内容

- 多様体と接束、ベクトル場と Lie 括弧、微分形式と Cartan の公式
- de Rham コホモロジー（Poincaré の補題、Mayer–Vietoris）
- ベクトル束と構造群、貼り合わせ関数
- 接続・曲率・Bianchi 恒等式
- Chern–Weil の入口（Chern 形式の閉性と、de Rham 類が接続によらないこと）
- 問題40問（基本12・標準20・発展8）、全問に解答、自己診断10問

## 検査の状況

- 全40問の解答を、別の AI が独立に解き直して検算しました。誤りは解答2件（符号と導出の不足）、問題文の不備1件、条件の欠落3件（Poincaré 双対の連結性など）、例1件、出典の章番号の誤りで、すべて修正済みです。
- 計算は自作の検算コード（有理係数の多項式による外積代数・Lie 微分・行列値形式）で確認しました。sympy は使えなかったためです。
- 手計算のみのもの：Mayer–Vietoris の計算、S² の Levi-Civita 接続、巻き数の議論。標準定理（Poincaré 双対、Stokes、Frobenius、Gauss–Bonnet、de Rham の定理）は引用で、証明はしていません。
- 【要確認】のもの：Kobayashi–Nomizu・Huybrechts・Milnor–Stasheff の一部の章番号、Dorfman 括弧の符号規約（第12巻で確認）、Chern 形式の因子の各文献での記号。

## 改訂履歴

- 2026-11-22：v1 公開。
