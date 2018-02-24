# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem
# from itcast.items import TencentItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名称，启动爬虫时使用
    allowed_domains = ['http://www.itcast.cn'] #可选参数
    
    #起始url列表，列表，可迭代对象可写多个地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list=response.xpath("//div[@class='li_txt']")
        
        #创建列表存储所有item
        items=[]
        for node in node_list:
            #创建item字段，用来存储信息
            item=ItcastItem()
            # .extract()将xpath取到的数据转换为Unicode字符串
            name=node.xpath("./h3/text()").extract()
            title=node.xpath("./h4/text()").extract()
            info=node.xpath("./p/text()").extract()
            
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            
           
            yield item #返回每次取到的数据给管道处理
#             items.append(item)
#         return items

#爬取腾讯招聘网的爬虫
# class TencentSpider(scrapy.Spider):
#     name="tencent"
#     allowed_domains=['tencent.com']
#     
#     baseURL="http://hr.tencent.com/position.php?&start="
#     offset=0#偏移量
#     start_urls=[baseURL+str(offset)]
#     
#     def parse(self, response):
#         node_list=response.xpath("//tr[@class='even'] | //tr[@class='odd']")
#         
#         for node in node_list:
#             item=TencentItem()
#             item['positionName']=node.xpath("./td[1]/a/text()").extract()[0].encode('utf-8')
#             item['positionLink']=node.xpath("./td[1]/a/@href").extract()[0].encode('utf-8')#取属性值
#             if len(node.xpath("./td[2]/text()")):
#                 item['positionType']=node.xpath("./td[2]/text()").extract()[0].encode('utf-8')
#             else:
#                 item['positionType']=""
#             item['peopleNumber']=node.xpath("./td[3]/text()").extract()[0].encode('utf-8')
#             item['workLocation']=node.xpath("./td[4]/text()").extract()[0].encode('utf-8')
#             item['publishTime']=node.xpath("./td[5]/text()").extract()[0].encode('utf-8')
#             
#             yield item
#         if self.offset<2737:
#             self.offset+=10
#             url=self.baseURL+str(self.offset)
#             yield scrapy.Request(url,callback=self.parse)#继续下次请求