# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseURL = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset=0#偏移量，表示数据开始的位置
    start_urls=[baseURL+str(offset)]
    
    def parse(self, response):
        data_list=json.loads(response.body)['data']#json将返回的内容转化为json字符串
        #数据提取完，不再发送请求
        if len(data_list)==0:
            return
        
        for data in data_list:
            item=DouyuItem()
            item['nickName']=data['nickname']
            item['imageLink']=data['vertical_src']
            yield item
            
        self.offset+=20
        #执行回调方法,再次执行之前的操作
        yield scrapy.Request(self.baseURL+str(self.offset),callback=self.parse)
# vertical_src  链接  nickname 昵称