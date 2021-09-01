# Takes advantage of collection of elements that is already sorted by ignoring half of the elements 
# after just one comparison.

# https://www.geeksforgeeks.org/binary-search/
# Search a sorted array by repeatadly dividing the search interval in half. Begin with an interval 
# covering the whole array of the value of the search key is less then the item in the middle then narrow search to the lower half
# if its larger narrow search to the upper half. 

# The idea of binary search is to reduce the time comeplxity of an already sorted array

# iterative binary search
def binarySearch_iter(arr, l, r ,x):

    while l <= r:

        mid = l + (r - l) // 2 # Get middle element , calculate with the low + high - low / 2 to avoid out of bounds calcs
        if arr[mid] == x:
            return mid # Found match
        elif arr[mid] < x: # If mid is less then target then we only need to search on right side of the array
            l = mid + 1 
        else: # If mid is less then x then we only need to search on left side of the array
            r = mid - 1

    return - 1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
  
# Function call
result = binarySearch_iter(arr, 0, len(arr)-1, x)
print(result)

# Compare x with middle element
# If x matches middle element we return the mid index
# If x is greater then the mid element then x can only lie on the right side of the array. Then we apply the algorithm again for half
# If x is smaller then the mid element then x can only lie on the lower half, so we apply the algorithm to the left half

# Returns index of x in arr if present else -1
def binary_search(arr, low, high, x):

    # If length of the array is greater then 0
    if high >= low:

        mid = (high + low) // 2
        print("Current Mid")
        print(mid)

        # If index of mid in array is equal to the target we found our item and return the index
        if arr[mid] == x:
            return mid
        
        # IF element is smaller then mid, then it can only be present in the left array
        elif arr[mid] > x:
            return binary_search(arr, low, mid -1, x)
        # Else element can only be present in the right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    
    else:
        return -1

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while high >= low:

        mid = (high + low) // 2

        # If middle point is less then x, then ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If middle point is greater then x, then ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    
    return -1

# Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
 
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)

# result = binary_search_iterative(arr, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


