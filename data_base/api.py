""" This module will import data from the Openfoodfacts API """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import CATEGORIES, P_MAX, URL
import requests
import json

class Api:

    """ This class will import data from the API and dispatch it into the local
    data base """

    def __init__(self):
        
        self.payload = {
                        "search_simple": 1,
                        "action": "process",
                        "tagtype_0": "categories",
                        "tag_contains_0": "contains",
                        "tag_0": None,
                        "sort_by": "unique_scans_n",
                        "page_size": P_MAX,
                        "json": 1,
                        "fields": "code,brands,product_name_fr,categories,stores,nutriscore_grade,url"
                        }
        self.products = []
        self.get_all_categories_datas()
        

    def set_payload_from_category(self, category):
        self.payload["tag_0"] = category
        return self.payload

    def get_data_from_category(self, category):
        
        try:
            data = requests.get(URL, params= self.set_payload_from_category(category))
            results = data.json()
            return results
        
        except ValueError as err:
            print("Error: {}".format(err))
            

    def get_all_categories_datas(self):

        for category in CATEGORIES:
            category = self.get_data_from_category(category)
            for products in category["products"]:
                self.products.append(products)
                

if __name__ == '__main__':
    data = Api()
    for product in data.products:
        print(product, '\n')
    
    
    
