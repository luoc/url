# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class UrlPipeline(object):
    def __init__(self):
        self.file = open('urlman.log', 'wb')

    def process_item(self, item, spider):
        line = item['url'] + '\r\n'
        self.file.write(line)
        return item
