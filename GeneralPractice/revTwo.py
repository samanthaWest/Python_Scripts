# Sorting

# Insertion Sort
# Set init indexing length
# Loop through list
# Check if value to sort is less than previous and switch
# Continue until all is sorted

# Time Complexity O(n^2)
def insertion_sort(list_a):
    index_length = range(1, len(list_a)) # We start at one because we will always be comparing to the left element

    for i in index_length:
        print("IN FIRST FOR LOOP -------")
        value_to_sort = list_a[i]
        print(value_to_sort)

        while list_a[i - 1] > value_to_sort and i > 0: # While the value to the left is greater than value to sort keep switching the value
            print("WHILE ITEM TO LEFT IS GREAT THAN SORT")
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1

    return list_a

# Test Cases ( Write before contining solving the problem )
print(insertion_sort([1,6,2,8,4]))
print(insertion_sort([]))
print(insertion_sort([2,1]))
print(insertion_sort([1]))

# Quick Sort
# Check base case to see lenght of array
# Assign pivot
# Move items less than and greater then into seperate lists
# Call recursive method returning with lesser and pivot and greater items

# Time Complexity n (Log n)
def quick_sort(seq):
    length = len(seq)

    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

        greater = []
        lesser = []

        for item in seq:

            if item > pivot:
                greater.append(item)
            else:
                lesser.append(item)
    
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

print(quick_sort([5,6,7,4,3,5,5,6,7,5,4,3]))

# Binary Search
# Time Complexity O(log n)

# * If yu want to find a possible position, do this code + keep an answer var
# then that can determin where the spot could have been
def find_number(nums, target):
    low = 0
    high = len(nums) - 1
    mid = 0
    #ans = -1

    while low <= high:

        mid = low + ( high - low) // 2
        mid_v = nums[mid]

        if mid_v == target:
            return mid
        elif target < mid_v:
            high = mid - 1
            # ans = mid
        else:
            low = mid + 1
            #ans = mid +1

    return - 1

def pointer_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:

        sUm = nums[left] + nums[right]

        if sUm == target:
            return [left, right]
        elif sUm > target:
            right -= 1
        else:
            left += 1

    return -1

def peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right- left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left


# Stack

stack = [ 1 , 2, 3]
stack.append(4)
stack.pop()

# Queue

q = [1,2,3,4,5]

q.insert(0, -1)
q.pop()



# pop(3) remove from index 3
# remove(3) remove value 3 from list

# get end of list
print(q[-1:])

d = {
    'sam': 455666,
    'liam': 354535
}

print(d.keys())
print(d.values())
print(d.get('sam'))

for x in d:
    print(x)
    print(d[x])

for x,y in d.items():
    print(x)
    print(y)

list_temp = [ 1,2,3,4,5,6,67,7,4,4,3,]

# for i in range(0,10,1):
#     print(list_temp[i])

for i in range(len(list_temp) -1, -1, -1):
    print(list_temp[i])

print(5 % 3)