
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None 
        self.left = None






root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
# root.left.left.left = Node(8)
root.left.right = Node(5)
root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)

def dispaly(root):
    if root is None:
        return None
    else:
        print(root.val,end=" ")
        dispaly(root.left)
        dispaly(root.right)
dispaly(root) 

print('preorder')
def preorder(root):
    if root is None:
        return None
    
    print(root.val,end = " ")
    preorder(root.left)
    preorder(root.right)
preorder(root) 
    
print('inorder')
def inorder(root):
    if root is None:
        return None 
    
    inorder(root.left)
    print(root.val, end= " ")
    inorder(root.right)
inorder(root) 

print('postorder')

def postorder(root):
    if root is None:
        return None 
    
    postorder(root.left)
    postorder(root.right)
    print(root.val, end= " ")
    
postorder(root) 


