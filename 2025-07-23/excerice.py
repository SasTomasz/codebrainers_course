# My helper functions
def get_middle_index(data):
    mid_idx = len(data) // 2
    return mid_idx

# Ćwiczenie nr 1 - inna propozycja:
# Mając dany ciąg znaków o nieparzystej długości większej niż 7,
# zwróć nowy łańcuch złożony z trzech środkowych znaków tego ciągu.

# should return "rnm" or something else with custom data
def middle_chars(data="governments"):
    mid_idx = get_middle_index(data)
    print(f"{data[mid_idx - 1:mid_idx + 2]}")

# middle_chars()



# middle_chars()

# Ćwiczenie nr 2:
# Mając dane dwa ciągi znaków s1 i s2, utwórz nowy ciąg znaków,
# w którym s2 zostanie wstawiony dokładnie w środek s1.

def concatenate_strings(str1="Elephant", str2="Super"): 
    mid_idx = get_middle_index(str1)
    new_word = str1[:mid_idx] + str2 + str1[mid_idx:]
    print(new_word)

# concatenate_strings()


# Ćwiczenie nr 3:
# Mając dane dwa łańcuchy znaków s1 i s2 o nieparzystej długości,
# zwróć nowy łańcuch złożony z:
# - pierwszego, środkowego i ostatniego znaku z s1,
# - pierwszego, środkowego i ostatniego znaku z s2.
def get_three_chars(data):
    new_data = data[0] + data[get_middle_index(data)] + data[-1]
    return new_data

def modify_strings(str1="railway", str2="motorbike"):
    new_str1 = get_three_chars(str1)
    new_str2 = get_three_chars(str2)
    new_word = new_str1 + new_str2
    print(new_word)

# modify_strings()

# Ćwiczenie nr 4:
# Odwróć podany ciąg znaków.
def reverse_string(data="Amazing"):
    new_str = data[::-1]
    print(new_str)

reverse_string()

