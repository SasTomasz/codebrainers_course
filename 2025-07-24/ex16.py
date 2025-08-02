# ### Ćwiczenie nr 16:
# Napisz program wypisujący tabliczkę mnożenia podanej liczby

# Przykład `num = 2`, więc wyjście powinno być
# ```python
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# ```

user_number = int(input("Podaj liczbę: "))
for i in range (1, 11):
    print(user_number * i)