#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
                    

def insertNodeAtPosition(llist, data, position):
    # Check if head node is not null
    if llist is not None:
        next_node = llist
        idx = 0
        while next_node is not None:
            # Check for idx before insertion position
            if idx == (position - 1):
                new_node = SinglyLinkedListNode(data)
                new_node.next = next_node.next # New nodes next is now the previous nodes next
                next_node.next = new_node # previous nodes next is now the new node
                break
            else:
                idx += 1
                next_node = next_node.next
            
    return llist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
