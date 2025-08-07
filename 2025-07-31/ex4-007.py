# ### Ćwiczenie nr 4:

# Spróbuj dodać `int` do ciągu.

# Umieść:

# ```python
# msg = "Nie możesz dodać int do string"
# ```

# aby program uniknął błędu `TypeError`.

# Możesz użyć wyjątku `Exception`, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.

msg = "Nie możesz dodać int do string"
try:
    1 + "1"
except Exception: 
    print(msg)