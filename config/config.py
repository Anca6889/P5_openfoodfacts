""" This module contains all the constants of the program """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# selected categories for the local data base
URL = "https://fr.openfoodfacts.org/cgi/search.pl"

CATEGORIES = [
                "pates-a-tartiner",
                "boissons",
                "condiments",
                "biscuits-et-gateaux",
                "pizzas"
                ]

MAIN_MENU = {
                1: "Trouvez un substitut à un produit",
                2: "Afficher les substituts enregistrés",
                3: "Réinitialiser la base de données",
                4: "Quitter le programme"
                }
# Number of categories
CAT_NUMBER = 5
# Maximal number of product by categorie
P_MAX = 25

# Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = "mu122238"
DATABASE = "db_p5"
