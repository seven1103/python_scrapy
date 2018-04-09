# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from mysql.items import MusicItem, MusicReviewItem
from scrapy.linkextractors import LinkExtractor
from scrapy import log

import re

import sys
 
reload(sys)
sys.setdefaultencoding('utf-8')


class MusicSpider(CrawlSpider):
    name = 'music'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/subject/1406522/']
    rules = (
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews$")),
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?sort=time$")),
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?sort=time\&start=\d+$")),
        Rule(LinkExtractor(allow=r"/review/\d+/$"), callback="parse_review", follow=True),
    )

    def parse_review(self,response):
        print('安徽萨斯 ')
        try:
            item = MusicReviewItem()
            item['review_title'] = "".join(response.xpath('//*[@property="v:summary"]/text()').extract())
            content = "".join(
                response.xpath('//*[@id="link-report"]/div[@property="v:description"]/text()').extract())
            item['review_content'] = content.lstrip().rstrip().replace("\n", " ")
            item['review_author'] = "".join(response.xpath('//*[@property = "v:reviewer"]/text()').extract())
            item['review_music'] = "".join(response.xpath('//*[@class="main-hd"]/a[2]/text()').extract())
            item['review_time'] = "".join(response.xpath('//*[@class="main-hd"]/p/text()').extract())
            item['review_url'] = response.url
            yield item
        except Exception as error:
            log(error)
