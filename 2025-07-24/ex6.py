def is_condition_met(x=3, y=15):
    if x > 3 or y % 2 == 0:
        print("Co najmniej jeden z warunków jest spełniony")
    else: 
        print("Żaden warunek nie jest spełniony")

if __name__ == "__main__": 
    is_condition_met()