# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest, HtmlResponse


class OdiansoSpider(scrapy.Spider):
    name = 'odianso'
    allowed_domains = ['mydemo']
    start_urls=['http://mydemo/leo/1.0/data/directDayStatistics/getShopDeviceInfo?t=1538837804339&data=%7B%22shopId%22%3A%22416946%22%7D']


    def start_requests(self):
        start_url = 'http://mydemo/leo/1.0/h5/login?t=1538821359012&data={"mobile":"123","token":"xxxxx"}'
        return [
            Request(start_url, callback=self.afterLogin)
        ]




    def afterLogin(self, response):
        #yield Request(self.start_urls)
       yield Request('http://mydemo/leo/1.0/data/directDayStatistics/getShopDeviceInfo?t=1538837804339&data=%7B%22shopId%22%3A%22416946%22%7D',callback=self.parse)

    def parse(self, response):
        print (response.text)

        #pass
