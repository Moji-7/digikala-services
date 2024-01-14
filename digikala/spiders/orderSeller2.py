import scrapy

CUSTOM_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"

class DigikalaSpider(scrapy.Spider):
    name = "dd"
    base_url = "https://api.digikala.com/v1/profile/orders/?activeTab=sent&status=sent/"
    Cookie = "Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwNTQ5OTgxMSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.1PO-JDop48Fa4OOxEJA-wnILjKZ34HnsV3WOc14KJew;"

    def __init__(self, page=1, *args, **kwargs):
        super(DigikalaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"{self.base_url}&page={page}"]

    def start_requests(self):
        headers = {
            'Accept-Encoding': ' gzip, deflate, br',
            "Cookie": self.Cookie}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse, meta = {'dont_redirect': True, 'dont_merge_cookies': True})

    def parse(self, response):
        try:
            data = response.body.decode("utf-8")  # Assuming text-based response
            yield {"data": data}  # Yield as a single item
        except Exception as e:
            self.logger.error(f"Error processing response: {e}")

    # Set the user agent in the custom_settings attribute
    custom_settings = {
        "USER_AGENT": CUSTOM_USER_AGENT
    }
