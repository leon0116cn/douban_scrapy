# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMoviesTop250Item(scrapy.Item):
    movie_rank = scrapy.Field()
    movie_name = scrapy.Field()
    movie_detail = scrapy.Field()
    rating_num = scrapy.Field()
    comment_num = scrapy.Field()
    quote = scrapy.Field()
    request_url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
