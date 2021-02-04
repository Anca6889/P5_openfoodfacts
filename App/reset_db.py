""" This module will reset the data base """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

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
        # ololol


if __name__ == '__main__':
    Reset()
