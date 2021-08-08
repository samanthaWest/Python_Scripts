#!/bin/python3

import math
import os
import random
import re
import sys

def isWinner(a,b, total_points) -> list:
    if a != b:
        if a > b:
            total_points[0] =  total_points[0] + 1
        if b > a:
            total_points[1] =  total_points[1] + 1
            
    return total_points    

def compareTriplets(A, B) -> list:
    total_points = [0,0]
    
    for (a,b) in zip(A,B):
        total_points = isWinner(a,b, total_points)
    
    return total_points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
