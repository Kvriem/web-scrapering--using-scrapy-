import scrapy
from chocolate.items import productitem
from chocolate.itemloader import ChocolateProductLoader


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        products = response.css('.product-item')

        for product in products:
            
            chocolate = ChocolateProductLoader(item=productitem(), selector=product)
            chocolate.add_css('name', '.product-item-meta__title::text')
            chocolate.add_css('price','span.price',re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()

        next_page_url = response.xpath('//button[contains(@aria-label, "Jump to last page")]/@href').extract_first()

        if next_page_url:
            # Follow the next page URL
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)