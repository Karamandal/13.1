from abc import ABC, abstractmethod


class Category:
    total_categories = 0
    total_products = set()

    def __init__(self, name, description, products):
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
        if isinstance(product_data, Product) or issubclass(type(product_data), Product):
            self.__products.append(product_data)
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    @property
    def get_total_products(self):
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.")
        return products_list

    def __len__(self):
        return sum(product.quantity_in_stock for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."


class ProductBase(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def create_new_product(self, product_data):
        pass

    @abstractmethod
    def price(self):
        pass


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        repr(self)

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"


class Product(CreationInfoMixin, ProductBase):
    def __init__(self, name, description, price, quantity_in_stock):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    @classmethod
    def create_new_product(cls, product_data):
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        if isinstance(other, Product):
            total_price = (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
            return total_price
        else:
            raise TypeError("Можно складывать только объекты класса Product или его наследников")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity_in_stock, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity_in_stock, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
