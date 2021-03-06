""" This module will generate the main menu """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from Config.config import MAIN_MENU
from App.select_products import SelectProducts
from App.reset_db import Reset
from App.saved_substitutes import ShowSavedSub
import time


class MainMenu:
    """ This class will display the main menu and record the user choice"""

    def __init__(self):
        self.option = MAIN_MENU
        self.display()
        self.choice = None

    def display(self):
        """ Display the main menu """

        print(
            "\n Bienvenue dans OFF substitutes \n"
            "\n (NOTE: pour une première utilisation: sélectionner 3"
            " pour créer la base de données) \n"
                )
        for key, val in self.option.items():
            print(key, val, '\n')
        self.get_choice()

    def get_choice(self):
        """ Record the user choice """

        self.choice = input(
            "\nEntrez le chiffre correspondant à votre choix puis"
            " pressez sur ENTER : ")
        if self.choice == "1":
            SelectProducts()
            self.display()

        elif self.choice == "2":
            ShowSavedSub()
            self.display()

        elif self.choice == "3":
            Reset()
            self.display()

        elif self.choice == "4":
            print("A bientôt ! \n Fermeture du programme...")
            time.sleep(1)
            quit()

        else:
            print(
                "Le choix que vous avez entré n'existe pas \n"
                "veuillez effectuer un choix valide.\n")
            time.sleep(2)
            input("\n Appuyer sur ENTER pour continuer \n")
            self.display()
