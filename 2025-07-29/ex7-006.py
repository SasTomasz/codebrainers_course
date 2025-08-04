# ### Ćwicznie nr 7:

# Napisz funkcję w Pythonie, która zlicza ciągi znaków, w których
# * długość ciągu wynosi `2` lub więcej
# * a pierwszy i ostatni znak  danego słowa są takie same.

# Przykładowa lista : `['abc', 'xyz', 'aba', '1221']`

# Oczekiwany wynik: `2`

def find_elements_met_conditions(elements):
    number_of_approved_elements = 0
    for element in elements:
        if len(element) >= 2 and element[0] == element[-1]:
            number_of_approved_elements += 1
    return number_of_approved_elements

example_list = ['abc', 'xyz', 'aba', '1221']
print(find_elements_met_conditions(example_list))