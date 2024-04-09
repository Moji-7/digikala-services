# Import the necessary modules
import json
import scrapy
from scrapy.spiders import Spider
from scrapy.utils.response import open_in_browser
from scrapy import signals
import redis
r = redis.Redis(host="localhost", port="6379", db=0)

class CommentSpider(Spider):
    name = 'comment'
    # Use the productId argument to construct the start_urls
    def __init__(self, productId=None, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        self.productId = productId
        self.args = kwargs
        self.comments_data_all = []
        self.redis = redis.Redis(host="localhost", port="6379", db=0)

    def start_requests(self):
        base_url = f'https://api.digikala.com/v1/product/{self.productId}/comments/' #806044
        num_pages = 2 # shoulb be more
        for page in range(1, num_pages + 1):
            url = base_url + f'?page={page}'
            request = scrapy.Request(url, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        data = json.loads(response.body)
        comments = data['data']['comments']
        productId = self.productId

        for comment in comments:
            comment_data = {
                'id': comment['id'],
                'product_id': productId,
                'title': comment['title'],
                'body': comment['body'],
                'created_at': comment['created_at'],
                'rate': comment['rate'],
                'likes': comment['reactions']["likes"],
                'dislikes': comment['reactions']["dislikes"],
                'recommendation_status': comment['recommendation_status'],
                # Check if the seller information is available, and if not, assign null
                'seller_id' :"", #comment['purchased_item']["seller"]["id"] if comment.get('purchased_item', {}).get('seller') else None,
                'seller_title' :"", #comment['purchased_item']["seller"]["title"] if comment.get('purchased_item', {}).get('seller') else None,
                'seller_code' :"", #comment['purchased_item']["seller"]["code"] if comment.get('purchased_item', {}).get('seller') else None,
                'advantages': comment['advantages'],
                'disadvantages': comment['disadvantages'],
            }
            #print(comment_data)
            self.comments_data_all.append(comment_data)
            yield {**comment_data}

    def closed(self, reason):
        #print(self.comments_data_all)
        print('Ali')
        print('Ali')
        print('Ali')
        r.publish("scrapy_comment_channel", json.dumps(self.comments_data_all))
