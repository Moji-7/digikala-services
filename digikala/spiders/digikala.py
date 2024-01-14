import jsonpath
import scrapy

import json



class DigikalaSpider(scrapy.Spider):
    # Define the name of the digikala spider
    name = "product"
    def __init__(self, product_urls=None, *args, **kwargs):
        # Call the parent constructor
        super(DigikalaSpider, self).__init__(*args, **kwargs)
        # Set the start_urls as the product URLs
        self.start_urls = product_urls

    def parse(self, response):
        # Get the product ID from the URL
        product_id = response.url.split('/')[-2].split('-')[-1]
       
        api_url = f'https://api.digikala.com/v2/product/{product_id}/'
        # Send a GET request to the API URL
        yield scrapy.Request(api_url, callback=self.parse_api)

    def parse_api(self, response):
        # Parse the JSON object from the response
        data = response.json()
        # Create a product item
        item = ProductItem()
        # Get the product ID from the JSON object
        item["id"] = jsonpath.jsonpath(data, '$.data.product.id')
        # Get the main image URL from the JSON object
        item["image_main"]  = jsonpath.jsonpath(data, '$.data.product.images.main.url')
        # Get the list of image URLs from the JSON object
        item["image_urls"] = jsonpath.jsonpath(data, '$.data.product.images.list[*].url')
        # Return the product item
        yield item