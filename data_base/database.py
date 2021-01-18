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
        self.connect = None
        self.cursor = None

    def connecting(self):
        """Provide connection to MySQL Server"""

        self.connect = mysql.connector.connect(host=self.host,
                                user=self.user,
                                password=self.password,
                                database=self.database)
        
        self.cursor = self.connect.cursor()
        return self.connect, self.cursor
        
    def disconnecting(self):
        """Disconnect connection to MySQL Server"""

        self.connect.close()
        self.cursor.close()

    def database_gen(self):
        """Generate the database schema"""

        self.connecting()

        try:
            with open("data_base/db_p5.sql", "r") as db_script:
                file = db_script.read()
                sql = file.split(";")
                for s in sql:
                    self.cursor.execute(s)
                    self.connect.commit()
                    print(s)

        except mysql.connector.errors.ProgrammingError as error:
            print("Erreur lors de la création de la DBB:", error)
        
        finally:
            if self.connect:
                self.disconnecting()
                print("Déconnexion...")

if __name__ == '__main__':
    db = Database()
    db.database_gen()