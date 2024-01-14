import gzip
import http.client
import scrapy

class MySpider(scrapy.Spider):
    name = 's3'

    def start_requests(self):
        conn = http.client.HTTPSConnection("api.digikala.com")
        payload = ''
        headers = {
            'Accept-Encoding': ' gzip, deflate, br',
            'Cookie' : 'Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;'
        }
        conn.request("GET", "/v1/profile/orders/?activeTab=sent&page=2&status=sent", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = gzip.decompress(data)  # decompress the data
        decoded_data = data.decode("utf-8")  # decode the data as utf-8
        yield scrapy.Request(url="https://api.digikala.com/v1/profile/orders/?activeTab=sent&status=sent/", callback = self.parse, meta = {'dont_redirect': True, 'dont_merge_cookies': True})

    def parse(self, response):
        data = response.body.decode("utf-8")  # Assuming text-based response
        print(data)
        yield {"data": data}  # Yield as a single item
        # Parse the response here
        pass
