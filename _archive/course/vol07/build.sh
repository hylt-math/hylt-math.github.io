cd "$(dirname "$0")"
cat part0.tex part1.tex part2.tex part3.tex part4.tex part5.tex part6.tex > vol07.tex
xelatex -interaction=nonstopmode vol07.tex >build.log 2>&1; xelatex -interaction=nonstopmode vol07.tex >build.log 2>&1
grep -E "^!|undefined|Missing|Overfull|multiply" build.log | head -40; pdfinfo vol07.pdf | grep Pages
