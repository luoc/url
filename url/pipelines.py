# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class UrlPipeline(object):
    def __init__(self):
        self.links = open('links.log', 'wb')
        self.imgs = open('imgs.log', 'wb')

    def process_item(self, item, spider):
        for link in item['links']:
            if link[:4] == 'http':
                self.links.write(link+os.linesep)
        for img in item['imgs']:
            if img[:4] == 'http':
                self.imgs.write(img+os.linesep)
        return item
