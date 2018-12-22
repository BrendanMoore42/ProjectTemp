"""
author: @BrendanMoore42
date: November 22, 2018

Player classes:

Warrior, Princess, Wizard, Falco Lombardi
"""

import os, cmd, sys
import time, random
import textwrap

# player meta class
class Player():

    def __init__(self, name, level=1, hp=100, attack=50, defense=50, weapon='Hands', status='Strong'):
        self.name = name
        self.level = level
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

    def update_level(self, critical=False):
        """
        If monster defeated, level up. If critical strike, level up 5 levels.
        :return:
        """
        if critical:
            self.level += 5
        else:
            self.level += 1


# character classes
class Warrior(Player):

    def __init__(self, name='Warrior', weapon="Sword", attack=75):
        super().__init__(name=name, weapon=weapon, attack=attack)

    def __str__(self):
        return super().__str__()

class Princess(Player):

    def __init__(self, name='Princess', weapon="Bow", defense=75):
        super().__init__(name=name, weapon=weapon, defense=defense)

    def __str__(self):
        return super().__str__()

class Wizard(Player):

    def __init__(self, name='Wizard', weapon="Magic", attack=75, defense=25):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

class Falco(Player):

    def __init__(self, name='Falco Lombardi', weapon="Pillar Combos", attack=1000, defense=1000):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

