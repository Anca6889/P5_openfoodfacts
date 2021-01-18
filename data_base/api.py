""" This module will import data from the Openfoodfacts API """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config import config
import requests
import json


class Api:

    """ This class will import data from the API and dispatch it into the local
    data base """

    def __init__(self):
        pass

    def get_cat():
        
        categories = requests.get(config.URL, params= config.PARAMS_PIZZA)

        results = categories.json()
        print(results)
        print(categories.url)

if __name__ == '__main__':
    print(config.CATEGORIES)
    Api()
    print(Api.get_cat())
