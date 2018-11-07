"""
author: @BrendanMoore42
date: Nov 6, 108

User Account API
"""
import pandas as pd

with open('imdbtop250.txt', 'r') as f:
    lines = f.read().splitlines()

print(lines)

class User():

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

