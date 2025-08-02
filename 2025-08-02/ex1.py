# ### Ćwiczenie nr 1:
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście `content_list`.
# `content_list` to lista zawierająca przeczytane wiersze.

def save_text_on_list(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

content_list = save_text_on_list(r"2025-08-02\example1.txt")
print(content_list)