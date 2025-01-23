def ex2(lst):
    max_num = lst[0]
    min_num = lst[0]

    for i in lst:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    print(f"Max num: {max_num}\nMin num: {min_num}")


ex2([12, 5, -3, 0, -7, 9, 2, 7, 10, 5])
