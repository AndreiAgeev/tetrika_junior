BOT_NAME = "parse_animals"

SPIDER_MODULES = ["parse_animals.spiders"]
NEWSPIDER_MODULE = "parse_animals.spiders"

ADDONS = {}

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
)

ROBOTSTXT_OBEY = False  # https://ru.wikipedia.org/robots.txt запррещает стандартные парсеры

DOWNLOAD_DELAY = 1  # чтобы уменьшить скорость запросов

FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'parse_animals.pipelines.ParseAnimalsPipeline': 300
}
