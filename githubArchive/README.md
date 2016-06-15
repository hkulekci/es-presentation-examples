### Elasticsearch Graph Examples

We try to use [https://www.githubarchive.org/](https://www.githubarchive.org/) datas for our examples. Firstly, we will
download archive files to our file systems with abov command.

```
./download.sh 2016-05-30
```

If you get any permission error, you can use `chmod +x download.sh` command to fix this issue. After that, we should
use `index.py` file to index these datas to our Elasticsearch index. Python environment installation and indexing 
operations is below:

```
source bin/activate
pip install -r requirement.txt
python index.py data/2016-05-01-0.json
```
