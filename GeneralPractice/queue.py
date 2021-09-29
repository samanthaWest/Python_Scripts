from collections import deque

# Qeue is FIFO
# Items added to the end of the queue and popped from the start - left of queue
Q = deque(['Sam','Liam'])
Q.append('Leffen')
Q.popleft()
print(Q)
Q.append('Lana')

q2 =[]
q2.insert(0, 3)
q2.insert(0, 1)
q2.insert(0, 5)
q2.insert(0, 2)
print("Un-Sorted List")
# print(q2)

# O (N2)
# Selection Sort on List/Queue
indexing_length = range(0, len(q2)-1)
# Sorting a Queue
for i in indexing_length:
    min_val = i

    for j in range(i+1, len(q2)):
        if q2[j] < q2[min_val]:
            min_val = j
        
        if min_val != i:
            q2[min_val], q2[i] = q2[i], q2[min_val]
            break

print('Sorted')
print(q2)

# Quick Sort on List/Queue
q2 =[]
q2.insert(0, 3)
q2.insert(0, 1)
q2.insert(0, 5)
q2.insert(0, 2)
print("Un-Sorted Lis")

# N (Log n) Complexity
def quickSort(seq):
    l = len(seq)

    # Base Case this is sorted
    if l <= 1:
        return seq

    else:
        pivot = seq.pop()

    items_greater = []
    items_smaller = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)
    
    return quickSort(items_smaller) + [pivot] + quickSort(items_greater)

print(quickSort(q2))


# Reversing a Qeueue
# # Use a list to store reversed queue values
# reversed_queue = []

# for item in Q:
#     reversed_queue.insert(0, item)
# print(reversed_queue)

# # Making a queue with a list
# q_list = []

# q_list.insert(0, 1)
# q_list.insert(0, 2)
# q_list.insert(0, 3)

# print(q_list)
# q_list.pop()
# print(q_list)


