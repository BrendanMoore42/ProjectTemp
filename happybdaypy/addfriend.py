"""
Adds a friend to your list

Use: Run in bash with extra arguments being your friends
name and day/month to remember.

Example: Adding Dave, born on July 12th
python addfriend.py Dave 1207
"""
import sys
from friends import friends

def main(name, date):
    date = date[:1] + '/' + date[2:]
    if name in friends:
        print(f'{name} already in database')
    friends.update({name:date})

if __name__ == '__main__':
    main(sys.arg)
