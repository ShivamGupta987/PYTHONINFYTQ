class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
    def preorder_iterative(root):
        
        result = []
        
        if root is None:
            return result
        
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result