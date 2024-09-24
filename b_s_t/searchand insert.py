

def search(root, val):
   
    if root is None or root.val == val:
        return root


    if val > root.val:
        return search(root.right, val)


    return search(root.left, val)


def insert(root,key):
    if root is None:
        return root
    else:
        if root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)