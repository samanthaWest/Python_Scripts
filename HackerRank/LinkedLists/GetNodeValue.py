def getNode(llist, positionFromTail):
    # Get Length of Node List
    # Get Data at that point from end in node lst
    
    node = llist
    length = 0
    
    while node:
        length += 1
        node = node.next
    
    node = llist
    for _ in range(length - positionFromTail - 1):
        print(node.data)
        node = node.next
        
    return node.data