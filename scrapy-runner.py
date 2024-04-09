# scrapy-runner.py
import sys
import importlib
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class ScrapyRunner:
    def __init__(self, spider_module, spider_class_name, **kwargs):
        self.spider_module = spider_module
        self.spider_class_name = spider_class_name
        self.spider_kwargs = kwargs
        self.process = CrawlerProcess(get_project_settings())

    def run_spider(self):
        # Dynamically import the spider class
        SpiderModule = importlib.import_module(self.spider_module)
        SpiderClass = getattr(SpiderModule, self.spider_class_name)
        self.process.crawl(SpiderClass, **self.spider_kwargs)
        self.process.start()

if __name__ == '__main__':
    spider_module = sys.argv[1]  # The module where the spider is located
    spider_class_name = sys.argv[2]  # The name of the spider class to run
    product_id = sys.argv[3]  # The product ID to pass to the spider

    runner = ScrapyRunner(spider_module, spider_class_name, productId=product_id)
    runner.run_spider()
