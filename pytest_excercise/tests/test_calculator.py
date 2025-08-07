from pytest_excercise.calculator import *

calculator = Calculator()

def test_if_add_3_and_5_return_8():
    expected = 8
    result = calculator.add(3, 5)
    assert result == expected

def test_add_two_positive():
    expected = 10
    result = calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = calculator.add(-6, -4)
    assert result == expected

def test_subtract_two_positive():
    expected = 2
    result = calculator.subtract(6, 4)
    assert result == expected