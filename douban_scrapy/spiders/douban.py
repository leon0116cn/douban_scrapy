# -*- coding: utf-8 -*-
import scrapy
from douban_scrapy.items import DoubanMoviesItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movies_item = DoubanMoviesItem()
        items = response.xpath('//ol[@class="grid_view"]//div[@class="item"]')
        for item in items:
            movies_item['rank'] = item.xpath('./div[@class="pic"]/em/text()').get()
            movies_item['img_url'] = item.xpath('./div[@class="pic"]//img/@src').get()
            movies_item['detail'] = item.xpath('./div[@class="pic"]/a/@href').get()
            movies_item['movie_name'] = item.xpath('./div[@class="info"]/div[@class="hd"]//span/text()').get()
            movies_item['rating_num'] = item.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').get()
            movies_item['comment_num'] = item.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            movies_item['quote'] = item.xpath('./div[@class="info"]//p[@class="quote"]/span/text()').get()
            yield movies_item
        next_page_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').get()
        yield response.follow(url=next_page_url, callback=self.parse)
