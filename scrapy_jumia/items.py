# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyJumiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()  # jumia id for this product
