#1
arr = [1, 4, 2, 3, 5, 6, 7]
target = 10

n = len(arr)
triplets = []

arr.sort()  

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]

        if current_sum == target:
            triplets.append((arr[i], arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(triplets)  


#2
def counting_sort(arr):
    n = len(arr)
    counts = [0] * (max(arr) + 1) 

    for i in range(n):
        counts[arr[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        sorted_arr[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    return sorted_arr

arr = [0, 0, 1, 2, 0, 1, 2, 2, 1]
print(counting_sort(arr)) 
