#!/usr/bin/python3
"""
Created: September 22, 2018
Author: @BrendanMoore

PalPix

Requirements:

Creates list pairings of accounts to see if
the same movies have been selected.

If two people want to see the same film,
Marked RED - do not watch alone
If just one wants to see if,
Marked GREEN - go ahead!
"""
#import packages
import flask
import pickle
import numpy as np

#get move list
def show_movie(path_to_txt):
    """
    Retrieves up to date movies and returns list
    :param path_to_txt: csv or text with movies
    :return: list of movies
    """
    movies = []
    with open(f'{path_to_txt}', 'r') as f:
        lines = f.readlines()
        for line in lines:
            movies.append(line)
    return movies

#create random movie generator variable
movies = show_movie('imdbtop250.txt')
random_movie = np.random.choice(movies)
print(random_movie)


class UserAccount(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.my_movies = []

    def add_friend(self):
        print('Add a friend')

    def add_movie(self, title):
        print('Sup')

    def show_movies(self):
        return self.my_movies




# if __name__ == '__main__':
#     main()

