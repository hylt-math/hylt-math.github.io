cat part0.tex part1.tex part2.tex part3.tex part4.tex part5.tex part6.tex part7.tex part8.tex part9.tex part10.tex part11.tex > vol05.tex
xelatex -interaction=nonstopmode vol05.tex >build.log 2>&1; xelatex -interaction=nonstopmode vol05.tex >build.log 2>&1
grep -E "^!|undefined|Missing|Overfull|Multiply" build.log | head -40; pdfinfo vol05.pdf | grep Pages
