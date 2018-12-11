"""
date: December 11, 2018
author: @BrendanMoore42

Requirements:
- Twilio==>v.6.2.1
- Twilio trial account (or paid number)
- Python 3+

=========================
Myosotis - Forget me not!

Send a message to yourself to remember important
dates--like family birthdays, anniversaries, etc.

Message body can be modified in check_send.py.

Steps:
1. Set up
    a) Add credentials to credentials.py
    b) Run $ python user.py to create friends
       and add dates to database. Program will
       create a friends.json if one not in current
       directory.
2. Deploy
    a) Set cron job on local or real server through
       online cloud provider: AWS, Digital Ocean, etc.
    example cron job for every day at noon:
    0 12 * * * /usr/bin/python3 /root/check_send.py >/dev/null 2>&1

Always run the cron from the same directory as the friends.json
for up-to-date tasking.
"""
import sys
import json
import datetime
from pathlib import Path
from check_send import check_send
from credentials import credentials

def main():
    """
    Run in bash for menu to update friends with a GUI.
    """

    # checks if file exists, if not one is made
    filepath = Path('friends.json').exists()

    # creates empty friends.json database if none present
    if not filepath:
        friends = {}
        print('making friends.json...')
        with open('friends.json', 'w') as f:
            json.dump(friends, f)

    # import friend data
    with open('friends.json') as f:
        friends = json.load(f)

    # set date variables
    now = datetime.datetime.now()
    now_string = str(now.day) + '/' + str(now.month)

    def show_friends(friends_list):
        """
        Displays list of friends and dates then returns to menu.
        """
        for name, date in friends_list.items():
            print(name, date)


    def add_friend(friends_list):
        """
        Date format must be Day/Month and just numbers.
        """
        print('\n*Hint Date format => Day/Month: ex. 28/07 \n')

        # define variables
        name = input('Please type name: \n')
        date = input('Please type date: \n')

        # search through friends
        if name in friends:
            print(f'{name} exists: Date {date}\n')
        else:
            friends.update({name: date})
            with open('friends.json', 'w') as outfile:
                json.dump(friends, outfile)
            print(f'{name} added\n')


    def remove_friend(friends_list):
        """
        Removes a friend from list.
        """
        # define variables
        name = input('Type name to remove:  ')
        # if name exists, remove
        try:
            del friends_list[name]

            print(f'{name} removed from list.')
            with open('friends.json', 'w') as outfile:
                json.dump(friends, outfile)
        except:
            print(f'{name} returns no matches.')


    def open_menu():
        """
        Opens the main menu and cycles through options.
        """

        print('=' * 25, '\n')
        print('Welcome to Myosotis\n'
              'Never forget a birthday again!\n')

        def options():
            """
            Displays possible options for selection
            """
            print('='*25,
                  '\n\nOptions: \n'
                  '\t1. Check Friend List\n'
                  '\t2. Add Friend\n'
                  '\t3. Remove Friend\n'
                  '\t4. Test Phone\n'
                  '\t5. Press "q" anytime to quit\n')

            # input choice
            command = str(input('Please choose an option: \n'))

            # viable commands
            commands = ['1', '2', '3', '4', 'q']

            # cycle through menu items
            if command == '1':
                show_friends(friends)
            elif command == '2':
                add_friend(friends)
            elif command == '3':
                remove_friend(friends)
            elif command == '4':
                check_send(test=True)
            elif command in ['5', 'q', 'Q']:
                print('\nExiting...\n')
                print('=' * 25, '\n\n')
                sys.exit()
            else:
                print(f'\n{command} invalid option.\n'
                      f'Please try again...\n')
            options()
        options()

    # run menu
    open_menu()

if __name__ == '__main__':
    main()