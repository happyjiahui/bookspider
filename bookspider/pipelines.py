# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import ujson


class BookspiderPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'w')

    def process_item(self, item, spider):
        line = ujson.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        print()
        print('-' * 10)
        print(item)
        print('*' * 10)
        return item
