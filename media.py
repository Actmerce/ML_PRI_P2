# -*- coding:utf-8 -*-
# __author__ = 'ActMerce'
# __date__ = '2017/10/28 21:11'


class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
