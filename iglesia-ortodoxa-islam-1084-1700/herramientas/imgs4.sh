#!/bin/bash
UA='Mozilla/5.0 (research; contact via claude.ai)'
get() { # slug url
  for k in 1 2 3 4; do
    c=$(curl -sS -m 90 -L -A "$UA" -o "IMG/$1.jpg" -w '%{http_code}' "$2"); echo "$1 try$k $c $(stat -c %s IMG/$1.jpg)"
    [ "$c" = "200" ] && return 0; sleep 40; done
}
get zonaras 'https://upload.wikimedia.org/wikipedia/commons/1/12/Jean_Zonare_Historien_Grec._%28BM_1879%2C1213.109%29.jpg'
sleep 8
get zigabeno 'https://upload.wikimedia.org/wikipedia/en/thumb/7/75/Commentary_on_Psalms_by_Euthymios_Zygabenos.jpg/960px-Commentary_on_Psalms_by_Euthymios_Zygabenos.jpg'
echo DONE
