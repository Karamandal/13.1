class Category:
    name = str
    description = str
    gods = str

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods


    def total_number_of_categories(self, categories):
        return len(categories)

    def total_number_of_goods(self):
        return len(self.goods)

class Product:
    name = str
    description = str
    price = float
    quantity_in_stock = int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock