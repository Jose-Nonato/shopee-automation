from database import products


def fetch_products():
    products_db = products.find()
    return list(products_db)


def insert_product(products: list):
    for product in products:
        print(product)
