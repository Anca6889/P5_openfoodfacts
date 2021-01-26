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