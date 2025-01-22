def ex2(text):
    upper_case = 0
    lower_case = 0
    other = 0

    for char in text:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        else:
            other += 1

    print(f"Capital letters: {upper_case}\nLower case: {lower_case}\nOther: {other}")


ex2(input("Enter a sentence: "))
