#!/bin/bash
# 第1巻 v2 のビルド：part*.tex, sol*.tex, front.tex, back.tex, main.tex, pre_vol01.tex, pre_course.tex から
# 1 本の vol01.tex（\input を展開したもの）を作り、xelatex を 2 回通して vol01.pdf を作る。
# 使い方: ./build.sh   （最終 PDF は vol01.pdf）
set -e
cd "$(dirname "$0")"
python3 - <<'PY'
import re
def expand(path, seen=()):
    s = open(path, encoding='utf-8').read()
    def rep(m):
        name = m.group(1)
        if not name.endswith('.tex'): name += '.tex'
        return expand(name, seen + (path,))
    return re.sub(r'\\input\{([^}]*)\}', rep, s)
out = expand('main.tex')
open('vol01.tex', 'w', encoding='utf-8').write(
    '% 自動生成（build.sh）。編集は part*.tex / sol*.tex / front.tex / back.tex で行う。\n' + out)
PY
xelatex -interaction=nonstopmode vol01.tex > vol01.build1.log 2>&1 || true
xelatex -interaction=nonstopmode vol01.tex > vol01.build2.log 2>&1 || true
echo "--- errors / Overfull / undefined / multiply defined ---"
grep -nE "^!|Overfull|undefined|Undefined|multiply|Missing" vol01.log || echo "(none)"
echo "--- fancyhdr headheight warnings ---"
grep -c "headheight is too small" vol01.log || true
pdfinfo vol01.pdf | grep Pages
python3 check_integ.py 2>/dev/null | head -8 || true
