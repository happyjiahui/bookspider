# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()


class BookChapterItem(scrapy.Item):
    book = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
