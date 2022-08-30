import cairosvg
import scrapy


class WikisvgSpider(scrapy.Spider):
    name = 'wikisvg'
    start_urls = ['https://commons.wikimedia.org/wiki/File:Public_Domain_Mark_button.svg']
    # allowed_domains = ['wikipedia.org']

    def parse(self, response):
        print(response.headers.get('Content-Type'))
        for svg in response.xpath('//img[contains(@src,".svg")]/@src').getall():
            # yield scrapy.Request(svg, callback=self.download_svg)
            self.logger.info(f'Downloading {svg}')
            cairosvg.svg2png(url=svg, write_to=svg.split('/')[-1], output_width=512)


