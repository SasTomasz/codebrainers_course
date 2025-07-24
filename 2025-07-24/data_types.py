# Insert element before particular index
fruits = ["apple", "banana", "orange", "raspberry"]
fruits.insert(2, "blueberry")
print(fruits)

# Modify with equal sign
fruits[0:2] = ["coconut"]
print(fruits)

# list methods
"""
.append(x) - add x to end of list
.remove(x) - remove first x element from list
.pop() - remove last element from list and return it
.extend(x) - Add to end of list iterable x, there will be add as last element/s of list as in example below
.count(x) - return how many element x are on list
.index(x) - index of first occurence of x
.sort() - sort list ascending or descending with parameter reverse=True
.reverse() - reverse list
"""

list2 = [1, 2, 3, 4, 5]
list2.extend([6, 7])
print(list2)

list2.reverse

# Function working on sequence
"""
len() - return length of list
reversed() - return object with reverce sequence
sorted(list) - return copy of list sorted ascending
sorted(list, reverse=True) - return copy of list sorted descending
enumerate() - return indexes and their elements
"""