import scrapy
from scrapy import Selector,Spider
from crawl.items.zgrb_item import Zgrb_item
from urllib.parse import urljoin
from scrapy import Request


class Zgrb(scrapy.Spider):
    name='zgrb'
    start_urls=['http://cn.chinadaily.com.cn/5b753f9fa310030f813cf408/5bd54ba2a3101a87ca8ff5ee/5bd54bdea3101a87ca8ff5f0']
    def parse(self, response):
        item=Zgrb_item()
        sel=Selector(response)
        li=sel.css('div.busBox3 ')
        for i in li:
            item['urls']=''.join(i.css('h3 a::attr(href)').extract())
            item['url'] = urljoin(response.url, item['urls'])
            # print(item['url'])
            yield Request(url=item['url'],callback=self.parse_xqy)
        next_urls = sel.xpath('//a[contains(text(),"下一页")]/@href').extract_first()
        # if next_urls:
        #     next_url = urljoin(response.url, next_urls)
        #     yield Request(url=next_url,callback=self.parse)
    def parse_xqy(self,response):
        item=Zgrb_item()
        sel=Selector(response)
        item['title']=sel.css('h1::text').extract()
        # print(item['title'])
        if item['title']==None:
            item['span']=response.xpath('//div[@class="main_title"]/h1/span[1]/text()').extract()
            print(item['span'])
        item['time']=sel.css('div.xinf-le ::text').re('\d+-\d+-\d+')
        item['laiyuan']=response.xpath('//div[@class="xinf-le"]/a[2]/text()').extract()
        item['txt']=sel.css('div.article p::text').extract()
        # print(item['time'])
        # print(item['laiyuan'])
        # print(item['txt'])

