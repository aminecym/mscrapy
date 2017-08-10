# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
import spynner
import pyquery
import time
import BeautifulSoup
import sys
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    def __init__(self):
        super(RandomUserAgentMiddleware, self).__init__()

        self.ua = UserAgent()

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random)


class WebkitDownloaderTest(object):
        def process_request(self, request, spider):
            #        if spider.name in settings.WEBKIT_DOWNLOADER:
            #            if( type(request) is not FormRequest ):
            browser = spynner.Browser()
            browser.create_webview()
            browser.set_html_parser(pyquery.PyQuery)
            browser.load(request.url, 20)
            try:
                browser.wait_load(10)
            except:
                pass
            string = browser.html
            string = string.encode('utf-8')
            renderedBody = str(string)
            return HtmlResponse(request.url, body=renderedBody)

        # class MyprojectSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
