# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BbcNewsPipeline:
    def process_item(self, item, spider):
        # How to add 'http://www.bbc.com' to incomplete articles URL
        for i in range(0,len(item['article_url'])):
            if item['article_url'][i][0:4] != 'http':
                item['article_url'][i] = 'http://www.bbc.com' + item['article_url'][i]

        return item
