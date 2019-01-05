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

    def __init__(self, name, weapon, level=1, status='Strong', attack=5, defense=5, tokens=0, grunt_count=0, boss_count=0, chances=3, rolls=[], levels=[], max_defense=[]):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.levels = levels
        self.status = status
        self.attack = attack
        self.defense = defense
        self.max_defense = max_defense
        self.tokens = tokens
        self.grunt_count = grunt_count
        self.boss_count = boss_count
        self.chances = chances
        self.rolls = rolls


    def __str__(self):
        return textwrap.dedent(f'''\n
                                Name: {self.name}
                                Attack: {round(self.attack, 2)}
                                Defense: {round(self.defense, 2)}
                                Weapon: {self.weapon}
                                Status: {self.status}
                                Chips: {self.tokens}
                                Chances: {self.chances}
                                Level: {self.level}\n
                                ''')


    def update_level(self, critical=False, enemy_type='Grunt'):
        """
        If monster defeated, level up. If critical strike, level up 5 levels. If Poor Squire, you level slower.
        :return:
        """
        # add to counter
        self.grunt_count += 1

        if critical:
            self.defense = max(self.max_defense)
            self.level += 5
            self.attack = round(self.attack * 1.35, 2)
            self.defense = round(self.defense * 1.35, 2)
            self.tokens += 3

            if enemy_type == 'Boss':
                action = random.choice(['attack', 'defense'])
                # fix grunt count, add boss count
                self.grunt_count -= 1
                self.boss_count += 1
                self.buff_stat(action)
                self.level += 1
                self.tokens += 2
                print(f'\nBoss defeated! Level {self.level}, {action} buffed, +5 Chocolate Chips!')
                pass
            self.status = 'Buffed'
            print(f'\nNice Moves! You moved 5 levels up to level {self.level}! Status buffed!')
        else:
            if self.name == 'Poor Squire':
                self.attack = round(self.attack * 1.05, 2)
                self.defense = round(self.defense * 1.05, 2)
            else:
                self.attack = round(self.attack * 1.15, 2)
                self.defense = round(self.defense * 1.15, 2)

            if self.defense < max(self.max_defense):
                self.defense = max(self.max_defense) * 0.75

            self.level += 1
            self.tokens += 1

            praise = random.choice(['Nice', 'Awesome', 'Radical', 'Congrats',
                                    'No Way', 'Close One', 'Wow', 'Yeehaw',
                                    'Amazing', 'Woohoo', 'Aw Yeah'])

            if self.tokens % 6 == 0:
                self.status = 'Buffed'
                print(f'\n{praise}! Level {self.level}! \nChocolate Chips: +1 \nCondition: {self.status}')

            print(f'\n{praise}! You are now level {self.level}! \nChocolate Chips: +{self.tokens} \nCondition: {self.status}')


    def update_rolls(self, roll, level):
        self.rolls.append(roll)
        self.levels.append(level)
        # print(f'Added {roll}. Player rolls: {self.rolls}')


    def log_stats(self):
        '''
        Record highscores
        '''
        pass
        #with open('player_log.', 'r') as f:


    def on_continue(self, tokens, chances):
        # keep chips and chances
        self.tokens = tokens
        self.chances = chances
        # reset defense
        self.max_defense = []


    def game_over(self):
        print(f'Game over!\n')
        print(f'Playthrough\n'
              f'Highest Level: {max(self.levels)}\n'
              f'Chocolate Chips: {self.tokens}\n'
              f'Grunts Beaten: {self.grunt_count}\n'
              f'Bosses Defeated: {self.boss_count}\n'
              f'Character: {self.name}\n'
              f'\nRoll Stats\n'
              f'Avg. Roll: {round(sum(self.rolls)/len(self.rolls), 1)}\n'
              f'Lowest Roll: {min(self.rolls)}\n'
              f'Highest Roll: {max(self.rolls)}\n')


    def update_defense(self, enemy_attack):
        self.max_defense.append((self.defense))
        self.defense -= enemy_attack
        self.defense = round(self.defense)

        if self.defense <= 0:
            self.defense = 0
            self.status = False
            self.chances -= 1
            print('\nOh no! You were defeated.\n')

            if self.chances == 0:
                self.game_over()


    def recover(self):
        '''
        If less than 2 defense, +2 health added, else regular stat boost
        :return:
        '''
        if max(self.max_defense) < 2:
            stats_recovered = 2
        else:
            stats_recovered = round(self.defense * 0.25)
        self.defense = self.defense + round(stats_recovered)
        print(f'{self.name} recovered {stats_recovered}')


    def buff_stat(self, category):
        if category == 'attack':
            self.attack = round(self.attack * 1.15)
        if category == 'defense':
            if self.defense > (max(self.max_defense) * 1.25):
                self.defense = max(self.max_defense)
            else:
                self.defense = round(self.defense * 1.15)


    def roll_stats(self, category):
        """
        Generates random player starter stats. Category is type of character
        1. Warrior: High Attack, Low Defense
        2. Princess: High Defense, Low Attack
        3. Wizard: Random ~~MaGiC~~
        """
        if category == 'Warrior':
            self.attack = random.randint(9, 16)
            self.defense = random.randint(5, 10)
        if category == 'Princess':
            self.attack = random.randint(5, 10)
            self.defense = random.randint(9, 16)
        if category == 'Wizard':
            self.attack = random.randint(4, 16)
            self.defense = random.randint(4, 16)
        if category == 'Squire':
            self.attack = random.randint(4, 4)
            self.defense = random.randint(4, 4)

        if self.attack == 0:
            self.attack = 3
        if self.defense == 0:
            self.defense = 3

        # Initialize value
        self.max_defense.append(self.defense)



# character classes
class Warrior(Player):

    def __init__(self, name='Warrior', weapon="Calamitous Claymore"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category='Warrior')

    def __str__(self):
        return super().__str__()


class Princess(Player):

    def __init__(self, name='Princess', weapon="Luxurious Longbow"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category='Princess')

    def __str__(self):
        return super().__str__()

class Wizard(Player):

    def __init__(self, name='Wizard', weapon="Mysterious Magic"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category='Wizard')

    def __str__(self):
        return super().__str__()

class Squire(Player):

    def __init__(self, name='Poor Squire', weapon="Filthy Hands"):
        super().__init__(name=name, weapon=weapon)
        super().roll_stats(category='Squire')

    def __str__(self):
        return super().__str__()

