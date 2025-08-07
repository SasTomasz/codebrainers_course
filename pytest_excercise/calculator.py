class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply (self, a, b):
        return a * b
    
if __name__ == "__main__": 
    calculator = Calculator()
    result = calculator.add(a=3, b=5)
    # result = Calculator().add()
    print(result)