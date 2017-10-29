# -*- coding:utf-8 -*-
# __author__ = 'ActMerce'
# __date__ = '2017/10/28 21:18'
import fresh_tomatoes
import media


# 电影列表
what_your_name = media.Movie('君の名は',
                             '作品讲述了男女高中生在梦中相遇，并寻找彼此的故事。',
                             'https://i.ytimg.com/vi/sjhbO8lIc2s/movieposter.jpg',
                             'https://www.youtube.com/watch?v=sjhbO8lIc2s&list=PLHPTxTxtC0iaN9kA37m6MRrxFkgby2CDR')  # noqa
harry_potter = media.Movie('Harry Potter',
                           '描写的是年轻的巫师学生哈利·波特在霍格沃茨前后六年的学习生活和冒险故事',
                           'https://i.ytimg.com/vi/8GKHFtMaoOY/movieposter.jpg',
                           'https://www.youtube.com/watch?v=8GKHFtMaoOY&list=PLHPTxTxtC0iaN9kA37m6MRrxFkgby2CDR')  # noqa
jin_sang = media.Movie('银魂',
                       '江户时代末期，有一个武士与同伴愉快地过着异想天开的生活。',
                       'https://i.ytimg.com/vi/wyFQ2aQL6b4/movieposter.jpg',
                       'https://www.youtube.com/watch?v=wyFQ2aQL6b4&list=PLxaUumW-X5DcGVwlxF7IJEPKwUw74NiPq')  # noqa
dead_pool = media.Movie('死侍',
                        '死侍（Deadpool）是美国漫威漫画旗下反英雄',
                        'https://i.ytimg.com/vi/MD-VMxmWezE/movieposter.jpg',
                        'https://www.youtube.com/watch?v=MD-VMxmWezE&list=PLAXJzGOFS3xOOJXl2dJAeUg92LZ-WNrSX')  # noqa

# 集
movies = [what_your_name, harry_potter, jin_sang, dead_pool]

fresh_tomatoes.open_movies_page(movies)
