from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from scrapy.http    import Request
import re
import os


class MySpider(Spider):
	name            = "myalt"
	allowed_domains = ["alternativeto.net"]
	start_urls      = ["https://alternativeto.net/"]

	def parse(self, response):
		links = response.xpath('//a/@href').extract()
		crawledLinks = []
		for link in links:
			link = "https://alternativeto.net/" + link
			print "New link started: ", link, "  CrawledPages: ", str(len(crawledLinks)) 
			os.system('echo ' + str(len(crawledLinks)) + link + ' >> alt_log.txt')
			crawledLinks.append(link)
			yield Request(link, self.parse)

