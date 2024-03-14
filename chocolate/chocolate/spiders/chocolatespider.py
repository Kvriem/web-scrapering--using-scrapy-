import scrapy
from items import productitem


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    #collecting data about chocolate products from the website 
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        products=response.css('.product-item')
        
        product_item = productitem()
        
        for product in products:
            
                product_item['name']= product.css('.product-item-meta__title::text').get(),
                product_item['price']= product.css('.product-item__info span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
                product_item['link']=  product.css('div.product-item-meta a').attrib['href'] 
                yield product_item

        next_page=response.css('a.pagination__nav-item:nth-child(5)').attrib['href']
        if next_page is not None:
            next_page_url='https://www.chocolate.co.uk'+next_page
            yield response.follow(next_page, callback=self.parse)