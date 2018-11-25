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

# environment variables
menu_options = ['b', 'back', 'q', 'quit',
                'p', 'play', 'h', 'help']

characters = ['Bird', 'Falco', 'Warrior', 'Princess', 'Wizard']

# functions block
def start_game():

    print('='*25, '\n')
    print('>> Player beware, for the path is dangerous...')
    print('>> The Warrior\'s sword is a strong and sturdy weapon...')
    print('>> The Princess\'s magical armour protects her from most attacks...')
    print('>> The Wizard is powerful but at what cost?...\n')

    player = input('>> Who will you choose?... >> ')

    '''
    thinking here that someway to auto assign player classes
    without it getting to complex. might have to do each class
    gets its own if line like it already does.
    '''
    if player in characters:
        pass

    if player in ['q', 'quit']:
        print('>> Exiting...')
        sys.exit()
    elif player in ['bird', 'falco']:
        player = Falco()
        print(Falco)
    elif player in ['warrior', 'w']:
        player = Warrior()
        print(Warrior)
    elif player in ['princess', 'p']:
        player = Princess()
        print(Princess)
    elif player in ['wizard', 'w']:
        player = Wizard()
        print(Wizard)

    # get back to where we need to be
    title_screen()


def help_menu():
    print('\n', '='*25)
    print('******* Help Menu *******')
    print('>> Press "b" to navigate back to title')

    menu = textwrap.dedent(f'''\n
                            > Play: Press 'p' or 'play' to start game
                            > Quit: 'q' or 'quit' to exit game\n
                            ''')
    print(menu)
    print('=' * 25, '\n')
    title_screen()

def menu_nav(option):
    if option.lower() in ['p', 'play']:
        # launch game
        start_game()
    elif option.lower() in ['h', 'help']:
        # launch help
        help_menu()
    elif option.lower() in ['q', 'quit']:
        # I'm not sure what this does
        sys.exit()


def title_screen():

    print('>> Welcome to DiaDungeon!')
    option = input('>> ')

    if option.lower() not in menu_options:
        print('Please enter a valid command.\n')
        title_screen()
    else:
        menu_nav(option)



if __name__ == '__main__':

    title_screen()


