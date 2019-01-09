"""
author: BrendanMoore42
date: Jan 9, 2019

Nortia--Human Automation Bot

Runs a function or script 9-5 workdays with lunch breaks,
smoke breaks.
"""
import datetime

class Nortia():

    def __init__(self, seconds=0, minutes=0, start = 900, end=1700, lunch=True, smoke=True):
        self.seconds = seconds
        self.minutes = minutes
        self.start = start
        self.end = end
        self.lunch = lunch
        self.smoke = smoke
        self.now = datetime.datetime.now()

    def now_is(self):
        print(self.now)


def check_website():
    link = 'https://www.google.ca'
    print('Checking link')


n = Nortia()
n.now_is()