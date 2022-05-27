# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名，电影评分，电影信息，电影简介
    name = scrapy.Field()
    score = scrapy.Field()
    info = scrapy.Field()
    desc = scrapy.Field()
    pass
