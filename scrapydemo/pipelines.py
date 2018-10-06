# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapydemo.settings import mysql_host,mysql_port,mysql_db

class ScrapydemoPipeline(object):

    def __init__(self):
        # 初始化数据库相关
         print (mysql_port)
         print (mysql_host)
         print (mysql_db)

    def process_item(self, item, spider):
    #     serial_number=scrapy.Field()
    # movie_name=scrapy.Field()
    # star=scrapy.Field()

        print (item["serial_number"])
        print (item["movie_name"])
        print (item["star"])

        return item
