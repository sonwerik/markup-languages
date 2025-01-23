def ex10(lst, n):
    n = n % len(lst)
    print(lst[n:] + lst[:n])



ex10([2, 4, 6, 8], 2)