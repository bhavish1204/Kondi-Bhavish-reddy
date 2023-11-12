#Binary Search Tree Node Search
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def search_node_by_value(root, value):
    if root is None or root.val == value:
        return root

    if root.val < value:
        return search_node_by_value(root.right, value)

    return search_node_by_value(root.left, value)

# Example usage
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

value_to_find = 4
result = search_node_by_value(root, value_to_find)
if result is not None:
    print(result.val)  
else:
    print("Node not found")
  



# Leaf Node Sum in a Tree
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def leaf_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    return leaf_sum(root.left) + leaf_sum(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

result = leaf_sum(root)
print(result)  



# Spinal (Zig-Zag) Order Tree Traversal
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def zigzag_traversal(root):
    if root is None:
        return []

    result = []
    level = 0
    queue = [root]

    while queue:
        level_size = len(queue)
        level_nodes = []

        for i in range(level_size):
            curr_node = queue.pop(0)
            level_nodes.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

        if level % 2 == 1:
            level_nodes.reverse()

        result.extend(level_nodes)
        level += 1

    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

result = zigzag_traversal(root)
print(result)  

