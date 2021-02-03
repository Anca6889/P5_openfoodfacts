""" This module will generate the category display """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

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
            while prod_exist is False:
                prod_choice = int(input(
                    "\n Entrer le numéro correspondant au produit"
                    " que vous voulez remplacer: "))
                for product in product_list:
                    if prod_choice == product[0]:
                        prod_exist = True
                        print("\n Vous avez sélectionné: \n\n", product[0],
                              " Nom du produit:", product[1], "\n",
                              "   Marque:", product[2], "\n",
                              "   Nutriscore:", product[3], "\n",
                              "    Catégorie:", product[4], "\n")
                        prod_save = product
                if prod_exist is False:
                    print("Le numéro entré n'est pas présent dans la liste"
                          " des produits")

            print("Confirmer vous ce choix ?")
            confirm = input("Entrez OUI pour confirmer sinon entrez n'importe"
                            " quoi pour revenir en arrière : ")
            if confirm == "OUI":
                self.show_substitute(prod_save)

            else:
                self.come_back()

        except ValueError:
            print("Vous n'avez pas entré un numéro. \n"
                  "Veuillez réesayer dans 3...2...1... ")
            time.sleep(3)
            self.show_products(cat_id)

    def show_substitute(self, product):

        sub_list = []
        self.db.cursor.execute(
              "SELECT product_name_fr, brands, nutriscore_grade, stores,\
                url, product_id \
                FROM product \
                WHERE nutriscore_grade<%(nutriscore_grade)s \
                AND category_id=%(category_id)s",
              {'nutriscore_grade': product[3], 'category_id': product[4]}
              )
        print("\n")
        for line in self.db.cursor.fetchall():
            print(
                    "Substitut potentiel à:", product[1], product[2], "\n",
                    "Nom du produit:", line[0], "\n",
                    "Marque:", line[1], "\n", "Nutriscore:", line[2], "\n",
                    "Magasins:", line[3], "\n", "Url:", line[4], "\n",
                    "identifiant produit:", line[5], "\n"
                    )
            sub_list.append(line)

            try:

                sub_exist = False
                while sub_exist is False:
                    sub_choice = int(input(
                        "\n Entrer le numéro (identifiant produit)"
                        " correspondant au produit"
                        " que vous voulez remplacer: "))
                    for sub in sub_list:
                        if sub_choice == sub[5]:
                            sub_exist = True
                            print("\n Vous avez sélectionné: \n\n",
                                  "Nom du produit:", sub[0], "\n",
                                  "Marque:", sub[1], "\n", "Nutriscore:",
                                  sub[2], "\n",
                                  "Magasins:", sub[3], "\n", "Url:",
                                  sub[4], "\n",
                                  "identifiant produit:", sub[5], "\n")
                            sub_save = sub
                    if sub_exist is False:
                        print("Le numéro entré n'est pas présent dans la liste"
                              " des produits")

                print("Confirmer vous ce choix ?")
                confirm = input("Entrez OUI pour confirmer sinon entrez"
                                " n'importe quoi pour revenir en arrière : ")
                if confirm == "OUI":
                    print(sub_save)
                    # self.show_substitute(sub_save)

                else:
                    self.show_substitute(product)

            except ValueError:
                print("Vous n'avez pas entré un numéro. \n"
                      "Veuillez réesayer dans 3...2...1... ")
                time.sleep(3)
                self.show_substitute(product)

    def come_back(self):
        """ This method switch to select product menu if user do wrong choice
         """

        print("Choix NON VALIDE, vous allez être redirigé vers la "
              "selection de produit dans 3...2...1...")
        time.sleep(3)
        self.show_categories()


if __name__ == '__main__':
    SelectProducts()
