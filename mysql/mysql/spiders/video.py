# -*- coding: utf-8 -*-
import scrapy


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        pass
