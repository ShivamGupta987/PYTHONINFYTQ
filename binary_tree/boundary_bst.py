class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_boundary(root, boundary):
    if root is None:
        return
    if root.left:
        boundary.append(root.data)  
        left_boundary(root.left, boundary) 
    elif root.right:
        boundary.append(root.data)  
        left_boundary(root.right, boundary) 

def right_boundary(root, boundary):
    if root is None:
        return
    if root.right:
        right_boundary(root.right, boundary)  
        boundary.append(root.data) 
    elif root.left:
        right_boundary(root.left, boundary)
        boundary.append(root.data) 

def leaves(root, boundary):
    if root is None:
        return
    leaves(root.left, boundary)
    # Only add leaf nodes
    if root.left is None and root.right is None:
        boundary.append(root.data)
    leaves(root.right, boundary)

def boundary_traversal(root):
    if root is None:
        return []

    boundary = [root.data]  


    left_boundary(root.left, boundary)

    leaves(root.left, boundary)
    leaves(root.right, boundary)

    right_boundary(root.right, boundary)

    return boundary


if __name__ == "__main__":
 
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    print("Boundary Traversal of the binary tree is:")
    print(boundary_traversal(root))
