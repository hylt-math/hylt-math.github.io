#!/bin/bash
# vol09 build: concatenate parts then run xelatex twice
cd "$(dirname "$0")"
cat part0.tex part1.tex part2.tex part3.tex part4.tex part5.tex part6.tex part7.tex part8.tex part9.tex > vol09.tex
xelatex -interaction=nonstopmode vol09.tex >build.log 2>&1; xelatex -interaction=nonstopmode vol09.tex >build.log 2>&1
grep -E "^!|undefined|Missing|Overfull" build.log | head -30; pdfinfo vol09.pdf | grep Pages
