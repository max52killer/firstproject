# -*- coding: utf-8 -*-

import pymysql

def database(path):    #调用这个自定义函数来实现对数据库的操作  
        connect = pymysql.connect(  
            user = "root",  
            password = "oyhj",  #连接数据库，不会的可以看我之前写的连接数据库的文章  
            port = 3306,  
            host = "127.0.0.1",  
            db = "MYSQL",  
            charset = "utf8"  
            )  
        con = connect.cursor()  #获取游标  
#         con.execute("create database w_tencent")  #创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了  
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
                    # 这一句就是将信息保存至t_zhaopin表中  
                else:  
                    break  
        connect.commit()   #我们需要提交数据库，否则数据还是不能上传的  
        con.close()   #关闭游标  
        connect.close()  #关闭数据库  
        print("Over!!!!!!!!!")  


# util=DBUtil()
# sql="INSERT INTO EMPLOYEE(FIRST_NAME, \
#         LAST_NAME, AGE, SEX, INCOME)\
#                          VALUES('%s', '%s', '%d', '%c', '%d')"%\
#                          ('ninini', 'hhhhhh', 20, 'G', 2011)
# util.insert(sql)
# util.close()
    
