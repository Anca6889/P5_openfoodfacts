""" This module contains all the constants of the program """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# selected categories for the local data base
URL = "https://fr.openfoodfacts.org/cgi/search.pl"

CATEGORIES = [
                "pates-a-tartiner",
                "petit-dejeuners",
                "sodas",
                "snacks",
                "snacks-sucres",
                "charcuteries",
                "fromages",
                "condiments",
                "surgeles",
                "pizzas"
                ]

MAIN_MENU = {
                1: "Quel aliment souhaitez-vous remplacer ?",
                2: "Retrouver mes aliments substitués",
                3: "Réinitialiser la base de données",
                4: "Quitter le programme"
                }
# Number of categories
CAT_NUMBER = len(CATEGORIES)
# Maximal number of product by categorie
PAGE_SIZE = 100

# Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = "mu122238"
DATABASE = "db_p5"

# All texts / messages of the app (IN FRENCH)
