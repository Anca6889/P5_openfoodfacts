""" This module will import data from the Openfoodfacts API """

#!/usr/bin/python3
# -*- coding: Utf-8 -*

from Config import config
import requests

class Api:

    """ This class will import data from the API and dispatch it into the local
    data base """

    def __init__(self):
        self.categories = config.CATEGORIES
        self.max_products = config.P_MAX

    def get_cat(self):

        categories = requests.get(
            "https://fr.openfoodfacts.org/categorie/{self.categories}.json")

        print(categories)

if __name__ == '__main__':
    print(config.CATEGORIES)
    
