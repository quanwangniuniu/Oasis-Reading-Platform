import scrapy
from scrapy import Selector, Request
from book.items import UrlItem

class VikSpider(scrapy.Spider):
    name = 'url'

    def start_requests(self):
        for page in range(70):
            yield Request(url=f"https://book.vik.im/index.php?p={page}")


    def parse(self, response):

        sel = Selector(response)
        list_items = sel.css('div.list-book')

        for item in list_items:
            url_item = UrlItem()
            url_item['url'] = item.css('p.list-title > a::attr(href)').extract_first()
            yield url_item