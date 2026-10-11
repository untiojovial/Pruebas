#!/bin/bash
# uso: scan.sh <bookid> <desde> <hasta>  -> descarga páginas a dl/<bookid>/
b=$1; mkdir -p dl/$b
seq $2 $3 | xargs -P 8 -I{} sh -c "[ -s dl/$b/p{}.html ] || curl -sS -m 60 -o dl/$b/p{}.html https://shamela.ws/book/$b/{}"
