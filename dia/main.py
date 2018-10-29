"""
author: @BrendanMoore42
date: Oct 28, 2018

Automatic Type I Diabetes Pump Regulator

Keeps blood sugar between a set threshold
"""
import numpy as np

class User():

    def __init__(self, name):
        self.name = name
        #self.blood_sugar = blood_sugar


    def check_sugar():
        pass

def create_user():
    name = input(print('Name? '))
    return User(name)

def main():
    print('Initializing...\n')


    user = create_user()

    print(user.name)




    # while True:
    #     pass




if __name__ == "__main__":
    main()