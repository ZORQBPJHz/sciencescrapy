# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SciencescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    issue = scrapy.Field()
    vol = scrapy.Field()
    year = scrapy.Field()
    date = scrapy.Field()
    img = scrapy.Field()
    img_name = scrapy.Field()
    summary = scrapy.Field()
    pass
