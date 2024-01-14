# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DigikalaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
# items.py


class ProductItem(Item):
    # define the fields for your product item here like:
    id = Field()
    title = Field()
    image = Field()



class OrderTotalInfo(scrapy.Item):
    id = scrapy.Field()
    created_at = scrapy.Field()
    payable_price = scrapy.Field()
    status = scrapy.Field()
    last_delivery_at = scrapy.Field()
    product_images = scrapy.Field()

class OrderPaymentInfo(scrapy.Item):
    id = scrapy.Field()
    amount = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    successful = scrapy.Field()
    status = scrapy.Field()
    reference_code = scrapy.Field()
    is_user_paid = scrapy.Field()
    is_user_received = scrapy.Field()






class VariantItem(Item):
    # define the fields for your variant item here like:
    name = Field()
    price = Field()
    seller = Field()

class ProductItem(scrapy.Item):
    id = scrapy.Field()
    quantity = scrapy.Field()
    product = scrapy.Field()
    variant = scrapy.Field()
    price = scrapy.Field()



class OrderRoot(scrapy.Item):
    id = scrapy.Field()
    payable_price = scrapy.Field()
    orderItemProductroot = scrapy.Field()
    order_item = scrapy.Field(default=[])

####################################################################
#product in order_items
class OrderItemProductroot(scrapy.Item):
    id = scrapy.Field()
    quantity = scrapy.Field()
    product = scrapy.Field()
    variant = scrapy.Field()
    price = scrapy.Field()

class OrderItemUrl(scrapy.Item):
    base = scrapy.Field()
    uri = scrapy.Field()
class OrderItemImages(scrapy.Item):
    main = scrapy.Field()
class OrderItemMainImage(scrapy.Item):
    storage_ids = scrapy.Field()
    url = scrapy.Field()


####################################################################
#order_items > variant +price + product

#product
class OrderItemProduct(scrapy.Item):
    id = scrapy.Field()
    title_fa = scrapy.Field()
    title_en = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    data_layer = scrapy.Field()
    images = scrapy.Field()
#parent is product
class OrderItemDataLayer(scrapy.Item):
    brand = scrapy.Field()
    category = scrapy.Field()
    dimension20 = scrapy.Field()
    item_category2 = scrapy.Field()
    item_category3 = scrapy.Field()

class OrderItemPrice(Item):
    selling_price = scrapy.Field()
    rrp_price = scrapy.Field()
    order_limit = scrapy.Field()
    discount_percent = scrapy.Field()
    is_incredible = scrapy.Field()
    is_promotion = scrapy.Field()
    is_locked_for_digiplus = scrapy.Field()
    bnpl_active = scrapy.Field()


class OrderItemVariant(scrapy.Item):
    id = scrapy.Field()
    seller = scrapy.Field()
#parent is varient
class OrderItemSeller(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    code = scrapy.Field()
    url = scrapy.Field()
