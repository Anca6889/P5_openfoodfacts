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

PARAMS = {"search_simple": 1,
           "action": "process",
           "tagtype_0": "countries",
           "tag_contains_0": "contains",
           "tag_0": "france",
           "tagtype_0": "categories",
           "tag_contains_0": "contains",
           "tag_0": "boissons",
           "page_size": 10,
           "json": 1,
           "fields": "brands,url,stores,nutriscore_grade,"
                     "categories,product_name_fr,code"
           }

# Maximal number of product by categorie
P_MAX = 50

# Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = "mu122238"
DATABASE = "db_p5"
