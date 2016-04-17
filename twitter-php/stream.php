<?php
require_once('vendor/autoload.php');
require_once('config.php');

class ElasticsearchStorage
{
    protected $client;
    protected $indexName;
    protected $typeName;

    /**
     * @param \Elastica\Client $client
     */
    public function __construct(\Elastica\Client $client)
    {
        $this->client = $client;
    }

    /**
     * @param string $indexName
     */
    public function setIndexName($indexName)
    {
        $this->indexName = $indexName;

        return $this;
    }

    /**
     * @param string $typeName
     */
    public function setTypeName($typeName)
    {
        $this->typeName = $typeName;

        return $this;
    }

    /**
     * @param array $data
     */
    public function write($data)
    {
        $doc = new \Elastica\Document('', $data);
        $this->client->getIndex($this->indexName)
                     ->getType($this->typeName)
                     ->addDocument($doc);
    }
}

/**
* Example of using Phirehose to display a live filtered stream using track words
*/
class FilterTrackConsumer extends \OauthPhirehose
{
    protected $storage = null;

    /**
     * @param \ElasticsearchStorage $storage
     */
    public function setStorage(\ElasticsearchStorage $storage)
    {
        $this->storage = $storage;
    }

    /**
     * @param string $status
     */
    public function enqueueStatus($status)
    {
        $data = json_decode($status, true);
        if ($this->storage !== null) {
            $this->storage->write($data);
        }
        if (is_array($data) && isset($data['user']['screen_name'])) {
            print $data['user']['screen_name'] . ': ' . urldecode($data['text']) . "\n";
        }
    }
}

$elasticaClient = new \Elastica\Client(array(
    'host' => '127.0.0.1',
    'port' => 9200
));
$storage = (new \ElasticsearchStorage($elasticaClient))
    ->setIndexName('twitter_php')
    ->setTypeName('tweet');

array_shift($argv);

// Start streaming
$sc = new FilterTrackConsumer(OAUTH_TOKEN, OAUTH_SECRET, Phirehose::METHOD_FILTER);
$sc->setStorage($storage);
$sc->setTrack($argv);
$sc->consume();
