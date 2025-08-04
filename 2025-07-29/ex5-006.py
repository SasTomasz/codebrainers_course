# ### Ćwiczenie nr 5:

# Napisz funkcję w Pythonie, która znajdzie i zwróci najmniejszą liczbę w liście.

def find_smallest_number(numbers: list):
    numbers.sort()
    return numbers[0]

my_numbers = [23, 1, 346, 45, 8, 34, -3, -29, 36, 457]
print("The smallest numer is:", find_smallest_number(my_numbers))