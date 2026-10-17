#!/bin/bash
UA='Mozilla/5.0 (research; contact via claude.ai)'
until grep -q DONE IMG/imgs5.log; do sleep 5; done
sleep 20
for k in 1 2 3 4 5 6 7 8; do
  c=$(curl -sS -m 90 -L -A "$UA" -o IMG/zonaras.jpg -w '%{http_code}' 'https://upload.wikimedia.org/wikipedia/commons/1/12/Jean_Zonare_Historien_Grec._%28BM_1879%2C1213.109%29.jpg'); echo "zonaras try$k $c $(stat -c %s IMG/zonaras.jpg)"
  [ "$c" = "200" ] && break; sleep 60; done
echo DONE
