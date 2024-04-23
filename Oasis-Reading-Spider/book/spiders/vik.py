import scrapy
from scrapy import Selector, Request
from book.items import BookItem
import time, csv

class VikSpider(scrapy.Spider):
    name = 'vik'
    allowed_domains = ['book.vik.im']

    def start_requests(self):
        with open('C:\\wangke\\computer_science\\15.scrapy\\book\\test.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield Request(url=row['url'])

    def parse(self, response):
        # 生成书籍id
        sel = Selector(response)
        book_item = BookItem()
        book_id = int(round(time.time() * 1000))

        book_item['id'] = book_id
        book_item['title'] = sel.xpath('//h1[@class="title"]/text()').extract_first()
        book_item['author'] = sel.xpath('//*[@itemprop="author"]/a/text()').extract_first()
        book_item['language'] = sel.xpath('//*[@itemprop="inLanguage"]/text()').extract_first()
        book_item['rate'] = eval(sel.xpath('//*[@itemprop="ratingValue"]/text()').extract_first()) * 10
        book_item['publisher'] = sel.xpath('//*[@itemprop="publisher"]/text()').extract_first()
        book_item['description'] = sel.xpath('//*[@itemprop="description"]//text()').getall()
        book_item['book_path'] = sel.xpath('//*[@title="epub"]/@href').extract_first()
        book_item['book_url'] = f"http://114.67.248.226:5000/books/{book_item['id']}.epub"
        book_item['img_path'] = sel.xpath('//div[@id="cover"]//img/@src').extract_first()
        book_item['img_url'] = f"http://114.67.248.226:5000/covers/{book_item['id']}.jpeg"
        yield book_item