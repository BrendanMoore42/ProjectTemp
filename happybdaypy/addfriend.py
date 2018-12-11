"""
Adds a friend to your list without gui.

Arguments are name and day/month.

Run in bash:
$ python addfriend.py Zapp 3006

Now on June 30th of every year a text will notify you
with your reminder.
"""
import sys
import json

def main(args):
    """
    args[1] = Name
    args[2] = Date
    Date format must be Day/Month and just numbers.
    """
    # define variables
    name = args[1].capitalize()
    date = args[2][:2] + '/' + args[2][2:]

    # import friend data
    with open('friends.json') as f:
        friends = json.load(f)

    # search through friends
    if name in friends:
        print(f'{name} exists: Date {date}')
    else:
        friends.update({name: date})
        with open('friends.json', 'w') as f:
            json.dump(friends, f)
        print(f'{name} added')

if __name__ == '__main__':
    main(sys.argv)
