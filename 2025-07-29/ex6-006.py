# ### Ćwiczenie nr 6:

# Napisz funkcję w Pythonie, która zlicza liczbę znaków (częstotliwość znaków) w ciągu.

# Przykładowy ciąg: `google.com`

# Oczekiwany wynik:

# `{'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}`

letters = {}
def compute_letter_frequency(sentence: str): 
    sentence = sentence.lower()
    for i in sentence:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
    
print(compute_letter_frequency("Information"))