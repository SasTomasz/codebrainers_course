# ### Ćwiczenie nr 7:
# Napisz program, w którym:
# * Utwórz listę zawierającą imiona: prowadzącego oraz wszystkich osób uczestniczacych w kursie
# * Następnie ją posortuj alfabetycznie, oraz
# * Policz ile z osób na liście jest imion żeńskich
#     * W tym celu możesz sprawdzić czy imię kończy się na „`a`”

names = ["Eryka", "Tomasz", "Damian", "Adrian", "Klaudia", "Łukasz", "Angelika", "Krzysztof"]
names.sort()
female_names_number = 0
for name in names:
    if name.endswith("a"):
        female_names_number +=1

print(f"There are {female_names_number} female names on the list.")