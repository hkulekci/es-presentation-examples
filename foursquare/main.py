from elasticsearch import Elasticsearch
import config
import sys
import signal
import foursquare
import json

# Getting Data Directly From API

client = foursquare.Foursquare(client_id=config.conf["client_id"], client_secret=config.conf["client_secret"])
es = Elasticsearch(config.conf['es'])


def main(argv):
    res = client.venues.search(params={
        'query': 'cafe',
        # 'll':'41.01860,29.00039',
        'near': u'Sisli, Istanbul',
        'radius': 10000,
        'limit': 50
    })
    print len(res['venues'])
    for venue in res['venues']:
        # print venue['name'], ' - ', venue['location']['address'], ' - ', venue['location']['lat']
        data = json.loads(venue)
        es.index(index="foursquare", doc_type="venue", id=venue['referenceId'], body=data)


def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
