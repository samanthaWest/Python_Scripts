def findMergeNode(head1, head2):
    while head1:
        node = head2
        while node:
            if head1 == node:
                return head1.data
            node = node.next
        head1 = head1.next