
import json
import scrapy

from digikala.spiders.product import ProductSpider
from scrapy import signals

from scrapy.signalmanager import dispatcher

# Connect to redis
import redis
r = redis.Redis(host="localhost", port="6379", db=0)

class IncrediblesSpider(scrapy.Spider):
    name = 'incredibles'
    start_urls = ['https://api.digikala.com/v1/fresh-offers/']
    # Add custom_settings attribute
    custom_settings = {
        'ITEM_PIPELINES': {}
    }

    # def __init__(self):
    #     # Connect a signal listener for spider_closed
    #     dispatcher.connect(self.spider_closed, signals.spider_closed)
    def parse(self, response):
        self.incredibleproducts_all = []
        self.relatedProducts_all = []
        data = json.loads(response.body)
        Incredibleproducts = data['data']['selected_incredible_products']['products']

        for product in Incredibleproducts:
            incredibleproducts_all = {
                'id': product['id'],
                'title_fa': product['title_fa'],
                'title_en': product['title_en'],
                'url': product['url']['uri'],
                'brand': product['data_layer']['brand'],
                'category': product['data_layer']['category'],
                'item_category2': product['data_layer']['item_category2'],
                'item_category3': product['data_layer']['item_category3'],
                'item_category4': product['data_layer']['item_category4'],
                'item_category5': product['data_layer']['item_category5'],
                'main_image_url': product['images']['main']['url'][0],
                'is_fast_shipping': product['properties']['is_fast_shipping'],
                'is_ship_by_seller': product['properties']['is_ship_by_seller'],
                'min_price_in_last_month': product['properties']['min_price_in_last_month'],
                'seller_id': product['default_variant']['seller']['id'],
                'seller_title': product['default_variant']['seller']['title'],
                'seller_url': product['default_variant']['seller']['url'],
                'selling_price': product['default_variant']['price']['selling_price'],
                'rrp_price': product['default_variant']['price']['rrp_price'],
                'order_limit': product['default_variant']['price']['order_limit'],
                'is_incredible': product['default_variant']['price']['is_incredible'],
                'discount_percent': product['default_variant']['price']['discount_percent'],
                'shipment_description': product['default_variant']['shipment_methods']['description'],
                'has_lead_time': product['default_variant']['shipment_methods']['has_lead_time']
            }
            print(incredibleproducts_all)
            self.incredibleproducts_all.append(incredibleproducts_all)
            # Yield a request object with the product data as arguments
            yield scrapy.Request(url=f'https://api.digikala.com/v1/product/{product["id"]}/', callback=self.run_product_spider, cb_kwargs=incredibleproducts_all)

    # Define a method to run the Incredibleproductspider class
    def run_product_spider(self, response, **kwargs):
        # Create an instance of the ProductSpider class
        product_spider = ProductSpider(productId=kwargs['id'], incredibleproducts_all=kwargs)
        for data in product_spider.parse(response):
            # Put your data into a list
            data_list = [data]
            # Convert the list to a JSON string
            json_string = json.dumps(data_list)
            self.relatedProducts_all.append(data)
        return product_spider.parse(response)

    def closed(self, reason):
        r.publish(self.name, json.dumps(self.incredibleproducts_all))
        #r.publish("product", json.dumps(self.relatedProducts_all))



