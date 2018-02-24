# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()#片名
    rates=scrapy.Field()#评分
    author=scrapy.Field()#作者，导演
#     star=scrapy.Field()#主演
#     type=scrapy.Field()#类型
#     country=scrapy.Field()#制片地区
#     outYear=scrapy.Field()#出品年份
    
    
