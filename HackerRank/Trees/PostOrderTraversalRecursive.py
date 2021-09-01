def postOrder(root):
    
    if root is None:
        return
    
    postOrder(root.left)
    
    postOrder(root.right)
    
    
    print(root.info, end=' ')