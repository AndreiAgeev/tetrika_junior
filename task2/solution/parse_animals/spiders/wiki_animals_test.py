import scrapy

from parse_animals.items import ParseAnimalsItem

class WikiAnimalsTestSpider(scrapy.Spider):
    name = "wiki_animals_test"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"]
    animal_list_selector = '//div[@class="mw-category mw-category-columns"]//a/text()'

    def parse(self, response):
        for animal_name in response.xpath(self.animal_list_selector).getall():
            yield ParseAnimalsItem({"name": animal_name})
