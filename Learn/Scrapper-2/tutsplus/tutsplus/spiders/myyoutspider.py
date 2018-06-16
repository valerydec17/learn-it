from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from tutsplus.items import AlternativetoItem
from tutsplus.items import YoutubeItem
from scrapy.http    import Request
import re
import os
from bs4 import BeautifulSoup
import pdb

crawledLinks = []

class MySpider(Spider):
	name            = "myyout"
	allowed_domains = ["youtube.com"]
	start_urls      = ["https://www.youtube.com/user/VEVO"]


	def parse(self, response):
		os.system('echo ' + ' !!!!!!!!!!!!! ' + ' >> yout_log.txt')
		os.system('echo ' + ' '.join(crawledLinks) + ' >> yout_log.txt')
		
		# Parse Item
		# item = AlternativetoItem()
		# item["title"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract()[0]
		# item["likes"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/div/div[2]/span/text()').extract() 
		# item["description"] = response.xpath('/html/body/form/section/div[2]/div[1]/div[1]/div/span/text()').extract()
		# item["officialSite"] = response.xpath('/html/body/form/section/div[2]/div[3]/div[1]/div/a[2]/text()').extract()

		# os.system('echo  Hi ' + ' '.join(response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract() )  + ' >> items.txt')

		str_title = ""
		str_shortDescription = ""
	
		item = YoutubeItem()
		# if statements should be put here

		# Grabs the loaded page for desirable items and perks.
		try:


			pdb.set_trace()

			# //*[@id="text"]
			# //*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]
			# //*[@id="button"]
			# //*[@id="text"]

			# item["title"] = response.xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch/div[2]/div[2]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string/text()').extract()[0]
			# item["liked"] = 
			# item["disliked"] = response.xpath('//*[@id="text"]/text()').extract()[0]
			# item["channelName"] = 


			# str_title = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract()[0]
			# str_shortDescription = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/p/text()').extract()[0]

			# item["atitle"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1/text()').extract()[0].strip()
			# item["shortDescription"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/p/text()').extract()[0].strip()
			# item["likes"] = response.xpath('/html/body/form/section/div[2]/header/div[1]/div/div/div[2]/span/text()').extract()[0].strip() 
			# item["description"] = response.xpath('/html/body/form/section/div[2]/div[1]/div[1]/div/span/p/text()').extract()[0].strip()
			# item["officialSite"] = response.xpath('/html/body/form/section/div[2]/div[3]/div[1]/div/a[2]/@href').extract()[0].strip()

		except:
			print "Item not found on the page"

		print str_title, str_shortDescription

		# pdb.set_trace()

		# Parse links
		links = response.xpath('//a/@href').extract()
			
		linkPattern = re.compile("\/watch\?")

		linksToCrawl = []
		for link in links:
			if linkPattern.match(link) and not link in crawledLinks:
				linksToCrawl.append(link)
				crawledLinks.append(link)

		for link in linksToCrawl:
			link = "https://www.youtube.com" + link
			print "New link started: ", link, "  CrawledPages: ", str(len(crawledLinks)) 
			os.system('echo ' + 'Link num. : ' + str(len(crawledLinks)) + ' Link :  ' + link + ' >> yout_log.txt')
			# crawledLinks.append(link)
			yield Request(link, self.parse)

		# # Avoids blanket lines in the output. Which for some reasons can occur.  	
		# if len(item["atitle"]) > 0:
		# 	yield item 


