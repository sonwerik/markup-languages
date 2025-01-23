def ex5(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    print(new_lst)

ex5([4,2,2,4,1,2,2,4,1,3,])