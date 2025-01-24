import json

def read_db(file_path, field) -> dict:
    print(file_path)
    with open(file_path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    items_dict = {item["id"] : item for item in data[field]}
    return items_dict


def save_db(file_path, data):
    data = {"products": list(data.values())}
    with open(file_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
