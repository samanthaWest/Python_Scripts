import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    primary_dig = 0
    secondary_dig = 0
    length = len(arr[0])
    
    for count in range(length):
        primary_dig += arr[count][count]
        secondary_dig += arr[count][length-count - 1]
           
    return abs(primary_dig - secondary_dig)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
