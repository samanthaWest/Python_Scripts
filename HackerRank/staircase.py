
import math
import os
import random
import re
import sys


def staircase(n):
    counter = 1 # what level of the staircase we are on
    spaces = n - 1 # Amount of spaces starting from the top
    
    while counter <= n:
        space_list = [' ' for item in range(spaces)]
        counter_list = ['#' for item in range(counter)]
        joined = ''.join(space_list + counter_list)
        print(joined)
        spaces -= 1
        counter += 1
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
