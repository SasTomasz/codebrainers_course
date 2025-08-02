# ### Ćwiczenie nr 3:

# Napisz funkcję w Pythonie, która mnoży wszystkie elementy na liście.

# input: `[1, 2, -8]`

# output: `-16`

def multiply_elements(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

    

print(multiply_elements([1, 2, -8]))
