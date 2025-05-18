import csv
from collections import defaultdict

from itemadapter import ItemAdapter

from .constants import RESULT_DIR


class ParseAnimalsPipeline:

    def __init__(self):
        RESULT_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.animal_dict = defaultdict(int)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.animal_dict[adapter['name'][0]] += 1
        return item

    def close_spider(self, spider):
        self.animal_dict['Total'] = sum(self.animal_dict.values())
        filename = 'beasts.csv'
        filepath = RESULT_DIR / filename
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerows(
                (('Буква', 'Количество'), *self.animal_dict.items())
            )
