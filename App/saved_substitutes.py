""" This module will generate the display of the recorded substitutes """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

from data_base.database import Database


class ShowSavedSub:
    """ This class will show the saved substitutes """

    def __init__(self):

        self.db = Database()
        self.get_data_sub()

    def get_data_sub(self):

        self.db.connecting()

        query = """ SELECT product.product_id, substitution.product_id,
        substitution.substitute_id
        FROM product
        INNER JOIN substitution
        ON product.product_id = substitution.substitute_id """

        self.db.cursor.execute(query)
        res = self.db.cursor.fetchall()
        for line in res:
            prod = line[1]
            sub = line[2]
            self.print_sub(prod, sub)

    def print_sub(self, prod, sub):

        self.db.cursor.execute(
            "SELECT product_id, product_name_fr, brands, \
            nutriscore_grade, stores, url \
            FROM product \
            WHERE product_id=%(product_id)s", {'product_id': prod})

        prod_list = []
        res_prod = self.db.cursor.fetchall()
        for line in res_prod:
            prod_list.append(line)

        self.db.cursor.execute(
            "SELECT product_id, product_name_fr, brands, \
            nutriscore_grade, stores, url \
            FROM product \
            WHERE product_id=%(product_id)s", {'product_id': sub})

        sub_list = []
        res_sub = self.db.cursor.fetchall()
        for line in res_sub:
            sub_list.append(line)

        for prod in prod_list:
            for sub in sub_list:
                print(
                    "                  ORIGINE          VS         SUBSTITUT\n"
                    "_______________________________________________________\n"
                    "numéro ID:      ", prod[0], "      VS      ", sub[0], "\n"
                    "nom produit:    ", prod[1], "      VS      ", sub[1], "\n"
                    "marque:         ", prod[2], "      VS      ", sub[2], "\n"
                    "nutriscore:     ", prod[3], "      VS      ", sub[3], "\n"
                    "magasin(s):     ", prod[4], "      VS      ", sub[4], "\n"
                    "URL:            ", prod[5], "      VS      ", sub[5], "\n"
                    "_______________________________________________________\n"
                )


if __name__ == '__main__':
    ShowSavedSub()
