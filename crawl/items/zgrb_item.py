import scrapy

class Zgrb_item(scrapy.Item):
    urls=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    span=scrapy.Field()
    time=scrapy.Field()
    laiyuan=scrapy.Field()
    txt=scrapy.Field()