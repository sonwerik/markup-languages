# Crear un arxiu JSON si no existeix
from pathlib import Path
import json


def ensure_json_exists(file_path, initial_data=None):
    if not Path(file_path).exists():
        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump(initial_data or {"products": []}, f, indent=4)


# Create
def create(item: dict):
    # Afegir ID automàtic
    current_id = max(DATA.keys(), default=0) + 1
    item["id"] = current_id
    DATA[current_id] = item
    save_db(DATA_PATH, DATA)


# Update
def update(item: dict):
    item_id = item.get("id")
    if item_id in DATA:
        DATA[item_id].update(item)
        save_db(DATA_PATH, DATA)
    else:
        raise ValueError(f"Item with ID {item_id} not found.")


# Delete
def delete(item_id: int):
    if item_id in DATA:
        del DATA[item_id]
        save_db(DATA_PATH, DATA)
    else:
        raise ValueError(f"Item with ID {item_id} not found.")


# Funcions personalitzades
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
