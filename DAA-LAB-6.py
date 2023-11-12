# Matrix Sorting and Diagonal Replacement
def sort_and_replace(matrix):
    n = len(matrix)
    flattened = []
    for row in matrix:
        for element in row:
            flattened.append(element)
    for i in range(n*n - 1):
        for j in range(n*n - i - 1):
            if flattened[j] > flattened[j+1]:
                flattened[j], flattened[j+1] = flattened[j+1], flattened[j]
    sorted_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(flattened[i*n + j])
        sorted_matrix.append(row)
    for i in range(n):
        sorted_matrix[i][i] = 0
        sorted_matrix[i][n-i-1] = 0

    return sorted_matrix

matrix = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
sorted_and_replaced_matrix = sort_and_replace(matrix)
print(sorted_and_replaced_matrix)

# Integer Multiplication without Operators
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    elif x < 0 and y < 0:
        x = -x
        y = -y
    elif x < 0 or y < 0:
        x = abs(x)
        y = abs(y)
        return -multiply(x, y)
    elif x == 1:
        return y
    elif y == 1:
        return x

    result = 0
    for i in range(y):
        result += x

    return result

x = 5
y = 3
product = multiply(x, y)
print(product) 

