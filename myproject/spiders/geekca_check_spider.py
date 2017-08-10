from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from myproject.items import UrlItem
from urlparse import urlparse
import requests
import logging
import time
import sys


logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger('scrapy').setLevel(logging.WARNING)

GEEKCA_DOMAIN = 'geekca.cubead.com'

args = sys.argv
target_domain = str(args[1])
start_scraw_first_page = str(args[2])


class GeekCACheckSpider(CrawlSpider):
    name = "geekca_check"
    allowed_domains = [target_domain]
    start_urls = [start_scraw_first_page]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        begin = time.time()
        logger.info("start to scrawl url:{0}".format(response.url))


        hxs = HtmlXPathSelector(response)
        scripts = hxs.xpath("//script/@src")
        is_exsisted = False

        for script in scripts:
           script_src = script.extract()

           if "http" not in script_src:
               parsed_uri = urlparse(response.url)
               domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
               script_src = domain + script_src

           r = requests.get(script_src)

           if GEEKCA_DOMAIN in r.content:
               is_exsisted = True
               break

        if not is_exsisted:
            titles = hxs.xpath("//script[contains(.,'geekca.cubead.com')]/text()")
            items = []

            if not titles:
                item = UrlItem()
                item["url"] = response.url
                items.append(item)

            logger.info("end to scrawl url:{0} and cost time:{1}".format(response.url,(time.time()-begin)))
            return(items)
