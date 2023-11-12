#1
def find_leaders(arr):
    n = len(arr)
    max_so_far = arr[n-1]
    leaders = [max_so_far]

    for i in range(n-2, -1, -1):
        if arr[i] >= max_so_far:
            max_so_far = arr[i]
            leaders.append(max_so_far)

    return leaders[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))




#2
def sort_and_alternate(arr):
    arr.sort()  
    n = len(arr)
    output = []

    i, j = 0, n-1
    while i <= j:
        if i == j:
            output.append(arr[i])
        else:
            output.append(arr[i])
            output.append(arr[j])
        i += 1
        j -= 1

    return output


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sort_and_alternate(arr))  
