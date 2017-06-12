import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html#subcategory=mobile']

    def parse(self, response):
        self.log('I just visited ' + response.url)

        yield{
        	'product_name': response.css('a.prdct-item__name::text').extract(),
        	'price': response.css('span.prdct-item__prc-val::text').extract(),
        }
