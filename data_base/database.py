""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from data_base.api import Api
import time
import mysql.connector
from data_base.product import Product
from Config.config import HOST, USER, PASSWORD, DATABASE, CATEGORIES, \
    PAGE_SIZE, CAT_NUMBER


class Database:
    """ This class generate the local data base and provide connection """

    def __init__(self):

        self.connect = None
        self.cursor = None
        self.products_list = []

    def connecting(self):
        """Provide connection to MySQL Server"""

        self.connect = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        self.cursor = self.connect.cursor()

    def disconnecting(self):
        """Disconnect connection to MySQL Server"""

        self.connect.close()
        self.cursor.close()

    def schema_gen(self):
        """Generate the database schema"""

        try:
            with open("data_base/db_p5.sql", "r") as db_script:
                file = db_script.read()  # read the data base script
                # split all the instructions of the script
                sql = file.split(";")
                for instructions in sql:
                    # execute each instruction
                    self.cursor.execute(instructions)
                    self.connect.commit()

        except mysql.connector.errors.ProgrammingError as error:
            print("Erreur lors de la création de la DBB:", error)

    def insert_category(self, cat_name):
        """Insert one category from config file"""

        query = "INSERT INTO category (category_name) VALUES ('%s')" % cat_name

        try:
            self.cursor.execute(query)
            self.connect.commit()

        except ValueError as err:
            print("Error: {}".format(err))

    def insert_categories(self, categories):
        """" Insert all categories from config file """

        for category in categories:
            self.insert_category(category)

    def download_products(self):
        """ this method will download all the products from the API """

        self.cursor.execute("SELECT category_id, category_name FROM category")
        # catch the contain of the table category in the data base.

        for cat_key, value in self.cursor.fetchall():
            api_request = Api()
            p = Product()
            # we use the categories names (value) to request the API.
            results = api_request.get_data_from_category(value)
            for line in results["products"]:
                try:
                    save = True

                    if line.get('product_name_fr') is None:
                        save = False
                    else:
                        p.product_name_fr = line.get('product_name_fr')

                    if line.get('nutriscore_grade') is None:
                        save = False
                    else:
                        p.nutriscore_grade = line.get('nutriscore_grade')

                    if line.get('brands') is None:
                        save = False
                    else:
                        p.brands = line.get('brands')

                    if line.get('stores') is None:
                        save = False
                    else:
                        p.stores = line.get('stores')

                    if line.get('url') is None:
                        save = False
                    else:
                        p.url = line.get('url')
                    #  all the below chain of "if" and "else" remove the
                    #  products with empty fields.
                    p.category_id = cat_key  # catch the category id number.

                    if save:
                        self.products_list.append(
                            {"product_name_fr": p.product_name_fr,
                                "nutriscore_grade": p.nutriscore_grade,
                                "brands": p.brands,
                                "stores": p.stores,
                                "url": p.url,
                                "category_id": p.category_id
                             })
                        # create a list of dictionaries of all the productsks
                except TypeError as err:
                    print("Error: {}".format(err))

    def insert_product(self, product):
        """" Insert one product from API """

        query = """ INSERT INTO product (product_name_fr,
        nutriscore_grade, brands, stores, url, category_id)
        VALUES (%(product_name_fr)s, %(nutriscore_grade)s, %(brands)s,
        %(stores)s, %(url)s, %(category_id)s) """

        try:
            self.cursor.execute(query, product)
            self.connect.commit()

        except KeyError as err:
            print("Error: une ou plusieures clés sont inexistentes"
                  "sur un produit: {}".format(err))

    def insert_products(self, products):
        """ Insert all products from API"""

        for product in products:
            self.insert_product(product)

    def all_gen(self):
        """ Run all the necessary methods to generate local data base and
            download all the products
            This method is also use for RESET the data base """

        self.connecting()
        print("connexion au serveur MYSQL...")
        time.sleep(1)
        print("connexion établie")
        print("Création de la base de donnée...")
        self.schema_gen()
        print("Création des catégories de produits...")
        self.insert_categories(CATEGORIES)
        print("Envoi de la requête à Openfoodfacts...")
        print("Import de", CAT_NUMBER * PAGE_SIZE,
              "produits en base de données")
        time.sleep(1)
        self.download_products()
        self.insert_products(self.products_list)
        print("Import réussi avec succès !")
        self.disconnecting()
        print("Déconnexion du serveur MYSQL...")
        time.sleep(1)
        print("Déconnecté")
