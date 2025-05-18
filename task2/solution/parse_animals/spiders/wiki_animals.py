import scrapy

from parse_animals.items import ParseAnimalsItem


class WikiAnimalsSpider(scrapy.Spider):
    name = "wiki_animals"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"]
    animal_list_selector = '//div[@class="mw-category mw-category-columns"]//a/text()'
    next_page_selector = '//a[contains(., "Следующая страница")]/@href'

    def parse(self, response):
        for animal_name in response.xpath(self.animal_list_selector).getall():
            yield ParseAnimalsItem({"name": animal_name})
        next_page = response.xpath(self.next_page_selector).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
