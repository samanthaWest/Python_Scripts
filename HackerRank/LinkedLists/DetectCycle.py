

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    
    if head is None:
        return 0
    else:
        
        current_node = head
        # prev_node = None
        seen_nodes = set()
        
        while current_node:
            
            # if current_node == prev_node or\
            #     prev_node == current_node.next:
            #     return 1
        
            if current_node in seen_nodes:
                return 1
            
            seen_nodes.add(current_node)
            # Next Set Of Nodes
            # prev_node = current_node
            current_node = current_node.next
    
    return 0