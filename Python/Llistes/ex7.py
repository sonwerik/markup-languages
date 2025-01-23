def ex5(lst):
    new_lst = []
    lst.sort()
    for i in lst:
        if i in new_lst:
            new_lst.append(i)

    print(new_lst)

ex5([4,2,2,5,7,6,6,8,4,1,2,2,4,1,3,])