# -*- coding:utf-8 -*-
# __author__ = 'ActMerce'
# __date__ = '2017/10/28 21:18'
import fresh_tomatoes, media


# 电影列表
what_your_name = media.Movie('君の名は', 'https://i.ytimg.com/vi/sjhbO8lIc2s/movieposter.jpg',
                             'https://www.youtube.com/watch?v=sjhbO8lIc2s&list=PLHPTxTxtC0iaN9kA37m6MRrxFkgby2CDR')
harry_potter = media.Movie('Harry Potter', 'https://i.ytimg.com/vi/8GKHFtMaoOY/movieposter.jpg',
                           'https://www.youtube.com/watch?v=8GKHFtMaoOY&list=PLHPTxTxtC0iaN9kA37m6MRrxFkgby2CDR')
jin_sang = media.Movie('银魂', 'https://i.ytimg.com/vi/wyFQ2aQL6b4/movieposter.jpg',
                       'https://www.youtube.com/watch?v=wyFQ2aQL6b4&list=PLxaUumW-X5DcGVwlxF7IJEPKwUw74NiPq')
dead_pool = media.Movie('死侍', 'https://i.ytimg.com/vi/MD-VMxmWezE/movieposter.jpg',
                        'https://www.youtube.com/watch?v=MD-VMxmWezE&list=PLAXJzGOFS3xOOJXl2dJAeUg92LZ-WNrSX')

# 集
movies = [what_your_name, harry_potter, jin_sang, dead_pool]

fresh_tomatoes.open_movies_page(movies)
