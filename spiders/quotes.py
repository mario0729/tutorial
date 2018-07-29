# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem

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
            
        next = response.css('.pager .next a::attr(href)').extract_first() 
        print(next)
        print(response.url)
        url = response.urljoin(next)
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)