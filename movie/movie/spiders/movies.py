# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    # allowed_domains = ['https://www.80s.tw']
    start_urls = ['https://www.80s.tw/movie/list']

    def parse(self, response):
        
       for href in response.css('ul:nth-child(2) li a::attr(href)'):
           full_url = response.urljoin(href.extract())
           yield scrapy.Request(full_url,callback=self.parse_question)

    def parse_question(self,response):
        title = response.css('.info h1::text').extract()[0]
        content = response.css('.info span::text').extract()[0]
        title = title.decode('utf-8')
        content = content.decode('utf-8')
        yield {
            'title':title,
            'content':content,
            'link':response.url,
        }