def simplify(data, field, data_filter):
    # simplified version of products
    # data[field]
    items = []
    for item in data["products"]:
        new_dict = {}
        for key, value in item.items():
            new_dict[key] = value
            if new_dict:
                items.append(new_dict)
    new_data = {field: items}
    return new_data
