# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutsplusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()



class AlternativetoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    atitle = scrapy.Field()
    shortDescription = scrapy.Field()
    description = scrapy.Field()
    likes = scrapy.Field()
    officialSite = scrapy.Field()


class YoutubeItem(scrapy.Item):
	title = scrapy.Field()
	liked = scrapy.Field()
	disliked = scrapy.Field()
	channelName = scrapy.Field()
