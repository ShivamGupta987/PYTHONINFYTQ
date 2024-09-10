# define node
class Node:
    def __init__(self,value):
        # value left right
        self.val = value
        self.left = None
        self.right = None
        
root =Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print tree
def display(root):
    if root is None:
        return None 
    print(root.val)
    display(root.left)
    display(root.right)

display(root)

# sum of binary tree 

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

print(sum_of_nodes(root))

# max_value

def max_of_tree(root):
    if root is None:
        return float('-inf')
    return max(root.val, max_of_tree(root.left), max_of_tree(root.right))

print(max_of_tree(root))

# height of binary tree

def find_height(root):
    if root is None:
        return -1
    return 1 + max(find_height(root.left),find_height(root.right)) 
    
print(find_height(root))

# size of tree 

def size_of_tree(root):
    if root is None:
        return 0 
    return size_of_tree(root.left) + size_of_tree(root.right)+1 

print(size_of_tree(root))
