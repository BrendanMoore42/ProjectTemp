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

    def __init__(self, name, weapon, level=1, status='Strong', attack=5, defense=5):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status


    def __str__(self):
        return textwrap.dedent(f'''\n
                                Name: {self.name}
                                Attack: {round(self.attack, 2)}
                                Defense: {round(self.defense, 2)}
                                Weapon: {self.weapon}
                                Status: {self.status}
                                Level: {self.level}\n
                                ''')


    def update_level(self, critical=False):
        """
        If monster defeated, level up. If critical strike, level up 5 levels.
        :return:
        """
        if critical:
            self.level += 5
            self.attack = round(self.attack * 3.75, 2)
            self.defense = round(self.defense * 3.75, 2)
            print(f'\nNice Moves! You moved 5 levels up to level {self.level}!')
        else:
            self.level += 1
            self.attack = round(self.attack * 1.75, 2)
            self.defense = round(self.defense * 1.75, 2)
            print(f'\nLevel Up! You are now level {self.level}')

    def update_defense(self, defense_power, enemy_attack):
        self.defense -= enemy_attack

        if self.defense <= 0:
            self.defense = 0
            print('Oh no! You were defeated. Play again?\n')


    def buff_stat(self, category):
        if category == 'attack':
            self.attack = round(self.attack * 1.5)
        if category == 'defense':
            self.defense = round(self.defense * 1.5)


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

class Falco(Player):

    def __init__(self, name='Falco Lombardi', weapon="Pillar Combos", attack=1000, defense=1000):
        super().__init__(name=name, weapon=weapon, attack=attack, defense=defense)

    def __str__(self):
        return super().__str__()

