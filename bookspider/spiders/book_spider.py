import scrapy
from bookspider.items import BookItem, BookChapterItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        for sel in response.xpath('//*[@id="main"]/div[1]/ul/li[1]'):
            item = BookItem()
            item['title'] = sel.xpath('a/text()').extract()[0]
            item['link'] = sel.xpath('a/@href').extract()[0]
            yield scrapy.Request(item['link'],
                                 callback=self.parse_book_chapter,
                                 meta={'book_title': item['title']})

    def parse_book_chapter(self, response):
        for sel in response.xpath('//*[@id="list"]/dl/dd[*]'):
            item = BookChapterItem()
            item['book'] = response.meta.get('book_title')
            item['title'] = sel.xpath('a/text()').extract()[0]
            item['link'] = sel.xpath('a/@href').extract()[0]
            yield item
