# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyXiurenPipeline:
    def process_item(self, item, spider):
        # print(item['image_urls'])
        return item


class downloadPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        return item['organization'] + os.sep + item['star'] + \
            os.sep + item['title'] + os.sep + request.url.split('/')[-1]
