#!/bin/bash
###########
# Find the senventh word of each line in the file
# then replaces it with the dictionary entry seven
# lines down from it in the system dictionary
########
# Usage:
# napalm.sh input-file-path output-file-path
###########

out=$2
touch $out
dict="/usr/share/dict/words"
while read line; do
  if [ $(wc -w $out | tr -d [:alpha:][:punct:][:space:]) -lt 50000 ]; then
      seventh=$(echo $line | awk '{print $7}')
      linenum=$(grep -xn "$seventh" $dict | tr -d [:alpha:][:punct:])
      if [ $linenum > 0 ]; then
        let linenum-=7
        replacement=$(awk 'NR == $linenum' $dict)
        echo ${line/$seventh/$replacement} >> $out
      else
        echo $line >> $out
      fi
  else
    exit 0
  fi
done < $1
