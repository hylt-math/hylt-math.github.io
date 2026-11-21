---
layout: post
title: "一般化複素幾何における Serre 型消滅・双対性・Riemann–Roch 型公式：正則 Poisson 構造の例から"
status: partial
tags: [一般化複素幾何, 正則Poisson構造, Serre消滅, Riemann-Roch, 研究ノート]
abstract: "複素幾何の三種の神器（Riemann–Roch、Serre 消滅、Kodaira 埋め込み）の一般化複素幾何版を目指し、正則 Poisson 構造から作る一般化複素構造と一般化正則直線束の具体例を調べた研究ノート。Serre 型消滅は「横断次数」での消滅として定式化され、対数シンプレクティックな曲面では留数に応じたコホモロジーの閉じた公式が得られた。Kodaira 埋め込みは未着手。査読を受けていない。"
updated: 2026-11-22
pdf: /assets/pdf/generalized-geometry-poisson-v2-ja.pdf
pdf_version: "v2"
---

調査・執筆：Claude　／　問題設定：森

<div class="remark">
**英語版 PDF**：[generalized-geometry-poisson-v2-en.pdf]({{ '/assets/pdf/generalized-geometry-poisson-v2-en.pdf' | relative_url }})（日本語版が原本です）。旧版：[v1（日本語）]({{ '/assets/pdf/generalized-geometry-poisson-v1-ja.pdf' | relative_url }})、[v1（英語）]({{ '/assets/pdf/generalized-geometry-poisson-v1-en.pdf' | relative_url }})。
本稿は**査読を受けていない研究ノート**です。PDF 中の各主張には【文献】【証明済】【計算で確認】【予想】【要確認】の区別を付けています。文献の定理番号や書誌には、記憶や要約に基づく未確認のものが残っています（【要確認】）。
</div>

## 背景と目的

複素幾何の三種の神器、すなわち Hirzebruch–Riemann–Roch の定理、Serre の消滅定理、Kodaira の埋め込み定理を、一般化複素幾何に拡張することが最終目標です。先行研究の調査では、Hu（2024）の Lie 亜群版の Kodaira–Nakano 消滅と Riemann–Roch、Pal–Poddar（2024）の正則型の場合の消滅定理が見つかりましたが、一般の一般化複素構造に対する Kodaira 埋め込みや Riemann–Roch は見つかりませんでした。

そこで、型が跳ぶ最も簡単な非自明な例として、複素多様体 $$X$$ 上の正則 Poisson 構造 $$\sigma$$ から $$\beta$$-変換で作る一般化複素構造 $$\mathcal J_\sigma$$ と、その上の一般化正則直線束（Poisson 加群）を調べました。

## 主な結果

一般化正則直線束 $$L$$ に対する一般化 Dolbeault 複体は、$$(\wedge^\bullet T\otimes L,\ \bar\partial+[\sigma,\cdot])$$ の超コホモロジー $$\mathbb H^\bullet(L)$$ で計算できます（Laurent-Gengoux–Stiénon–Xu による同一視を引用）。

<div class="theorem" data-name="Serre 型消滅（横断次数）">
$$X$$ を射影多様体、$$\sigma$$ を任意の正則 Poisson 構造、$$L_0$$ を豊富で Poisson 加群になる直線束とする。$$m\gg0$$ のとき、$$H^a(X,\wedge^bT\otimes E\otimes L_0^m)=0\ (a>0)$$ なので $$\mathbb H^\bullet(E\otimes L_0^m)$$ は大域切断の複体のコホモロジーとなり、全次数 $$k>n$$ で $$\mathbb H^k=0$$ である。
</div>

<div class="remark">
全次数での消滅は成り立ちません（$$\sigma=0$$ でも成り立たない）。正しい形は「横断次数 $$a$$ での消滅」です。$$\sigma$$ の非退化性はこの定理には不要です。
</div>

<div class="theorem" data-name="対数シンプレクティックな曲面">
コンパクト複素曲面 $$X$$ 上の正則 Poisson 構造 $$\sigma$$ が、通常の結節点のみを持つ被約な曲線 $$D$$ に沿って対数シンプレクティックで、直線束 $$L$$ が各成分に沿って留数 $$r_i$$ をもつ Poisson 加群であるとする。留数がすべて等しい値 $$r\ne1$$ のとき、$$U=X\setminus D$$ の第1 Betti 数を $$b_1$$ として、$$\mathbb H^\bullet(L)$$ の Poincaré 多項式は

$$
P_r(t)=\chi(X)\,t^2+[r\le0]\,\Delta(t)+[r\ge2]\,t^4\Delta(1/t),\qquad \Delta(t)=(1+t)\bigl(1+(b_1-1)t\bigr)
$$

で与えられる（$$r\notin\mathbb Z$$ では $$\chi(X)t^2$$ のみ）。全 Euler 標数は $$\chi(X)$$ で、留数によらない。
</div>

例として $$X=\mathbb{CP}^2$$、$$D$$ を滑らかな3次曲線とすると、$$\mathcal O(m)$$ はどの $$m$$ でも一意に一般化正則構造をもち（留数 $$r=-m/3$$）、コホモロジーの次元は $$m$$ について周期3で跳びます。$$m=3k\ (k\ge0)$$ では $$(1,0,2,0,0)$$、それ以外の $$m\ge-3$$ では $$(0,0,3,0,0)$$ です。$$m=-15,\dots,15$$ で直接計算と一致しています。

そのほか、PDF には次の結果を含みます。

- 任意の次元・任意の正則 Poisson 構造で成り立つ双対性 $$\mathbb H^k(L)^*\cong\mathbb H^{2n-k}(L^\vee\otimes K^2)$$（$$n\le4$$ では恒等式を機械的に確認）。
- トーリックな高次元の例に対する重み公式と、3重点などの特異点に対する局所項の予想。
- Riemann–Roch に関する観察：全複体の Euler 標数は $$m$$ によらない位相不変量になるので、精密化が必要になること。Hu の Lie 亜群版は、この複体の指数とは別物であること。
- 指数理論（b-計算、指数根）の見通し（予想）。

## 現状と今後

<div class="remark">
Kodaira 埋め込みの一般化は未着手です。非結節点の特異点、次元4以上の一般の場合、留数が不等な場合は予想または部分的な計算にとどまります。複素 Lie 亜群 $$L$$ に対する指数定理は見つかっておらず、Riemann–Roch の一般化はこれが課題です。
</div>

## 改訂履歴

- 2026-11-22：v1 公開（日本語版・英語版）。
- 2026-11-22：v2 公開。文献の書誌・定理番号の誤りを訂正した（arXiv:0905.3227 の著者は Hitchin、Gualtieri 2011 の番号、Pal–Poddar の題名・定理番号、Lang–Jia–Liu の書誌など）。定理・命題の主張そのものは変更していない。訂正の一覧は PDF 末尾の「v2 改訂点」を参照。
