---
layout: post
title: "学習コース 第4巻　Riemann 面と Riemann–Roch の定理（曲線版）"
short_title: "第4巻：Riemann 面と Riemann–Roch の定理（曲線版）"
series: "学習コース：一般化幾何への道"
series_order: 4
series_label: "第4巻"
status: textbook
tags: [学習コース, 教科書, 問題集]
abstract: "コンパクト Riemann 面、因子と直線束、Riemann–Roch の定理（完全な証明）、Serre 双対、Riemann–Hurwitz、種数 0・1・2 の曲線の分類、標準写像と埋め込み、Weierstrass の gap までを、問題40問と全問の解答つきでまとめた第4巻。「Riemann–Roch は ∂̄ 作用素の指数である」という見方を通して、第6〜8巻（HRR・指数定理）につなぐ。"
pdf: /assets/pdf/course-04-v1-ja.pdf
pdf_version: "v1"
---

企画：森　／　執筆：Claude

<div class="remark">
日本語の教科書と問題集です（43ページ）。各節の末尾に問題（[基本][標準][発展]）があり、**全問の解答**と自己診断10問、参考文献が付いています。外部の査読は受けていません。執筆とは別の AI による独立検査と、可能な範囲の計算での検算は行いました。確認できていない出典・記述は PDF 中で【要確認】と示しています。全体の計画は[学習地図]({{ '/2026/11/22/course-00-map/' | relative_url }})にあります。
</div>

## この巻の内容

- コンパクト Riemann 面、有理型関数と有理型1形式、因子と直線束（Pic = 因子類群）
- Riemann–Roch の定理（層の完全列からの帰納で完全に証明）、Serre 双対（主張と骨子）、Clifford の不等式
- Riemann–Hurwitz の公式、種数の計算、g=0,1,2 の分類（楕円曲線とその℘関数、超楕円曲線）
- 標準写像と曲線の埋め込み（deg D ≥ 2g+1）、Serre 消滅・Kodaira 消滅の1次元版
- Abel の定理と Jacobi 多様体（主張と例）、Weierstrass の gap と Weierstrass 点
- Riemann–Roch は ∂̄ 作用素の指数であること、統合論文との対応（類似としての読み）
- 問題40問、全問に解答、自己診断10問

## 検査の状況

- 全40問の解答を、別の AI が独立に解き直しました。定理・解答に数式の誤りは見つからず、修正したのは次の点です：標準写像定理の証明の抜け（deg f=2g+2 の場合）、不正確な記述（g=5 の完全交叉、Brill–Noether の条件など）、問題文1件、出典の節番号の誤り（Forster、Miranda、Hartshorne）。
- 統合論文に関する橋渡しの段落は、論文と矛盾していたため書き直しました（論文は全 Euler 標数が c_1(E) によらないと述べています）。対数シンプレクティック曲面との対応は「形式的な類似」に弱めました。
- Riemann–Hurwitz と種数の公式、℘ の微分方程式、Hurwitz の 84(g−1)、Fermat 4 次曲線の超変曲点12個などを、手計算と Python（numpy、自作コード）で確認しました。
- 引用のみ（証明なし）：Serre 双対の完全証明、Clifford の等号の分類、Abel・Jacobi・Torelli、Brill–Noether。
- 【要確認】のもの：Griffiths–Harris、Huybrechts、ACGH などの節・章番号、有限性定理・Serre 双対の出典の節番号、Picard 束の Chern 指標。

## 改訂履歴

- 2026-11-22：v1 公開。
