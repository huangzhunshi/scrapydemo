# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest, HtmlResponse


class OdiansoSpider(scrapy.Spider):
    name = 'odianso'
    allowed_domains = ['o.dian.so']
    #start_urls = ['https://o.dian.so/']
    start_urls=['http://o.dian.so/leo/1.0/data/directDayStatistics/getShopDeviceInfo?t=1538837804339&data=%7B%22shopId%22%3A%22416946%22%7D']

    #login_url = ['http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}']

    def start_requests(self):
        start_url = 'http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}'
        return [
            Request(start_url, callback=self.afterLogin)
        ]


    # def parseWelcome(self, response):
    #
    #     lt = response.xpath('//input[@name="lt"]/@value').extract_first()
    #     #logging.info('lt:' + lt)
    #     return FormRequest.from_response(
    #         response,
    #         url='http://o.dian.so/leo/1.0/h5/login?t=1538821359012&data={"mobile":"13285977597","token":"120501300104"}',
    #         #meta={'cookiejar': response.meta['cookiejar']},
    #         #formdata={'data':'{"mobile":"13285977597","token":"120501300104"}', "lt" : lt},
    #         callback=self.afterLogin
    #     )

    def afterLogin(self, response):
        #yield Request(self.start_urls)
       yield Request('http://o.dian.so/leo/1.0/data/directDayStatistics/getShopDeviceInfo?t=1538837804339&data=%7B%22shopId%22%3A%22416946%22%7D',callback=self.parse)

    def parse(self, response):
        print (response.text)

        #pass
