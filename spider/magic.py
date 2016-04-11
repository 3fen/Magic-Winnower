import scrapy
import time

class StackOverflowSpider(scrapy.Spider):
    name = 'magic'
    #start_urls = ['http://stackoverflow.com/questions?sort=votes']
    start_urls = ['http://magiccards.info/soi/en.html']
    def parse(self, response):
        print len( response.xpath('//body/table[@cellpadding="3"]/tr'))
        for href in response.xpath('//body/table[@cellpadding="3"]/tr/td/a/@href'):
            full_url = response.urljoin(href.extract())
            print '[ full_url ]', full_url

            time.sleep(.5)
            yield scrapy.Request(full_url, callback=self.parse_question)
    def parse_question(self, response):
        yield {
            'img': response.xpath('//body/table/tr/td/img[@width=312]/@src').extract()[0],
            'link': response.url,
        }
