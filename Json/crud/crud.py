from database import read_db, save_db
from pathlib import Path

"""
fem servir la llibreria pathlib per definir el path, d'aquesta forma el programa corre a linux i windows
i es pot cridar des de qualsevol fitxer
"""
DATA_PATH = Path(__file__).parent / Path("data/products_simp.json")
# DATA_PATH = "data/products_simp.json"
DATA = read_db(DATA_PATH, "products")


def read() -> list:
    return list(DATA.values())


def read_item(item_id: int) -> dict:
    return DATA[item_id]


def create(item: dict):
    # assuming item has no id
    current_id = max(list(DATA.keys()))
    item["id"] = current_id
    DATA[current_id] = item
    save_db(DATA_PATH, DATA)


def update(item: dict):
    # assuming item has id
    item_id = item.get("id")
    if item_id in DATA:
        DATA[item_id].update(item)
        save_db(DATA_PATH, DATA)
    else:
        raise ValueError(f"Item with ID {item_id} not found.")


def delete(item_id: int):
    if item_id in DATA:
        del DATA[item_id]
        save_db(DATA_PATH, DATA)
    else:
        raise ValueError(f"Item with ID {item_id} not found.")


def count_categories(category: str) -> int:
    return sum(1 for item in DATA.values() if item["category"] == category)


# Promig de preus
def avg_price() -> float:
    prices = [item["price"] for item in DATA.values()]
    return sum(prices) / len(prices) if prices else 0


# Màxim stoc (simulat)
def max_price() -> tuple[int, float]:
    max_item = max(DATA.values(), key=lambda item: item["price"], default=None)
    return (max_item["id"], max_item["price"]) if max_item else (None, None)
