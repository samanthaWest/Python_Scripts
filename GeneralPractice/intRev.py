# Interview Preperation xD O.O >.< ...

# Searching 

# Binary Search: using a high and low pointer continue to calc a mid point through each loop until reaching the value found or nothing
# Pre-requisit - must be sorted unique list

# 1. (Binary Search to look for number)
def bs_1(nums: [int], target: int):
    low = 0 
    high = len(nums) - 1
    mid = 0
    print(nums)
    while low <= high: 
        # Calc midpoint
        mid = low + (high - low) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif target < mid_val:
            high = mid - 1
        else:
            low = mid + 1

    return -1

#   Test Cases:
sequence_a = [1,2,3,4,5,6,7]
print(bs_1(sequence_a, 7)) # End of list
print(bs_1(sequence_a, 1)) # Start of list
print(bs_1(sequence_a, 4)) # Middle of list
print(bs_1(sequence_a, 9)) # Not in list
print(bs_1([], 7)) # Empty array

# 2. (Binary Search to match a number or and answer as to where that index could be)
def bs_2(nums: [int], target: int):

    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:

        mid = left + (right - left) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            # Search right side of array
            left = mid + 1
            ans = mid + 1
        else:
            right = mid - 1
            ans = mid

    return ans

#   Test Cases:
sequence_b = [1,2,6,8,10,13]
print(bs_2(sequence_b, 5))
print(bs_2(sequence_b, 15))
print(bs_2(sequence_b, 0))
print(bs_2([], 5))

# 3. (Pointer Search Inspired By Binary to match on  multiple numbers i.e finding numbers that add up to a target value)
def bs_3(nums: [int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        currSum = nums[left] + nums[right]

        if currSum == target:
            return [left, right]
        elif currSum > target: # Sum is greater than target value move right ptr to the left
            right -= 1
        else: # Sum is less than the target value, move the left ptr to the right
            left += 1
    
    return -1 # If not found

#   Test Cases:
sequence_c = [1,2,4,5,7,9,13]
print(bs_3(sequence_c, 6))
print(bs_3(sequence_c, 25))
print(bs_3(sequence_c, 14))
print(bs_3([], 25))

# 4. (Binary Search Matrix 1)
def bs_4(matrix: [int], target: int):
    ROWS, COL = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1

    while top <= bot:

        row = ( top + bot ) // 2

        if target > matrix[row][-1]: # Go to next row
            top = row + 1
        elif target < matrix[row][0]: # Go back a row
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False

    row = (top + bot) //2
    l, r = 0, COL -1

    while l <= r:

        mid = (l + r ) // 2
        
        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True

    return False

#   Test Case:
seq_f = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(bs_4(seq_f, 5))
print(bs_4(seq_f, -1))
print(bs_4(seq_f, 70))

# 5 ( Binary Search Matrix 2)
def bs_5(matrix: [int], target: int):
    row = len(matrix)
    col = len(matrix[0])

    top = 0 # Horiz
    bot = row - 1 # Vertical

    while bot >= 0 and top < col:
        if matrix[bot][top] == target:
            return True
        
        if matrix[bot][top] < target: # Elim last row
            top += 1
        else: # target is less then matrix
            bot -= 1

    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(bs_5(matrix, 7))
print(bs_5(matrix, 100))

# 6. (Binary Search Find Peak Element )
def bs_6(nums: [int]):
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

print("FIND PEAK ELE")
seq_d = [1,2,3,1]
seq_e = [2,3,2,2,5,2,2]
print(bs_6(seq_d))
print(bs_6(seq_e))

# Searching Un-Sorted Array ( Requires Checking every element )
# Use front & back technique going from two pointers
# Loop through once and store everything in a hashtable than create a sorted list using that hash table

# Sorting

# Quick Sort: 
def quick_sort(seq):
    length = len(seq)

    if length <= 1:
        return seq

    else:
        pivot = seq.pop()

        items_greater = []
        items_lower = []

        for item in seq:

            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

            
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

#   Test Case:
print(quick_sort([5,6,7,4,3,5,5,6,7,5,4,3]))


# Insertion Sort: 
def insertion_sort(list_a):
    
    index_length = range(1, len(list_a))

    for i in index_length:
        print('FOR LOOP ----')
        value_to_sort = list_a[i]
        print(i)
        print(value_to_sort)
        while list_a[i - 1] > value_to_sort and i > 0:
            print("YES")
            print(list_a[i - 1])
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1
        
            print(list_a)

    return list_a

print(insertion_sort([6,7,4,3]))

# Data Structures