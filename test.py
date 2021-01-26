""" This is only a testing module what will be deleted"""

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from data_base.database import Database
import mysql.connector

class Test:
    """ this is only a testing class what will be deleted """

    def __init__(self):
        
        self.db = Database()
        self.main_menu()

    def main_menu(self):

        self.db.connecting()
        self.db.cursor.execute("SELECT category_id, category_name FROM category")
        for ligne in self.db.cursor.fetchall():
            print(ligne)

if __name__ == '__main__':
    Test()