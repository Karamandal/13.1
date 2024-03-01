from classes import Category
from classes import Product

def test_total_number_of_categories():
    categories = [Category("Category1", "Description1", []),
                  Category("Category2", "Description2", []),
                  Category("Category3", "Description3", [])]
    category = Category("Category4", "Description4", [])
    categories.append(category)
    assert category.total_number_of_categories(categories) == 4

def test_total_number_of_goods():
    goods = ["Good1", "Good2", "Good3"]
    category = Category("Category", "Description", goods)
    assert category.total_number_of_goods() == 3

"""Аналогично, в файле test_main.py можно написать тестовые функции для класса Product:"""


def test_quantity_in_stock():
    product = Product("Product", "Description", 10.99, 5)
    assert product.quantity_in_stock == 5

def test_total_number_of_products():
    products = [Product("Product1", "Description1", 9.99, 10),
                Product("Product2", "Description2", 19.99, 15),
                Product("Product3", "Description3", 14.99, 20)]
    assert len(products) == 3

