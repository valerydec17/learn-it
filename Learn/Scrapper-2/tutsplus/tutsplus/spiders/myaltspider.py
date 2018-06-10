from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from tutsplus.items import AlternativetoItem
from scrapy.http    import Request
import re
import os

import pdb

crawledLinks = []

class MySpider(Spider):
	name            = "myalt"
	allowed_domains = ["alternativeto.net"]
	start_urls      = ["https://alternativeto.net/"]


	def parse(self, response):
		os.system('echo ' + ' !!!!!!!!!!!!! ' + ' >> alt_log_1.txt')
		os.system('echo ' + ' '.join(crawledLinks) + ' >> alt_log_1.txt')
		
		# Parse Item
		# item = AlternativetoItem()
		# item["title"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract()[0]
		# item["likes"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/div/div[2]/span/text()').extract() 
		# item["description"] = response.xpath('/html/body/form/section/div[2]/div[1]/div[1]/div/span/text()').extract()
		# item["officialSite"] = response.xpath('/html/body/form/section/div[2]/div[3]/div[1]/div/a[2]/text()').extract()

		# os.system('echo  Hi ' + ' '.join(response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract() )  + ' >> items.txt')

		str_title = ""
		str_shortDescription = ""
		
		try:
			str_title = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract()[0]
			str_shortDescription = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/p/text()').extract()[0]
		except:
			print "Item not found on the page"

		print str_title, str_shortDescription


		item = AlternativetoItem()
		# if statements should be put here
		item["title"] = str_title.strip()
		item["shortDescription"] = str_shortDescription.strip()

		# os.system('echo Hi >> items.txt')
		os.system('echo ' + str_title.strip() + ' >> items.txt')
		os.system('echo ' + str_shortDescription.strip() + ' >> items.txt')

		# pdb.set_trace()


		item["title"] = "6"
		item["likes"] =  "5"
		item["shortDescription"] = "4"
		item["description"] = "3"
		item["officialSite"] = "1"



		# Parse links
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





# /html/body/form/section/div[2]/header/div[1]/div/h1     - title

# /html/body/form/section/div[2]/header/div[1]/div/div/div[2]/span   -   likes

# /html/body/form/section/div[2]/div[1]/div[1]/div/span      --  description

# /html/body/form/section/div[2]/header/div[1]/div/p  - short description

# /html/body/form/section/div[2]/div[3]/div[1]/div/a[2]  - official site


