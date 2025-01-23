def ex9(lst):
    square_lst = []
    lst.sort()
    for i in lst:
        i **= 2
        square_lst.append(i)

    print(square_lst)


ex9([2, 4, 6, 8])