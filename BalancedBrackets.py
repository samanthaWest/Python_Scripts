# import functools
# import math
# import numpy

# Simple Pairings
# p = ()
# b = []
# c = []

# Check if the symbols pairings follow these conditions: 
# Correctly ordered
# Correct Pairings
# Same kind of pairing

# Do you want to break as soon as they dont follow these conditions?
# Will there be other items in the string besides the symbols


if __name__ == '__main__':
    input = '{{[]}}'
    stack = []
    dict_lst = {
        '{': '}',
        '[': ']',
        '(': ')'
        
    }
    
    for ele in input:
        if ele in list(dict_lst.keys()):
            stack.append(ele)
        else:
            # Check for matching pair (if current el == last el in stack)
            stack_length = len(stack) -1 if len(stack) > 1 else 0
            last_item = stack[stack_length :][0] # Account for this -1 value
            if ele == dict_lst[last_item]:
                stack.pop()
            else:
                print("MISSING CORRESPONDING BRACE")

    print(len(stack))
    print("0 means no issues :)")