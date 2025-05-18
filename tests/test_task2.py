import re
from time import sleep

import pytest
from scrapy.crawler import CrawlerProcess

from constants import Task2Constants
from parse_animals.spiders.wiki_animals_test import WikiAnimalsTestSpider


def test_task2_parser(mock_dirs):
    mock_base_dir = mock_dirs
    process = CrawlerProcess(settings=Task2Constants.SETTINGS)
    process.crawl(WikiAnimalsTestSpider)
    process.start()

    dirs = [
        directory.name for directory in mock_base_dir.iterdir()
        if directory.is_dir()
    ]
    output_files = [
        file for file in mock_base_dir.glob('**/*')
        if str(file).endswith('.csv')
    ]
    assert 'results' in dirs, 'Отсутствует диркектория results.'
    assert 'beasts' in [str(file) for file in output_files][0], (
        'Отсутствует файл beasts.csv в директории results.'
    )
    with open([file for file in output_files if 'beasts' in str(file)][0], 'r') as file:
        file_result = file.read()
        re_pattern = re.compile(r'\w{1},\d+')
        assert re.search(re_pattern, file_result), (
            'Строки в файле beasts.csv должны записываться в формате: "Буква,Количество"'
        )