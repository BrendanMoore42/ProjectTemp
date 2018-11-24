"""
author: @BrendanMoore42
date: November 22, 2018

DiaDungeons

RPG crawler that uses blood sugar numbers as attack/defensive rolls

Warrior, Princess, Wizard

"""

import os, cmd, sys
import time, random
import textwrap



class Player():

    status = ['Buffed', 'Strong', 'Weakened', 'Injured', 'Ghost']

    def __init__(self, name, hp=100, attack=50, defense=50, weapon='Hands', status=status[1]):
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


def start_game():

    print('='*25, '\n')
    print('>> Player beware, for the path is dangerous to go alone...')
    print('>> The Warrior\'s sword is strong but his shield is weak...')
    print('>> The Princess\'s magical armour protects her from most attacks...')
    print('>> The Wizard is powerful but at what cost?...\n')
    player = input('>> Who will you choose?... >> ')

    if player == 'quit':
        print('>> Exiting...')
        sys.exit()
    elif player == 'Falco':
        player = Falco()
        print(Falco)
    elif player == 'Warrior':
        player = Warrior()

def help_menu():

    print('\n', '='*25)
    print('******* Help Menu *******')
    print('>> Press "b" to navigate back to title')

    menu = textwrap.dedent(f'''\n
                            > Play: Press 'p' or 'play' to start game
                            > Quit: 'q' or 'quit' to exit game\n
                            ''')
    print('=' * 25, '\n\n')



def title_screen():

    print('>> Welcome to DiaDungeon!')
    option = input('>> Enter Command or "h" for help >> ')

    def select_option(arg):
        if arg.lower() in ['p', 'play']:
            # launch game
            start_game()
        elif arg.lower() in ['h', 'help']:
            help_menu()
        elif arg.lower() in ['q', 'quit']:
            sys.exit()

    select_option(option)

    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command.\n')
        select_option()



if __name__ == '__main__':

    title_screen()


