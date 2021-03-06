""" This module will import data from the Openfoodfacts API """

# !/usr/bin/python3
# -*- coding: Utf-8 -*

import requests
from Config.config import PAGE_SIZE, URL, FIELDS


class Api:
    """ This class will import data from the API and dispatch it into the
        local data base """

    def __init__(self):

        self.payload = {
            "search_simple": 1,
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": None,
            "sort_by": "unique_scans_n",
            "page_size": PAGE_SIZE,
            "json": 1,
            "fields": FIELDS
        }
        self.products = []

    def set_payload_from_category(self, category):
        """ This method will turn the "tag_0" value in the payload to the
            name of a categorie """

        self.payload["tag_0"] = category
        # categories are available and settable in the config file.
        return self.payload

    def get_data_from_category(self, category):
        """ This method will send one request for one category to the API """

        try:
            data = requests.get(
                URL, params=self.set_payload_from_category(category))
            results = data.json()
            return results

        except ValueError as err:
            print("Error: {}".format(err))
