# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import calculator
import random, statistics, math

def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x: int = 14
    y: int = 7
    expected: int = 7

    # Act
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_small():
    # Arrange
    x: int = 8
    y: int = 9
    expected: int = 72

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_zero():
    # Arrange
    x: int = 1000
    y: int = 0
    expected: int = 0

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_small():
    # Arrange
    x: int = 99
    y: int = 11
    expected: int = 9

    # Act
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    # Arrange
    x: int = 99
    y: int = 0

    # Act
    try:
        actual: int = calculator.divide(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.divide(x, y)

    assert str(ex.value) == "Cannot divide by zero!"

def test_calculator_power():
    x:int = 3
    y:int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(x, y)

    # Assert
    assert actual == expected

def test_calculator_sqrt():
    x:int = 25
    expected: int = 5

    actual: int = calculator.sqrt(25)
    assert actual == expected

def test_calculator_sqrt_phase2():
    x: int = -5
    with pytest.raises(ValueError) as ex:
        actual: int = calculator.sqrt(x)

    assert str(ex.value) == "math domain error"

def test_calculator_is_prime():
    x:int = 0
    expected:bool = False
    actual:bool = calculator.is_prime(x)
    assert actual == expected

def test_calculator_factorial():
    x:int = 5
    expected = 120
    actual = calculator.factorial(x)
    assert actual == expected

def test_calculator_factorial_pphase2():
    x:int = -5
    with pytest.raises(ValueError) as ex:
        actual: int = calculator.factorial(x)

    assert str(ex.value) == "factorial not defined for negative values"









