def ex9(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in text:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                if j <= len(alphabet):
                    print(alphabet[(j + n) % len(alphabet)], end='')


ex9("vsfasg", int(input("Introdueix el nombre de desencriptació: ")))
