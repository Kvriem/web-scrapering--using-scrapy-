import scrapy

class YahoospiderSpider(scrapy.Spider):
    name = 'yahoospider'
    allowed_domains = ['https://finance.yahoo.com/crypto']
    start_urls = ['https://finance.yahoo.com/crypto']

    def parse(self, response):
        items = response.css('tr.simpTblRow')
        for item in items:
            name = item.css('td:nth-child(2)::text').get()
            price = item.css('td[aria-label="Price (Intraday)"] fin-streamer::text').get()
            change = item.css('td:nth-child(4) span::text').get()
            percent_change = item.css('td:nth-child(5) span::text').get()
            volume_in_currency_24Hr = item.css('td:nth-child(7)::text').get()
            yield {
                'name': name,
                'price': price,
                'change': change,
                'percent_change': percent_change,
                'volume_in_currency_24Hr': volume_in_currency_24Hr
            }
        
        next_button_link = response.css('button.Va\\(m\\) > span').xpath('.//span[contains(text(), "Next")]').xpath('parent::button/@href').get()

        if next_button_link:
            yield response.follow(next_button_link, self.parse)
        else:
            self.logger.info("No more pages to load")