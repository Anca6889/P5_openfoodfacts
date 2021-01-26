""" This module will generate the main menu """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import MAIN_MENU

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
            print(key, val, '\n') # make it more confortable to read
        self.get_choice() #launch automaticly the choice method after display

    def get_choice(self):
        """ Record the user choice """

        self.choice = int(input("\nEntrez le chiffre correspondant à votre choix puis pressez sur ENTER : "))
        return self.choice

    # def dispatch(self):
    #     """ Generate the class relative of choice """
        
    #     if self.choice == 1
            

if __name__ == '__main__':
    MainMenu()
