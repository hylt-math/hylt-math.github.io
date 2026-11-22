#!/usr/bin/env python3
"""使い方: publish_vol.py NN slug "題" "短い題" pdf_path "概要" "内容(改行区切り)" "検査の状況(改行区切り)" [pages]
   assets/pdf/course-NN-v1-ja.pdf と _posts/2026-11-22-course-NN-slug.md を作る。"""
import sys,shutil,datetime
nn,slug,title,short,pdf,abstract,contents,checks=sys.argv[1:9]
pages=sys.argv[9] if len(sys.argv)>9 else ""
date=datetime.date.today().isoformat()
dst=f"assets/pdf/course-{nn}-v1-ja.pdf"; shutil.copy(pdf,dst)
bul=lambda s:"\n".join("- "+x for x in s.split("\n") if x.strip())
post=f'''---
layout: post
title: "学習コース 第{int(nn)}巻　{title}"
short_title: "第{int(nn)}巻：{short}"
series: "学習コース：一般化幾何への道"
series_order: {int(nn)}
series_label: "第{int(nn)}巻"
status: textbook
tags: [学習コース, 教科書, 問題集]
abstract: "{abstract}"
pdf: /{dst}
pdf_version: "v1"
---

企画：森　／　執筆：Claude

<div class="remark">
日本語の教科書と問題集です（{pages}）。各節の末尾に問題（[基本][標準][発展]）があり、**全問の解答**と自己診断10問、参考文献が付いています。外部の査読は受けていません。執筆とは別の AI による独立検査と、可能な範囲の計算での検算は行いました。確認できていない出典・記述は PDF 中で【要確認】と示しています。全体の計画は[学習地図]({{{{ '/2026/11/22/course-00-map/' | relative_url }}}})にあります。
</div>

## この巻の内容

{bul(contents)}

## 検査の状況

{bul(checks)}

## 改訂履歴

- {date}：v1 公開。
'''
open(f"_posts/2026-11-22-course-{nn}-{slug}.md","w",encoding="utf-8").write(post)
print("wrote",dst,f"_posts/2026-11-22-course-{nn}-{slug}.md")
