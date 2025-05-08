#Hashsets

s = set()
print(s)

#Add items into Set - O(1)

s.add(1)
s.add(2)
s.add(3)
s.add(4)

#Lookup uf item in set - O(1)

if 1 in s:
    print(True)

# Remove item from set - O(1)

s.remove(4)
print(s)

#Set construction - O(S) - S is the length of the string
string = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddddddeeeeeeeeeeeee"
sett = set(string)

print(sett)

#Loop over items in set
for x in s:
    print(x)


# --------------------------------------------------------------------------------------------


#Hashmaps -  Dictionaries

d = {'greg' : 1 , 'steve' : 2, 'rob' : 3 }
print(d)

#Add key:value in dictionary - O(1)

d['arsh'] = 4
print(d)

#Check for presence of key in dictionary - O(1)

if 'greg' in d:
    print(True)

#Check value corresponding to key in the dictionary - O(1)
if 'greg' in d:
    print(True)
    print(d['greg'])

#Loop over the key:value pairs of the dictionar - O(n)
for key,value in d.items():
    print(f'key {key} : value {value}')

#Default Dictionary

from collections import defaultdict

default = defaultdict(int)
print(default[2]) 
print(default) 

#Counter

from collections import Counter
counter = Counter(string)
print(counter)
