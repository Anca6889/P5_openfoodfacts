import sys
sys.path.append('C:/Users/guthj/OneDrive/Bureau/coding/P5_openfoodfacts')
# import sys = Problème perso d'import à dégager par la suite.

from data_base.database import Database


class Test:
    """ This is only a testing class """

    def __init__(self):
        
        self.db = Database()
        self.show()

    def show(self):
        
        self.db.connecting()
        self.db.cursor.execute("SELECT product_name_fr, product_brands, product_nutriscore_grade FROM product ")
        for product in self.db.cursor.fetchall():
            print(product)

if __name__ == '__main__':
    Test()
