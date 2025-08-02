# ### Ćwiczenie nr 4:

# Napisz funkcję w Pythonie, która znajdzie i zwróci największą liczbę w liście.

def find_bigger_number(numbers: list):
    numbers.sort()
    return numbers[-1]

my_numbers = [1, 4, 7, 3, 2, 7, 9, 12, 53, 745, 8]
print(find_bigger_number(my_numbers))