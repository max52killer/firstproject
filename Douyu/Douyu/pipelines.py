# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from Douyu.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline

#实现图片下载的管道类
class DouyuPipeline(ImagesPipeline):
#     def process_item(self, item, spider):
#         return item
    def get_media_requests(self,item,info):
        image_link=item['imageLink']
        print("--------*******-------")
        print(images_store)
        print("--------*******-------")
        yield scrapy.Request(image_link)
        
        #取出results中图片的路径：path=[x["path"] for ok,x in results if ok]
    def item_completed(self, results, item, info):
#         images_store="D:/NutchWorkPlat/workspace/Douyu/Douyu/spiders/images/"
        image_path=[x["path"] for ok,x in results if ok]
        
        os.rename(images_store+image_path[0], images_store+item["nickName"]+".jpg")
        return item