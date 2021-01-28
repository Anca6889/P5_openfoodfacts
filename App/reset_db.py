""" This module will reset the data base """

# !/usr/bin/python3
# -*- coding: Utf-8 -*
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')
# import sys = Problème perso d'import à dégager par la suite.

from data_base.database import Database


class Reset:
    "Clear and reset the database"

    def __init__(self):

        self.db = Database()
        self.reset_db()

    def reset_db(self):
        "Lauch the reset"

        print("Régénération de la base de données...")
        self.db.all_gen()


if __name__ == '__main__':
    Reset()
