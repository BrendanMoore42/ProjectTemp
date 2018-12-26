"""
author: @BrendanMoore42
date: November 22, 2018

Enemy classes:

Scary Snail, Gaseous Ghoul, Hairy Hagraven, Phenomenal Phantom, Terrible Troll, Dangerous Dragon

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
                                Attack: {round(self.attack, 2)}
                                Defense: {round(self.defense, 2)}\n
                                ''')


    def update_defense(self, player_attack):
        self.defense -= player_attack
        self.defense = round(self.defense)

        if self.defense <= 0:
            print(f'\n{self.name} defeated!')
            self.status = False
        if self.defense > 0:
            print(f'{self.name} Defense: {self.defense}')

    def critical_defeat(self):
        self.status = False

    def buff_stat(self, category):
        if category == 'attack':
            self.attack = round(self.attack * 1.5)
        if category == 'defense':
            self.defense = round(self.defense * 1.5)

    def recover(self):
        self.defense = self.defense + (self.defense * 0.05)
        self.defense = round(self.defense)

    def action_defense(self):
        enemy.status =

    def roll_stats(self, category):
        """
        Generates random enemy starter stats. Category is type of character.
        1. Snail: High Defense, Low Attack
        2. Ghoul: High Attack, Low Defense
        3. Hagraven: Random ~~MaGiC~~
        4. Phantom: Low Attack, Low Defense
        5. Troll: High Attack, High Defense
        """

        def get_lower_range(whole, percent=0):
            lower = whole - (percent * whole)
            if lower == 0:
                lower = whole * random.uniform(0.5, 1.5)
            return int(lower)


        def get_upper_range(whole, percent=0):
            upper = (percent * whole) + whole
            return int(upper)


        if category == 1:
            self.attack = random.randint(get_lower_range(self.attack, 0.75), get_upper_range(self.attack))
            self.defense = random.randint(get_lower_range(self.defense, 0.15), get_upper_range(self.defense, 0.25))
        if category == 2:
            self.attack = random.randint(get_lower_range(self.attack, 0.15), get_upper_range(self.attack, 0.15))
            self.defense = random.randint(get_lower_range(self.defense, 0.75), get_upper_range(self.defense))
        if category == 3:
            self.attack = random.randint(get_lower_range(self.attack, 0.5), get_upper_range(self.attack, 0.5))
            self.defense = random.randint(get_lower_range(self.defense, 0.5), get_upper_range(self.defense, 0.5))
        if category == 4:
            self.attack = random.randint(get_lower_range(self.attack, 0.75), get_upper_range(self.attack, -0.15))
            self.defense = random.randint(get_lower_range(self.defense, 0.75), get_upper_range(self.defense, -0.15))
        if category == 5:
            self.attack = random.randint(get_lower_range(self.attack, 0.05), get_upper_range(self.attack, 0.65))
            self.defense = random.randint(get_lower_range(self.defense, 0.05), get_upper_range(self.defense, 0.65))

# enemy classes
class Snail(Enemy):

    def __init__(self, level, attack, defense, name='Scary Snail', weapon="Slime Squall", status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status
        super().roll_stats(category=1)
        # super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    def __str__(self):
        return super().__str__()

class Ghoul(Enemy):

    def __init__(self, level, attack, defense, name='Gaseous Ghoul', weapon="Stink Attack", status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status
        super().roll_stats(category=2)
    #     super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)
    #
    def __str__(self):
        return super().__str__()

class Hagraven(Enemy):

    def __init__(self, level, attack, defense, name='Hairy Hagraven', weapon="Hairball Hurl", status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status
        super().roll_stats(category=3)
    #     super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)
    #
    def __str__(self):
        return super().__str__()


class Phantom(Enemy):

    def __init__(self, level, attack, defense, name='Scary Snail', weapon="Slime Squall", status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status
        super().roll_stats(category=4)
        # super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    def __str__(self):
        return super().__str__()


class Troll(Enemy):

    def __init__(self, level, attack, defense, name='Scary Snail', weapon="Slime Squall", status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.status = status
        super().roll_stats(category=5)
        # super().__init__(player_level=player_level, name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    def __str__(self):
        return super().__str__()

# bosses
class Dragon(Enemy):

    def __init__(self, name='Dangerous Dragon', weapon="Fire Breath", attack=50, defense=100, status=True):
        super().__init__(name=name, weapon=weapon, attack=attack*player_level, defense=defense*player_level)

    def __str__(self):
        return super().__str__()

