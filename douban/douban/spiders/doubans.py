# -*- coding: utf-8 -*-
import scrapy
import re
from douban.items import DoubanItem

class DoubansSpider(scrapy.Spider):
    name = 'doubans'
    allowed_domains = ['www.douban.com/doulist/1264675']
    
    baseURL="https://www.douban.com/doulist/1264675"
    start_urls = [baseURL]

    def parse(self, response):
        
        print(response)
        
        node_list=response.xpath("//div[@class='bd doulist-subject']")
        
        for node in node_list:
            item=DoubanItem()
            title=node.xpath("div[@class='title']/a/text()").extract()[0]
            rates=node.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()
            
            if rates:
                rate = rates[0]
                
            author=re.search('<div class="abstract">(.*?)<br', each.extract(), re.S).group(1)
            title = title.replace(' ', '').replace('\n', '')
            author = author.replace(' ', '').replace('\n', '')
            
            print(title)
            
            item['title']=title
            item['rates']=rates
            item["author"] = author
            yield item
        nextPage=response.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            next = nextPage[0]
            print (next)
            yield scrapy.http.Request(next, callback=self.parse)
