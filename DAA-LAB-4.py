# Diagonal Interchange
def diagonal_interchange(matrix):
    n = len(matrix)

    matrix[0][0], matrix[0][n-1] = matrix[0][n-1], matrix[0][0]
    matrix[n-1][0], matrix[n-1][n-1] = matrix[n-1][n-1], matrix[n-1][0]

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
interchanged_matrix = diagonal_interchange(matrix)
print(interchanged_matrix)

# Index Finder
def find_indices(arr, num):
    indices = []

    for i in range(len(arr)):
        if arr[i] == num:
            indices.append(i)

    return indices

arr = [1, 2, 3, 2, 4, 1, 5, 6, 3]
num = 2
indices = find_indices(arr, num)
print(indices)  
