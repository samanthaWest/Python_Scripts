# Jump Search
# https://www.geeksforgeeks.org/jump-search/
# Alg for sorted arrays, check fewer elements then linear
# search by jumping ahead by fixed steps or skipping some eements in place of searching all ele
# Binar ysearch is better then jump search but jump searches advantage is being able to traverse back only once, where the
# smallest element of the smaller group. So in a system where binary search is costly we do a jump search.
# https://www.youtube.com/watch?v=63kS6ZkMpkA&ab_channel=GeeksforGeeks
# Jump the amuont of steps until you find something gret then or ewqual to x then do a linear search backwards
# https://www.youtube.com/watch?v=wNOoyZ45SmQ&ab_channel=TECHDOSE

import math

def jumpSearch(arr, x, n):

    # finding size of block to be jumped
    step = math.sqrt(n)

    prev = 0

    # finding block where ele is present
    while arr[int(min(step, n) -1)] < x: # Min number between step and n - 1 value in the array is it greater then the target valyue
        print('-------')
        print(int(min(step, n) -1))
        print(arr[int(min(step, n) -1)])
        print(x)
        prev = step
        step += math.sqrt(n) # go up another 4 steps
        print(step)

        if prev >= n:
            return -1
    
    # Doing a linear search for x in
    # block beginning with prev.
    print(prev)
    while arr[int(prev)] < x:
        prev += 1
         
        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1
     
    # If element is found
    if arr[int(prev)] == x:
        return prev
     
    return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)
 
# Find the index of 'x' using Jump Search
print(jumpSearch(arr, x, n))