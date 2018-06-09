from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from scrapy.http    import Request
import re
import os

crawledLinks = []

class MySpider(Spider):
	name            = "myalt"
	allowed_domains = ["alternativeto.net"]
	start_urls      = ["https://alternativeto.net/"]


	def parse(self, response):
		os.system('echo ' + ' !!!!!!!!!!!!! ' + ' >> alt_log_1.txt')
		os.system('echo ' + ' '.join(crawledLinks) + ' >> alt_log_1.txt')
		links = response.xpath('//a/@href').extract()
		
		
		linkPattern = re.compile("^\/software\/[a-zA-Z0-9\-]+\/$")

		linksToCrawl = []
		for link in links:
			if linkPattern.match(link) and not link in crawledLinks:
				linksToCrawl.append(link)
				crawledLinks.append(link)

		for link in linksToCrawl:
			link = "https://alternativeto.net" + link
			print "New link started: ", link, "  CrawledPages: ", str(len(crawledLinks)) 
			os.system('echo ' + 'Link num. : ' + str(len(crawledLinks)) + ' Link :  ' + link + ' >> alt_log.txt')
			# crawledLinks.append(link)
			yield Request(link, self.parse)

