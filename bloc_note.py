    def get_categories_id_for_products(self):

        self.cursor.execute("SELECT category_id, category_name FROM category")
        for cat_key, value in self.cursor.fetchall():    
            api_request = Api()
            p = Products()
            results = api_request.get_data_from_category(value)
            for line in results["products"]:
                p.product_name_fr = line.get('product_name_fr')
                p.nutriscore_grade = line.get('nutriscore_grade')
                p.brands = line.get('brands')
                p.stores = line.get('stores')
                p.url = line.get('url')
                p.category_id = cat_key
                self.products_list.append(p)
                print(self.products_list)

.\data_base\product.py:10:1: E402 module level import not at top of file
.\data_base\product.py:10:1: F401 'data_base.api.Api' imported but unused
.\data_base\product.py:10:30: W291 trailing whitespace
.\data_base\product.py:12:1: E302 expected 2 blank lines, found 1
.\data_base\product.py:15:1: W293 blank line contains whitespace
.\data_base\product.py:23:1: E305 expected 2 blank lines after class or function definition, found 1
.\data_base\product.py:24:15: W292 no newline at end of file