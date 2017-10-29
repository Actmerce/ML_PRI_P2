# -*- coding:utf-8 -*-
# __author__ = 'ActMerce'
# __date__ = '2017/10/28 21:11'


class Movie(object):
    """喜爱的电影"""
    def __init__(self, title, intro, poster_image_url, trailer_youtube_url):
        """
        构造函数
        :param title:电影的标题
        :param intro:电影的简介
        :param poster_image_url:缩略图url
        :param trailer_youtube_url: 预告片url(须要油管源)
        """
        self.title = title
        self.intro = intro
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
