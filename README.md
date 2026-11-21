# 数学研究ノート（公開用サイト）

GitHub Pages を使って無料で公開できる、数式（MathJax）対応のサイトです。

## 公開までの手順（初回のみ・すべて無料）

1. **GitHub アカウントを作る**: https://github.com/signup
2. **リポジトリを作る**: 右上「+」→「New repository」
   - Repository name を **`ユーザー名.github.io`** にすると、`https://ユーザー名.github.io/` で公開されます。
   - **Public** を選ぶ（無料プランで Pages を使うには公開リポジトリが必要です）。
3. **ファイルをアップロード**: 作ったリポジトリの「Add file」→「Upload files」で、このフォルダの中身（`_config.yml` や `_posts` フォルダなど）を**中身ごと**ドラッグ＆ドロップし、「Commit changes」。
4. **Pages を有効化**: リポジトリの「Settings」→「Pages」→ Source を「Deploy from a branch」、Branch を `main` / `/(root)` にして Save。
5. 1〜2分待つと公開されます。

## 公開前に書き換える場所

- `_config.yml` の `title` / `description` / `author` / `url`（`USERNAME` を自分のユーザー名に）
- リポジトリ名を `ユーザー名.github.io` 以外にした場合は `baseurl: "/リポジトリ名"`
- `about.md` の連絡先と説明文

## 記事を追加するには

`_posts/` に `2026-12-01-title.md` のような Markdown ファイルを追加するだけです。
書き方は `CLAUDE.md` と `_posts/2026-11-21-welcome.md` を参照してください。
Claude に研究を依頼している別のプロジェクトにこのリポジトリを連携すれば、Claude が記事を直接追加できます。
