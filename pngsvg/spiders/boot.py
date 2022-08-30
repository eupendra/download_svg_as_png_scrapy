import scrapy


class BootSpider(scrapy.Spider):
    name = 'boot'
    start_urls = ['https://icons.getbootstrap.com/']

    def parse(self, response):
        for url in response.css('#content li > a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_icon)
    
    def parse_icon(self, response):
        icon_url = response.css('a[download] ::attr(href)').get()
        yield {
            'icon_url':response.urljoin(icon_url),
            'icon_name':response.css('h1 ::text').get(),
            'icon_markup' : response.css('.icon-demo svg').get()
        }