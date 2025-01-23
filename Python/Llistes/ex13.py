def ex13(x, y):
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(x * i + j + 1)
        matrix.append(row)

    print(matrix)


ex13(3, 3)
