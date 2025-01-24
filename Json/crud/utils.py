def simplify(data, name, data_filter):
    items = []
    for item in data[name]:
        item_dict = {}
        for key, value in item.items():
            if key in data_filter:
                item_dict[key] = value
        if item_dict:
            items.append(item_dict)
    new_data = {name: items}
    return new_data

def simplify2(data, name, data_filter):
    for item in data[name]:
        for key in list(item.keys()):
            if key not in data_filter:
                del item[key]
    return {name: data[name]}
