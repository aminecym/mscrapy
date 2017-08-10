# -- coding:utf-8 --
from scrapy.cmdline import execute
import sys
import os
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":

    args = sys.argv
    if len(args) != 3:
        logging.error(u"对不起,您输入的参数有问题,请看正确例子:python scraw_main.py cubead.com http://www.cubead.com \n参数说明:\n'cubead.com'表示网址允许检查的主域名;\n"
                      u"'http://www.cubead.com'表示开始检查的初始页面")
    else:

         logging.info(u'正在检测中...')
         execute("scrapy crawl geekca_check -o results.jl -t jl".split())

