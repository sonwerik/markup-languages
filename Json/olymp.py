import json
import os

with open("data/olymp.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

gods = data.get("gods", [])


def menu():
    while True:
        print("\n--- TRADUCTOR OLÍMPIC ---")
        list_greek_names()
        list_roman_names()
        translate()

def clear():
    # Per a Windows
    if os.name == 'nt':
        os.system('cls')
    # Per a Unix/Linux/MacOS
    else:
        os.system('clear')


def list_greek_names():
    print("\nLlista dels déus grecs:")
    count = 0
    for i in gods:
        print(i["greek"], end=", " if count < 9 else "")
        count += 1
        if count == 9:
            print()
            count = 0
    print()


def list_roman_names():
    print("\nLlista dels déus romans:")
    count = 0
    for i in gods:
        print(i["roman"], end=", " if count < 9 else "")
        count += 1
        if count == 9:
            print()
            count = 0
    print()


def translate():
    while True:

        god = input("\nQuin nom vols traduir? ")

        found = False
        for i in gods:
            if god.lower() == i.get("greek", "").lower():
                print(i["greek"] + " en romà és " + i["roman"])
                found = True
                break
            elif god.lower() == i.get("roman", "").lower():
                print(god + " en romà és " + i["greek"])
                found = True
                break

        if not found:
            print("Déu no trobat.")

        input("\nPrem enter per cercar un altre déu...")
        clear()


menu()
