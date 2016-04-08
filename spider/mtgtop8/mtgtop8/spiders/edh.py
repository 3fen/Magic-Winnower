import scrapy

class EDHSpider(scrapy.Spider):
    name = 'edh'
    allowed_domains = ['mtgtop8.com']
    start_urls = [
        "http://news.ycombinator.com"
    ]

    def parse(self, response):
        for t in response.xpath('//body/center/table/tr/td/table/tr[@class="athing"]/td[@class="title"]/a/text()').extract():
            print '[EDH] title=<', t, '>'

