""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

# import sys = Problème perso d'import à dégager par la suite.
import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')

from Config import config
import mysql.connector


class Database:
    """ This class generate the local data base and provide connection """

    def __init__(self):
        self.host = config.HOST
        self.user = config.USER
        self.password = config.PASSWORD
        self.database = config.DATABASE

    def connect(self):
        """Provide connection to MySQL Server"""

        self.connect = mysql.connector.connect(host=self.host,
                                user=self.user,
                                password=self.password,
                                database=self.database)

    def disconnect(self):
        """Disconnect connection to MySQL Server"""

        self.connect.close()

    def database_gen(self):
        """Generate the database schema"""

        self.connect()
        with open("data_base/db_p5.sql", "r") as db_script:
            read_file = db_script.read()
            print(read_file)
        

if __name__ == '__main__':
    db = Database()
    print(db.database_gen())