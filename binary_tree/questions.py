# prints elemenets on nth level 
 
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None 
        self.left = None

def print_nth_level(root,n):
    if root is None:
        return 
    level = 0 
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        if level == n:
            for i in range(level_size):
                node = queue.popleft()
                print(node.val, end= " ")
                
            return
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        level+=1
        
    print('level not found') 
    
    
root =Node(1) 
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_nth_level(root,n=1)


# leetcode 226 invert binary trr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
# leetcode 100 same tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True 

        if not p or not q:
            return False 
        if p.val != q.val:
            return False 

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# leetcode 543 diameter of binary tree

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)

            right = depth(node.right)
            self.diameter = max(self.diameter,right+left)
            return max(left,right) + 1 

        depth(root)
        return self.diameter

 

