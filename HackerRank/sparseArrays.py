#!/bin/python3

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries) -> list:
    """ This method counts the occurances of each
        query in the list of strings and returns 
        the result of each match count.
    """
    results = []
    for q in queries:
        results.append(len(list(filter(lambda x: (x == q), strings))))
    return results
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
