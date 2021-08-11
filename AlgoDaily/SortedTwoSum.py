# import functools
# import math
# import numpy

# Sorted Two Sum
# Input Params:
#     Array of Numbers
#     Goal Number

# Problem :
#    Write a method to return an array of indexes of the two elements
#    in the array that sum up the goal. If there are no such elements
#    return an empty array.


# There could be more then one solution to the problem? How do you deal with multiple matches? How should it be stored?

# What if the match is it's own element in the list? Do we need
# another list before checking to see if its included so its not 
# returning its own number i.e target 10 and 5 is first number, will
# it look for itself 5 again and return [0, 0] instead of 
# looking for other numbers?

if __name__ == '__main__':
    
    # Input Params
    target = 10
    sorted_array = [ 1, 3, 7, 9, 11]
    

    result = []
    
    for idx, ele in enumerate(sorted_array):
        number_needed = target - ele
        
        # Check if needed element in rest of array
        if number_needed in sorted_array:
            result = [ idx, sorted_array.index(number_needed) ]
                      
    print(result)