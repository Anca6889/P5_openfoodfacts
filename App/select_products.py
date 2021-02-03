""" This module will generate the category display """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')
from data_base.database import Database
import time


class SelectProducts:
    """ This class will display the category choice """

    def __init__(self):

        self.db = Database()
        self.show_categories()

    def show_categories(self):

        self.db.connecting()
        print("\n veuillez choisir une catégorie de produit \n")
        self.db.cursor.execute("SELECT category_id, category_name \
            FROM category")
        cat_numbers = []
        for line in self.db.cursor.fetchall():
            cat_id = line[0]
            cat_name = line[1]
            cat_numbers.append(line[0])
            print(cat_id, cat_name)

        try:
            cat_choice = int(input(
                "\n Entrer le chiffre correspondant à la catégéorie: \n"))
            if cat_choice in cat_numbers:
                self.show_products(cat_choice)
            else:
                self.come_back()

        except ValueError:
            self.come_back()

    def show_products(self, cat_id):

        product_list = []
        self.db.cursor.execute(
            "SELECT product_id, product_name_fr, brands,\
            nutriscore_grade, category_id \
            FROM product \
            WHERE category_id=%(category_id)s", {'category_id': cat_id})
        for line in (self.db.cursor.fetchall()):
            print(line[0], " Nom du produit:", line[1], "\n",
                  "   Marque:", line[2], "\n", "   Nutriscore:", line[3], "\n",
                  "    Catégorie:", line[4], "\n")
            product_list.append(line)

        try:

            prod_exist = False
            while prod_exist == False:
                prod_choice = int(input(
                    "\n Entrer le numéro correspondant au produit"
                    " que vous voulez remplacer: "))
                for product in product_list:
                    if prod_choice == product[0]:
                        prod_exist = True
                        print(product)
                        prod_save = product
                if prod_exist == False:
                    print("Le numéro entré n'est pas présent dans la liste"
                          " des produits")

            print("Confirmer vous ce choix ?")
            confirm = input("Tapez OUI pour confirmer sinon tapez ce que vous"
                            " voulez pour revenir en arrière : ")
            if confirm == "OUI":
                self.show_substitute(prod_save)

            else:
                self.come_back()

        except IndexError:
            self.come_back()

    def show_substitute(self, prod_choice):

        self.db.get_subsitute(prod_choice)

    def come_back(self):
        """ This method switch to select product menu if user do wrong choice
         """

        print("Choix NON VALIDE, vous allez être redirigé vers la "
              "selection de produit dans 3...2...1...")
        time.sleep(3)
        self.show_categories()


if __name__ == '__main__':
    SelectProducts()
