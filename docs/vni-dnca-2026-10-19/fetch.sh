#!/bin/bash
# args: outdir ; reads lines "ISIN fundslug shareslug pagepath"
B=https://www.dnca-investments.com
while read isin f s p; do
  J=$1/cj_$isin.txt; rm -f $J
  curl -sSL -c $J -b $J -o /dev/null "$B$p"
  curl -sS -c $J -b $J -H 'Accept: application/json' -H 'X-Requested-With: XMLHttpRequest' -H "Referer: $B$p" -o $1/$isin.json -w "$isin %{http_code} %{size_download}\n" "$B/api/v1/funds/$f/shares/$s/components/nav_evolution?locale=en"
done
