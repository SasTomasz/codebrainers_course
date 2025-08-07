# ### Ćwiczenie nr 3:
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób po przechwyceniu.

from datetime import date

def count_age():
    year_of_birth = int(input("When You was born (type year): "))
    today = int(date.today().year)
    age = today - year_of_birth
    return age

if __name__ == "__main__":
    try:
        user_age = count_age()
        print(f"You are {user_age} years old.")
    except Exception:
        pass
