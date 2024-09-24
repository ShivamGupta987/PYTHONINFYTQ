# leetcode 700 search in tree 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return None
        if root.val == val:
            return root
        if root.val >= val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)    
        
        
        
# leetcode 701 insert in bst tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new_node = TreeNode(val=val)

        if root is None:
             root = new_node
             return root


        current = root 

        while True:

            if val< current.val:
                if current.left is None:
                    current.left = new_node 
                    return root
                current = current.left 
            else:
                    if current.right is None:
                        current.right = new_node 
                        return root 
                    current = current.right 
                       


#  ### 235 - lca of bst in leetcode

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            if root is None:
                return root
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left,p,q)
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right,p,q)
            
            return root
    
    
# leetcode-98 valid BST  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node,low,high):
            if not node:
                return True
                 
            if not ( low< node.val < high):
                return False

            return (validate(node.left , low , node.val ) and validate(node.right , node.val , high)) 
        return validate(root,low = float('-inf'), high = float('inf'))

