# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#爬取传智博客的教师信息
class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    #姓名：
    name = scrapy.Field()
    #职称
    title=scrapy.Field()
    #老师信息
    info=scrapy.Field()
    
    #pass
    
#爬取腾讯招聘网 
# class TencentItem(scrapy.Item):
#     
#     #职位名称
#     positionName=scrapy.Field()
#     #职位链接
#     positionLink=scrapy.Field()
#     #职位类别
#     positionType=scrapy.Field()
#     #招聘人数
#     peopleNumber=scrapy.Field()
#     #工作地点
#     workLocation=scrapy.Field()
#     #发布时间
#     publishTime=scrapy.Field()
