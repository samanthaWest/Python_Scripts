def sortedInsert(llist, data):
    current_node = llist
    new_node = DoublyLinkedListNode(data)

    if llist is None:
        llist = new_node
    elif llist.data == data or llist.data > data:
        llist.prev = new_node
        new_node.next = llist
        llist = new_node
    else:
        while current_node:
            if current_node.next is not None:
                if data >= current_node.data and data < current_node.next.data:
                    next_node = current_node.next
                    
                    new_node.prev = current_node
                    new_node.next = next_node
                    
                    current_node.next = new_node
                    next_node.prev = new_node
                    break
            else:
                current_node.next = new_node
                break
                
            current_node = current_node.next   
        
    return llist