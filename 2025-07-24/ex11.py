# ### Ćwiczenie nr 11:
# Napisz program w Pythonie, aby znaleźć liczby podzielne przez `7` i będące wielokrotnością `5` między `2000` a `2700` (obie uwzględnione)

# ##### Oczekiwany wynik:

# ```['2030', '2065', '2100', '2135', '2170', '2205', '2240', '2275', '2310', '2345', '2380', '2415', '2450', '2485', '2520', '2555', '2590', '2625', '2660', '2695']```

numbers = list(range(2000, 2701))
approved_numbers = []
for number in numbers:
    if number % 7 == 0 and number % 5 == 0:
        approved_numbers.append(number)

print(approved_numbers)
