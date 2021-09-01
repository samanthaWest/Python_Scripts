def height(root):
    if root is None:
        return 0 
    
    if(root.left is None and root.right is None):
         return max(height(root.left), height(root.right))
    else:
        return 1 + max(height(root.left), height(root.right))