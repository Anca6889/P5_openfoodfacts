""" This module will transform the products datas gotten from the API in a usable object """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from data_base.api import Api 

class Products:

    def __init__(self):
        
        self.data = []
        self.code = []
        self.categories = []
        self.brands = []
        self.product_name_fr = []
        self.nutriscore_grade = []
        self.stores = []
        self.url = []
        self.superlist = []
        self.superlistgen()
        

    def api_gen(self):
        api = Api()
        self.data = api.products

    def sort_out(self):
        for dicos in self.data:
            for key, val in dicos.items():
                if key == "code":
                    self.code.append(val)
                elif key == "categories":
                    self.categories.append(val)
                elif key == "brands":
                    self.brands.append(val)
                elif key == "product_name_fr":
                    self.product_name_fr.append(val)
                elif key == "nutriscore_grade":
                    self.nutriscore_grade.append(val)
                elif key == "stores":
                    self.stores.append(val)
                elif key == "url":
                    self.url.append(val)
        return self.code, self.categories,self.brands, self.product_name_fr, self.nutriscore_grade, self.stores, self.url

    def superlistgen(self):
        self.api_gen()
        self.sort_out()
        self.superlist = [self.code, self.categories,self.brands, self.product_name_fr, self.nutriscore_grade, self.stores, self.url]

if __name__ == '__main__':
    prod = Products()
    prod.sort_out()
    print(prod.superlist)
    