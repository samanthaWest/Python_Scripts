# Dict

tel = {'jack': 456, 'john': 567}
print(tel['jack'])
del tel['jack']
print(tel)

print(list(tel))
tel['jack'] = 5567

if 'jack' in tel:
    print('yes')

if 'sam' not in tel:
    print('yes')

# List comprehension with dict

{x: print(x) for x in tel }

print(tel.keys())
print(tel.values())
print(tel.get('jack'))

for x in tel:
    print(x)

for x in tel.values():
    print(x)

print('items')
for x,y in tel.items():
    print(x)
    print(y)

tel.pop('jack')
tel.popitem()

print(tel)
