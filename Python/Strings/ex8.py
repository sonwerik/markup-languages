def ex8(sentence):
    count = 1

    for char in sentence:
        if char == ' ':
            count += 1

    print(count)

ex8(input())