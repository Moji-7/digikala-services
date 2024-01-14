# Import the scrapy module and the Request and JsonItem classes
from urllib.request import Request

import scrapy


class DigikalaItem():

    # For example, you can add fields for the order id, date, status, etc.
    order_id = scrapy.Field()
    order_date = scrapy.Field()
    order_status = scrapy.Field()


class DigikalaSpider(scrapy.Spider):

    name = "login"

    start_urls = ["https://api.digikala.com/v1/profile/orders/?activeTab=sent&page=2&status=sent"]


    def parse(self, response):
        # Create a Request object that will send the same headers and cookies that you used in your python class
        # You also need to specify a callback method that will handle the response from the API
        return Scrapy.Request(
            url=response.url,
            headers={
                'Accept-Encoding': ' gzip, deflate, br',
                'Cookie': 'Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;',
            },
            callback=self.parse_api
        )

    # Define the callback method that will parse the JSON data from the response and yield items or requests
    def parse_api(self, response):
        # Parse the JSON data from the response and yield items or requests
        # You can use the response.json method to load the data as a dictionary
        data = response.json()
    #     # You can then iterate over the data and extract the information that you want
    #     for order in data["orders"]:
    #         # Create an item object using the custom item class that you defined
    #         item = DigikalaItem()
    #         # Assign the values to the item fields
    #         item["order_id"] = order["id"]
    #         item["order_date"] = order["date"]
    #         item["order_status"] = order["status"]
    #         # Yield the item
    #         yield item
    #         # You can also make requests to other API endpoints using the headers and cookies that you used before
    #         # For example, you can make a request to get the details of each order
    #         # You can use response.follow or Request methods, as explained before
    #         # You also need to specify a callback method that will handle the response from the API
    #         yield response.follow(
    #             url=f"https://api.digikala.com/v1/profile/orders/{order['id']}/",
    #             #callback=self.parse_order_details,
    #             headers=response.request.headers
    #         )

