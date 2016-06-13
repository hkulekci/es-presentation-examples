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

Your IP address may be different instead of `192.168.99.100`. 

### External Tools

You can use [Sense](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig) 
Chrome Browser plugin to execute your queries easily. This tool already will be able to be reachable in 
your dashboard with 5.x version.
