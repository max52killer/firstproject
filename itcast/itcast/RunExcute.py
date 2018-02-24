# -*- coding: utf-8 -*-

# import threading  
# #在项目外用脚本启动爬虫   
# from twisted.internet import reactor  
# from scrapy.crawler import CrawlerRunner  
# import itcast.items  
# from itcast.spiders.itcast import ItcastSpider
# from itcast.pipelines import ItcastPipeline  
# from scrapy.settings import Settings  
#   
# #配置文件在这里手动实现   
# #下面是官方说法    
# #Running spiders outside projects it’s not much different.   
# #You have to create a generic Settings object and populate it as needed (See 内置设定参考手册 for the available settings),   
# #instead of using the configuration returned by get_project_settings.   
# #翻译   
# #运行蜘蛛外项目没有多少不同。  
# #你必须根据需要创建一个通用设置对象并填充它(见内置设定参考手册可用的设置),而不是使用配置由get_project_settings返回。  
# def run_itcast():  
#     settings = Settings({  
#         #Spiders can still be referenced by their name if SPIDER_MODULES is set with the modules where Scrapy should look for spiders.  
#         #Otherwise, passing the spider class as first argument in the CrawlerRunner.  
#         #翻译  
#         #蜘蛛仍然可以引用他们的名字如果SPIDER_MODULES设置模块,Scrapy应该找蜘蛛。  
#         #否则,将蜘蛛CrawlerRunner类作为第一个参数。  
#         'SPIDER_MODULES':['itcast.itcast.spiders.itcast'],    
#   
#         'ROBOTSTXT_OBEY':True,  
#         #设置包头  
#         'DEFAULT_REQUEST_HEADERS':{  
#         'Referer':'http://www.itcast.cn/',  
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},  
#         #启用pipelines组件  
#         'ITEM_PIPELINES':{  
#         'itcast.itcast.pipelines.ItcastPipeline': 300,},  
#   
#         'CONCURRENT_REQUESTS':1,     #同时只处理一个请求    
#         'DOWNLOAD_DELAY':2          #每个2秒 下载一个页面    
#         })  
#     runner=CrawlerRunner(settings)  
#   
#     d=runner.crawl('itcast')  
#     d.addBoth(lambda _: reactor.stop())  
#     reactor.run()  
#     return 0  
# #下面的代码仅共参考，实际上直接run_itcast() 也可以    
# def thread_itcast():  
#     print("--------------")  
#     threading.Thread(target=run_itcast())  
# if __name__ == '__main__':  
#     thread_itcast()  

import scrapy.cmdline
 
# if __name__ == '__main__':
cmdline.execute('scrapy crawl itcast'.split()) #这就是我们在命令行中的代码

