"""
author: @BrendanMoore42
date: Nov 6, 108

User Account API
"""
# import pandas as pd
from movie_db import movies

#import movies
movies = movies()

print(movies)

class User():

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

