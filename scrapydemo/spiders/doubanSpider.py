# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import ScrapydemoItem
#from ScrapydemoItem import doubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    #默认解析方法
    def parse(self, response):
        #循环要抓取的信息
        move_list=response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for item in move_list:
            douban_item= ScrapydemoItem()
            douban_item["serial_number"]=item.xpath('.//div/div/em/text()').extract_first()
            douban_item["movie_name"]=item.xpath('.//div/div[2]/div[1]/a/span[1]/text()').extract_first()
            douban_item["star"]=item.xpath('.//div/div[2]/div[2]/div/span[2]/text()').extract_first()
            #print (douban_item["serial_number"])

            #将数据yield到pipelines中去，进行数据的清洗和存储
            yield douban_item

        next_link=response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()
        #print (next_link[0])

        #解析下一页，获取下一页的xpath
        if next_link:
             next_link=next_link[0]
             yield scrapy.Request('https://movie.douban.com/top250'+next_link,callback=self.parse)


        #print (response.text)
        #pass
