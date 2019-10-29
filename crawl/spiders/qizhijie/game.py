import scrapy
from scrapy import Selector,Request
from scrapy_redis.spiders import RedisCrawlSpider
from urllib.parse import urljoin


class Game(scrapy.Spider):
    name='game'
    # redis_key='game:start_urls'
    start_urls=['https://www.ali213.net/news/pingce/']
    def parse(self, response):
        sel=Selector(response)
        # print(123)
        li=sel.css('div.one_l_con')
        for i in li:
            urls=''.join(i.css('div.one_l_con_tit a::attr(href)').extract())
            yield Request(url=urls,callback=self.parse_game)
        next_urls = sel.xpath('//a[contains(text(),"下页")]/@href').extract_first()
        if next_urls:
            next_url = urljoin(response.url, next_urls)
            # print(next_url)
            yield Request(url=next_url,callback=self.parse)

    def parse_game(self,response):
        sel=Selector(response)
        li=sel.css('div.n_show')
        for i in li:
            img=i.css('p img::attr(src)').extract()
            txt=i.css('p::text').extract()
            print(img)
            print(txt)

