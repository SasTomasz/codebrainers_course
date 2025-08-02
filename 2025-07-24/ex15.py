# ### Ćwiczenie nr 15:
# Napisz program akceptujący liczbę od użytkownika i obliczający sumę wszystkich liczb od 1 do podanej liczby

# Na przykład, jeśli użytkownik wpisał `10`, wynik powinien wynosić `55` (`1+2+3+4+5+6+7+8+9+10`)

# Oczekiwany wynik:

# ```
# Wpisz liczbę: 10

# Suma to: 55
# ```

user_number = int(input("Wpisz dowolną liczbę całkowitą: "))
result = 0
for i in range(1, user_number + 1):
    result += i

print("Wynik to:", result)