from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from myproject.items import UrlItem
from urlparse import urlparse
import requests
import logging
import time


logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger('scrapy').setLevel(logging.WARNING)

GEEKCA_DOMAIN = 'geekca.cubead.com'

class Test(CrawlSpider):
    name = "test"
    allowed_domains =["angularjs.cn"]
    start_urls = ["http://angularjs.cn/?p=1"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        begin = time.time()
        logger.info("start to scrawl url:{0}".format(response.url))

        hxs = HtmlXPathSelector(response)
        scripts = hxs.xpath("//a[@class='ng-binding']/text()")
        for script in scripts:
           script_src = script.extract()
           logger.info("value:{0}".format(script_src))

        logger.info("end to scrawl url:{0} and cost time:{1}".format(response.url, (time.time() - begin)))
        return([])
