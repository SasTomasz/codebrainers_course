# ### Ćwiczenie nr 2:
# Napisz program w Pythonie, aby odczytać i wyświetlić zawartość pliku w którym
# piszesz kod

def show_text_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())
    
show_text_from_file(r"2025-08-02\ex2-008.py")