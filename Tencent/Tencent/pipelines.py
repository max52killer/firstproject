# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class TencentPipeline(object):
    def __init__(self):
        #创建文件对象，存储数据，存储在当前文件下的目录下面
        self.f=open("tencent_1.txt","w")
    
    def process_item(self, item, spider):
          #将数据存储为json格式
#         content=json.dumps(dict(item), ensure_ascii=False)+",\n"
#         print('-----===:'+content)
#         #转换为utf-8格式存储
#         self.f.write(content.encode('utf-8'))

        data=dict(item)
        self.f.write(data['positionName']+";"+data['positionLink']+";"+data['positionType']+";"+data['peopleNumber']+";"+data['workLocation']+";"+data['publishTime']+"\n")
        return item  #数据处理返回引擎继续执行
    
    def close_spider(self,spider):
        self.f.close()
        self.database("D:/NutchWorkPlat/workspace/Tencent/Tencent/spiders/tencent_1.txt")

#这个方法主要实现将数据从tencent.txt文件中取出，然后存入数据库
    def database(self,path):    #调用这个自定义函数来实现对数据库的操作  
            connect = pymysql.connect(  
                user = "root",  
                password = "oyhj",  #连接数据库，不会的可以看我之前写的连接数据库的文章  
                port = 3306,  
                host = "127.0.0.1",  
                db = "MYSQL",  
                charset = "utf8"  
                )  
            con = connect.cursor()  #获取游标  
    #         con.execute("create database spider_data")  #创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了  
            con.execute("use spider_data")   #使用数据库  
            con.execute("drop table if exists tencent")  #判断是否存在这个数据库表  
            sql = """create table tencent(id int primary key not null AUTO_INCREMENT,positionName varchar(200),positionLink varchar(500),positionType varchar(20),peopleNumber varchar(2),workLocation varchar(20),publishTime varchar(25))"""  
            con.execute(sql)  #执行sql命令  创建tencent表来保存信息  
            with open(path,"r") as f:  #打开path本地文档  
                while True:  
                    info = f.readline()   #一行一行的读取文档信息  
                    if info:  
                        info = info.strip()  #去掉换行符  
                        info = info.split(";")  #以;来分割将信息变换为列表形式  
                        positionName = info[0]  
                        positionLink = info[1]  
                        positionType = info[2]  
                        peopleNumber = info[3]  
                        workLocation = info[4]  
                        publishTime = info[5] 
                        con.execute("insert into tencent(positionName,positionLink,positionType,peopleNumber,workLocation,publishTime)values(%s,%s,%s,%s,%s,%s)",[positionName,positionLink,positionType,peopleNumber,workLocation,publishTime])  
                        # 这一句就是将信息保存至tencent表中  
                    else:  
                        break  
            connect.commit()   #我们需要提交数据库，否则数据还是不能上传的  
            con.close()   #关闭游标  
            connect.close()  #关闭数据库  
            print("Over!!!!!!!!!")  