def removeDuplicates(llist):
    prev = None
    head = llist
    uniq_set = []
    
    while head:
        print(head.data)
        if head.data not in uniq_set or uniq_set == []:
            uniq_set.append(head.data)
            prev = head
            head = head.next
        else:
            prev.next = head.next
            head = head.next
            
    return llist
    
        
