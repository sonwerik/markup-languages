import json

from utils import simplify

with open("data/products.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)


def info(products_data):
    print(type(products_data))
    print(products_data)
    print(len(products_data["products"]))
    print(len(products_data["products"][0]))
    print(products_data.keys())

info(data)

data_simple = simplify(data, None, None)

info(data_simple)