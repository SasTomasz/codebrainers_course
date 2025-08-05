# Ćwiczenie nr 1
# Napisz program, który poprosi użytkownika o podanie dwóch liczb. 
# * Dodaj wprowadzone liczby i wypisz wynik
# * Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie
# * Dodaj obsługę wyjątku w przypadku błędu konwersji znaku na liczbę

def add_two_numbers(number_1, number_2): 
    return number_1 + number_2

def add_numbers_from_user(): 
    attemp = 5
    while attemp != 0:
        try: 
            fisrt_number = int(input("Podaj pierwszą liczbę: "))
            second_number = int(input("Podaj drugą liczbę: "))
        except ValueError: 
            print("Podawane wartości muszą byc liczbami calkowitymi - spróbuj jeszcze raz")
            attemp -= 1
        else: 
            break

    if attemp != 0:
        print(f"Wynik dodawania podanych liczb to", add_two_numbers(fisrt_number, second_number))
    else: 
        print(f"Zbyt dużo nieudanych prób, spróbuj ponownie za jakiś czas")

if __name__ == "__main__": 
    add_numbers_from_user()
