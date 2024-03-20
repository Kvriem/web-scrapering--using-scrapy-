# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahoofinanceItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price= scrapy.Field()
    change= scrapy.Field()
    percent_change= scrapy.Field()
    volume_in_currency_24Hr= scrapy.Field()

