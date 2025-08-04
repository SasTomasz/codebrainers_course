# ### Ćwiczenie nr 9:

# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych `2` i ostatnich `2` znaków z danego łańcucha.

# * Jeśli długość ciągu jest mniejsza niż `2`, zwróć zamiast tego pusty ciąg.

# Przykładowy ciąg : `CodeBrainers`

# Oczekiwany wynik: `Cors`

# Przykładowy ciąg : `CB`

# Oczekiwany wynik: `CBCB`

# Przykładowy ciąg : `C`

# Oczekiwany wynik: pusty ciąg

def modify_strings(text):
    if len(text) < 2:
        return ""
    else:
        new_word = text[0:2] + text[-2:]
        return new_word

print(modify_strings("CodeBrainers"))
print(modify_strings("CB"))
print(modify_strings("C"))