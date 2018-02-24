# -*- coding: utf-8 -*-
import json
import scrapy
import xml
import redis
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#通过使用yield调用管道实现引擎逐步将数据写入管道
class ItcastPipeline(object):
    def __init__(self):
        #创建文件对象，存储数据
#         self.f=open("itcast_pipeline.json","wb+")
#         self.r = redis.Redis(host='127.0.0.1', port=6379,db=0)
        self.connect = pymysql.connect(  
                user = "root",  
                password = "oyhj",  #连接数据库，不会的可以看我之前写的连接数据库的文章  
                port = 3306,  
                host = "127.0.0.1",  
                db = "MYSQL",  
                charset = "utf8"  
                )  
        self.con = self.connect.cursor()  #获取游标  
#         con.execute("create database spider_data")  #创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了  
        self.con.execute("use spider_data")   #使用数据库  
        self.con.execute("drop table if exists itcast")  #判断是否存在这个数据库表  
        sql = """create table itcast(id int primary key not null AUTO_INCREMENT,name varchar(200),title varchar(200),info varchar(500))"""  
        self.con.execute(sql)  #执行sql命令  创建itcast表来保存信息  
    
    def process_item(self, item, spider):
#         content=json.dumps(dict(item), ensure_ascii=False)
#         print('-----:'+content)
#         self.f.write(content.encode("utf-8"))
        ditem=dict(item)
        name=ditem['name']
        title=ditem['title']
        info=ditem['info']
        
        #逐条将数据写入mysql数据库
        self.con.execute("insert into itcast(name,title,info) values(%s,%s,%s)",[name,title,info])  
        self.connect.commit()   #我们需要提交数据库，否则数据还是不能上传的  
        return item  #数据处理返回引擎继续执行
    
    def close_spider(self,spider):
#         self.r.set('itcast', self.d)   #添加
#         self.f.close()
        self.con.close()   #关闭游标  
        self.connect.close()  #关闭数据库  
        print("Over!!!!!!!!!")  
        pass