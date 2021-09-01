# Exponential Search
# https://www.geeksforgeeks.org/exponential-search/
# Comes from the way it searches an element
# Find range where element is present, do a binary search on found range
# Find range element is present then do a binary search.

# https://www.youtube.com/watch?v=BDVYtuWXgXE&ab_channel=TECHDOSE
# call exponantial search because your using i to get the boundray and it increeases exponentially 
# useful for un bounded arrays, array of ifinit
# works better then binary search, when the element to be search it closer to the first element then it can be found faster

def binarySearch( arr, l, r, x):
    if r >= l:
        mid = l + ( r-l ) / 2
         
        # If the element is present at
        # the middle itself
        if arr[mid] == x:
            return mid
         
        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if arr[mid] > x:
            return binarySearch(arr, l,
                                mid - 1, x)
         
        # Else he element can only be
        # present in the right
        return binarySearch(arr, mid + 1, r, x)
         
    # We reach here if the element is not present
    return -1
 
# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
    # IF x is present at first
    # location itself
    if arr[0] == x:
        return 0
         
    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    print(i)
    # Call binary search for the found range
    return binarySearch( arr, i / 2,
                         min(i, n-1), x)
     
 
# Driver Code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
# if result == -1:
#     print "Element not found in thye array"
# else:
#     print "Element is present at index %d" %(result)
 
# This code is contributed by Harshit