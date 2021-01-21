""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import HOST, USER, PASSWORD, DATABASE, CATEGORIES, P_MAX
from data_base.api import Api 
from data_base.products import Products
import mysql.connector
import json
import time


class Database:
    """ This class generate the local data base and provide connection """

    def __init__(self):
        
        self.connect = None
        self.cursor = None
        self.all_gen()
        
    def connecting(self):
        """Provide connection to MySQL Server"""

        self.connect = mysql.connector.connect(
                                                host=HOST,
                                                user=USER,
                                                password=PASSWORD,
                                                database=DATABASE
                                                )
        self.cursor = self.connect.cursor()
        print("connexion au serveur MYSQL...")
        time.sleep(1)
        print("connexion établie")

    def disconnecting(self):
        """Disconnect connection to MySQL Server"""

        self.connect.close()
        self.cursor.close()
        print("Déconnexion du serveur MYSQL...")
        time.sleep(1)
        print("Déconnecté")

    def schema_gen(self):
        """Generate the database schema"""

        try:
            with open("data_base/db_p5.sql", "r") as db_script:
                file = db_script.read()
                sql = file.split(";")
                for instructions in sql:
                    self.cursor.execute(instructions)
                    self.connect.commit()

        except mysql.connector.errors.ProgrammingError as error:
            print("Erreur lors de la création de la DBB:", error)
        

    def insert_category(self, cat_name):
        
        query = "INSERT INTO category (name) VALUES ('%s')" % cat_name

        try:
            self.cursor.execute(query)
            self.connect.commit()
            
        except ValueError as err:
            print("Error: {}".format(err))


    def insert_categories(self, categories):
        for category in categories:
            self.insert_category(category)


    def insert_product(self, product): # on considère un objet product passé en argument
            
        query = "INSERT INTO product (code, categories, brands, product_name_fr, nutriscore_grade, stores, url) VALUES (%(code)s, %(categories)s, %(brands)s, %(product_name_fr)s, %(nutriscore_grade)s, %(stores)s, %(url)s)"
        
        try:
            self.cursor.execute(query, product)
            self.connect.commit()

        except KeyError as err:
            print("Error: une ou plusieures clés sont inexistentes sur un produit: {}".format(err))


    def insert_products(self, products):
        for product in products:
            self.insert_product(product)

    def all_gen(self):
        self.connecting()
        print("Création de la base de donnée...")
        self.schema_gen()
        print("Création des catégories de produits...")
        self.insert_categories(CATEGORIES)
        print("Envoi de la requête à Openfoodfacts...")
        api = Api()
        print("Import de", 5 * P_MAX, "produits en base de données locale")
        time.sleep(1)
        self.insert_products(api.products)
        self.disconnecting()

if __name__ == '__main__':
    Database()
