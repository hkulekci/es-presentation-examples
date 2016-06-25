#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
import config
import sys
import signal
import foursquare
import os
from dateutil import parser

# Getting Data From Sample Dataset
# Firstly, download dataset from here: https://sites.google.com/site/yangdingqi/home/foursquare-dataset
# After that, run import.py <filename>

client = foursquare.Foursquare(client_id=config.conf["client_id"], client_secret=config.conf["client_secret"])
es = Elasticsearch(config.conf['es'])


def processline(data):

    data = [x.strip() for x in data.split("\t")]

    print data, len(data)

    if len(data) <= 7:
        return
    # Tue Apr 03 18:00:09 +0000 2012
    parsed_date = parser.parse(data[7])

    keyValueData = {
        "userId": data[0],
        "venueId": data[1],
        "venueCategoryId": data[2],
        "VenueCategoryName": data[3].decode("utf-8"),
        "location": data[4] + ', ' + data[5],
        "date": parsed_date.strftime('%Y-%m-%dT%H:%M:%S')
    }

    print keyValueData
    es.index(index="checkins", doc_type="checkin", body=keyValueData)


def main(argv):
    if len(argv) < 1:
        sys.stderr.write("Usage: %s <filename>" % (argv[0],))
        return 1

    print argv
    path = argv[1]

    if os.path.isdir(path):
        print path
        files = os.listdir(path)
        for file in files:
            if file[0] != '.':
                main([argv[0], 'data/' + file])

        print "All files executed!"
        sys.exit(0)

    if not os.path.isfile(path):
        sys.stderr.write("File not found" % (argv[1],))
        sys.exit(0)

    count = 0
    with open(path) as f:
        for line in f:
            count += 1
            processline(line)
            if count % 500 == 0:
                print "Imported Data Count For This File : ", count


def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    sys.exit(main(sys.argv))
