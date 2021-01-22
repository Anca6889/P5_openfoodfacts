""" This module will generate the products display """

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