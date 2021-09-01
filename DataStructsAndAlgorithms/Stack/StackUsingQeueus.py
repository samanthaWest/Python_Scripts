# Push Operation Costly
# push - add x to q2, remove everything from q1 to q2
#           swap the names of q1 and q2
# pop - remove item from q1 and return it

from queue import Queue

class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self._curr_size = 0


    def push(self, x):
        self._curr_size += 1
        
        # Putting element at end of the queue but top of the stack
        self.q2.put(x)

        # Push all remaining ele from q1 into q2
        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0]) # Appending into the queue
            self.q1.get()  # Removing from the previous que
        
        # Swap 2 queues
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):

        if (self.q1.empty()):
            return
        
        self.q1.get() # Get Item from stack
        self.curr_size -= 1


# Pop Operation Costly
# push - element is alaways pushed/put into qeue
# pop - one by one deq everything except for last element fro q1 to q2, deque the last item. the dequed item is the result, store it.
# swap names of q1 and q2

