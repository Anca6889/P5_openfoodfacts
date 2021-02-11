""" This module contains all the constants of the program """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# Link and fields for the payload of the API request
URL = "https://fr.openfoodfacts.org/cgi/search.pl"

FIELDS = "brands,product_name_fr,stores,nutriscore_grade,url"

# selected categories for the local data base
CATEGORIES = [
                "pates-a-tartiner",
                "petit-dejeuners",
                "sodas",
                "snacks",
                "aperitif",
                "produits-laitiers",
                "plats-prepares",
                "desserts",
                "complements-alimentaires",
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
DATABASE = "db_p5"  # (DO NOT CHANGE THIS PARAMETER)
