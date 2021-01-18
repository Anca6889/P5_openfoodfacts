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

PARAMS_TOTAL = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "countries",
                    "tag_contains_0": "contains",
                    "tag_0": "france",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                "nutriscore_grade,url"
                    }

PARAMS_SPREAD = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "pates-a-tartiner",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                "nutriscore_grade,url"
                    }

PARAMS_DRINK = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "boissons",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                "nutriscore_grade,url"
                    }

PARAMS_SPICE = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "condiments",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                    "nutriscore_grade,url"
                    }

PARAMS_CAKE = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "biscuits-et-gateaux",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                    "nutriscore_grade,url"
                    }

PARAMS_PIZZA = {
                    "search_simple": 1,
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "pizzas",
                    "sort_by": "unique_scans_n",
                    "page_size": 100,
                    "json": 1,
                    "fields": "code,brands,product_name_fr,categories,stores,"
                                    "nutriscore_grade,url"
                    }
# Maximal number of product by categorie
P_MAX = 50

# Mysql server configuration:
HOST = "localhost"
USER = "root"
PASSWORD = "mu122238"
DATABASE = "db_p5"
