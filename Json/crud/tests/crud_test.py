from crud import read, read_item, create, delete, update, DATA

# print(DATA)
# print(type(DATA))
print(read())
print(read_item(3))
print(f"len: {len(DATA)}")

item1 = {
    "title": "new",
    "category": "new",
    "price": 43.49
}

# create(item1)
# delete(31)

item2 = {
    "id": 33,
    "title": "update",
    "category": "update",
    "price": 43.49
}

# update(item2)
# print(f"len: {len(DATA)}")


# delete(31)
# delete(32)
# delete(33)

print(DATA)
print(len(DATA))