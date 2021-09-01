
# https://www.geeksforgeeks.org/stack-in-python/
# Linear Data Structure Last in First Out
# Uses push and pop
# Funcs associated with stack, empty, size, top, push, pop
# Stack can be implemented by a list or deque

# Two Stacks in An Array
# Ideal Solution is to create stacks from outmost corners of the array
# https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

# Sort Stack Using Temporary Stack
# Loop through input stack and use temp stack as sorted, if another
# number that comes in is higher then top of the stack, loop till find lower and add the higher ones back to input stack
# to be sorted again
# https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

# Sort Array Using Stack
# https://www.geeksforgeeks.org/sorting-array-using-stacks/
# Given an array of elements task is to sort using a stack
# use temporary sort stack, put sorted elements back to the array that dont pass condition

# Circular Queue
# https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
# Last position connectd back to first position to make a circle. Called a 'Ring Buffer'
# In a normal queue we can insert elements until queue becomes full. But once queue becomes full,
# we can not insert the next element even if there is a space in front of the quque.
# front of queue changes depending on what is delete will go to the next number in the queue to be the front
# while the rear position changes will the elements are added

# Application Needs of a Stack
# re-do and un-do features for editors/photoshop
# for ward and backward feature in web browsers
# back tracking (maze or chess programs)
# in memory management
# string reversal

# List Implementation
stack = []
stack.append('a')
stack.pop()

# Implementation Using Deque
from collections import deque
stack = deque()
stack.append('a')
stack.pop()

# Implementation Using Single Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # Adding to the top of the stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

    # Remove value from the top of the list
    def pop(self):
        remove = self.head.next
        self.head.next = self.head.next.next
        return remove.value