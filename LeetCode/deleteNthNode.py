# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev_node = None
        current_node = head
        nodesLen = 0
        idx = 0
        
        # Get Length of Node List
        while current_node is not None:
            nodesLen += 1
            current_node = current_node.next
            
        
        current_node = head
        
        while current_node is not None:

            if (nodesLen - n) == idx or (nodesLen - n) == 0:
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    if current_node.next is not None:
                        head = current_node = current_node.next
                    else:
                        head = current_node = None
                break
            
            # Increment(s)
            prev_node = current_node
            current_node = current_node.next
            idx += 1
        
        return head

# Alternative Efficient Technique
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Do it in one pass, faster way w/ slow and fast pointer
        # Use dummy node as a start to slow and fast pointer, start at -1
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        n = n + 1
        
        # breakout condition fast next is not null meaning end of the list
        while fast.next is not None:
            print("move fast")
            fast = fast.next
            
            # Decrement n till its at 0
            if (n != 0):
                n = n - 1
            
            # Don't start slow point until n is at 0
            # meaning the spaces between slow node and fast node will equal the nth node
            # after further traversal
            if (n == 0):
                print("move slow")
                slow = slow.next
        
        # Assign the new next to nexts, next node
        slow.next = slow.next.next
        return dummy.next
        
