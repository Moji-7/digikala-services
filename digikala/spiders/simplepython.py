# Save this file as digikala.py in the same directory as your spider
import gzip
import http.client

class DigikalaAPI:
    def __init__(self, cookie):
        self.conn = http.client.HTTPSConnection("api.digikala.com")
        self.headers = {
            "Accept-Encoding": " gzip, deflate, br",
            'Cookie': 'Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;',
        }

    def get_orders(self, active_tab, page, status):
        path = f"/v1/profile/orders/?activeTab={active_tab}&page={page}&status={status}"
        #conn.request("GET", "/v1/profile/orders/?activeTab=sent&page=2&status=sent", payload, headers)
        self.conn.request("GET", path, "", self.headers)
        res = self.conn.getresponse()
        data = res.read()
        data = gzip.decompress(data) # decompress the data
        return data.decode("utf-8") # decode the data as utf-8
