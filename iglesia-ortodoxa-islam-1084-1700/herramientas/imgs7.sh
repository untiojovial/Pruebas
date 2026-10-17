#!/bin/bash
# Una sola tanda tras la pausa de 10 min que pide Wikimedia (Retry-After: 600)
UA='Mozilla/5.0 (research; contact via claude.ai)'
sleep 700
get() { c=$(curl -sS -m 90 -L -A "$UA" -o "$1" -w '%{http_code}' "$2"); echo "$1 $c $(stat -c %s $1)"; }
get IMG/zonaras.jpg 'https://upload.wikimedia.org/wikipedia/commons/1/12/Jean_Zonare_Historien_Grec._%28BM_1879%2C1213.109%29.jpg'
sleep 20
get IMG/manuel-orig.jpg 'https://upload.wikimedia.org/wikipedia/commons/d/db/Manuel_II_Paleologus.jpg'
echo DONE
