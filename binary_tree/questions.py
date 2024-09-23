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

 

# leetcode 257
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def helper(node,path,paths):

            if not node:
                return
        
            path+=str(node.val)

            if not node.left and not node.right:
                return paths.append(path)
            else:
                path+="->"

                helper(node.left,path,paths)
                helper(node.right,path,paths)
        paths=[]
        helper(root,"",paths)
        return paths


# lweetcode 199 rightside view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result 
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size-1:
                    result.append(node.val)
        return result


          

# lweetcode 199 top view
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def top_view(root):
    if not root:
        return

    # Dictionary to store the top view nodes
    top_view_map = {}

    # Queue for level-order traversal (node, horizontal distance)
    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)

        # Check if this horizontal distance is being visited for the first time
        if hd not in top_view_map:
            top_view_map[hd] = node.data

        # Add the left and right children to the queue with updated HD
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Print the top view from leftmost to rightmost
    for hd in sorted(top_view_map):
        print(top_view_map[hd], end=" ")

# Example usage:
if __name__ == "__main__":
    # Constructing the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Top view of the binary tree is:")
    top_view(root)

# level order left to right 
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Level Order Traversal:")
level_order(root)


# level order right to left 
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")


        if node.right:
            queue.append(node.right)
        from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Level Order Traversal:")
level_order(root)


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Level Order Traversal:")
level_order(root)

# 236 leetcode lowestc ommon ancestors

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

     if root is None:
        return None 
    
     if root == p or root == q:
        return root
     left = self.lowestCommonAncestor(root.left,p,q)
     right = self.lowestCommonAncestor(root.right,p,q)

     if left and right:
        return root
     else:
        return left or right
    
    
# 113 pathsum2
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, currentpath, currentsum):
            if not node:
                return

            currentpath.append(node.val)
            currentsum += node.val

            if node.left is None and node.right is None and currentsum == targetSum:
                result.append(list(currentpath))

            if node.left:
                dfs(node.left, currentpath, currentsum)
            if node.right:
                dfs(node.right, currentpath, currentsum)

            currentpath.pop()

        result = []
        dfs(root, [], 0)
        return result
    
    # paths sum 3 437
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum+=node.val
            if current_sum == targetSum:
                total_path = 1
            else:
                total_path = 0
            
            total_path+=dfs(node.left,current_sum)
            total_path+=dfs(node.right,current_sum)

            return total_path
        def count_paths(node):
            if not node:
                return 0
            total_paths = dfs(node,0)

            total_paths += count_paths(node.left)
            total_paths += count_paths(node.right)
            return total_paths
        
        return count_paths(root)
    
    # optimal solutiom
    
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        if not root:
            return 0
        def dfs(node,current_sum):
            nonlocal count 

            if not node:
                return 
            
            current_sum += node.val 

            if current_sum == targetSum:
                count+=1
            
            count += prefix_sum[current_sum - targetSum]
            
            prefix_sum[current_sum]+=1

            dfs(node.left,current_sum)
            dfs(node.right,current_sum)

            prefix_sum[current_sum] -=1 

        count = 0 
        prefix_sum = defaultdict(int)
        dfs(root,0)
        return count       
