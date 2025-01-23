def ex3(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Even: {even}\nOdd: {odd}")


ex3([1,2,3,4,5,6,7,8,9,10])