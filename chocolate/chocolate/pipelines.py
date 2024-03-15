# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


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