# Problem : https://algodaily.com/challenges/product-except-self

# If we are given an array of integers, can you return an output array such that each corresponding 
# inputs elemetns return the product of the input array except iteself?

# i.e [ 1, 2, 4, 16]
# if we want to store our product at 0 idx our product will be 2 x 4 x 16 (product of all values except index value)
# The ouput of the array will be 128
import functools
import numpy

def multiplyList(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

# Alternative if cant use func tools
def product_calculation(input_values):
    return numpy.prod(input_values)

def product_self_except(input_values):
    result_list = []
    # Return list of product except self
    for idx, value in enumerate(input_values):
        temp_list = list(input_values)
        temp_list.pop(idx)
        result_list.append(product_calculation(temp_list))
    return result_list

if __name__ == '__main__':
    input_values = [1,2,3,4]
    print(product_self_except(input_values))

# Alt to generate w/o user built in reduce etc
