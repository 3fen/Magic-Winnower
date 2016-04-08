import scrapy

class TitleSpider(scrapy.Spider):
    name = 'soli_title'
    allowed_domains = ['solidot.org']
    start_urls = [
        "http://www.solidot.org"
    ]

    def parse(self, response):
        for t in response.xpath('//body/div[@id="main"]/div[@id="center"]/div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/text()').extract():
            print '[EDH] title=<', t, '>'
