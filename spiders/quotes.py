# -*- coding: utf-8 -*-
import scrapy
import re
from tutorial.items import QuoteItem

page = 2

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            print(item)
            yield item
            
        next = '/page/'+str(page)+'/'
        print(next)
        url = response.urljoin(next)
        print(url)
        page = page + 1
        return page
        yield scrapy.Request(url=url,callback=self.parse)

page = 