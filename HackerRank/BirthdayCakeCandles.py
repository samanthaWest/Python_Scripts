#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # Check for the highest candle
    # Check for occurances of the highest candle
    # return occurance count of highest candle
    max_value = max(candles)
    occurances = candles.count(max_value)
    return occurances
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
