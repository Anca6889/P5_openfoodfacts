""" This module will generate the category display """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')
from data_base.database import Database


class SelectCategory:
    """ This class will display the category choice """

    def __init__(self):

        self.db = Database()
        self.show_categories()
        self.cat_choice = None

    def show_categories(self):

        self.db.connecting()
        self.db.cursor.execute("SELECT category_id, category_name FROM category")
        for line in self.db.cursor.fetchall():
            cat_id = line[0] 
            cat_name = line[1]
            print(cat_id, cat_name)
        cat_choice = input(
            "\n Entrer le chiffre correspondant à la catégéorie:")
        self.show_products(cat_choice)

    def show_products(self, cat_id):

        self.db.cursor.execute(
            "SELECT product_name_fr FROM product WHERE category_id=%(category_id)s", {'category_id': cat_id})
        for line in enumerate(self.db.cursor.fetchall()):
            print(line[0], line[1])


if __name__ == '__main__':
    SelectCategory()
