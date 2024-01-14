# In your spider file, import the DigikalaAPI class and use it in your callback methods
import json

import scrapy

from digikala.spiders.simplepython import DigikalaAPI


class DigikalaSpider(scrapy.Spider):
    name = "new2"
    start_urls = ["https://www.digikala.com/"]

    def start_requests(self):
        # You can pass the cookie as a spider argument or hardcode it here
        self.api = DigikalaAPI("")
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # You can pass the active_tab, page, and status as spider arguments or hardcode them here
        data = self.api.get_orders("sent", 2, "sent")
        data = json.loads(data)
        # Loop through the orders in the data
        for order in data["data"]["orders"]:
            # Print the order for debugging purposes
            print(order["id"])
            # Get the order ID
            order_id = order["id"]
            # Construct the API URL for the order details
            order_url = f"https://api.digikala.com/v1/order/{order_id}/?orderId={order_id}"
            # Make a request to the order URL and pass the response to another callback function
            #yield scrapy.Request(url=order_url, callback=self.parse_order)

    def parse_order(self, response):
        # Load the response data as a Python dictionary using json.loads
        data = json.loads(response.text)
        # Extract the order details from the data
        order_details = data["data"]["order"]
        # Print the order details for debugging purposes
        print(order_details)
        # Yield the order details as an item or a request
        yield order_details