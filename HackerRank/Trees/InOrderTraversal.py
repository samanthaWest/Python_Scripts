def inOrder(root):
    if root: 
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)