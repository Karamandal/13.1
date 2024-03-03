import json
from classes import Category, Product


def load_data_from_json():
    categories = []
    products = []

    with open('products.json', encoding='utf-8') as file:
        data = json.load(file)

    for category_data in data:
        category_name = category_data['name']
        category_description = category_data['description']
        category_products = []

        for product_data in category_data.get('products', []):
            product_name = product_data['name']
            product_description = product_data['description']
            product_price = product_data['price']
            product_quantity = product_data['quantity']

            product = Product(product_name, product_description, product_price, product_quantity)
            category_products.append(product)

        category = Category(category_name, category_description, category_products)
        categories.append(category)

    return categories, products


categories, _ = load_data_from_json()
for category in categories:
    print(f'{category.name}\n{category.description}')
    for product in category.products:
        print(f" - {product.name}: {product.price}")
