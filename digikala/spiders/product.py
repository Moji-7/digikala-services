# Import the Redis library
import json
import scrapy


import redis
r = redis.Redis(host="localhost", port="6379", db=0)

class ProductSpider(scrapy.Spider):
    name = 'product'
    # Use the productId argument to construct the start_urls
    def __init__(self, productId=None, product_data=None, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.productId = productId
        self.product_data = product_data
        self.start_urls = [f'https://api.digikala.com/v1/product/{productId}/']
        self.args = kwargs  # Define the args attribute and assign it to kwargs


    def parse(self, response):
        self.variant_data_all = []
        data = json.loads(response.body)
        variants = data['data']['product']['variants']
        productId = data['data']['product']['id']

        for variant in variants:
            variant_data = {
                'id': variant['id'],
                'product_id': productId,
                'seller_id': variant['seller']['id'],
                'seller_title': variant['seller']['title'],
                'seller_url': variant['seller']['url'],
                'selling_price': variant['price']['selling_price'],
                'rrp_price': variant['price']['rrp_price'],
                'order_limit': variant['price']['order_limit'],
                'is_incredible': variant['price']['is_incredible'],
                'discount_percent': variant['price']['discount_percent'],
            }
            #print(variant_data)
            self.variant_data_all.append(variant_data)
            yield {**variant_data}
    def closed(self, reason):
        #print("aaa")
        r.publish(self.name, json.dumps(self.variant_data_all))
