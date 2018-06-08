
TEST_DIR=~/learn-it/Learn/Scrapper-tests
CRAWLER_DIR=~/learn-it/Learn/Scrapping/scrapper/batch-example/Scrapy-Samples/crawlspider
VENV_DIR=~/learn-it/Learn/Scrapping/scrapper

cd $VENV_DIR
source venv/bin/activate

cd $CRAWLER_DIR

scrapy crawl craigs -o $TEST_DIR/items.csv -t csv
