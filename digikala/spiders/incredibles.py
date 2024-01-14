import scrapy


class IncrediblesSpider(scrapy.Spider):
    name = "incredibles"
    allowed_domains = ["digikala.com"]
    start_urls = ["http://digikala.com/"]

    def parse(self, response):
        pass
