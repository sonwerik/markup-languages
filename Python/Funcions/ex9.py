def ex9(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in text:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                if j <= len(alphabet):
                    print(alphabet[j + 1], end='')


ex9("miau")
