import pickle
import toga
from toga.style.pack import *


def sort_letters(a):
    return "".join(sorted(list(a)))


def solver(a):
    sorted_a = sort_letters(a)
    if sorted_a in dict:
        return dict[sorted_a]
    else:
        return []


def build(app):
    left_box = toga.Box()
    left_box.style.update(direction=COLUMN, padding=10)
    left_input = toga.TextInput()
    left_label = toga.Label('Anagram', style=Pack(text_align=LEFT))
    solve_button = toga.Button('Solve')
    left_box.add(left_label)
    left_box.add(left_input)
    left_box.add(solve_button)
    left_box.style.update(flex=1, padding=5)

    table = toga.Table(['Words'])
    table.style.update(flex=1)

    main_box = toga.Box()
    main_box.add(left_box)
    main_box.add(table)
    return main_box


def main():
    return toga.App('Anagram App', 'org.promentol.anagrama', startup=build)


if __name__ == '__main__':
    main().main_loop()