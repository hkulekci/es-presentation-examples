## Elasticsearch Examples

To install your environment on [docker](https://www.docker.com/), follow the below steps. 

Firstly, build your images for elasticsearch, kibana and their plugins (graph, sense, head, ...):

```
docker-compose build
```

After that, run your images:

```
docker-compose up
```

Right now, you can reach elasticsearch from your browser:

[http://localhost:9200/](http://localhost:9200/)

In this container, there is head plugin for elasticsearch and graph plugin for 

### External Tools

#### Sense Chrome Plugin

You can use [Sense](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig) 
Chrome Browser plugin to execute your queries easily. This tool already will be able to be reachable in 
your dashboard with 5.x version.

#### Head ES Plugin (Manually Install)

Also, you can install elasticsearch [head plugin](https://mobz.github.io/elasticsearch-head/). Use 
following commands to install head plugin to your dockerized Elasticsearch service.

```
➜  ~ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                                                                                              NAMES
19fa8b384527        elasticsearch:latest   "/docker-entrypoint.s"   19 minutes ago      Up 5 minutes        0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp, 0.0.0.0:32771->9200/tcp, 0.0.0.0:32770->9300/tcp   elasticsearch-2
➜  ~ 
➜  ~ docker exec -it 19fa8b384527 bin/plugin install mobz/elasticsearch-head
-> Installing mobz/elasticsearch-head...
Trying https://github.com/mobz/elasticsearch-head/archive/master.zip ...
Downloading ....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................DONE
Verifying https://github.com/mobz/elasticsearch-head/archive/master.zip checksums if available ...
NOTE: Unable to verify checksum for downloaded plugin (unable to find .sha1 or .md5 file to verify)
Installed head into /usr/share/elasticsearch/plugins/head
```

#### Graph Plugin (Manually Install)

```
➜  ~ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                                                                                              NAMES
19fa8b384527        elasticsearch:latest   "/docker-entrypoint.s"   17 hours ago        Up 16 hours         0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp, 0.0.0.0:32771->9200/tcp, 0.0.0.0:32770->9300/tcp   elasticsearch-2
a4a83a5e5762        kibana:latest          "/docker-entrypoint.s"   12 days ago         Up 5 minutes        0.0.0.0:9201->5601/tcp, 0.0.0.0:32772->5601/tcp                                                    kibana-2
➜  ~
➜  ~ docker exec -it 19fa8b384527 bin/plugin install license
-> Installing license...
Trying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/license/2.3.3/license-2.3.3.zip ...
Downloading .......DONE
Verifying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/license/2.3.3/license-2.3.3.zip checksums if available ...
Downloading .DONE
Installed license into /usr/share/elasticsearch/plugins/license
➜  ~ 
➜  ~ docker exec -it 19fa8b384527 bin/plugin install graph
-> Installing graph...
Trying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/graph/2.3.3/graph-2.3.3.zip ...
Downloading ....DONE
Verifying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/graph/2.3.3/graph-2.3.3.zip checksums if available ...
Downloading .DONE
Installed graph into /usr/share/elasticsearch/plugins/graph
➜  ~ 
➜  ~ docker exec -it a4a83a5e5762 /opt/kibana/bin/kibana plugin --install elasticsearch/graph/latest
Installing graph
Attempting to transfer from https://download.elastic.co/elasticsearch/graph/graph-latest.tar.gz
Transferring 69301 bytes....................
Transfer complete
Extracting plugin archive
Extraction complete
Optimizing and caching browser bundles...

Plugin installation complete
➜  ~ 
```
