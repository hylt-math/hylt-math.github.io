#!/bin/bash
# usage: build.sh [jobname]  -- concatenates parts/*.tex in order, builds wip (default) ; "final" builds vol03
cd "$(dirname "$0")"
job=${1:-wip}
cat parts/p0.tex parts/p1.tex parts/p2.tex parts/p3.tex parts/p4.tex parts/p5.tex parts/p6.tex parts/p7.tex parts/p8.tex 2>/dev/null > $job.tex
echo '\end{document}' >> $job.tex
xelatex -interaction=nonstopmode $job.tex >$job.build.log 2>&1; xelatex -interaction=nonstopmode $job.tex >$job.build.log 2>&1
grep -E "^!|undefined|Missing|Emergency" $job.build.log | head -30
grep -c "Overfull" $job.build.log
pdfinfo $job.pdf | grep Pages
