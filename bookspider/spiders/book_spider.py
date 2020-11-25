import scrapy
from bookspider.items import BookItem
from urllib.parse import urljoin


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        for sel in response.xpath('//*[@id="main"]/div[1]/ul/li[1]'):
            title = sel.xpath('a/text()').extract()[0]
            link = sel.xpath('a/@href').extract()[0]
            yield scrapy.Request(link,
                                 callback=self.parse_book_chapter,
                                 meta={'title': title, 'link': link})

    def parse_book_chapter(self, response):
        for sel in response.xpath('//*[@id="list"]/dl/dd[1]'):
            chapter_title = sel.xpath('a/text()').extract()[0]
            response.meta['chapter'] = chapter_title
            link = urljoin(response.meta['link'], sel.xpath('a/@href').extract()[0])
            print(link)
            yield scrapy.Request(link, callback=self.parse_book_content, meta=response.meta)

    def parse_book_content(self, response):
        print('hello world')
        book = BookItem()
        book['title'] = response.meta['title']
        book['chapter'] = response.meta['chapter']
        book['content'] = response.xpath('//*[@id="content"]/text()').extract()
        return book

