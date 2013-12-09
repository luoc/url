from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from url.items import UrlItem

class UrlmanSpider(CrawlSpider):
    name = 'urlman'
    #allowed_domains = ['sina.com.cn']
    start_urls = ['http://www.sina.com.cn']

    rules = (
        Rule(SgmlLinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = Selector(response)
        item = UrlItem()
        item['links'] = hxs.xpath('//a[@href]/@href').extract()
        item['imgs'] = hxs.xpath('//img[@src]/@src').extract()
        return item
