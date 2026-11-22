# 研究の状態と再開手順（Claude 用）

最終更新: 2026-11-22（ラウンド1: Part II 公開）

## 方針（ユーザー指示、2026-11-22 02:29）
- このサイトへの PDF／記事の追加・更新は、確認なしで公開してよい。arXiv 投稿・先生への連絡はしない。
- 公開の基準: 自分で検算して誤りがないと判断したもののみ。未確認は【要確認】のまま、ステータスは実態どおり（証明済みは確認したときだけ）。
- 日本語版・英語版の PDF を両方作る。誤りが見つかったら `-v2` を追加し、記事の `pdf:` を差し替え、`updated:` と改訂履歴を書く（古い PDF は消さない）。新しい内容は別記事（別スラッグ）で公開する。
- 1ラウンドの並行作業は最大2つ。細かめにデータを保存する。失敗して止まったら次の実行時に途中から再開する。
- 作業ファイルは `_archive/<日付>/`（notes, scripts, paper_ja, paper_en）に保存し、ラウンド終了時に push する。`_archive/` は Jekyll では公開されない。
- ユーザーは 2026-11-22 夜（約22:30 JST）まで返信不可。確認を待たずに進め、アプリで見られる短い報告（SendUserMessage）を区切りごとに出す。

## 停止条件（ユーザー指示 2026-11-22 09:57）
- 総合論文（Part I–V を統合した日本語版・英語版）を公開し、STATE.md に記録したら、自動再開をやめる。具体的には、予約中の再開（trigger trig_015zFgr7B9fRffzGqeu2J4mS、12:31 JST）が動いたときに総合論文が公開済みなら、新しい予約を入れず、delete_trigger でこの予約も削除し、全成果の要約を SendUserMessage で送って終了する。総合論文が未完なら、完了まで継続。

## 公開済み
- 2026-11-22 generalized-geometry-poisson v1（ja/en）、v2（ja/en、書誌・定理番号の訂正、commit e299fc2）。status: partial。v2 のソースは _archive/2026-11-22/paper_v2_ja, paper_v2_en。
- Part II: generalized-geometry-poisson-part2 v1, v2（局所公式の訂正）。Part III: generalized-geometry-poisson-part3 v1（Kodaira 型）。Part V: generalized-geometry-poisson-part5 v1（Riemann–Roch 型公式 K1/K、局所公式の証明、指数予想）。Part IV: generalized-geometry-poisson-part4 v1（正則型 Gauss–Manin と対数シンプレクティック型の比較、簡約定理 R）。いずれも ja/en、status partial。
- 注意: v2 公開後、公開サイトでの反映確認は未了（ブラウザ系ツールが使えず、WebFetch は古いキャッシュを返した）。次ラウンドで確認する。

- 2026-11-22 generalized-geometry-poisson-part2 v1（ja/en、新記事、status: partial）。ソースは _archive/2026-11-22/paper2_ja, paper2_en。Part I への影響確認の結果（撤回なし）は notes/v3_corrections.md。

## 作業キュー（優先順・更新）
G. 公開サイトの反映確認（ブラウザ系ツールが使えるとき、または WebFetch で新しい URL を取得）。
H. 完了（Part V）。残り: 準斉次な局所公式の収束複体への移行の詳細、s=1。
I'. 予想 C は定理 R（条件 (GEN') つき）として証明済み。残り: (GEN') が ν_T≢0 から従うか（非線形化 σ）、正則な対数 Darboux の文献、予想 NR（非被約）。
L'. 正則型との比較（定理 L）は完了。残り: 非平坦束、hard Lefschetz が成り立たない場合。
J. Poisson–Kodaira 予想: P^2 の m>=3、P^1×P^1 の Segre、Jacobiator 障害の解析。
K. Part V で定理 K1/K を公開。残り: r∉Z, n>2 で H^k(U;L_U)=0 (k<n) の証明、b-計算による指数定理（予想 I1–I4）。
L. Pal–Poddar の枠組み（正則型）との統合: 型 1 の例 Y×X で Part I–III の公式と Thm 11.12 を直接比較。
M. 全体を一つの総合論文（Part I–III の統合・整理）にまとめる準備（記号表・仮定表の統一）。

## ラウンド記録
- ラウンド0 (02:35–05:30): アーカイブ、A・B（書誌確認、Pal–Poddar 再読）、C・D・E・F を完了。Part I v2, Part II v1→v2, Part III v1 を公開。
- ラウンド0 続き (〜06:30): Task I, L 完了。Part IV v1 を公開（commit 59661d6）。次回ラウンド(07:31〜): G（サイト確認）, H, J, K, M を優先。
- ラウンド1 (07:31〜08:50): Task H, K 完了。Part V v1 公開（commit 74f6203）。次: M（総合論文）、J（Poisson–Kodaira）、G（サイト確認）、K の残り。
- 09:57: 総合論文（M）の作成を開始。Poisson–Kodaira と H^k(U;L_U)=0 の穴の補強を並行。
