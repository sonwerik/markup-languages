def ex6(text):
    word = ""
    for char in text:
        if char not in word:
            word += char

    print(word)


ex6(input())
