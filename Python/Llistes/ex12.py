def ex12(lst):
    largest = larger = float('-inf')
    for n in lst:
        if n > largest:
            larger = largest
            largest = n
        elif n > larger and n != largest:
            larger = n

    print(f"First largest number: {largest}\nSecond larger number: {larger}")


ex12([1,2,3,4,5,6,7,8,9,10])