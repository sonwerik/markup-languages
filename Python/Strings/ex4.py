def ex4(text):
    vowels = set('aeiou')
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    print(count)


ex4(input())