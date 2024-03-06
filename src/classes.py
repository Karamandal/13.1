class Category:
    total_categories: int = 0
    total_products = set()

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        self.total_number_of_products(products)

    def total_number_of_categories(self) -> int:
        return Category.total_categories

    def total_number_of_products(self, products):
        for product in products:
            Category.total_products.add(product.name)

    def add_product(self, product_data):
        self.__products.append(product_data)

    @property
    def get_total_products(self):
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.")
        return products_list


class Product:
    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def create_new_product(cls, product_data):
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price_changer(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        elif new_price < self.__price:
            confirmation = input("Вы уверены, что хотите уменьшить цену? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = new_price
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price
