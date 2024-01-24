# Import the Redis library
import json

import redis

# Define a custom pipeline class
class RedisPipeline:
    # Define the constructor
    def __init__(self, host, port, db, channel):
        # Initialize the Redis connection and channel
        self.r = redis.Redis(host=host, port=port, db=db)
        self.channel = channel

    # Define a class method to get the settings from the crawler
    @classmethod
    def from_crawler(cls, crawler):
        # Get the host, port, db, and channel from the settings
        host = crawler.settings.get('REDIS_HOST', 'localhost')
        port = crawler.settings.get('REDIS_PORT', 6379)
        db = crawler.settings.get('REDIS_DB', 0)
        channel = crawler.settings.get('REDIS_CHANNEL', 'product')
        # Return an instance of the pipeline class
        return cls(host, port, db, channel)

    # Define a method to process each item
    def process_item(self, item, spider):
        # Convert the item to JSON
        data = json.dumps(dict(item))
        # Publish the item to the channel
        self.r.publish(self.channel, data)
        # Return the item
        return item
####################################################################################################
####################################################################################################
# Then, you need to enable this pipeline in your settings.py file, like this:
# Enable the pipeline
ITEM_PIPELINES = {
    'digikala.pipelines.RedisPipeline': 300,
}