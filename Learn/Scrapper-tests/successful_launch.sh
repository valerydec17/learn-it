cd ..
cd Scrapping/scrapper/
source venv/bin/activate
TEST_DIR=~/learn-it/Learn/Scrapper-tests

cd batch-example/Scrapy-Samples/crawlspider
scrapy crawl craigs -o $TEST_DIR/items.csv -t csv

 

