# import functools
# import math
# import numpy

# Two Stack Queue
# Stack LIFO
# Queue FIFO

# Implementing Queue using 2 stacks
# 

class TwoStackQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def en(self, e):
        self.s1.append(e)

    def de(self):
        if not self.s2:
            self.s2 = list(reversed(self.s1))
            self.s1 = []
        return self.s2.pop()
    
    def isEmpty(self):
        # Returns True if both stacks are empty, otherwise False
        return True if not self.s2 and not self.s1 else False
    
    def size(self):
        # Returns size of stacks = queue
        return len(self.s1) + len(self.s2)


if __name__ == '__main__':
    print("TWO STACK QUEUE")
    q = TwoStackQueue()
    q.en('a')
    q.en('b')
    
    print(q.isEmpty())
    print(q.size())
    
    print(q.de())
    q.en('c')
    print(q.de())
    print(q.de())