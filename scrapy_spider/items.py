# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy.item import Item, Field


class hopitem(Item):
    name = Field()
    aka = Field()
    characteristics = Field()
    purpose = Field()
    alpha_acid = Field()
    beta_acid = Field()
    co_humulone = Field()
    country = Field()
    myrcene = Field()
    humulene = Field()
    caryophyllene = Field()
    farnesene = Field()
    substitutes = Field()