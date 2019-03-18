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
    def __init__(self, habit, frequency=0.0, weekend=False):
        self.habit = habit
        self.daily = 0.0
        self.weekly = 0.0
        self.monthly = 0.0
        self.weekend = weekend
        self.frequency = frequency

        self.calc_frequency()

        print(self.frequency)
        print(self.habit)


    def calc_frequency(self):


        if self.frequency:
            return self.frequency
        if self.weekend:
            max_value = 2

        weekly_odds = [1] * int(self.weekly)
        while len(weekly_odds) != 7:
            weekly_odds.append(0)
        print(weekly_odds)
        frequency = random.choice([0,1])
        return frequency








def main():

    with open('freq_log.txt', 'r') as f:
        freqs = f.readlines()

        print(freqs)

    freqs = list(zip(freqs[::2], freqs[1::2]))

    for habit in freqs:
        habit = Habit(habit)


if __name__ == "__main__":
    main()
