def return_false_if_result_is_true(x=1):
    # if result is true function should print false
    result = not(x > 3 and x < 10) 
    print(not result)

if __name__ == "__main__":
    return_false_if_result_is_true()