def solutionMatrix(matrix):
    countNegative = countNeg(matrix)

    if countNegative == 0:
        return matrix
    if countNegative % 2 == 0:
        to_replace = countNegative // 2
        replaced = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0 and replaced < to_replace:
                    matrix[i][j] = 0
                    replaced += 1
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    matrix[i][j] = countNegative

    return matrix

def countNeg(matrix):
    count = 0
    for row in matrix:
        for el in row:
            if el < 0:
                count += 1
    return count

def paintMatrix(matrix):
    for row in matrix:
        print(row)

def main():
    matrix1 = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30]
    ]

    matrix2 = [
        [1, -2, 3, -4, 5, 6],
        [-7, 8, 9, -10, 11, 12],
        [13, 14, -15, 16, 17, -18],
        [19, 20, 21, -22, 23, 24],
        [-25, 26, 27, 28, 29, 30]
    ]

    matrix3 = [
        [1, -2, 3, -4, 5, 6],
        [-7, 8, 9, -10, 11, 12],
        [13, 14, -15, 16, 17, -18],
        [19, 20, 21, 22, 23, 24],
        [-25, 26, 27, 28, 29, 30]
    ]

    print("Початкова матриця:")
    paintMatrix(matrix3)

    result = solutionMatrix(matrix3) 

    print("\nОброблена матриця:")
    paintMatrix(result)


main()
