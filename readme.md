1.新建项目
scrapy startproject 项目名称

2.在项目中新建爬虫
cd spiders
scrapy genspider 爬虫名 站点名

3.运行爬虫
运行爬虫
scrapy crawl 爬虫名

4.数据导出

scrapy crawl 爬虫名 -o xxx.json
scrapy crawl 爬虫名 -o xxx.csv

5.数据放入pipelines中，用于保存和清洗

6.相关中间件开发（代理ip,agent-head）middle