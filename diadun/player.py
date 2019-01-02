"""
author: @BrendanMoore42
date: November 22, 2018

Player classes:

Warrior, Princess, Wizard, Poor Squire


To add:
- Counter system for lives ==> how many chocolate chips can you get with 3 lives?
--> Regular mode: 3 Lives, redeem 25% of CC for one more life
--> Gauntlet: 1 Lives, go until you're defeated
"""

import os, cmd, sys
import time, random
import textwrap

# player meta class
class Player():

    def __init__(self, name, weapon, level=1, status='Strong', attack=5, defense=5, tokens=0, chances=3):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.status = status
        self.attack = attack
        self.defense = defense
        self.tokens = tokens
        self.chances = chances


    def __str__(self):
        return textwrap.dedent(f'''\n
                                Name: {self.name}
                                Attack: {round(self.attack, 2)}
                                Defense: {round(self.defense, 2)}
                                Weapon: {self.weapon}
                                Status: {self.status}
                                Chips: {self.tokens}
                                Level: {self.level}\n
                                ''')


    def update_level(self, max_defense, critical=False, enemy_type='Grunt'):
        """
        If monster defeated, level up. If critical strike, level up 5 levels. If Poor Squire, you level slower.
        :return:
        """

        if critical:
            self.defense = max_defense
            self.level += 5
            self.attack = round(self.attack * 1.35, 2)
            self.defense = round(self.defense * 1.35, 2)

            if enemy_type == 'Boss':
                action = random.choice(['attack', 'defense'])
                self.buff_stat(action)
                print(f'\nYou took down a boss! +6 Levels, {action} buffed, 3 Chocolate Chips earned!')
            print(f'\nNice Moves! You moved 5 levels up to level {self.level}!')
        else:
            if self.name == 'Poor Squire':
                self.attack = round(self.attack * 1.05, 2)
                self.defense = round(self.defense * 1.05, 2)
            else:
                self.attack = round(self.attack * 1.15, 2)
                self.defense = round(self.defense * 1.15, 2)

            if self.defense < max_defense:
                self.defense = max_defense*0.75

            self.level += 1
            self.tokens += 1

            praise = random.choice(['Nice', 'Awesome', 'Radical',
                                    'No Way', 'Close One', 'Wow',
                                    'Amazing', 'Woohoo', 'Aw Yeah'])

            if self.tokens % 6 == 0:
                self.status = 'Buffed'
                print(f'\n{praise}! You are now level {self.level}! Chocolate Chips: {self.tokens} Condition: {self.status}')

            print(f'\n{praise}! You are now level {self.level}! Chocolate Chips: {self.tokens} Condition: {self.status}')

    def log_stats(self):
        '''
        Record highscores
        '''
        pass
        #with open('player_log.', 'r') as f:


    def update_defense(self, enemy_attack):
        self.defense -= enemy_attack
        self.defense = round(self.defense)

        if self.defense <= 0:
            self.defense = 0
            self.status = False
            self.chances -= 1
            print('\nOh no! You were defeated.\n')
            if self.chances == 0:
                print(f'Game over!\n')
                print(f'Playthrough:\n'
                      f'Level: {self.level}\n'
                      f'Chocolate Chips: {self.tokens}\n'
                      f'Character: {self.name}\n')
                self.tokens = 0


    def recover(self):
        '''
        If less than 2 defense, +2 health added, else regular stat boost
        :return:
        '''
        if self.defense <= 2:
            stats_recovered = 2
        else:
            stats_recovered = round(self.defense * 0.25)
        self.defense = self.defense + round(stats_recovered)
        print(f'{self.name} recovered {stats_recovered}')

    def buff_stat(self, category):
        if category == 'attack':
            self.attack = round(self.attack * 1.15)
        if category == 'defense':
            self.defense = round(self.defense * 1.15)


    def roll_stats(self, category):
        """
        Generates random player starter stats. Category is type of character
        1. Warrior: High Attack, Low Defense
        2. Princess: High Defense, Low Attack
        3. Wizard: Random ~~MaGiC~~
        """
        if category == 1:
            self.attack = random.randint(9, 16)
            self.defense = random.randint(5, 10)
        if category == 2:
            self.attack = random.randint(5, 10)
            self.defense = random.randint(9, 16)
        if category == 3:
            self.attack = random.randint(4, 16)
            self.defense = random.randint(4, 16)
        if category == 4:
            self.attack = random.randint(4, 4)
            self.defense = random.randint(4, 4)



# character classes
class Warrior(Player):

    def __init__(self, name='Warrior', weapon="Sword"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category=1)

    def __str__(self):
        return super().__str__()


class Princess(Player):

    def __init__(self, name='Princess', weapon="Bow"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category=2)

    def __str__(self):
        return super().__str__()

class Wizard(Player):

    def __init__(self, name='Wizard', weapon="Magic"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category=3)

    def __str__(self):
        return super().__str__()

class Squire(Player):

    def __init__(self, name='Poor Squire', weapon="Filthy Hands"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category=4)

    def __str__(self):
        return super().__str__()

