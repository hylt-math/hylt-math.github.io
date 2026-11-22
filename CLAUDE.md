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
status: conjecture        # wip / conjecture / proved / partial / open / textbook / retracted
tags: [整数論, 数値実験]
abstract: "1〜3文の概要。数式は $$x^2$$ のように書ける。"
# updated: 2026-12-10     # 内容を改訂したときに追加
---

本文（Markdown）
```

## PDF を公開する場合

1. PDF を `assets/pdf/` に置く。ファイル名は英小文字・数字・ハイフン（例: `assets/pdf/generalized-geometry-v1.pdf`）。
2. 同じ内容を紹介する記事を `_posts/` に作り、front matter に次を加える。

```yaml
pdf: /assets/pdf/generalized-geometry-v1.pdf
pdf_version: "v1"   # 省略可
```

本文には主結果の要約（定理の主張など）を数式つきで数段落書く。記事ページには PDF を開くボタンと埋め込み表示が自動で付く。
3. PDF を改訂したら、新しいファイル名（`-v2.pdf` など）で追加し、記事の `pdf:` を差し替えて `updated:` と改訂履歴を書く。古い PDF は消さずに残す。

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

## シリーズ記事・一覧表示用の追加フィールド（任意）

```yaml
short_title: "Part II：トーリック多様体・Euler 標数"   # 一覧と目次に出す短いタイトル（本来のタイトルは title）
series: "シリーズ名"        # 同じ文字列の記事が一覧で1つにまとまり、記事ページに目次が出る
series_order: 2            # シリーズ内の並び順（総合版は 0）
series_label: "Part II"    # 一覧のバッジ
```

- シリーズの紹介文は `_config.yml` の `series_info` に同じシリーズ名で書く。
- 一覧ページ（`index.html`）は、シリーズ別／日付順／タイトル順／状態順の切り替えと、状態・タグ・キーワードでの絞り込みができる（JavaScript 使用）。
- 新しいシリーズ記事を追加するときは `short_title` を付けること。

- 教材（学習コースの各巻）は `status: textbook`、シリーズ名「学習コース：一般化幾何への道」、`series_order` に巻番号（学習地図は 0）を付ける。原稿は `_archive/course/`。

## 方針

- 誤りが見つかった記事は削除せず、`status: retracted` にして冒頭に理由と日付を書く。
- 改訂したら `updated:` を追加し、本文末に「改訂履歴」を残す。
- 画像は `assets/img/` に置き、`![説明]({{ '/assets/img/ファイル名.png' | relative_url }})` で参照する。
