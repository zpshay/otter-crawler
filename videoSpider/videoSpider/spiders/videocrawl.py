# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:35:25 2017

@author: Zachary
"""

import scrapy

class videoCrawl(scrapy.Spider):
    name = "video"

    start_urls = [
        'http://www.w3schools.com/html/html5_video.asp',
        'https://www.html5rocks.com/en/tutorials/video/basics/',
            ]

    def parse(self, response):
        for video in response.css('video'):
            http_exists = video.xpath('./source/@src').extract_first()[:4]
            if http_exists == "http":
                full_url = video.xpath('./source/@src').extract_first()
            
                yield{
                    'video': full_url
                }
            else:
                video_url = str(video.xpath('./source/@src').extract_first())
                count_path = video_url.count("../")
                if count_path >= 1: 
                    split_url = response.url.rsplit('/',count_path)
                else:
                    split_url = response.url.rsplit('/',1)
                delimeter_added_url = split_url[0] + "/"
                translation_table = dict.fromkeys(map(ord, "]'["), None)
                video_url = video_url.translate(translation_table)
                full_url = delimeter_added_url + video_url
                
                yield{
                    'video': full_url
                }