# As above example shows, you can concatenate lists in Python using the `+` operator.
# This allows you to combine multiple lists into one.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + [11, 12, 13, 14, 15] + list2

print(list3)

# Adding a new element to a list
list3.append("NEW ELEMENT")
print(list3)

# Add new iterable element
list3.extend(list1)
print(list3)

# List lenght
print(len(list3))

# Count how many particular element exist on list
print(list3.count(1))

# Copy of list and problems with it
print("Problems with list copy")
list4 = [1, 2, 3, 4]
list5 = list4

print(list4)
print(list5)

list4.append(5)

print(list4)
print(list5)

print("Resolution of above problem")
list6 = [1, 2, 3, 4]
list7 = list6[:]

print(list6)
print(list7)

list6.append(5)

print(list6)
print(list7)