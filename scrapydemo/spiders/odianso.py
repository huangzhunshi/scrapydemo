# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest, HtmlResponse


class OdiansoSpider(scrapy.Spider):
    name = 'odianso'
    allowed_domains = ['z.dian.so']
    #start_urls = ['https://o.dian.so/']
    start_urls=['https://z.dian.so/shop/index/getShopList?t=1538818309418&data=%7B%22districtCode%22%3Anull%2C%22shopType%22%3Anull%2C%22status%22%3A-1%2C%22offset%22%3A0%2C%22pageSize%22%3A20%7D']

    #login_url = ['http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}']

    def start_requests(self):
        start_url = 'http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}'
        return [
            Request(start_url, callback=self.parseWelcome)
        ]


    def parseWelcome(self, response):
        lt = response.xpath('//input[@name="lt"]/@value').extract_first()
        #logging.info('lt:' + lt)
        return FormRequest.from_response(
            response,
            url='http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}',
            #meta={'cookiejar': response.meta['cookiejar']},
            formdata={'data':'{"mobile":"13285977597","token":"120501300104"}', "lt" : lt},
            callback=self.afterLogin
        )

    def afterLogin(self, response):
        yield Request(self.start_urls)

    def parse(self, response):
        print (response.text())

        #pass
