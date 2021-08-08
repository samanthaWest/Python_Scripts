
import math
import os
import random
import re
import sys


def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    
    for a in arr:
        perc_increase = 1/length
        if a == 0:
            zero += perc_increase
        if a > 0:
            positive += perc_increase
        if abs(a) != a:
            negative += perc_increase
    
    print(positive)
    print(negative)
    print(zero)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
