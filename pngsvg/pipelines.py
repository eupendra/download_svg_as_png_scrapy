# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import cairosvg


class PngsvgPipeline:
    def process_item(self, item, spider):
        spider.logger.info('Entering PIPELINE')
        icon_name = item.get('icon_name').lower().replace(' ','-')
        icon_name +='.png'
        icon_markup = item.get('icon_markup')
        icon_url = item.get('icon_url')

        # OPTION 1
        spider.logger.info(f'Downloading {icon_name}')
        cairosvg.svg2png(url=icon_url,
                         write_to='./png_files/'+icon_name, 
                         output_width=512)
        # OPTION 2
        # spider.logger.info(f'Downloading {icon_name}')
        # cairosvg.svg2png(bytestring=bytes(icon_markup,'utf-8'),
        #                  write_to='./png_files/'+icon_name, 
        #                  output_width=512)
        return item
