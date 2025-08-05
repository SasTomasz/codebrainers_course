# ### Ćwiczenie nr 10: (*)

# Napisz funckję obliczjącą ciąg Fibonacciego w Pythonie za pomocą rekurencji.

def fibonacci(n):
    """
    Example 1: For length 5 fibonacci sequence is [0, 1, 1, 2, 3, 5]
    Example 2: For length 10 fibonacci sequence is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    This function assumes that fibonacci(0) = 0 and fibonacci(1) = 1
    """
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
