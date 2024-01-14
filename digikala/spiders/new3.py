import json

from scrapy import Request
import scrapy
from scrapy.exporters import JsonItemExporter
from scrapy import signals

from itemloaders import ItemLoader

from itemloaders.processors import TakeFirst, Identity

from scrapy.exporters import JsonItemExporter
from digikala.items import OrderTotalInfo,OrderPaymentInfo
from digikala.items import (
    OrderRoot,
    OrderItemProductroot,OrderItemProduct, OrderItemUrl, OrderItemDataLayer, OrderItemImages, OrderItemMainImage, OrderItemVariant,
    OrderItemPrice,OrderItemSeller)

import redis

# define  item loader class
class OrderRootLoader(ItemLoader):
    default_item_class = OrderRoot
    default_output_processor = TakeFirst() # use TakeFirst for all fields
    order_item_out = Identity() # keep the order_item field as a list


class MySpider(scrapy.Spider):
    name = 'myOrders'

    def start_requests(self):
        request = Request.from_curl(
            "curl --location 'https://api.digikala.com/v1/profile/orders/?activeTab=sent&page=2&status=sent' --header 'Cookie:Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;'"
        )
        yield request

    def parse(self, response):
        data = response.json()
        #print(data["data"]["orders"][0]['id'])
        cookie='Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;'
        #yield from self.second_stepApi(data, cookie)
        yield from self.step_orderDetails(data, cookie)

    def step_orderDetails(self, data, cookie):
        for order in data["data"]["orders"]:
            #print(order["id"])
            order_id = order["id"]
            order_url = f"https://api.digikala.com/v1/order/{order_id}/?orderId={order_id}"
            request = Request.from_curl(
                f"curl --location '{order_url}' --header 'Cookie:Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;' -X GET",
                callback=self.parse_orderDetails  # this will override the -X option and call the parse() method
            )
            yield request

    def parse_orderDetails(self, response):
        data = response.json()
        #order_root = OrderRoot()
        # create an item loader instance with the response
        order_root = OrderRootLoader(response=response)  # use your item loader class

        # order_root['id'] = data["data"]["order"]["id"]
        # order_root['payable_price'] = data["data"]["order"]["payable_price"]
        order_root.add_value('id', data["data"]["order"]["id"])
        order_root.add_value('payable_price', data["data"]["order"]["payable_price"])
        for order_item_data in data["data"]["order"]["order_items"]:
            order_item_ = OrderItemProductroot()
            order_item_ = self.parse_order_items(order_item_data)
            #print(order_item_result)
            #MOJ MOJ
            order_root.add_value('order_item', order_item_)


        # Load the item
        order_root = order_root.load_item()
        # Append the item to the list
        self.items.append(order_root)
        #print(order_root)
        yield order_root

    # Define the from_crawler class method
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(MySpider, cls).from_crawler(crawler, *args, **kwargs)
        # Create an empty list to store the items
        spider.items = []
        # Create a JsonItemExporter object
        spider.exporter = JsonItemExporter(open("order_data.json", "wb"))
        # Start exporting
        spider.exporter.start_exporting()
        # Connect the spider_closed signal to the closed method
        crawler.signals.connect(spider.closed, signal=signals.spider_closed)
        return spider

    # Define the closed method
    def closed(self, spider):
        # Export the items to the JSON file
        for item in self.items:
            self.exporter.export_item(item)
        # Finish exporting
        self.exporter.finish_exporting()
        # Close the file
        self.exporter.file.close()

        #0 write to file
        r = redis.Redis(host="localhost", port="6379", db=0)
        with open('order_data.json', 'r') as file:
            order_items_json = file.read()
        # Parse the JSON content
        ddd_orders = json.loads(order_items_json)

        #1 NOW PUBLISH
        r.publish("orders",(order_items_json))


    def parse_order_items(self, data):
        product_item = OrderItemProductroot()
        product_item['id'] = data['id']
        product_item['quantity'] = data['quantity']

        orderItem_product = OrderItemProduct()
        orderItem_product['id'] = data['product']['id']
        orderItem_product['title_fa'] = data['product']['title_fa']
        orderItem_product['title_en'] = data['product']['title_en']
        url = OrderItemUrl()
        url['uri'] = data['product']['url']['uri']
        orderItem_product['url'] = url
        orderItem_product['status'] = data['product']['status']

        #parent is orderItem_product
        data_layer = OrderItemDataLayer()
        data_layer['brand'] = data['product']['data_layer']['brand']
        data_layer['category'] = data['product']['data_layer']['category']
        data_layer['dimension20'] = data['product']['data_layer']['dimension20']
        data_layer['item_category2'] = data['product']['data_layer']['item_category2']
        data_layer['item_category3'] = data['product']['data_layer']['item_category3']
        # Populate other fields in data_layer
        orderItem_product['data_layer'] = data_layer


        images = OrderItemImages()
        main_image = OrderItemMainImage()
        main_image['storage_ids'] = data['product']['images']['main']['storage_ids']
        main_image['url'] = data['product']['images']['main']['url']
        images['main'] = main_image


        orderItem_product['images'] = images
        product_item['product'] = orderItem_product


        variant_item = OrderItemVariant()
        variant_item['id'] = data['variant']['id']


        orderItemPrice = OrderItemPrice()
        orderItemPrice["rrp_price"] = data['price']['rrp_price']
        orderItemPrice["selling_price"] = data['price']['selling_price']
        orderItemPrice["discount_percent"] = data['price']['discount_percent']
        orderItemPrice["is_incredible"] = data['price']['is_incredible']
        orderItemPrice["is_promotion"] = data['price']['is_promotion']
        orderItemPrice["is_locked_for_digiplus"] = data['price']['is_locked_for_digiplus']
        orderItemPrice["bnpl_active"] = data['price']['bnpl_active']
        product_item['price'] = orderItemPrice

        seller = OrderItemSeller()
        seller['id'] = data['variant']['seller']['id']
        seller['title'] = data['variant']['seller']['title']
        seller['code'] = data['variant']['seller']['code']
        seller['url'] = data['variant']['seller']['url']
        variant_item['seller'] = seller
        product_item['variant'] = variant_item
        # Populate price and other fields in product_item
        #print(product_item)
        return product_item


