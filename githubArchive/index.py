from elasticsearch import Elasticsearch
import json
import config
import sys
import os
import signal

es = Elasticsearch(config.es_configuration)


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
            data = json.loads(line)
            es.index(index="github", doc_type="action", body=data)
            if count % 500 == 0:
                print "Imported Data Count For This File : ", count


def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
