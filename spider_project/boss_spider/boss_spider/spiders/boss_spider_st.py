import scrapy


class BossSpiderStSpider(scrapy.Spider):
    name = "boss_spider_st"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com"]

    def parse(self, response):
        pass
