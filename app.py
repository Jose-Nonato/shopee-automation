from core.shopee import get_products
from core.gemini import product_information
from core.telegram import send_message
import time

keyword = input("Informe o tipo de produto desejado: ")

response = get_products(keyword=keyword)
page_info = response["data"]["productOfferV2"]["pageInfo"]
products = response["data"]["productOfferV2"]["nodes"]

for product in products:
    time.sleep(10)
    product_info = product_information(product)
    print(product_info)
    status = send_message(message=product_info)
    print(status)
