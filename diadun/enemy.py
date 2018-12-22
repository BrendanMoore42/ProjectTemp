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

    status = ['Buffed', 'Strong', 'Weakened', 'Injured', 'Defeated']

    def __init__(self, name, hp=50, attack=50, defense=50, weapon='Hands', status=status[1]):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status

    def __str__(self):
        return textwrap.dedent(f'''\n
                                Name: {self.name}
                                HP: {self.hp}
                                Attack: {self.attack}
                                Defense: {self.defense}
                                Weapon: {self.weapon}
                                Status: {self.status}\n
                                ''')

# enemy classes
class Snail(Enemy):

    def __init__(self, name='Scary Snail', weapon="Slime Squall", attack=5, defense=15):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

class Ghoul(Enemy):

    def __init__(self, name='Gaseous Ghoul', weapon="Stink Attack", attack=15, defense=25):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

class Hagraven(Enemy):

    def __init__(self, name='Hairy Hagraven', weapon="Hairball Hurl", attack=25, defense=35):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

class Dragon(Enemy):

    def __init__(self, name='Dangerous Dragon', weapon="Fire Breath", attack=50, defense=100):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

