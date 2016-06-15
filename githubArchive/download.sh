#!/bin/sh
SEL_DATE=$1

if [[ $SEL_DATE == "" ]]; then
    echo "Select a date to fetch data from archive.\n\n"
    exit
fi

echo $SEL_DATE " files downloading ...\n\n"

for (( i = 0; i < 24; i++ )); do
    FILENAME="$SEL_DATE-$i.json"
    if [[ ! -e "data/$FILENAME" ]]; then
        curl http://data.githubarchive.org/$FILENAME.gz | gunzip -c > data/$FILENAME
    else 
        echo "File already exist!" $FILENAME
    fi
done

echo "\n\nAll files Downloaded!"