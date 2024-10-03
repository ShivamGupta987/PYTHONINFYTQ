

class TreeNode:
    def __init__(self,value = 0,left = None, right= None):
        self.val = value
        self.right = right
        self.left = left 
        
    def findPreSuc(root,key):
        # return treenode pre and succesors.
        pre, suc = None , None
        
        
        if not root:
            return None,None 
        
        while root:
            if root.val == key:
                if root.left:
                    pre =root.left
                    while pre.right:
                        pre = pre.right 
                if root.right:
                    suc = root.right
                    while suc.left:
                        suc = suc.left
                        
                return pre,suc
                                   
            elif root.val > key:
                # move to left treekey
                suc = root
                root = root.left                          
            else:
                # move krrhe right subtree
                pre = root 
                root = root.right
                
        return pre , suc
    
    
        
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
key = 70
p,q = TreeNode.findPreSuc(root,key)
print('predecssor',p.val)
print('succesosr',q.val)


