# Linear Data Structure following particular order. FIFO
# The difference is in the removing, in a stack we remove the item most recently added
# in a queue we remove the item least recently added

# Sorting a Queue without extra space
# https://www.geeksforgeeks.org/sorting-queue-without-extra-space/
# Use the end of the queue as the min and add the next min to the end of the queue

# Reverse a Queue
# https://www.geeksforgeeks.org/reversing-a-queue/
# Store elements of queue in another data structure then add them back in reverse order

# Applications of a Queue
# breadth first search, first in first out
# resource shared amount multiple consumers
# data is transferred async , data not ness recied at the same time sent btw 2 processes like buffers, pipes, file IO
# Priority Quee

# Things dont have to be processed immediatly but have to be processed in FIFO like Breadth First Search

# Ensque - add item
# Deque - remove item
# Front  [ ] [ ] [ ] < -- front item
# Rear -->  [ ] [ ] [ ] 

# Implement using an array
queue = []
queue.append(1)
queue.pop(0) # pop from the start of the list

# Implement using a collection
from collections import deque

q = deque()
q.append(1)
q.popleft()

# Que.Que
# Build in methods like maxsize, empty, full, get , getnowwait(), put , putnowwait, qsize
from queue import Queue

q = Queue(maxsize = 3)
print(q.qsize())
q.put(1)
q.get()

# Array Implementation 
class Queue:

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    # Adding items to the array (queue)
    def enQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1

    # Removing items at the front of the array (queue)
    def deQueue(self):
        if self.isEmpty():
            print("EMPTY")
            return

        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1

