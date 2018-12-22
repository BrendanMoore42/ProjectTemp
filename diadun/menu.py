#!/usr/bin/env
"""
author: @BrendanMoore42
date: November 22, 2018

FivePointFive

RPG crawler that uses blood sugar numbers as attack/defensive rolls

Player classes
Warrior, Princess, Wizard

Enemies:
Scary Snail, Gaseous Ghoul, Hairy Hagraven, Dangerous Dragon

"""
import os, cmd, sys
import time, random
import textwrap
from player import *
from enemy import *

# environment variables
menu_options = ['b', 'back', 'q', 'quit',
                'p', 'play', 'h', 'help']

characters = {'1': Warrior(),
              '2': Princess(),
              '3': Wizard(),
              '4': Falco()
              }

environments = {'Regular': ['Perilous Path', 'Haunted Woods', 'Creepy Cave', 'Mighty Mountain'],
                "Boss": ["Dragon's Den", "Denny's Diner", "Crumbling Castle"]}

status_buffs = {'Buffed': 2,
                'Strong': 1,
                'Weakened': 0.75,
                'Injured': 0.25,
                'Ghost': 1}

# functions block
def choose_character():

    print('\n', '='*25, '\n')
    print('Player beware, for the path is dangerous...')
    print('1. The Warrior\'s sword is a strong and sturdy weapon...')
    print('2. The Princess\'s magical armour protects her from most attacks...')
    print('3. The Wizard is powerful but at what cost?...\n')

    action = input('>> Who will you choose? ')

    if action in characters.keys():

        player = characters[action]
        print(f"You selected: {player.name}")

    return player


def start_game(player, environments):

    if player.level % 5 != 0:
        location = random.choice(environments['Regular'])
    if player.level % 5 == 0:
        location = random.choice(environments['Boss'])

    print(f"Welcome {player.name}!\n\n"
          f"Weapon: {player.weapon}. Player Level: {player.level}.\n"
          f"Location: {location}\n")

    run_encounter(player, location)


def run_encounter(player, location):

    enemies = [Snail(level=player.level), Ghoul(level=player.level), Hagraven(level=player.level)]

    def boss_encounter():
        pass

    def roll_attack():
        return input("\nEnter Blood Sugar: ")

    def enemy_attack(level, buff=False):
        """
        if buff, attack was missed, so monster gets 1.25x boost
        :param level: player level dictates strength of enemy -> attack
        :return:
        """
        pass

    def enemy_status(player_attack=1, critical=False):
        """
        Updates enemies stats on attack
        :param player_attack:
        :param critical: If True, enemy automatically defeated
        :return:
        """

        if critical:
            print('Critical attack!! Monster defeated!\n')
            enemy.critical_defeat()
            player.update_level(critical=True)
            run_encounter(player, location)

        print(f'\nEnemy: {enemy.name}\n'
              f'Health: {enemy.defense}\n')

        print(f"The {player.name} used {player.weapon} with attack power of {player_attack}")

        enemy.update_health(player_attack=player_attack)

        print(f'\nEnemy: {enemy.name}\n'
              f'Health: {enemy.defense}\n')

    def player_turn(action):

        buff = status_buffs[player.status]
        roll = float(roll_attack())

        # attack
        if action == '1':
            attack_power = round((player.attack + player.level + buff)/roll, 2)

            print(f"Status buff: x {buff}\n"
                  f"Attack Power: {attack_power}\n"
                  f"Roll Attack: {roll}\n")

            if 0 < roll <= 2.0:
                print('\n', '='*25)
                print('\nBlood Sugar Critically Low SEEK IMMEDIATE CARE\n')
                print('Exiting game.')
                sys.exit()
            if 2.1 <= roll <= 3.0:
                print('\nVery Weak attack!')
                enemy_status(attack_power)
            if 3.1 <= roll <= 4.0:
                print('\nWeak attack!')
                enemy_status(attack_power)
            if 4.1 <= roll <= 5.0:
                print('\nStrong attack!')
                enemy_status(attack_power)
            if roll == 5.5:
                print('\nCritical Success!!')
                enemy_status(critical=True)
            if 5.1 <= roll <= 6.0:
                print('\nVery Strong attack!')
                enemy_status(attack_power)
            if 6.1 <= roll <= 7.0:
                print('\nStrong attack!')
                enemy_status(attack_power)
            if 7.1 <= roll <= 9.0:
                print('\nWeak attack!')
                enemy_status(attack_power)
            if 9.1 <= roll <= 12.0:
                print('\nExtremely Weak attack!')
                enemy_status(attack_power)
            if roll >= 12.1:
                print('\nAttack Missed! Monster buffed!')
                enemy_attack(player.level)


        # defend
        if action == 2:
            defense_power = player.defense * player.level * buff
            pass

        if enemy.status:
            action = input("1. Attack\n"
                           "2. Defend\n"
                           "3. Check Stats\n"
                           "4. Check Monster\n"
                           "5. Title screen\n"
                           ">> ")
            player_turn(action)


        if not enemy.status:
            # enemy is defeated, update level and run next encounter
            player.update_level()

    if player.level % 5 != 0:
        enemy = random.choice(enemies)
        init_action = input(f"\nOh no! a {enemy.name} blocks your path!\n"
                        "1. Attack\n"
                        "2. Defend\n"
                        ">> ")
        player_turn(init_action)


    if player.level % 5 == 0:
        boss_encounter()





def help_menu():
    print('\n', '='*25)
    print('******* Help Menu *******\n')
    print("Press 'b' to navigate back to title")

    menu = textwrap.dedent(f'''\n
                            Play: Press 'p' or 'play' to start game
                            Quit: 'q' or 'quit' to exit game\n
                            ''')
    print(menu)
    print('=' * 25, '\n')
    title_screen()


def menu_nav(option):
    if option.lower() in ['p', 'play']:
        # launch game
        player = choose_character()
        start_game(player, environments)
    elif option.lower() in ['h', 'help']:
        # launch help
        help_menu()
    elif option.lower() in ['q', 'quit']:
        # I'm not sure what this does
        sys.exit()


def title_screen():

    print("Welcome to DiaDungeon!\n\n"
          "Play: Press 'p' to start game\n"
          "Restart: Press 'r' to restart game\n"
          "Quit: Press 'q' to exit game\n")

    option = input('>> ')

    if option.lower() not in menu_options:
        print('Please enter a valid command.\n')
        title_screen()
    else:
        menu_nav(option)


if __name__ == '__main__':
    title_screen()
