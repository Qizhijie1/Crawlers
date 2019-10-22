import scrapy

class Xy_Item(scrapy.Item):
    urls=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    time=scrapy.Field()
    laiyuan=scrapy.Field()
    author=scrapy.Field()
    txt=scrapy.Field()
    span=scrapy.Field()
    img=scrapy.Field()