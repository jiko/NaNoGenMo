#!/bin/bash
###########
# Usage:
# napalm.sh input-file-path output-file-path
###########

count=0
out=$2
N=7
dict="/usr/share/dict/words"
touch $out
while read line; do
  let count++
  if [ $(wc -w $out | tr -d [:alpha:][:punct:][:space:]) -lt 50000 ]; then
      seventh=$(echo $line | cut -d " " -f $N)
      linenum=$(grep -xn "$seventh" $dict | tr -d [:alpha:][:punct:])
      if [ $linenum > 0 ]; then
        let linenum-=7
        replacement=$(awk -vlineNum=$linenum 'NR == lineNum { print $0 }' $dict)
        echo ${line/$seventh/$replacement} >> $out
      else
        echo $line >> $out
      fi
  else
    exit 0
  fi
done < $1
