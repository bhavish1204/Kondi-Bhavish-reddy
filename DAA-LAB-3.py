# Removing Duplicate Values:
def remove_duplicates(arr):
    n = len(arr)
    unique = []

    for i in range(n):
        if arr[i] not in unique:
            unique.append(arr[i])

    return unique

arr = [1, 2, 3, 2, 4, 1, 5, 6, 3]
print(remove_duplicates(arr))  

# Finding a Loop in a Linked List:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_loop(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next  

print(has_loop(head)) 

# Maximum Sum:
def max_sum(arr):
    n = len(arr)
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, n):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum(arr))  
