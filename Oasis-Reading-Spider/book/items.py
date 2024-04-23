# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    language = scrapy.Field()
    rate = scrapy.Field()
    description = scrapy.Field()
    book_url = scrapy.Field()
    book_path = scrapy.Field()
    img_url = scrapy.Field()
    img_path = scrapy.Field()
    book_success = scrapy.Field()
    img_success = scrapy.Field()


class UrlItem(scrapy.Item):
    url = scrapy.Field()