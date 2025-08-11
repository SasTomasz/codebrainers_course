# ### Ćwiczenie nr 3:
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# input: plik `008_file_text.txt`

# output: `['przeznaczenia.', 'programowania,']`

def get_the_longest_word(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    words = content.split()
    words = [word.strip() for word in words]
    longest_words = {}
    for word in words:
        if len(word) in longest_words.keys():
            longest_words[f"{len(word)}"] = longest_words[f"{len(word)}"].append(word)
        else:
            longest_words[f"{len(word)}"] = [word]
    print(longest_words)
    
    # TODO Continue from here

get_the_longest_word(r"2025-08-02\story.txt")