import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

from digikala.spiders.incredibles import IncrediblesSpider
from digikala.spiders.product import ProductSpider


class Orchestrator:
    def run_spiders(self):
        # Create a single CrawlerProcess instance
        process = CrawlerProcess(get_project_settings())
        # Run the IncrediblesSpider first
        process.crawl(IncrediblesSpider)
        # Join the process and wait for the spider to finish
        process.join()
        # Run the ProductSpider for each productId from the IncrediblesSpider
        for product_data in IncrediblesSpider.product_data:
            productId = product_data['id']
            process.crawl(ProductSpider, productId=productId, product_data=product_data)
        # Start the process
        process.start()

if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run_spiders()
