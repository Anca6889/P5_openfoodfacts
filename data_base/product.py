""" This module will transform the products datas gotten from the API in a
usable object """

# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Products:
    """ this class create an usable object for insert the products in the
    database """

    def __init__(self):

        self.category_id = ""
        self.brands = ""
        self.product_name_fr = ""
        self.nutriscore_grade = ""
        self.stores = ""
        self.url = ""
        self.categories = ""
