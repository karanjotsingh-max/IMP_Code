#In Python hash table can be built using dictionaries i.e
from collections import defaultdict
hash_map={}
n = int(input("Enter range:"))
for i in range(0,n):
    hash_map[i]=i
if 2 in hash_map:
    print(True)
print(ord("b"))
#if key doesnot exits return a 0 value by default
count = defaultdict(int)
# Looping through hash maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)