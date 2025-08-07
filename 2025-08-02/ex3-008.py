# ### Ćwiczenie nr 3:
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# input: plik `008_file_text.txt`

# output: `['przeznaczenia.', 'programowania,']`

def get_the_longest_word(path):
    with open(path, "r", encoding="utf-8") as f:
        content = str(f.read())

    words = content.strip(r"\n")
    print(words)
    words = content.split(" ")
    print(words)
    # TODO Continue from here

get_the_longest_word(r"2025-08-02\story.txt")