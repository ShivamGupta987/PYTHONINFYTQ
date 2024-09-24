
from collections import deque

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None 
        
    
    def createNode(value):
        return Node(value) 
    
    def insert(root,value):
        if root is None: 
            return Node.createNode(value)
        
        elif value < root.data:
            root.left = Node.insert(root.left,value) 
        else:
            root.right = Node.insert(root.right,value)
            
        return root 
    
    def preorder(root):
        if root is not None:
            print(root.data,end= " ")
            Node.preorder(root.left)
            Node.preorder(root.right)
    
    def inorder(root):
        if root is not None:
            # print(root.data,end= " ")
            Node.inorder(root.left)
            print(root.data,end= " ")
            
            Node.inorder(root.right)
            
    def postorder(root):
        if root is not None:
            # print(root.data,end= " ")
            Node.postorder(root.left)
            Node.postorder(root.right)
            print(root.data,end= " ")
            
    def level_order(root):
        
        if root is  None:
            return 
        queue = deque([root])
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                print(node.data,end= " ")
                
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
                    
            print(" ")
            
data = [5,3,2,7,8,6,4,1]

root = None 

for item in data:
    root = Node.insert(root, item)
    
Node.level_order(root)
            
    

# search elemnt in bst

def searchiteratibe(root,val):
    current = root
    while current is not None:
        if current.data == val:
            return True
        elif current.data > val:
            current = current.left 
        else:
            current = current.right
                        
        
    return False 

print(searchiteratibe(root,9))
print(searchiteratibe(root,4))
print(searchiteratibe(root,8))



    
            
        
        