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

# Remove item from dictionary
del personal_data["number_of_cats"]
print(personal_data)

# Key without value
personal_data["city"] = None
print(personal_data)

# Check if object is on list
print("apple" in personal_data["favourite_fruits"])
print("coconut" in personal_data["favourite_fruits"])
