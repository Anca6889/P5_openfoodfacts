from data_base.database import Database
import mysql.connector

class Test:

    def __init__(self):
        
        self.db = Database()
        self.main_menu()

    def main_menu(self):

        self.db.connecting()
        self.db.cursor.execute("SELECT id, name FROM category")
        for ligne in self.db.cursor.fetchall():
            print(ligne)

if __name__ == '__main__':
    Test()