"""
author: @BrendanMoore
date: March 17, 2019

WCB Generator

Habit tracker--modulate bad habits by assigning frequencies and randomly
get a daily allowance for each behaviour. Calculates off weekly basis.

Takes each habit and returns on the odds you can do that that day and how much.
"""
import sys
import json
import random
import datetime


class Habit(object):
    def __init__(self, habit, frequency=0.0):
        self.habit = habit
        habits = self.habit.split(',')
        self.nickname = habits[0].split('=')[1]
        self.level = habits[1].split('=')[1]
        self.weekly = habits[2].split('=')[1]
        self.weekend = habits[3].split('=')[1]
        self.frequency = frequency


        self.calc_frequency()

        # print(self.frequency)
        print(f'Nickname: {self.nickname}, '
              f'Level: {self.level}, '
              f'Weekly: {self.weekly}, '
              f'Weekend: {self.weekend}')


    def calc_frequency(self):

        if self.frequency:
            return self.frequency
        if self.weekend:
            max_value = 2

        weekly_odds = [self.level] * int(self.weekly)

        while len(weekly_odds) != 7:
            weekly_odds.append(0)
        print(weekly_odds)
        frequency = random.choice(weekly_odds)
        return frequency


def main():

    with open('freq_log.txt', 'r') as f:
        freqs = f.readlines()

    # freqs = list(zip(freqs[::2], freqs[1::2]))

    for habit in freqs:
        habit = Habit(habit)


if __name__ == "__main__":
    main()
