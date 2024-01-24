import mysql.connector

class MySQLPipeline:

    def __init__(self, host, user, password, database):
        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="digikala"
        )
        self.cursor = self.db.cursor()

    def save_todb(self,values):
        # Insert the item into the MySQL table
        insert_query = """
        INSERT INTO incredibles (id, title_fa, title_en, url, brand, category, item_category2, item_category3, 
        item_category4, item_category5, main_image_url, is_fast_shipping, is_ship_by_seller, min_price_in_last_month, 
        seller_id, seller_title, seller_url, selling_price, rrp_price, order_limit, is_incredible, discount_percent, 
        shipment_description, has_lead_time) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # values = (
        #     item['id'], item['title_fa'], item['title_en'], item['url'], item['brand'], item['category'],
        #     item['item_category2'], item['item_category3'], item['item_category4'], item['item_category5'],
        #     item['main_image_url'], item['is_fast_shipping'], item['is_ship_by_seller'], item['min_price_in_last_month'],
        #     item['seller_id'], item['seller_title'], item['seller_url'], item['selling_price'], item['rrp_price'],
        #     item['order_limit'], item['is_incredible'], item['discount_percent'], item['shipment_description'],
        #     item['has_lead_time']
        # )
        try:
            self.cursor.executemany(insert_query, values)
            self.db.commit()
            print("Orders saved successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")