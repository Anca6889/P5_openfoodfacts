""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config.config import HOST, USER, PASSWORD, DATABASE, CATEGORIES, P_MAX, CAT_NUMBER
from data_base.api import Api 
from data_base.product import Products
import mysql.connector
import time


class Database:
    """ This class generate the local data base and provide connection """

    def __init__(self):
        
        self.connect = None
        self.cursor = None
        self.products_list = []
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
        """Insert one category from CONSTANT"""

        query = "INSERT INTO category (category_name) VALUES ('%s')" % cat_name

        try:
            self.cursor.execute(query)
            self.connect.commit()
            
        except ValueError as err:
            print("Error: {}".format(err))


    def insert_categories(self, categories):
        """" Insert all categories from CONSTANT """

        for category in categories:
            self.insert_category(category)

    def get_categories_id_for_products(self):

        self.cursor.execute("SELECT category_id, category_name FROM category")
        for cat_key, value in self.cursor.fetchall():    
            api_request = Api()
            p = Products()
            results = api_request.get_data_from_category(value)
            for line in results["products"]:
                save = True
                if line.get('product_name_fr') == None:
                    save = False
                else:
                    p.product_name_fr = line.get('product_name_fr')
                if line.get('nutriscore_grade') == None:
                    save = False
                else:
                    p.nutriscore_grade = line.get('nutriscore_grade')
                if line.get('brands') == None:
                    save = False
                else:
                    p.brands = line.get('brands')
                if line.get('stores') == None:
                    save = False
                else:
                    p.stores = line.get('stores')
                if line.get('url') == None:
                    save = False
                else:
                    p.url = line.get('url')

                p.category_id = cat_key
                if save:
                    self.products_list.append([p.product_name_fr, p.nutriscore_grade, p.brands, p.stores, p.url, p.category_id])
                    print(self.products_list) 

    def insert_product(self, product): 
        """" Insert one proudct from API """
            
        query = f"INSERT INTO product (product_name_fr,product_nutriscore_grade, product_brands, product_stores, product_url,category_id) VALUES ({product[0]}, {product[1]}, {product[2]}, {product[3]}, {product[4]}, {product[5]})"
        
        try:
            self.cursor.execute(query)
            self.connect.commit()

        except KeyError as err:
            print("Error: une ou plusieures clés sont inexistentes sur un produit: {}".format(err))


    def insert_products(self, products):
        """ Insert all products from API"""

        for product in products:
            self.insert_product(product)

    # def join_categories(self):
    #     """ Join the product table with the category table """

    #     query = ("SELECT category_id FROM category INNER JOIN Product ON Category.category_id = product.product_categories")

    #     try:
    #         self.cursor.execute(query)
    #         self.connect.commit()

    #     except TypeError as err:
    #         print("Error: {}".format(err))

    def all_gen(self):
        """ Run all the necessary methods to generate local data base"""

        self.connecting()
        print("Création de la base de donnée...")
        self.schema_gen()
        print("Création des catégories de produits...")
        self.insert_categories(CATEGORIES)
        print("Envoi de la requête à Openfoodfacts...")
        print("Import de", CAT_NUMBER * P_MAX, "produits en base de données locale")
        time.sleep(1)
        self.get_categories_id_for_products()
        self.insert_products(self.products_list)
        # self.join_categories()
        self.disconnecting()

if __name__ == '__main__':
    Database()
