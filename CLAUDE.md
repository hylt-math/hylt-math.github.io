# このリポジトリについて（Claude 向けの説明）

数学研究の結果を公開する Jekyll サイト（GitHub Pages で公開）です。
研究結果を公開するときは、以下の手順で記事を追加してください。

## 記事の追加

`_posts/YYYY-MM-DD-英数字のスラッグ.md` を新規作成する（例: `_posts/2026-12-01-collatz-bound.md`）。
ファイル名の日付が公開日になる。スラッグは英小文字・数字・ハイフンのみ。

```markdown
---
layout: post
title: "記事のタイトル"
status: conjecture        # wip / conjecture / proved / partial / open / retracted
tags: [整数論, 数値実験]
abstract: "1〜3文の概要。数式は $$x^2$$ のように書ける。"
# updated: 2026-12-10     # 内容を改訂したときに追加
---

本文（Markdown）
```

## 数式（kramdown + MathJax）

- 文中の数式も **`$$...$$`** で書く（単独の `$` は数式にならない）。
- 独立行の数式は `$$...$$` を **前後に空行** を入れて書く。
- `\label{...}` / `\eqref{...}` で式番号の参照が可能。
- 定義済みマクロ: `\N \Z \Q \R \C`。
- 表のセル内で `|` を使う場合は `\vert` や `\mid` を使う。

## 定理環境

```html
<div class="theorem" data-name="任意の名前">
内容（Markdown と数式がそのまま使える）
</div>
```

使えるクラス: `theorem` `lemma` `proposition` `corollary` `conjecture` `definition` `example`（通し番号つき）、`remark` `proof`（番号なし、proof には ∎ が付く）。
`data-name` は省略可。

## 方針

- 誤りが見つかった記事は削除せず、`status: retracted` にして冒頭に理由と日付を書く。
- 改訂したら `updated:` を追加し、本文末に「改訂履歴」を残す。
- 画像は `assets/img/` に置き、`![説明]({{ '/assets/img/ファイル名.png' | relative_url }})` で参照する。
