def ex5(text):
    text = text.lower()

    if text == text[::-1]:
        print(True)
    else:
        print(False)


ex5(input())
