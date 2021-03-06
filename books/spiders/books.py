# -*- coding: utf-8 -*-
import scrapy
import pkgutil
import logging


class BooksSpider(scrapy.Spider):
    name = "books"
    urls = pkgutil.get_data("books", "resources/urls.txt")
    keywords = pkgutil.get_data("books", "resources/keywords.txt")
    keylines = keywords.splitlines()
    for line in keylines:
        line = "https://douchezaak.nl/?s=" + line + "&post_type=product"
    start_urls = urls.splitlines() + keylines
    logging.warning("URL's: " + urls + keywords)

    def parse(self, response):
        item = {}

        results = response.css(
            "div.products columns-4 egm-products > article")
        logging.warning(results)
        logging.warning(len(results))
        item["price"] = results[0].css("span.woocommerce-Price-amount amount ::text")

        
        yield item


'''
        item["title"] = results[0].css("h2::text")


        item["everything"] = response.css["div"].extract
        logging.warning(response.ccs["div"])

        results = response.css("div.sh-dgr__grid-result").extract()
        logging.warning(results[0])

        for result in results[:10]:
            item["link"] = result.css("a ::attr(href)")
            item["price"] = result.css("span::text")
            item["descr"] = result.css("a::text")
'''

'''
        for book_url in response.css("div.sh-dgr__grid-result > h3 > a ::attr(href)").extract():
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
