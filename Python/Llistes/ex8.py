def ex8(lst):
    num_sum = 0
    lst.sort()
    for i in lst:
        if i > 0:
            num_sum += i

    print(num_sum)


ex8([4, 2, -2, -5, -7, -6, -6, -8, -4, 1, 2, -2, -4, -1, 3, ])
