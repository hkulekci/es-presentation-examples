Elasticsearch Docker Example 

Build your image:

```
docker build -t my_elasticsearch .
```

Run your image:

```
docker run -t -p 9200:9200 -p 9300:9300 --rm my_elasticsearch
```