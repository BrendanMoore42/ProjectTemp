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
import pickle
import random
import numpy as np


#create movie list
# movies = []
# with open('test_list.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         movies.append(line)

def show_movie(movie_list):
    movies = []
    with open('test_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            movies.append(line)




class UserAccount(object):
    def __init__(self, user_id, my_movies):
        self.user_id = user_id
        self.my_movies = []

    def add_movie(self, title):
        print('Sup')

    def show_movies(self):
        return self.my_movies




# if __name__ == '__main__':
#     main()

