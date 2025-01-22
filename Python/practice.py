title_list = []

for i in range(10):
    title_list.append(f"Title {i}"
        "Title: " + str(i))

title_list = [f"Title {i}" for i in range(10)]

my_object = {f"Key {i}": title for i, title in enumerate(title_list)}
print(my_object)