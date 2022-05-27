# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):

    def __init__(self):
        self.file = open('douban.json','w')

    def __del__(self):
        self.file.close()

    def process_item(self, item, spider):
        json_data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(json_data)

        return item
