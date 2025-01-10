import json

from utils import simplify

with open("data/products.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)


def info(data):
    print(type(data))
    print(data)
    print(len(data["products"]))
    print(len(data["products"][0]))
    print(data.keys())

info(data)

data_simple = simplify(data, None, None)

info(data_simple)