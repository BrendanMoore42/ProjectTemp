"""
Removes a friend from your list

Argument is only name to be removed.

Run in bash:
$ python remove_friend.py Zapp

"""
import sys
import json

# import friends
with open('friends.json') as f:
    friends = json.load(f)

def main(args):
    """
    args[1] = Name

    No duplicates allowed in system, so this deletes one at a time.
    """
    # define variables
    name = args[1].capitalize()

    # search through friends
    if name in friends:
        del friends[name]
        print(f'{name} removed from list.')
        with open('friends.json', 'w') as f:
            json.dump(friends, f)
    else:
        print(f'{name} returns no matches.')


if __name__ == '__main__':
    main(sys.argv)
