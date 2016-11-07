#!/bin/sh

#generate requests with the meta-data of 500 documents per request (= max as specified by the API)
python3 findIDs.py
#stores files in $start.json, e.g., 0.json, 500.json, 1000.json, ...

#parse all JSON files into the sqlite db (assumes only the above output files exist in the current dir...)
for i in `ls *.json`; do
  python scrape_to_db.py "$i"
done

