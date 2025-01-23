def ex4(lst):
    reversed_lst = []

    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])

    print(reversed_lst)

ex4([0,1,2,3,4,5,6,7,8,9])