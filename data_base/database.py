""" This module generate the local data base and provide connection """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from Config import config
import mysql.connector
import db_p5.sql


class Database
    """ This class generate the local data base and provide connection """

    def __init__(self):
        self.host = config.HOST
        self.user = config.USER
        self.password = config.PASSWORD
        self.database = config.DATABASE
        self.connected = connect()

    def connect(self):
        """Provide connection to MySQL Server"""

        mysql.connector.connect(host=self.host,
                                user=self.user,
                                password=self.password,
                                database=self.database)

    def unconnect(self):
        """Disconnect connection to MySQL Server"""

        self.connected.close()

    def database_gen(self):
        """Generate the database schema"""

        with open(db_p5, "r"):
            read_file = db_p5.read()
