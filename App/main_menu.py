""" This module will generate the main menu """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import MAIN_MENU
from App.select_products import SelectProducts
from App.reset_db import Reset


class MainMenu:
    """ This class will display the main menu and record the user choice"""

    def __init__(self):
        self.option = MAIN_MENU
        self.display()
        self.choice = None

    def display(self):
        """ Display the main menu """

        print('\n')
        for key, val in self.option.items():
            print(key, val, '\n')
        self.get_choice()  

    def get_choice(self):
        """ Record the user choice """

        self.choice = int(input(
            "\nEntrez le chiffre correspondant à votre choix puis"
            "pressez sur ENTER : "))
        
        self.dispatch()

    def dispatch(self):
        """ Generate the class relative of choice """

        if self.choice == 1:
            SelectProducts()

        if self.choice == 3:
            Reset()


if __name__ == '__main__':
    MainMenu()
