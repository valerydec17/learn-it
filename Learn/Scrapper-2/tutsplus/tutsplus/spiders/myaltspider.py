from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from scrapy.http    import Request
import re
import os
# import pdb



class MySpider(Spider):
	name            = "myalt"
	allowed_domains = ["alternativeto.net"]
	start_urls      = ["https://alternativeto.net/"]

	def parse(self, response):
		links = response.xpath('//a/@href').extract()
		
		crawledLinks = []
		linkPattern = re.compile("^\/software\/")

		linksToCrawl = []
		for link in links:
			if linkPattern.match(link) and not link in crawledLinks:
				linksToCrawl.append(link)

		# pdb.set_trace()
		# print linksToCrawl

		for link in linksToCrawl:
			link = "https://alternativeto.net" + link
			print "New link started: ", link, "  CrawledPages: ", str(len(crawledLinks)) 
			os.system('echo ' + 'Link num. : ' + str(len(crawledLinks)) + ' Link :  ' + link + ' >> alt_log.txt')
			crawledLinks.append(link)
			yield Request(link, self.parse)

