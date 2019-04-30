# -*- coding: utf-8 -*-
import scrapy
import pkgutil


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    data = pkgutil.get_data("books", "resources/urls.txt")
    start_urls = data[1]

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
