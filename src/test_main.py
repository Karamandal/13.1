import pytest
from classes import Category, Product


@pytest.fixture
def simple_data():
    product1 = Product("Laptop", "High-performance laptop", 1500, 10)
    product2 = Product("Smartphone", "Latest smartphone model", 800, 20)
    category1 = Category("Electronics", "Category for electronic devices", [product1, product2])

    product3 = Product("Headphones", "Wireless", 200, 15)
    product4 = Product("Tablet", "Portable tablet device", 600, 12)
    category2 = Category("Gadgets", "Category for cool gadgets", [product3, product4])

    product5 = Product("TV", "Smart TV with 4K resolution", 1200, 8)
    product6 = Product("Camera", "Professional DSLR camera", 1000, 5)
    category3 = Category("Electronics", "Category for electronic devices", [product5, product6])

    product7 = Product("Watch", "Smartwatch with fitness tracking", 300, 25)
    product8 = Product("Speaker", "Bluetooth speaker with surround sound", 150, 30)
    category4 = Category("Accessories", "Category for electronic accessories", [product7, product8])

    product9 = Product("Printer", "Wireless color printer", 400, 7)
    product10 = Product("Router", "High-speed WiFi router", 80, 18)
    category5 = Category("Office Equipment", "Category for office devices", [product9, product10])

    return [category1, category2, category3, category4, category5]


def test_total_number_of_categories(simple_data):
    assert Category.total_categories == 5


def test_total_number_of_products(simple_data):
    assert len(Category.total_products) == 10


def test_category_initialization():
    category = Category("Electronics", "Category for electronic devices", [])
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"


def test_product_initialization():
    product = Product("Laptop", "High-performance laptop", 999.99, 10)
    assert product.name == "Laptop"
    assert product.description == "High-performance laptop"
    assert product.price == 999.99
    assert product.quantity_in_stock == 10
