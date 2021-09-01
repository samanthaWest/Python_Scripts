# https://www.geeksforgeeks.org/interpolation-search/
# Interpolation

# Sorted array of uniformly distributed values, search for specific element in array.
# Can be faster then binary search, where values are sorted and interpolations search may go diff locations according to the key being search
# for example if the value of a key is closer to the last element interpolation search will start toward that side.

# The idea of the formula is to return a higher value of the pos when element is to be search closer to the arr hi and
# smaller value wjen closer to the array lo

# Un9frmyl distruvuted - gap between elemetns is almost all th same

# For interpolation search to work we need a sorted array and a faily uniformed array. The more uniformed the fast the search the less unifimred then binary search will
# provide the same performance
# https://www.youtube.com/watch?v=hF9iJEPegNc&ab_channel=TECHDOSE

# Forumla
# Position (pos) = start + (end - start) / A[end] - A[start] * (e - A[start])
# https://www.youtube.com/watch?v=UDzKXgTuSs0&ab_channel=AkeshSohan
# if a[pos] == e then ele found
# e > A[pos] then inrease start, start = pos + 1
# of e > A[pos] then make end = pos - 1

def interpolationSearch(arr, lo, hi, x):

    # Since array sorted, an element in the array must be in range defined by a corner.
    # Condition 1 . Lowest index is 0, highest index is length of the array - 1  ---- if lo less then or equal to hi
    # Condition 2 . target value is greatter then or equal to first element of the array, target value is less then or equal to highest valye of the array
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        
        # Probing position w/ keeping uniform distrubution in mind
        pos = lo + ( (hi - lo)) // (arr[hi] - arr[lo]) * (x - arr[lo])
        print(pos)

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)
        
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    
    return -2 

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 35
index = interpolationSearch(arr, 0, n - 1, x)