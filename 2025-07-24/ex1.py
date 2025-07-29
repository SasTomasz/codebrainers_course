def get_two_numbers_from_user():
    number_1 = int(input("Type number one: "))
    number_2 = int(input("Type number two (different than zero): "))

    while number_2 == 0:
        number_2 = int(input("The second number can't be zero. Type new number: "))
    
    print(f"The result of division {number_1} by {number_2} is {number_1 / number_2}")
    print(f"The remainder of division {number_1} by {number_2} is {number_1 % number_2}")
    print(f"The result of integer division {number_1} by {number_2} is {number_1 // number_2}")

if __name__ == "__main__":
    get_two_numbers_from_user()