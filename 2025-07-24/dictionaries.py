fruits = ["coconut", "blueberry", "pinapple"]

personal_data = {
    "first_name": "Tomasz",
    "last_name": "Sas", 
    "city": "Kraków",
    "country": "Poland",
    "number_of_cats": 3,
    "favourite_fruits": fruits
}

print(personal_data.keys())

personal_data["number_of_cats"] = 2
print(personal_data.values())