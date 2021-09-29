
knights = {
    1: 'a',
    2: 'b'
}
# Looping through dictionaries
for k, v in knights.items():
    print(k)
    print(v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i)
    print(v)

questions = [ 1,2,3]
answers = ['a','b','c']

for q, a in zip(questions, answers):
    print(q)
    print(a)

# Looping in reverse starting at idx 10 and going by 2 every time
for i in reversed(range(1, 10,2)):
    print(i)

# Looping in descending order up to index 10 every second element
for i in range(1,10,2):
    print(i)

basket = ['ban', 'apple', 'orange']

for i in sorted(basket):
    print(i)

testSet = set(["sam","liam"])

for id, val in enumerate(testSet):
    print(id)
    print(val)