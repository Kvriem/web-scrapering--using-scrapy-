import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    #collecting data about chocolate products from the website 
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        products=response.css('.product-item')
        
        for product in products:
            
            yield {
                'name': product.css('.product-item-meta__title::text').get(),
                'price': product.css('.product-item__info span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
                'link':  product.css('div.product-item-meta a').attrib['href'] 
            }
        next_page=response.css('a.pagination__nav-item:nth-child(5)').attrib['href']
        if next_page is not None:
            next_page_url='https://www.chocolate.co.uk'+next_page
            yield response.follow(next_page, callback=self.parse)