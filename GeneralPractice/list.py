listTest = [1,2,3,4]

listTest.append(5) # Add to end of list
listTest.insert(0,-1) # Add at position with value
print(listTest)

listTest.remove(3) # Remove 3 from the list
print(listTest)

listTest.pop() # Remove from end
print(listTest)

listTest.pop(3) # Remove at index 3
print(listTest)

print(listTest.index(-1)) # Get index of a value

listTest2 = [3,1,7,5,4]
listTest2.sort(key=None, reverse=False)
print(listTest2)
listTest2.sort(key=None, reverse=True)
print(listTest2)

newList = listTest2.copy()

# List Comprehension

squares = [ x ** 2 for x in range(10) ]

matrix = [ [1,2], [3,4]]
matrix_new = [ [ row[i]+1 for row in matrix ] for i in range(2) ]
print(matrix_new)
del matrix_new[0]

tupleTest = 123, 43444, 'hello'
print(tupleTest)

for i in range(len(tupleTest)):
    print(tupleTest[i])
    list(tupleTest).pop(0)

# Sets

basket = {'apple','orange',' apple',' pear'}

if 'apple' in basket:
    print("yes")

print(basket)

basket2 = set(['apple','orange',' apple',' pear'])
print(basket2)

a = set('abracadabra')
b = set('alacazm')

print(a-b) # Letters in a but not b
print(a | b) # Letters in a or b or both
print(a & b) # Letters in a and b
print(a ^ b) # Letters in a or b but not both