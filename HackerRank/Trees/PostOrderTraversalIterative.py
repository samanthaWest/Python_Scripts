from collections import deque

def postOrder(root):
    
    stack = deque()
    stack.append(root)
    
    out = deque()
    
    while stack:
        
        curr = stack.pop()
        out.append(curr.info)
        
        if curr.left:
            stack.append(curr.left)
        
        if curr.right:
            stack.append(curr.right)
            
    
    while out:
        print(out.pop(), end= ' ')