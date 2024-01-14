# Import the necessary modules
import scrapy
import json

from urllib.parse import parse_qs, urlencode

import datetime

#from proxy.redis.redis_helper import save_result_to_redis


# Define your category spider class
class SourceSpider(scrapy.Spider):
    name = "categories"
    base_url = "https://api.digikala.com/v1/promotions/plp_82840308/"
    params = {"sort": 7, "page": 1}
    query = urlencode(params)
    start_urls = [f"{base_url}?{query}"]
    headers = {
        "authority": "api.digikala.com",
        ":method": "GET",
        ":path": "/v1/digipay/balance/",
        ":scheme": "https",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-IR,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6",
        "Cookie": "tracker_glob_new=clNqw7W; _hjSessionUser_2754176=eyJpZCI6IjQyZWJmOWVhLTY2YWEtNTJjMC05ZTA0LWIwN2E5ODEzOGYzZCIsImNyZWF0ZWQiOjE2ODIzMjEzODI0MzQsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1x1r5yx|1|fbd|0; _ga_S5JJQD4MDE=GS1.1.1683355713.1.0.1683355722.0.0.0; _ga_4S04WR965Q=GS1.1.1685541595.14.1.1685544510.0.0.0; _ga_YTPKDQLPZM=GS1.1.1685544532.2.0.1685544532.0.0.0; Digikala:General:Location=NG1JU3pMSHdMamdDSlJZcGhZa251Zz09%26UEcvazFZTm5Ya00vaDliVXVXUkR4TTVDYnJzZ0w3dE5pYmk1SHNqUVFRTDRkYWtlV21aRnF1K2lhMjVnRm1nb2xkUFd2ZEl4RTF1SnYzNGxheDFuUWc9PQ~~; _conv_v=vi%3A1*sc%3A16*cs%3A1687256791*fs%3A1682321382*pv%3A189*seg%3A%7B10002577.1%7D*ps%3A1687254037*exp%3A%7B%7D; _ga_81X0VRMPVE=GS1.1.1691211770.4.1.1691211821.0.0.0; _ga_LR50FG4ELJ=GS1.1.1694421379.26.1.1694422922.52.0.0; _ga=GA1.1.1761187454.1682321379; _ga_50CEWK5GC9=GS1.1.1696246813.18.0.1696246813.0.0.0; Digikala:User:Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwMDY0MTA2OSwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.Kuc7zRE_1WRGMFclgUJM2YcrJIJhvqW6RR35_JgC8Iw; Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjg2NzkxLCJleHBpcmVfdGltZSI6MTcwMzc3MzA1MiwicGF5bG9hZCI6W10sInBhc3N3b3JkX3ZlcnNpb24iOjEsInR5cGUiOiJ0b2tlbiJ9.vtv-eS9hMGlK_vfVyBWYULIfJrxyJs2wXFCe-vKkmPE; ab_test_experiments=%5B%22c6f6be9223db7a046f937687eb253977%22%5D; TS01b6ea4d=010231059107efbe7a20e8c6dea5d89a57ae00be88ba26ac46253899a9017acc56b6cb7533d5eafaedd5633115d438cb03290608b3b42973f2bc8f060372abb9fb18d70259; _sp_ses.13cb=*; tracker_session=3wJ7gpq; TS01c77ebf=0102310591b07215bdfc8c03b8bcbfbb4ba539ab75adad707326d2eca49c9566706f0c3185e8ed18d2cca79f1ac75c2307497cebcfe2873f1eef07168b2218841faa3f099045d9aa003e355f14fbf8f16dadeb2ff0; _hp2_ses_props.1726062826=%7B%22z%22%3A1%2C%22ts%22%3A1702883523742%2C%22d%22%3A%22www.digikala.com%22%2C%22h%22%3A%22%2F%22%2C%22t%22%3A%22%D9%81%D8%B1%D9%88%D8%B4%DA%AF%D8%A7%D9%87%20%D8%A7%DB%8C%D9%86%D8%AA%D8%B1%D9%86%D8%AA%DB%8C%20%D8%AF%DB%8C%D8%AC%DB%8C%E2%80%8C%DA%A9%D8%A7%D9%84%D8%A7%22%7D; amp_d18768=XrGlZn9olh0HrwDXV4AK42.ODgwOTI3MzAtNzMxZS00ODAzLWJhZjEtMTUzZmEwZGUwNWQz..1hhts8qqb.1hhtshjcn.0.0.0; _hp2_id.1726062826=%7B%22userId%22%3A%223869217090784928%22%2C%22pageviewId%22%3A%223681775620752510%22%2C%22sessionId%22%3A%222152363281157860%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_QQKVTD5TG8=GS1.1.1702883524.40.1.1702883809.0.0.0; _sp_id.13cb=623cff0c-f9cb-4cd8-b608-b516633a0344.1682321376.90.1702883810.1702873761.6a1625f6-6ba5-4b12-8354-28d944f200a2.4845de9b-e33d-4f18-9bfa-83628c61d156.2075505a-452a-4ef2-abd6-394390574b19.1702883521912.22",
        "Origin": "https://www.digikala.com",
        "Referer": "https://www.digikala.com/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty"
    }
    def parse(self, response):
        # Call the function with the folder path you want to delete
        #delete_folder_content()
        data = json.loads(response.body)
        results = []  # List to store the yielded items
        for product in data["data"]["products"]:
            product_id = product["id"]
            product_title = product["title_fa"]
            product_url = product["url"]["uri"]

            yield {
                "id": product_id,
                "title_fa": product_title,
                "url": product_url
            }
        results.append({
            "id": product_id,
            "title_fa": product_title,
            "url": product_url
        })

        # current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # key = f"result:{current_datetime}"
        # save_result_to_redis(json.dumps(results), key)

        pages = list(range(1, 1))
        total_pages = int(data["data"]["pager"]["total_pages"])/20
        current_page = parse_qs(response.url)["page"][0]
        current_page = int(current_page)

        if current_page in pages:
            index = pages.index(current_page)
            if index < len(pages) - 1:
                next_page = pages[index + 1]
                next_page_url = response.url.replace(f"page={current_page}", f"page={next_page}")
                print("next_page_url: " + next_page_url)
                #yield scrapy.Request(next_page_url, callback=self.parse)
                yield scrapy.Request(next_page_url, headers=self.headers, callback=self.parse)

