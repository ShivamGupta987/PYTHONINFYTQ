class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    # Insert function for a binary search tree
    def insert(self, root: 'TreeNode', key: int) -> 'TreeNode':
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        return root


    def preorderTraversal(self, root: 'TreeNode') -> None:
        if root:
            print(root.val, end=" ")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

# Initialize the tree root as None
root = None
# List of keys to insert into the BST
keys = [50, 30, 20, 40, 70, 60, 80]

tree = TreeNode()

for key in keys:
    root = tree.insert(root, key)


print("Preorder traversal of the constructed BST:")
tree.preorderTraversal(root)
