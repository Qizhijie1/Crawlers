import scrapy,re
from scrapy import Spider
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.xinye_item import Xy_Item


class Qizj_xinye(scrapy.Spider):
    name='xinye'
    start_urls=['http://www.xinye.gov.cn/jrxy/']
    def parse(self, response):
        item=Xy_Item()
        sel=Selector(response)
        li=response.xpath('//ul/li')
        for i in li:
            item['urls']=i.css('a::attr(href)').extract_first()
            item['url'] = urljoin(response.url,item['urls'])
            print(item['url'])
            yield Request(url=item['url'],callback=self.parse_text)

    def parse_text(self,response):
        item=Xy_Item()
        sel=Selector(response)
        item['title']=''.join(sel.css('p.yTit ::text').extract())
        item['time']=''.join(response.xpath('//div[@class="lyBox cl"]/div/span[1]/text()').re('\d+-\d+-\d+'))
        item['laiyuan']=''.join(response.xpath('//div[@class="lyBox cl"]/div/span[2]/text()').extract())
        item['author']=''.join(response.xpath('//div[@class="lyBox cl"]/div/span[3]/text()').extract())
        item['txt']=''.join(sel.css('div.conBox p::text').extract())
        item['img']=sel.css('div.conBox p img::attr(src)').extract()
        if item['txt']==None:
            item['span']=''.join(sel.css('div.conBox p span:text').extract())
            yield item
            print(item['span'])
        if item['img']==None:
            item['img_url']=sel.css('div.conBox p psan::attr(src)').extract()
            print(item['img_url'])
            yield item
        # print(item['title'])
        # print(item['time'])
        # print(item['laiyuan'])
        # print(item['author'])
        # print(item['txt'])
        # print(item['img'])
        yield item