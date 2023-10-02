# -*- coding: utf-8 -*-
import scrapy


class DotaScraperItem(scrapy.Item):
    popular_hero = scrapy.Field()
    counterpick_heroes = scrapy.Field()
