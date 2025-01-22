def ex6(words, word):
    count = 0

    for i in range(len(words)):
        if words[i] == word:
            count += 1
        if count == 2:
            print(i)
            break

    if count < 2:
        print(-1)


ex6(["Hermes", "Hestia", "Athena", "Hermes", "Zeus"], "Hermes")
