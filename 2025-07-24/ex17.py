# ### Ćwiczenie nr 17:
# Napisz program wyświetlający tylko te liczby z listy, które spełniają następujące warunki

# * Liczba musi być podzielna przez pięć
# * Jeśli liczba jest większa niż 150, pomiń ją i przejdź do następnej liczby
# * Jeśli liczba jest większa niż 500, zatrzymaj pętlę

# **Dane:**

# ```python
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# **Oczekiwany wynik:**

# ```python
# 75
# 150
# 145
# ```
# ##### Wskazówka
# * Użyj pętli `for` do iteracji każdego elementu listy
# * Użyj instrukcji `break`, aby przerwać pętlę, jeśli bieżąca liczba jest większa niż 500
# * Użyj instrukcji `continue`, aby przejść do następnej liczby, jeśli bieżąca liczba jest większa niż 150
# * Użyj warunku `number % 5 == 0`, aby sprawdzić, czy liczba jest podzielna przez 5

numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)
