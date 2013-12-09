# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
class UrlPipeline(object):
    def __init__(self):
        date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        self.links = open('links-' + date + '.log', 'wb')
        self.imgs = open('imgs-' + date + '.log', 'wb')

    def process_item(self, item, spider):
        for link in item['links']:
            if link[:4] == 'http':
                self.links.write(link+os.linesep)
        for img in item['imgs']:
            if img[:4] == 'http':
                self.imgs.write(img+os.linesep)
        return item
