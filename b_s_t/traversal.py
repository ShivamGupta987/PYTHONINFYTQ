class Node:
    def __init__(self,value):
        self.data= value
        self.left = None
        self.right = None 
        

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = new_node
                    return 
                current = current.left 

            else:
                if current.right is None:
                    current.right = new_node
                    return  
                current = current.right 
                
    def preorderTraversal(self,node):
        if node is None:
            return

        print(node.data,end = " ")
        
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
        
    def inorderTraversal(self,node):
        if node is None:
            return

        print(node.data,end = " ")
        
        self.inorderTraversal(node.left)
        self.inorderTraversal(node.right)
        
    def psotorderTraversal(self,node):
        if node is None:
            return


        
        self.psotorderTraversal(node.left)
        
        self.psotorderTraversal(node.right)
        
        print(node.data,end = " ")
    
            
        
    
            
    
    
data = [6,2,9,7,8,11,3,1]
bst = BST()

for item in data:
    bst.insert(item)
    
print('preorder')
bst.preorderTraversal(bst.root)
print('ineorder')
bst.inorderTraversal(bst.root)
print('postorder')
bst.psotorderTraversal(bst.root)

