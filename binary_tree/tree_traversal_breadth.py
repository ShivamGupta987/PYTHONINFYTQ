from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None 
        self.left = None


def level_order(root):
    if root is None:
        return 
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val,end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    
root =Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(4)

level_order(root)