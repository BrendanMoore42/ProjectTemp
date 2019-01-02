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
                'p', 'play', 'h', 'help',
                'n', 'newgame']

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
                False: 1}

# set player variables
max_defense = []

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
    # set enemy variables
    enemy = None

    def boss_encounter(boss):
        pass


    def action_select():
        return random.choice(['attack', 'defense'])


    def enemy_turn(player_action, player_power):
        """

        """
        enemy_action = action_select()
        enemy_power = random.choice([0.15, 0.2, 0.25, 0.35, 0.5, 0.65, 0.75])

        print(f'\n{enemy.name} chose {enemy_action} with strength of {enemy.attack - (enemy.attack * enemy_power)}!')

        def turn_outcome(action, player_power, enemy_power):
            """
            compares each members choices and creates outcome
            :param player:
            :param enemy:
            :return:
            """
            player_power = round(player_power, 2)
            enemy_power = round(enemy_power, 2)

            print(f"action: {action}, player: {player_power}, enemy: {enemy_power}")
            if action == 'both_attack':
                enemy.update_defense(player_attack=player_power)
                if not enemy.status:
                    player.update_level(max(max_defense))
                    run_encounter(player, location)
                player.update_defense(enemy_attack=enemy_power)
            if action == 'player_attack':
                attack = round(player_power-enemy_power)
                enemy.update_defense(player_attack=attack)
            if action == 'both_defend':
                player.recover()
                enemy.recover()
            if action == 'player_defend':
                attack = round(enemy_power-player_power)
                player.update_defense(enemy_attack=attack)

            if not player.status:
                menu_nav('n')

            player_turn(None)


        # both attack
        if enemy_action == 'attack' == player_action:
            enemy_attack = enemy.attack - (enemy.attack * enemy_power)
            turn_outcome('both_attack', player_power, enemy_attack)

        # player defends attack
        if enemy_action == 'attack' != player_action:
            enemy_attack = enemy.attack - (enemy.attack * enemy_power)
            turn_outcome('player_defend', player_power, enemy_attack)

        # both defend
        if enemy_action == 'defense' == player_action:
            enemy_defense = enemy.defense - (enemy.defense * enemy_power)
            turn_outcome('both_defend', player_power, enemy_defense)

        # enemy shield player attacks
        if enemy_action == 'defense' != player_action:
            enemy_defense = enemy.defense - (enemy.defense * enemy_power)
            turn_outcome('player_attack', player_power, enemy_defense)


    def enemy_status(attack_power=None, defense_power=None, critical_attack=False, critical_block=False, enemy_buff=False):
        """
        Updates enemies stats on attack
        :param player_attack:
        :param critical: If True, enemy automatically defeated
        :return:
        """

        if critical_block:
            buff_cat = action_select()
            player.buff_stat(buff_cat)
            print(f'Critical Block! {player.name} {buff_cat} Buffed! {enemy.weapon} Missed!')

        if enemy_buff:
            if enemy.defense > 0:
                buff_cat = action_select()
                enemy.buff_stat(buff_cat)
                print(f'\n{enemy.name} {buff_cat} Buffed!')

        if critical_attack:
            print(f'Critical attack!! {enemy.name} defeated!\n')
            enemy.critical_defeat()
            player.update_level(critical=True, max_defense=max(max_defense))
            run_encounter(player, location)

        if attack_power != None:
            enemy_turn('attack', attack_power)

        if defense_power != None:
            enemy_turn('defense', defense_power)


    def player_turn(action):

        buff = status_buffs[player.status]

        # store defense value
        max_defense.append(player.defense)

        # check if boss just defeated

        def attack_power(roll, buff):
            if 0 < roll <= 2.0:
                print('\n', '='*25)
                print('\nBlood Sugar Critically Low SEEK IMMEDIATE CARE\n')
                print('Exiting game.')
                sys.exit()
            if 2.1 <= roll <= 3.0:
                power = round((player.attack / 12 + roll * buff), 2)
                enemy_status(attack_power=power, enemy_buff=True)
                print(f'\nVery Weak attack: {power}!')
            if 3.1 <= roll <= 4.0:
                power = round((player.attack / 8 + (roll * 1.25) * buff), 2)
                print(f'\nWeak attack: {power}!')
            if 4.1 <= roll <= 5.0:
                power = round((player.attack / 6 * roll * buff), 2)
                print(f'\nStrong attack: {power}!')
            if roll == 5.5:
                enemy_status(critical_attack=True)
            if 5.1 <= roll <= 5.4:
                power = round((player.attack / 6 * roll * buff), 2)
                print(f'\nVery Strong attack: {power}!')
            if 5.6 <= roll <= 6.0:
                power = round((player.attack / 8 * roll * buff), 2)
                print(f'\nVery Strong attack: {power}!')
            if 6.1 <= roll <= 7.0:
                power = round((player.attack / 8 * (roll / 2 * 1.15) * buff), 2)
                print(f'\nStrong attack: {power}!')
            if 7.1 <= roll <= 9.0:
                power = round((player.attack / 8 + (roll / 4 * 1.25) * buff), 2)
                print(f'\nWeak attack: {power}!')
            if 9.1 <= roll <= 12.0:
                power = round((player.attack / 12 + (roll / 6) * buff), 2)
                print(f'\nExtremely Weak attack: {power}!')
                enemy_status(attack_power=power, enemy_buff=True)
            if roll >= 12.1:
                print(f'\nAttack Missed!')
                enemy_status(enemy_buff=True)

            enemy_status(attack_power=power)


        def defense_power(roll, buff):
            if 0 < roll <= 1.9:
                print('\n', '='*25)
                print('\nBlood Sugar Critically Low SEEK IMMEDIATE CARE\n')
                print('Exiting game.')
                sys.exit()
            if 2.0 <= roll <= 3.0:
                power = round((player.defense / 12 + roll * buff), 2)
                enemy_status(defense_power=power, enemy_buff=True)
                print(f'\nVery Weak defense: {power}!')
            if 3.1 <= roll <= 4.0:
                power = round((player.defense / 8 + (roll * 1.25) * buff), 2)
                print(f'\nWeak defense: {power}!')
            if 4.1 <= roll <= 5.0:
                power = round((player.defense / 6 * roll * buff), 2)
                print(f'\nStrong defense: {power}!')
            if roll == 5.5:
                print('\nPerfect defense!!')
                enemy_status(critical_block=True)
            if 5.1 <= roll <= 6.0:
                power = round((player.defense / 2 * (roll * 1.15) * buff), 2)
                print(f'\nVery Strong defense: {power}!')
            if 6.1 <= roll <= 7.0:
                power = round((player.defense / 6 * roll * buff), 2)
                print(f'\nStrong defense: {power}!')
            if 7.1 <= roll <= 9.0:
                power = round((player.defense / 8 + (roll * 1.15) * buff), 2)
                print(f'\nWeak defense: {power}!')
            if 9.1 <= roll <= 12.0:
                power = round((player.defense / 12 + roll * buff), 2)
                enemy_status(defense_power=power, enemy_buff=True)
                print(f'\nExtremely Weak defense: {power}!')
            if roll >= 12.1:
                print('\n!')
                enemy_status(enemy_buff=True)

            enemy_status(defense_power=power)

        def roll_attack():
            x = ''
            while not isinstance(x, float):
                roll = input("\nEnter Blood Sugar: ")
                try:
                    x = float(roll)
                    return roll
                except (ValueError, TypeError):
                    print('error')

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

        # check if enemy alive
        if enemy.status:
            # check if player defeated
            print(f'status debug: {player.status}')
            if not player.status:
                menu_nav('newgame')

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
            player.update_level(max_defense=max(max_defense), enemy_type=enemy.enemy_type)
            run_encounter(player, location)

    # standard enemy
    if player.level % 5 != 0:
        enemy = Grunt(level=player.level, attack=player.attack, defense=player.defense)
        phrase = random.choice(['Oh no', 'Look out', 'Watch yourself', 'Ahh!'])
        print(f'\n{phrase}! A {enemy.name} blocks your path!\n')

    # boss encounter
    if player.level % 5 == 0:
        enemy = Boss(level=player.level, attack=player.attack, defense=player.defense)
        location = random.choice(environments['Boss'])
        print(f"\nBoss Battle! At the {location} the {enemy.name} awaits!")

    # display menu and initiate turn
    init_action = input(f"\n1. Attack\n"
                        "2. Defend\n"
                        "3. Check Stats\n"
                        "4. Check Monster\n"
                        "5. Location\n"
                        "6. Title Screen\n"
                        ">> ")
    print(enemy.enemy_type)
    player_turn(init_action)

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
    elif option.lower() in ['n', 'new']:
        # new game, new player
        player = None
        enemy = None
        max_defense = []
        player = choose_character()
        start_game(player, environments)
    elif option.lower() in ['h', 'help']:
        # launch help
        help_menu()
    elif option.lower() in ['q', 'quit']:
        # I'm not sure what this does
        sys.exit()


def title_screen():
    # set player variables
    max_defense = []

    print("Welcome to DiaDungeon!\n\n"
          "Play: Press 'p' to start game\n"
          "New Game: Press 'n' for new game\n"
          "Quit: Press 'q' to exit game\n")

    option = input('>> ')

    if option.lower() not in menu_options:
        print('Please enter a valid command.\n')
        title_screen()
    else:
        menu_nav(option)


if __name__ == '__main__':
    title_screen()
