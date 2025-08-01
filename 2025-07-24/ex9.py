# ### Ćwiczenie nr 9:
# Napisz program, który zamieni 2 listy w jeden słownik:
# * Dwie listy skonwertuj na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością

# ```python
# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
# ```

# ##### Oczekiwany wynik:

# ```python
# {'Dziesieć': 10, 'Dwadzieścia': 20, 'Trzydzieści': 30}
# ```

# ##### Wskazówka:

# Wykonaj iterację listy za pomocą pętli `for` i funkcji `range()`. W każdej iteracji dodaj nową parę klucz-wartość do `dict` za pomocą metody `update()`.

first_names = ["Leonerd", "Helene", "Lorenza", "Garvy", "Agnella", "Jobina", "Whit", "Brit", "Justina", "Harv"]
last_names = ["Roake", "Longstaff", "Troucher", "Rohan", "Eggleston", "Keri", "Boteman", "Rowsell", "Fossey", "Grunnill"]

full_names = {}
for idx in range(10):
    full_names.update({first_names[idx]:last_names[idx]})

print(full_names)