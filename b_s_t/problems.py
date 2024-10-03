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


# 1038 bst to gst 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            nonlocal current_sum

            if not root:
                return
            
            if root.right:
                dfs(root.right)

            current_sum += root.val

            root.val = current_sum

            if root.left:
                dfs(root.left)

        current_sum=0
        dfs(root)
        return root 

# leetcode 108

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        middle =len(nums) // 2 
        root = TreeNode(nums[middle])
        left_side = nums[:middle]
        right_side = nums[middle+1 :]

        root.left = self.sortedArrayToBST(left_side)
        root.right = self.sortedArrayToBST(right_side)

        return root
# 1008 leetcode BST for preorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        index = 0

        def bst_helper(preorder,boundary):
            nonlocal index 
            # Using `nonlocal index` so that the inner function modifies the outer `index` variable.


            if index >= len(preorder) or preorder[index] > boundary:
                return None 

            n = TreeNode(preorder[index])

            index+=1 

            n.left = bst_helper(preorder,n.val)
            n.right = bst_helper(preorder,boundary)

            return n
        return bst_helper(preorder,float('inf'))
        


            
# 669 leetcode trimtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
         
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left,low,high)

        if root.val < low:
            return self.trimBST(root.right,low,high)

        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)

        return root 

        

        
# 114 leetcode flatten binarytree linkedlist


