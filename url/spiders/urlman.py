from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from url.items import UrlItem

class UrlmanSpider(CrawlSpider):
    name = 'urlman'
    #allowed_domains = ['sina.com.cn']
    start_urls = ['http://www.baidu.com/s?wd=url%E6%B7%B1%E5%BA%A6%E6%90%9C%E7%B4%A2']

    rules = (
        Rule(SgmlLinkExtractor(unique=True), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = UrlItem()
        i['url'] = response.url
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
