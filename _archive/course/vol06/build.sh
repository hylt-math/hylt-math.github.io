cat part0.tex part1.tex part2.tex part3.tex part4.tex part5.tex part6.tex > vol06.tex
xelatex -interaction=nonstopmode vol06.tex >build.log 2>&1; xelatex -interaction=nonstopmode vol06.tex >build.log 2>&1
grep -E "^!|undefined|Missing|Overfull" build.log | head -30; pdfinfo vol06.pdf | grep Pages
