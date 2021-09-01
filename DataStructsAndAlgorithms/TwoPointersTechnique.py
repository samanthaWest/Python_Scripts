# Two Pointers
# https://www.geeksforgeeks.org/two-pointers-technique/

# Used for searching for pairs in a sorted array
# We take two pointers one representing the first element and the other representing the last element
# we add the values kept at both pointers, if their sum is smaller then target we shift left pointer to the 
# right. If sum is larger then target we shift right pointer to the left till be get closer to the sum.


def isPairSum(arr, lenghtArray, target):

    l = 0 # first pointer
    r = lenghtArray - 1 # second pointer

    while l < r:
        curSum = numbers[l] + numbers[r]
        
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]

