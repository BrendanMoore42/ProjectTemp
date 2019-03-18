"""
author: @BrendanMoore
date: March 17, 2019

WCB Generator

Habit tracker--modulate bad habits by assigning frequencies and randomly
get a daily allowance for each behaviour. Calculates off weekly basis.

Takes each habit and returns on the odds you can do that that day and how much.
"""
import sys
import random


class Habit(object):
    def __init__(self, daily=0, weekly=0, monthly=0, frequency=0.0, weekend=False):
        self.daily = daily
        self.weekly = weekly
        self.monthly = monthly
        self.weekend = weekend
        self.frequency = frequency

        self.calc_frequency()

        print(self.frequency)


    def calc_frequency(self):


        if self.frequency:
            return self.frequency
        if self.weekend:
            max_value = 2

        weekly_odds = [1] * self.weekly
        while len(weekly_odds) != 7:
            weekly_odds.append(0)
        print(weekly_odds)
        frequency = random.choice([0,1])
        return frequency

g = Habit(weekly=4)







def main():

    with open('freq_log.txt', 'r') as f:
        freqs = f.readlines()

        print(freqs)




if __name__ == "__main__":
    main()
