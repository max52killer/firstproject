# -*- coding: utf-8 -*-
import pymysql


db=pymysql.connect("localhost","root","oyhj","TESTDB")
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#         LAST_NAME, AGE, SEX, INCOME) \
#         VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#         ('mmp', 'ni', 20, 'M', 2010)
sql="insert into tencent(positionName,positionLink,positionType,peopleNumber,workLocation,publishTime) values ('%s','%s','%s','%s','%s','%s')"%("开发","www.kaifa.com","开发","2","上海","2018-1-5")
try:
   # 执行sql语句
   print(sql)
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
except:
   # 发生错误时回滚
   print("出错了")
   db.rollback()
 
# 关闭数据库连接
db.close()