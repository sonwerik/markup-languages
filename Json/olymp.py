import json
import os

with open("data/olymp.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

gods = data.get("gods", [])


def menu():
    while True:
        print("1. Mostrar llistat de déus grecs")
        print("2. Mostrar llistat de déus romans")
        print("3. Tradueix un nom")
        print("0. Sortir")

        opt = int(input("\n"))

        if opt == 1:
            list_greek_names()
        elif opt == 2:
            list_roman_names()
        elif opt == 3:
            translate()
        elif opt == 0:
            exit()


def clear():
    # Per a Windows
    if os.name == 'nt':
        os.system('cls')
    # Per a Unix/Linux/MacOS
    else:
        os.system('clear')


def list_greek_names():
    print(["gods", "romans"])


def list_roman_names():
    print(["gods", "romans"])


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

menu()