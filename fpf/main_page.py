import os

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT


class Fpf(toga.App):

    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # set main window
        main_box = toga.Box()
        attack_box = toga.Box()
        defense_box = toga.Box()

        left_container = toga.Box(attack_box)
        right_contatiner = toga.Box(defense_box)

        right_content = toga.Box(
            style=Pack(direction=COLUMN, padding_top=50)
        )



        # attack and defend boxes
        self.attack_label = toga.Label('Attack', style=Pack())
        attack_box.style.update(direction=COLUMN, padding=10)
        attack_box.add(self.attack_label)
        attack_box.style.update(flex=1, padding=5)

        defense_box.style.update(direction=COLUMN, padding=10)
        defense_label = toga.Label('Defense', style=Pack(text_align=RIGHT))
        defense_box.add(defense_label)
        defense_box.style.update(flex=1, padding=5)

        main_box.add(attack_box)
        main_box.add(defense_box)

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return Fpf('FpF', 'com.ds.fpf')


if __name__ == '__main__':
    main().main_loop()

