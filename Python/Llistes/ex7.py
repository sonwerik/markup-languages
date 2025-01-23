def ex7(lst):
    new_lst = []
    lst.sort()
    for i in lst:
        if lst.count(i) > 1 and i not in new_lst:
            new_lst.append(i)

    print(new_lst)


ex7([4, 2, 2, 5, 7, 6, 6, 8, 4, 1, 2, 2, 4, 1, 3, ])
