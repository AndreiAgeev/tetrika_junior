import scrapy


class ParseAnimalsItem(scrapy.Item):
    name = scrapy.Field()
