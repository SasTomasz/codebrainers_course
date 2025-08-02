# ### Ćwiczenie nr 12:
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# * W tym celu użyj operatora `%` oraz pętli `for`
# * dla liczb `7` i `21` odpowiedz to `7`

def find_greatest_common_divisor(x, y):
    sorted_numbers = [x, y].sort(reverse=True)
    for i in range(x + 1, 0, -1):
        if y % i == 0 and x % i == 0:
            return i 

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
result = find_greatest_common_divisor(number1, number2)
print(f"Największy wspólny dzielnik dla liczb {number1} i {number2} to {result}")
