z = ['1', '3', '2', '4', 'Alice', 'Bob']
z.sort()
z
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = 'Hello World'
s=spam.strip()
print(s) 
p=spam.lstrip('He')
print(p) 
a=spam.rstrip('rld')
print(a) 

hasil = [
    ', '.join(['cats', 'rats', 'bats']),
    ' '.join(['My', 'name', 'is', 'Simon']),
    'ABC'.join(['My', 'name', 'is', 'Simon']),
    'My name is Simon'.split(),
    'MyABCnameABCisABCSimon'.split('ABC'),
    'My name is Simon'.split('m')
]

for hasil in hasil:
    print(hasil)
    
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))