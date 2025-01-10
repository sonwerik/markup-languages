import json
import os

with open("data/olymp.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

gods = data.get("gods", [])


def clear():
    # Per a Windows
    if os.name == 'nt':
        os.system('cls')
    # Per a Unix/Linux/MacOS
    else:
        os.system('clear')


def translate():
    while True:
        god = input("Quin nom vols traduir? ")

        found = False
        for i in gods:
            if god.lower() == i.get("greek", "").lower():
                print(i["roman"])
                found = True
                break
            elif god.lower() == i.get("roman", "").lower():
                print(i["greek"])
                found = True
                break

        if not found:
            print("Déu no trobat.")

        input("\nPrem enter per cercar un altre déu...")
        clear()


translate()
