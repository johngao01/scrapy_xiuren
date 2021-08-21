# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyXiurenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class pageDataItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    page_nums = scrapy.Field()
    organization = scrapy.Field()
    desc = scrapy.Field()
    # 图片所在写真页面的地址
    photo_page_url = scrapy.Field()
    # 图片的地址,image_urls是默认的,不能改
    image_urls = scrapy.Field()
    # 图片的信息,image是默认的,不能改
    images = scrapy.Field()

