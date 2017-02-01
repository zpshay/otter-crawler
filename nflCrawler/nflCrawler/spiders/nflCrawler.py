import scrapy


class NflSpider(scrapy.Spider):
    name = "NFL"

    start_urls = [
        'http://www.nfl.com/news/story/0ap3000000781590/article/julio-jones-no-one-in-nfl-can-cover-me-oneonone'
            ]

    def pares(self, response):
        for NFL in response.css('title'):
            yield{
                'title': NFL.css('//title::text').extract_first()

            }