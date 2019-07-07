# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMoviesItem(scrapy.Item):
    rank = scrapy.Field()
    movie_name = scrapy.Field()
    img_url = scrapy.Field()
    detail = scrapy.Field()
    rating_num = scrapy.Field()
    comment_num = scrapy.Field()
    remark = scrapy.Field()
    quote = scrapy.Field()
