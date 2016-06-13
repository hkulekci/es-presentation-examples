## Elasticsearch Examples

To install your environment on [docker](https://www.docker.com/), follow the below steps. 

Firstly, build your image:

```
docker build -t my_elasticsearch .
```

After that, run your image:

```
docker run -t -p 9200:9200 -p 9300:9300 --rm my_elasticsearch
```

Right now, you can reach elasticsearch from your browser:

[http://192.168.99.100:9200/](http://192.168.99.100:9200/)

Your IP address may be different instead of `192.168.99.100`. You can use following command to see
your docker machine IP address.

```
docker-machine inspect --format "{{.Driver.IPAddress}}"
```

### External Tools

You can use [Sense](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig) 
Chrome Browser plugin to execute your queries easily. This tool already will be able to be reachable in 
your dashboard with 5.x version.

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
