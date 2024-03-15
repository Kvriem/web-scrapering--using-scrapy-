from email.policy import default
from scrapy. loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class ChocolateProductLoader(ItemLoader) :
    
    default_output_processor = TakeFirst() 
    price_in = MapCompose(lambda x: x.split('£')[-1])
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk'+ x)