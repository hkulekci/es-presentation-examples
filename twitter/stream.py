#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from elasticsearch import Elasticsearch
import json
import config
import sys


class StdOutListener(StreamListener):

    def __init__(self, es_configuration):
        self.es = Elasticsearch(es_configuration)

    def on_data(self, data):
        data = json.loads(data)
        print data
        self.es.index(index="twitter", doc_type="tweet", body=data)
        return True

    def on_error(self, status):
        print status


def main(argv):
    print(argv)
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <searchKeyword>" % (argv[0],))
        return 1

    l = StdOutListener(config.es_configuration)
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    stream = Stream(auth, l)
    print "Stream started\n"
    stream.filter(track=[argv[1]])
    print "Stream ended!\n"

if __name__ == "__main__":
    sys.exit(main(sys.argv))