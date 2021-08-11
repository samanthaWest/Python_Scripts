# import functools
# import math
# import numpy

# Challenge
# https://algodaily.com/challenges/add-linked-list-numbers

# Add Linked List Numbers
# Params:
#    Two Linked Lists : each one represents a number in reversed order
# so 1 -> 2 -> 3 -> 4 = 4321

# Lists are guarenteed to have at least one node and will not have any leading 0s. Each of the nodes contain a single digit.

# Problem: 
# Write a method to add the two numbers and return it as another linked list. 

# TODO:
# Create method in LinkedList to loop through nodes and return array of numbers
# Remove duplication in creating nodess

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None
        

if __name__ == '__main__':
    
    print("ADD LINKED LIST NUMBERS")
    
    list1 = LinkedList()
    list1.headval = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)
    
    list1.headval.next = second
    second.next = third
    third.next = four
    
    list2 = LinkedList()
    list2.headval = Node(2)
    second2 = Node(5)
    third2 = Node(8)

    list2.headval.next = second2
    second2.next = third2

    temp1 = list1.headval
    temp2 = list2.headval
    
    result1 = []
    result2 = []
    # Get Numbers from list 1
    while (temp1):
        result1.append(temp1.value)
        temp1 = temp1.next
        
    # Get Numbers from list 2
    while (temp2):
        result2.append(temp2.value)
        temp2 = temp2.next  
        
    
    # Get numbers for product and add to get result 
    result1 = int("".join(map(str,result1[::-1])))
    result2 = int("".join(map(str,result2[::-1])))
    
    print(result1)
    print("+")
    print(result2)
    print("=")
    print(result1 + result2)
    