# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        #创建文件对象，存储数据，存储在当前文件下的目录下面
        self.f=open("douban.txt","w")
    
    def process_item(self, item, spider):
        
        #将数据存储为json格式
        content=json.dumps(dict(item), ensure_ascii=False)+",\n"
        print('-----===:'+content)
        #转换为utf-8格式存储
        self.f.write(content.encode('utf-8'))
        return item
    
    def close_spider(self,spider):
        self.f.close()