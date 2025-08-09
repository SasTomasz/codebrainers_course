# ### Ćwiczenie nr 3:
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# input: plik `008_file_text.txt`

# output: `['przeznaczenia.', 'programowania,']`

def get_the_longest_word(path):
    with open(path, "r", encoding="utf-8") as f:
        content = str(f.read())
        
    words = content.split(" ")
    new_words = []
    longest_word = ""
    for word in words:
        new_word = word.strip("\n")
        new_words.append(new_word)
        if len(longest_word) < len(new_word):
            longest_word = new_word
    print(new_word)
    # TODO Continue from here

get_the_longest_word(r"2025-08-02\story.txt")