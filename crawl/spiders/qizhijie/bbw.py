import scrapy
import re
from scrapy import Selector,Request
from crawl.items.bbw_item import Bbw_item
from urllib.parse import urljoin



class Bbw(scrapy.Spider):
    name='bbw'
    start_urls=['https://www.bibenet.com/search?pageNum=1']
    page=1
    # custom_settings = {
    #     "DOWNLOAD_DELAY": '1'
    # }
    def parse(self, response):
        sel=Selector(response)
        urls=sel.css('td a::attr(href)').extract()
        for i in urls:
            # print(urls)
            yield Request(url=i,callback=self.parse_bbw)
        next_url=response.url
        self.page+=1
        next_url=re.sub('\d+',str(self.page),next_url)
        if next_url and self.page<3:
            next_url=urljoin(response.url,next_url)
            yield Request(url=next_url,callback=self.parse)

    def parse_bbw(self,response):
        sel=Selector(response)
        item=Bbw_item()
        item['title']=sel.css('h1.detailtitle ::attr(title)').extract()
        # print(item['title'])
        yield item