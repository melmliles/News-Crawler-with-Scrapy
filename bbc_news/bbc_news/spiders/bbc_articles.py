# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from bbc_news.items import BbcNewsItem

class BbcArticlesSpider(scrapy.Spider):
    name = 'bbc_articles'
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        news = response.xpath("//li/div/div[@class='media__content']")

        for n in news:
            loader = ItemLoader(item=BbcNewsItem(), selector=n)

            # Get the headline
            loader.add_xpath('headline', './/a[@class="media__link"]/text()')            
            # Get the summary
            loader.add_xpath('summary', './/p[@class="media__summary"]/text()')
            # Get the article URL    
            loader.add_xpath('article_url', './/a[@class="media__link"]/@href')

            yield loader.load_item()
