# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from  scrapy.exceptions import DropItem

class ChocolatePipeline:
    def process_item(self, item, spider):
        return item

class priceToUSDPipline :
    
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        if adapter.get('price'):
            
            price = float(item['price'])
            
            adapter['price'] = price  * 1.3
            
            return item
        else:
            raise DropItem(f"Missing price in {item}")

class Duplicatespiplane:
    
    def __init__(self):
        self.name_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('name') in self.name_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.name_seen.add(adapter.get('name'))
            return item
##problem on the postgres database
##class SavingToPostgresPipeline(object):
##
##    def __init__(self):
##        self.create_connection()
##
##    def create_connection(self):
##        self.conn = psycopg2.connect(
##            host="localhost",
##            database="chocolate_scraping",
##            user="root",
##            password="123456")
##        self.curr = self.conn.cursor()
##
##    def process_item(self, item, spider):
##        self.store_in_db(item)
##        # We need to return the item below as Scrapy expects us to!
##        return item
##
##    def store_in_db(self, item):
##        self.curr.execute("""INSERT INTO chocolate_products VALUES (%s, %s, %s)""", (
##            item["name"],
##            item["price"],
##            item["url"]
##        ))
##        self.conn.commit()