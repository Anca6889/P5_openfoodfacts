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
        self.get_data()
        self.results = []

    def get_data(self):
        
        data_pizza = requests.get(config.URL, params= config.PARAMS_PIZZA)

        self.results = data_pizza.json()
        print(self.results)
        print(data_pizza.url)

if __name__ == '__main__':
    Api()
    
