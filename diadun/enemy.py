"""
author: @BrendanMoore42
date: November 22, 2018

Enemy classes:

Scary Snail, Gaseous Ghoul, Hairy Hagraven, Dangerous Dragon

"""

import os, cmd, sys
import time, random
import textwrap

# enemy meta classs
class Enemy():

    def __init__(self, level, name, attack, defense, weapon, status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status

    def __str__(self):
        return textwrap.dedent(f'''\n
                                Name: {self.name}
                                Attack: {self.attack}
                                Defense: {self.defense}\n
                                ''')


    def update_health(self, player_attack):
        self.defense -= player_attack
        self.defense = round(self.defense)
        if self.defense <= 0:
            print(f'\n{self.name} defeated!')
            self.defense = 0
            self.status = False

    def critical_defeat(self):
        self.status = False

    def buff_stat(self, category):
        if category == 'attack':
            self.attack = round(self.attack * 1.5)
        if category == 'defense':
            self.defense = round(self.defense * 1.5)


# enemy classes
class Snail(Enemy):

    def __init__(self, level, name='Scary Snail', weapon="Slime Squall", attack=5, defense=15, status=True):
        self.level = level
        self.name = name
        self.attack = attack * level
        self.defense = defense * level
        self.weapon = weapon
        self.status = status
        # super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    # def __str__(self):
    #     return super().__str__()

class Ghoul(Enemy):

    def __init__(self, level, name='Gaseous Ghoul', weapon="Stink Attack", attack=15, defense=25, status=True):
        self.level = level
        self.name = name
        self.attack = attack * level
        self.defense = defense * level
        self.weapon = weapon
        self.status = status
    #     super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)
    #
    # def __str__(self):
    #     return super().__str__()

class Hagraven(Enemy):

    def __init__(self, level, name='Hairy Hagraven', weapon="Hairball Hurl", attack=25, defense=35, status=True):
        self.level = level
        self.name = name
        self.attack = attack * level
        self.defense = defense * level
        self.weapon = weapon
        self.status = status
    #     super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)
    #
    # def __str__(self):
    #     return super().__str__()

class Dragon(Enemy):

    def __init__(self, name='Dangerous Dragon', weapon="Fire Breath", attack=50, defense=100, status=True):
        super().__init__(name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    def __str__(self):
        return super().__str__()

