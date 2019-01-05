"""
author: @BrendanMoore42
date: November 22, 2018

Enemy classes:

Scary Snail, Gaseous Ghoul, Hairy Hagraven, Phenomenal Phantom, Terrible Troll

"""

import textwrap
import os, cmd, sys
import time, random

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

    def boss_encounter(self):
        pass


    def update_defense(self, player_attack):
        # current defense for comparison/have a max setting
        max_defense = self.defense * 1.25

        # set new defense
        self.defense = self.defense - player_attack
        self.defense = round(self.defense)

        if self.defense > max_defense:
            self.defense = max_defense
        if self.defense <= 0:
            print(f'\n{self.name} defeated!')
            self.status = False
        if self.defense > 0:
            print(f'{self.name} defense: {self.defense}')


    def critical_defeat(self):
        self.status = False


    def buff_stat(self, category, amount=1.05):
        for cat in category:
            if category == 'attack':
                self.attack = round(self.attack * amount)
            if category == 'defense':
                self.defense = round(self.defense * amount)


    def action_select(self):
        return random.choice(['attack', 'defense'])


    def recover(self):
        rec = self.defense + (self.defense * 0.05)
        self.defense = round(rec)
        print(f'{self.name} defense recovered {round(self.defense * 0.25)}!')

    def check_status(self):
        if self.defense <= 0:
            self.status = False
            print('enemy defeated')

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
            self.attack = random.randint(get_lower_range(self.attack, 0.45), get_upper_range(self.attack))
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
class Grunt(Enemy):

    def __init__(self, level, attack, defense, name='_', weapon='_', enemy_type='Grunt', status=True):
        self.level = level
        self.attack = attack
        self.defense = defense
        self.enemy_type = enemy_type
        self.status = status

        # monster type and weapon
        self.name = random.choice(['Scary Snail', 'Gaseous Ghoul', 'Hairy Hagraven',
                                   'Phenomenal Phantom', 'Terrible Troll', 'Rambunctious Redcap'])

        # assign stats
        if self.name == 'Scary Snail':
            super().roll_stats(category=1)
            self.weapon = 'Slime Squall'
        if self.name == 'Gaseous Ghoul':
            super().roll_stats(category=2)
            self.weapon = 'Stink Attack'
        if self.name == 'Hairy Hagraven':
            super().roll_stats(category=3)
            self.weapon = 'Hairball Hurl'
        if self.name == 'Phenonmenal Phantom':
            super().roll_stats(category=4)
            self.weapon = 'Spooky Scream'
        if self.name == 'Terrible Troll':
            super().roll_stats(category=5)
            self.weapon = 'Heavy Club'
        if self.name == 'Rambunctious Redcap':
            # randomized stats
            stats = random.choice([1,5])
            super().roll_stats(category=stats)
            self.weapon = 'Dirty Pikestaff'

    def __str__(self):
        return super().__str__()


# Boss class
class Boss(Enemy):

    def __init__(self, level, attack, defense, name='_', weapon='_', enemy_type='Boss', status=True):
        self.level = level
        self.name = name
        self.attack = attack
        self.defense = defense
        self.enemy_type = enemy_type
        self.weapon = weapon
        self.status = status

        super().roll_stats(category=random.choice([3, 5])) # 6 creates random stats

        # monster type and weapon
        self.name = random.choice(['Dangerous Dragon', 'Maniacal Manticore', 'Quick Qilin',
                                   'Greedy Grootslang', 'Knavish Kamaitachi', 'Bewitching Banshee'])

        if self.name == 'Dangerous Dragon':
            # Dragon's flames == stronger attack
            super().buff_stat('attack', 1.08)
            self.weapon = 'Giant Flameball'
        if self.name == 'Maniacal Manticore':
            # Manticore's venom lower's players defense
            super().buff_stat('attack', 1.06)
            self.weapon = 'Venomous Stinger'
        if self.name == 'Quick Qilin':
            # Qilin attacks first on first appearance, but has weaker attack
            self.weapon = 'Hoof Kick'
            pass
        if self.name == 'Greedy Grootslang':
            # The power of the grootslang is clear in its defense
            super().buff_stat('defense', 1.12)
            self.weapon = 'Tree Slam'
        if self.name == 'Knavish Kamaitachi':
            # The Kamaitachi attacks twice with its quick, but weak, dual blades
            super().buff_stat('defense', 1.04)
            self.weapon = 'Dual Blades'
        if self.name == 'Bewitching Banshee':
            # The banshee bewitches the attacker into pulling their hits and lowering their defenses.
            super().buff_stat('attack', 1.03)
            super().buff_stat('defense', 1.03)
            self.weapon = 'Pysch Out'

    def __str__(self):
        return super().__str__()

