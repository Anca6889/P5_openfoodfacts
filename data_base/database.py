""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import HOST, USER, PASSWORD, DATABASE, CATEGORIES
from data_base.api import Api 
import mysql.connector
import json


class Database:
    """ This class generate the local data base and provide connection """

    def __init__(self):
        
        self.connect = None
        self.cursor = None
        self.connecting()
        

    def connecting(self):
        """Provide connection to MySQL Server"""

        self.connect = mysql.connector.connect(
                                                host=HOST,
                                                user=USER,
                                                password=PASSWORD,
                                                database=DATABASE
                                                )
        self.cursor = self.connect.cursor()
        return self.connect, self.cursor

    def disconnecting(self):
        """Disconnect connection to MySQL Server"""

        self.connect.close()
        self.cursor.close()
        print("Déconnexion...")

    def database_gen(self):
        """Generate the database schema"""

        try:
            with open("data_base/db_p5.sql", "r") as db_script:
                file = db_script.read()
                sql = file.split(";")
                for instructions in sql:
                    self.cursor.execute(instructions)
                    self.connect.commit()
                    print(instructions)

        except mysql.connector.errors.ProgrammingError as error:
            print("Erreur lors de la création de la DBB:", error)
        
        finally:
            if self.connect:
                self.disconnecting()

    def insert_category(self, cat_name):
        self.connecting()
        query = "INSERT INTO category (name) VALUES ('%s')" % cat_name
        self.cursor.execute(query)
        self.connect.commit()

    def insert_categories(self, categories):
        for category in categories:
            self.insert_category(category)


    def insert_product(self, product): # on considère un objet product passé en argument
        self.connecting()
        query = f"INSERT INTO product (code, categories, brands, product_name_f nutriscore_grade, stores, url)" f"VALUES ({product.code}, {product.categories}, {product.brands}, {product.product_name_f}, {product.nutriscore_grade}, {product.stores}, {product.url});"
        self.cursor.execute(query)
        self.connect.commit()

if __name__ == '__main__':
    db = Database()
    api = Api()
    db.database_gen()
    db.insert_categories(CATEGORIES)
    db.insert_product(api.products)
    
    