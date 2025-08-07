# ### Ćwiczenie nr 5:

# Stwórz trójelementową listę.

# Spróbuj wypisać piąty element.

# Umieść:

# ```python
# "Jesteś poza zakresem listy"
# ```

# aby uniknąć wyjątku `IndexError`.

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Jesteś poza zakresem listy")