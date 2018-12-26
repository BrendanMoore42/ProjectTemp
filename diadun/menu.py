#!/usr/bin/env
"""
author: @BrendanMoore42
date: November 22, 2018

FivePointFive

RPG crawler that uses blood sugar numbers as attack/defensive rolls

Player classes
Warrior, Princess, Wizard

Enemies:
Scary Snail, Gaseous Ghoul, Hairy Hagraven, Phenomenal Phantom, Terrible Troll, Dangerous Dragon

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

status_buffs = {'Buffed': 1.5,
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

    enemies = [Snail(level=player.level, attack=player.attack, defense=player.defense),
               Ghoul(level=player.level, attack=player.attack, defense=player.defense),
               Hagraven(level=player.level, attack=player.attack, defense=player.defense),
               Phantom(level=player.level, attack=player.attack, defense=player.defense),
               Troll(level=player.level, attack=player.attack, defense=player.defense)]

    def boss_encounter():
        pass

    def roll_attack():
        return input("\nEnter Blood Sugar: ")

    def action_select():
        return random.choice(['attack', 'defense'])

    def enemy_turn(player_action, player_power):
        """

        """
        enemy_action = action_select()
        enemy_power = random.choice([0.05, 0.1, 0.15, 0.2, 0.25, 0.35, 0.5])

        def turn_outcome(action, player, enemy):
            """
            compares each members choices and creates outcome
            :param player:
            :param enemy:
            :return:
            """

            if action == "attack":




        if enemy_action == 'attack':
            enemy_attack = enemy.attack - (enemy.attack * enemy_power)
            print(f'{enemy.name} chose to {enemy_action} with a strength of {power}!')

            player.update_defense(enemy_attack=enemy_attack)
            enemy.update_defense(player_attack=player_power)


        if enemy_action == 'defense':
            power = enemy.defense - (enemy.defense * enemy_power)
            print(f'{enemy.name} chose to {enemy_action} with a strength of {power}!')

            enemy.update_defense(player_attack=player_attack)

        turn_outcome()


    def enemy_status(attack_power=None, defense_power=None, critical_attack=False, critical_block=False, enemy_buff=False):
        """
        Updates enemies stats on attack
        :param player_attack:
        :param critical: If True, enemy automatically defeated
        :return:
        """

        if attack_power != None:
            enemy_turn('attack', attack_power)
            # print(f"The {player.name} used {player.weapon} with attack power of {attack_power}\n")
            #enemy.update_health(player_attack=attack_power)

        if defense_power != None:
            enemy_turn('defense', defense_power)
            # print(f"The {player.name} shielded {enemy.weapon} with defense power of {defense_power}\n")

        if critical_attack:
            print(f'Critical attack!! {enemy.name} defeated!\n')
            enemy.critical_defeat()
            player.update_level(critical=True)
            run_encounter(player, location)

        if critical_block:
            buff_cat = action_select()
            player.buff_stat(buff_cat)
            print(f'Critical Block! {player.name} {buff_cat} Buffed! {enemy.weapon} Missed!')

        if enemy_buff:
            if enemy.defense > 0:
                buff_cat = action_select()
                enemy.buff_stat(buff_cat)
                print(f'\n{enemy.name} {buff_cat} Buffed!')


    def player_turn(action):

        def attack_power(roll, buff):
            if 0 < roll <= 2.0:
                print('\n', '='*25)
                print('\nBlood Sugar Critically Low SEEK IMMEDIATE CARE\n')
                print('Exiting game.')
                sys.exit()
            if 2.1 <= roll <= 3.0:
                power = round((player.attack / 12 + roll * buff), 2)
                enemy_status(attack_power=power, enemy_buff=True)
                print('\nVery Weak attack!')
            if 3.1 <= roll <= 4.0:
                power = round((player.attack / 8 + (roll * 1.25) * buff), 2)
                print('\nWeak attack!')
            if 4.1 <= roll <= 5.0:
                power = round((player.attack / 6 * roll * buff), 2)
                print('\nStrong attack!')
            if roll == 5.5:
                enemy_status(critical_attack=True)
            if 5.1 <= roll <= 6.0:
                power = round((player.attack / 2 * roll * buff), 2)
                print('\nVery Strong attack!')
            if 6.1 <= roll <= 7.0:
                power = round((player.attack / 6 * roll * buff), 2)
                print('\nStrong attack!')
            if 7.1 <= roll <= 9.0:
                power = round((player.attack / 8 + (roll * 1.25) * buff), 2)
                print('\nWeak attack!')
            if 9.1 <= roll <= 12.0:
                power = round((player.attack / 12 + roll * buff), 2)
                print('\nExtremely Weak attack!')
                enemy_status(attack_power=power, enemy_buff=True)
            if roll >= 12.1:
                print('\nAttack Missed!')
                enemy_status(enemy_buff=True)

            enemy_status(attack_power=power)


        def defense_power(roll, buff):
            if 0 < roll <= 2.0:
                print('\n', '='*25)
                print('\nBlood Sugar Critically Low SEEK IMMEDIATE CARE\n')
                print('Exiting game.')
                sys.exit()
            if 2.1 <= roll <= 3.0:
                power = round((player.defense / 12 + roll * buff), 2)
                enemy_status(defense_power=power, enemy_buff=True)
                print('\nVery Weak defense!')
            if 3.1 <= roll <= 4.0:
                power = round((player.defense / 8 + (roll * 1.25) * buff), 2)
                print('\nWeak defense!')
            if 4.1 <= roll <= 5.0:
                power = round((player.defense / 6 * roll * buff), 2)
                print('\nStrong defense!')
            if roll == 5.5:
                print('\nPerfect defense!!')
                enemy_status(critical_block=True)
            if 5.1 <= roll <= 6.0:
                power = round((player.defense / 2 * roll * buff), 2)
                print('\nVery Strong defense!')
            if 6.1 <= roll <= 7.0:
                power = round((player.defense / 6 * roll * buff), 2)
                print('\nStrong defense!')
            if 7.1 <= roll <= 9.0:
                power = round((player.defense / 8 + (roll * 1.25) * buff), 2)
                print('\nWeak defense!')
            if 9.1 <= roll <= 12.0:
                power = round((player.defense / 12 + roll * buff), 2)
                enemy_status(defense_power=power, enemy_buff=True)
                print('\nExtremely Weak defense!')
            if roll >= 12.1:
                print('\n!')
                enemy_status(enemy_buff=True)

            enemy_status(defense_power=power)



        buff = status_buffs[player.status]

        # attack
        if action == '1':
            roll = float(roll_attack())
            attack_power(roll, buff)
        # defend
        if action == '2':
            roll = float(roll_attack())
            defense_power(roll, buff)
        # check player stats
        if action == '3':
            print(player)
        # check enemy stats
        if action == '4':
            print(enemy)
        # check location
        if action == '5':
            print(f'\nLocation: {location}')
        # title
        if action == '6':
            title_screen()


        if enemy.status:
            action = input("1. Attack\n"
                           "2. Defend\n"
                           "3. Check Stats\n"
                           "4. Check Monster\n"
                           "5. Location\n"
                           "6. Title Screen\n"
                           ">> ")
            player_turn(action)

        if not enemy.status:
            # enemy is defeated, update level and run next encounter
            player.update_level()
            run_encounter(player, location)


    if player.level % 5 != 0:
        enemy = random.choice(enemies)
        init_action = input(f"\nOh no! a {enemy.name} blocks your path!\n"
                        "1. Attack\n"
                       "2. Defend\n"
                       "3. Check Stats\n"
                       "4. Check Monster\n"
                       "5. Location\n"
                       "6. Title Screen\n"
                       ">> ")
        player_turn(init_action)


    if player.level % 5 == 0:
        print('\n\n\nboss encounter!')
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
