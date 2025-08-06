# ### Ćwiczenie nr 2:
# Podziel przez siebie dwie liczby

# Wypisz:

# ```python
# "Nie możesz podzielić przez 0"
# ```

# aby program uniknął `ZeroDivisionError`

def get_data_from_user():
    num1 = int(input("Podaj pierwszą liczbę: "))
    num2 = int(input("Podaj drugą liczbę: "))
    return num1, num2

def divide_two_numbers():
    number1, number2 = get_data_from_user()
    try: 
        result = number1 / number2
        print("Twój wynik to:", result)
    except ZeroDivisionError: 
        print("Nie można dzielić przez zero, spróbuj jeszcze raz. ")
        divide_two_numbers()

if __name__ == "__main__": 
    divide_two_numbers()



