# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy


# class DigikalascrapItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
import scrapy

class ProductItem(scrapy.Item):
    id = scrapy.Field()
    image_main = scrapy.Field()
    image_urls = scrapy.Field()


class OrderGeneralInfo(scrapy.Item):
    id = scrapy.Field()
    created_at = scrapy.Field()
    payable_price = scrapy.Field()
    status = scrapy.Field()
    last_delivery_at = scrapy.Field()
    product_images = scrapy.Field()