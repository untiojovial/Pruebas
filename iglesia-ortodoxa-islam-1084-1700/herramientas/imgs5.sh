#!/bin/bash
UA='Mozilla/5.0 (research; contact via claude.ai)'
get() { # out url
  for k in 1 2 3 4 5; do
    c=$(curl -sS -m 90 -L -A "$UA" -o "$1" -w '%{http_code}' "$2"); echo "$1 try$k $c $(stat -c %s $1)"
    [ "$c" = "200" ] && return 0; sleep 40; done
}
get IMG/simeon-new.jpg 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Symeon_of_Thessaloniki.jpg'
sleep 8
get IMG/manuel-orig.jpg 'https://upload.wikimedia.org/wikipedia/commons/d/db/Manuel_II_Paleologus.jpg'
echo DONE
