def ex8(word):
    vowels = set("aeiou")
    consonants = set("bdcfghjklmnpqrstvwxyz")
    special = {'x'}

    value = 0

    for char in word.lower():
        if char in vowels:
            value += 3
        elif char == special:
            value += 10
        elif char in consonants:
            value += 1

    print(value)


ex8("miau")
