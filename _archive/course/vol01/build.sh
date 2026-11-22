cat part0.tex part1.tex part2.tex part3.tex part4.tex part5.tex part6.tex part7.tex part8.tex > vol01.tex
echo '\end{document}' >> vol01.tex
xelatex -interaction=nonstopmode vol01.tex >build.log 2>&1; xelatex -interaction=nonstopmode vol01.tex >build.log 2>&1
grep -E "^!|Overfull|undefined|Missing" build.log | head -40
pdfinfo vol01.pdf | grep Pages
