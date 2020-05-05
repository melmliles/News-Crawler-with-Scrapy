# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose

def remove_spaces(text):
    # strip white spaces
    text = text.strip()
    return text

class BbcNewsItem(scrapy.Item):
    headline = Field(
        input_processor=MapCompose(remove_spaces)
        )
    summary = Field(
        input_processor=MapCompose(remove_spaces)
        )
    article_url = Field()
