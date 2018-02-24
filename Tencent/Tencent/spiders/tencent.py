# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    #爬虫名
    name="tencent"
    #爬虫允许的域范围
    allowed_domains=['tencent.com']
    
    baseURL="http://hr.tencent.com/position.php?&start="
    offset=0#需要拼接的URL偏移量
    start_urls=[baseURL+str(offset)]
    
    def parse(self, response):
        #提取每页的response的数据
        node_list=response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        
        for node in node_list:
            item=TencentItem()
            item['positionName']=node.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink']=node.xpath("./td[1]/a/@href").extract()[0]#取属性值
            if len(node.xpath("./td[2]/text()")):
                item['positionType']=node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType']=""
            item['peopleNumber']=node.xpath("./td[3]/text()").extract()[0]
            item['workLocation']=node.xpath("./td[4]/text()").extract()[0]
            item['publishTime']=node.xpath("./td[5]/text()").extract()[0]
            
            #yield返回到管道处理，返回数据后还能回来继续个执行
            yield item
            #使用定长方式逐条提取数据，适用于页面没有
#         if self.offset<2737:
#             self.offset+=10
#             url=self.baseURL+str(self.offset)
#             yield scrapy.Request(url,callback=self.parse)#继续下次请求

        #循环查找下一页的数据
        if not len(response.xpath("//a[@class='noactive' and @id='next']")):
            url=response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("http://hr.tencent.com/"+url,callback=self.offset)
    