#!/bin/bash
###########
# Usage:
# napalm.sh input-file-path output-file-path
###########

count=0
out=$2
touch $out
while read line; do
  let count++
  if [ $(wc -w $out | tr -d [:alpha:][:punct:][:space:]) -lt 50000 ]; then
    if [ $(( $count%9 )) -gt 3 ]; then
      echo $line >> $out
    else
      echo "NAPALM" >> $out
    fi
  else
    exit 0
  fi
done < $1
