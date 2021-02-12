""" This module will generate the display and record the choices of users """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from data_base.database import Database
import mysql.connector
import time


class SelectProducts:
    """ This class will display the products and the choices of users
        All the below methods are working in chain """

    def __init__(self):

        self.db = Database()
        self.select_categories()

    def select_categories(self):
        """ This method show the different categories and alow selection """

        self.db.connecting()
        self.db.cursor.execute("SELECT category_id, category_name \
            FROM category")
        cat_numbers = []
        for line in self.db.cursor.fetchall():
            cat_id = line[0]
            cat_name = line[1]
            cat_numbers.append(line[0])
            # create a list with the category number
            # to control if user choice exist
            print(cat_id, cat_name)

        try:
            print("\n veuillez choisir une catégorie de produit \n")
            cat_choice = int(input(
                "Entrer le chiffre correspondant à la catégéorie: \n"))
            if cat_choice in cat_numbers:
                self.select_products(cat_choice)
            else:
                self.come_back()

        except ValueError:
            self.come_back()

    def select_products(self, cat_id):
        """ This method show the different products and alow selection """

        self.db.cursor.execute(
            "SELECT product_id, product_name_fr, brands,\
            nutriscore_grade, category_id \
            FROM product \
            WHERE category_id=%(category_id)s", {'category_id': cat_id})
        # SELECT products only with the category_id that user chosed.

        product_list = []
        for line in (self.db.cursor.fetchall()):  # show the products
            print(line[0], " Nom du produit:", line[1], "\n",
                  "   Marque:", line[2], "\n", "   Nutriscore:", line[3], "\n",
                  "    Catégorie:", line[4], "\n")
            product_list.append(line)

        prod_exist = False
        # while loop below will run till user enter a valid product number:
        while prod_exist is False:
            try:
                prod_choice = int(input(
                    "\n Entrer le numéro correspondant au produit"
                    " que vous voulez remplacer: "))
                for product in product_list:
                    if prod_choice == product[0]:
                        print(
                            "\n Vous avez sélectionné: \n\n", product[0],
                            " Nom du produit:", product[1], "\n",
                            "   Marque:", product[2], "\n",
                            "   Nutriscore:", product[3], "\n",
                            "    Catégorie:", product[4], "\n"
                        )
                        prod_save = product
                        prod_exist = True
                if prod_exist is False:
                    print(
                        "Le numéro entré n'est pas présent dans la liste"
                        " des produits"
                            )
            except ValueError:
                print("Vous n'avez pas entré un numéro. \n Veuillez réesayer.")

        print("Confirmer vous ce choix ?")
        confirm = input("Entrez OUI pour confirmer sinon entrez n'importe"
                        " quoi pour revenir en arrière : ")
        if confirm == "OUI":
            self.select_substitute(prod_save)
        else:
            self.come_back()

    def select_substitute(self, product):
        """ This method show the different substitutes and alow selection """

        self.db.cursor.execute(
              "SELECT product_name_fr, brands, nutriscore_grade, stores,\
                url, product_id \
                FROM product \
                WHERE nutriscore_grade<%(nutriscore_grade)s \
                AND category_id=%(category_id)s",
              {'nutriscore_grade': product[3], 'category_id': product[4]}
              )
        # SELECT product only with higher nutriscore and same category ID than
        # the chosen product
        sub_list = []
        res = self.db.cursor.fetchall()
        if not res:  # there is no better similar product in database
            print(
                "\n Vous avez sélectionné un produit avec un bon nutriscore!\n"
                "Il n'y a pas de meilleurs produit pour l'instant. \n"
                "Veuillez choisir un nouveau produit"
            )
            time.sleep(2)
            input("\n Appuyer sur ENTER pour continuer \n")
            self.db.disconnecting()
            self.select_categories()

        else:
            for line in res:  # Show all the substitutes of chosen product
                print(
                        "Substitut potentiel à:", product[1], product[2], "\n",
                        "Nom du produit:", line[0], "\n",
                        "Marque:", line[1], "\n", "Nutriscore:", line[2], "\n",
                        "Magasins:", line[3], "\n", "Url:", line[4], "\n",
                        "identifiant produit:", line[5], "\n"
                        )
                sub_list.append(line)

            sub_exist = False
            # while loop below will run till user enter a valid substitute n°
            while sub_exist is False:
                try:
                    sub_choice = int(input(
                        "\n Entrer le numéro (identifiant produit)"
                        " correspondant au produit"
                        " que vous voulez remplacer: "))
                    for sub in sub_list:
                        if sub_choice == sub[5]:
                            print(
                                    "\n Vous avez sélectionné: \n\n",
                                    "Nom du produit:", sub[0], "\n",
                                    "Marque:", sub[1], "\n", "Nutriscore:",
                                    sub[2], "\n",
                                    "Magasins:", sub[3], "\n", "Url:",
                                    sub[4], "\n",
                                    "identifiant produit:", sub[5], "\n"
                                    )
                            sub_save = sub
                            sub_exist = True
                    if sub_exist is False:
                        print(
                                "Le numéro entré n'est pas présent dans la"
                                " liste des produits"
                                )
                except ValueError:
                    print(
                        "Vous n'avez pas entré un numéro. \n"
                        "Veuillez réesayer."
                    )

            print("Confirmer vous ce choix ?")
            confirm = input("Entrez OUI pour confirmer sinon entrez"
                            " n'importe quoi pour revenir en arrière : ")
            if confirm == "OUI":
                self.record_substitute(product[0], sub_save[5])

            else:
                self.select_substitute(product)

    def record_substitute(self, prod, sub):
        """ allow the user to record substitute in the data base """

        choice = input(
                        "Voulez vous enregistrer votre substitut ? \n"
                        "Entrez OUI pour confirmer sinon entrez"
                        " n'importe quoi pour passer: "
                        )
        try:
            if choice == "OUI":
                # product_id of original and substitute products get recorded
                # in database in table "substitution"
                query = """ INSERT INTO substitution (product_id, substitute_id)
                VALUES (%s, %s) """

                self.db.cursor.execute(query, (prod, sub))
                self.db.connect.commit()
                print(self.db.cursor.rowcount, "substitut inséré en BDD.")

            else:
                print("le substitut n'a pas été enregistré.")
        except mysql.connector.errors.IntegrityError:
            # if products_id are already in the table
            print("le substitut est déjà présent en base de donnée")

        one_more = input(
                        "Voulez vous rechercher un autre produit ? \n"
                        "Entrez OUI pour confirmer sinon entrez"
                        " n'importe quoi pour revenir au menu principal : "
                        )
        # if user want to check for another product or go back to main menu
        if one_more == "OUI":
            self.db.disconnecting()
            self.select_categories()

        else:
            self.db.disconnecting()
            pass

    def come_back(self):
        """ This method switch to select categories menu if user do wrong choice
         """

        print("Choix NON VALIDE, vous allez être redirigé vers la "
              "selection de produit.")
        time.sleep(2)
        input("\n Appuyer sur ENTER pour continuer \n")
        self.db.disconnecting()
        self.select_categories()
