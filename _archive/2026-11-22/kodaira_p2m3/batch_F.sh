#!/bin/bash
# usage: batch_F.sh name...  (m=3, 2 starts each)
for n in "$@"; do python3 multistart.py 3 $n 2 200 > ms_m3_$n.log 2>&1; done
