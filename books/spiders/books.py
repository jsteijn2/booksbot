# -*- coding: utf-8 -*-
import scrapy
import pkgutil
import logging


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    keywords = pkgutil.get_data("books", "resources/keywords.txt")
    keylines = keywords.splitlines()
    for line in keylines:
        line = "https://www.google.com/search?q=" + line + "&hl=nl&tbm=shop&tbs=p_ord:p&ei=aBjIXLCBOILPwAKhhpmQAw&ved=0ahUKEwiw1duzw_fhAhWCJ1AKHSFDBjIQuw0IswQoAg"
    start_urls = urls.splitlines() + keylines

    def parse(self, response):
        item = {}
        item["title"] = response.css("h1 ::text").extract_first()
        yield item


'''
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}
        product = response.css("div.product_main")
        item["title"] = product.css("h1 ::text").extract_first()
        yield item
'''
