import re
from urllib.parse import unquote
import scrapy


class TestSpider(scrapy.Spider):
    name = 'testi'

    def parse(self, response):
        #for set_cookie in response.headers.getlist('Set-Cookie'):
         #   try:
          #      xsrf_token = re.findall(r'XSRF-TOKEN=(\w+==);', unquote(set_cookie.decode('utf-8')))[0]
          #  except IndexError:
           #     pass

        yield scrapy.Request(
            url='https://api.digikala.com/v1/profile/orders/?activeTab=sent&page=2&status=sent',
            callback=self.parse_data,
            headers={
                'Host': ' api.digikala.com',
                'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept': ' application/json, text/plain, */*',
                'Accept-Language': ' en-US,en;q=0.5',
                'Accept-Encoding': ' gzip, deflate, br',
                'Referer': ' https://www.digikala.com/',
                'X-Web-Optimize-Response': ' 1',
                'X-Web-Client': ' desktop',
                'Origin': ' https://www.digikala.com',
                'Sec-Fetch-Dest': ' empty',
                'Sec-Fetch-Mode': ' cors',
                'Sec-Fetch-Site': ' same-site',
                'Connection': ' keep-alive',
                'Cookie': ' _ga_QQKVTD5TG8=GS1.1.1702907767.1.1.1702908708.0.0.0; _ga=GA1.1.1160383936.1702907768; _sp_ses.13cb=*; _sp_id.13cb=fd7d8a48-3060-4d01-87ba-b74d7dbec9e6.1702907772.1.1702908711..378e7e81-dc07-4ab6-be6a-17e5a63fb9bb..862a5c7f-acd7-4729-816c-af96b77918c3.1702907772070.9; tracker_glob_new=7uD23wh; tracker_session=5nLOwNH; TS01c77ebf=01023105917a366eb56379cf732a57c3bd9d3d559eda6cc734e0f1d1dc5988306b886def39456dfb6e9f69301983a604a69dc63ecd4942c6cbc10ac69119030151d9d3528676988e2ba4aa897f928875b2a20cdbae4571c659c585702adc065c628d38cb09ae551755dec07a7809b76059facae3e2ef5381804f49295fa8394f693a1f3be2949d2dcc372cdc93de82c8a56315307146bd49ce14e03513be092e4b70d2c0a9b2044d95242870a3adadbb7330541f2b02cccd6a8b178f8aa0f18dc7704ef4cb; _hp2_ses_props.1726062826=%7B%22z%22%3A0%2C%22ts%22%3A1702907773597%2C%22d%22%3A%22www.digikala.com%22%2C%22h%22%3A%22%2Fprofile%2Forders%2F%22%2C%22t%22%3A%22%D9%81%D8%B1%D9%88%D8%B4%DA%AF%D8%A7%D9%87%20%D8%A7%DB%8C%D9%86%D8%AA%D8%B1%D9%86%D8%AA%DB%8C%20%D8%AF%DB%8C%D8%AC%DB%8C%E2%80%8C%DA%A9%D8%A7%D9%84%D8%A7%22%2C%22q%22%3A%22%3FactiveTab%3Dsent%26page%3D2%22%7D; _hp2_id.1726062826=%7B%22userId%22%3A%22737957610243712%22%2C%22pageviewId%22%3A%225264766418412600%22%2C%22sessionId%22%3A%223227132610013838%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; PHPSESSID=9aek73f33evpk6gbc4vo5pshh9; TS01b6ea4d=01023105916069a7ce4de5a7c256a85941f9c282b8797e73081cbbb493ce9897b54519f1885f1a8399f63a48b59dac8125db4f6215069a0bf123dcb19b9183de85fdc4a58ce1882f19f2b002a0c8cfed2c2271804688487e04b2ce8f6b908a8208d940657b6c7918e141a7b426db57c962ea0703b7f558cd9b270f2175fc1ab3340133cb14; Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew; ab_test_experiments=%5B%22c6f6be9223db7a046f937687eb253977%22%5D; TS01c77ebf=0102310591d20a7aad6dac31e9a9c1f65e8c5432c1f62a7010088fb617247a2a30ba7d1092685441418c124cf13dc02c7df8f6a516b3d1589f9bd3912870edf55371f997c83abb202a201947418fc5f8de30c037787be31e86ce9c1384cefb233f2fe898a5bc249f2470b3742b4f9a90d615ccc8f4e12768da62b211750df397bc41eea6b6d102ae37130bf26ca7a17a87aabfdc239dc2b564f5a398eacf88c3d9bc9722143a6efaf1db782f8aaaaaff297338c873780211a9b273f5c6d722743870eb011d; tracker_glob_new=7uD23wh; tracker_session=5nLOwNH',
                'TE': ' trailers'
            }
        )
        data = response.json()
        print(data)

    def parse_data(self, response):
        pass