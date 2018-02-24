# -*- coding: GBK -*-  #���������ַ���

import pymysql
def database(path):    #��������Զ��庯����ʵ�ֶ����ݿ�Ĳ���  
        connect = pymysql.connect(  
            user = "root",  
            password = "oyhj",  #�������ݿ⣬����Ŀ��Կ���֮ǰд���������ݿ������  
            port = 3306,  
            host = "127.0.0.1",  
            db = "MYSQL",  
            charset = "utf8"  
            )  
        con = connect.cursor()  #��ȡ�α�  
#         con.execute("create database w_tencent")  #�������ݿ⣬����������һ��������޵�һ��ʹ�ã��������ݿ��Ͳ�����ʹ����  
        con.execute("use spider_data")   #ʹ�����ݿ�  
        con.execute("drop table if exists tencent")  #�ж��Ƿ����������ݿ��  
        sql = """create table tencent(positionName varchar(200),positionLink varchar(500),positionType varchar(20),peopleNumber varchar(2),workLocation varchar(20),publishTime varchar(25))"""  
        con.execute(sql)  #ִ��sql����  ����tencent����������Ϣ  
        with open(path,"r") as f:  #��path�����ĵ�  
            while True:  
                info = f.readline()   #һ��һ�еĶ�ȡ�ĵ���Ϣ  
                print()
                if info:  
                    info = info.strip()  #ȥ�����з�  
                    info = info.split(";")  #��;���ָ��Ϣ�任Ϊ�б���ʽ  
                    positionName = info[0]  
                    positionLink = info[1]  
                    positionType = info[2]  
                    peopleNumber = info[3]  
                    workLocation = info[4]  
                    publishTime = info[5] 
                    con.execute("insert into tencent(positionName,positionLink,positionType,peopleNumber,workLocation,publishTime)values(%s,%s,%s,%s,%s,%s)",[positionName,positionLink,positionType,peopleNumber,workLocation,publishTime])  
                    # ��һ����ǽ���Ϣ������t_zhaopin����  
                else:  
                    break  
        connect.commit()   #������Ҫ�ύ���ݿ⣬�������ݻ��ǲ����ϴ���  
        con.close()   #�ر��α�  
        connect.close()  #�ر����ݿ�  
        print("Over!!!!!!!!!")

database("D:/NutchWorkPlat/workspace/Tencent/Tencent/spiders/tencent_1.txt")
