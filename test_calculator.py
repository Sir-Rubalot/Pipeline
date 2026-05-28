import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 6),
    (5, 5, 10),
    (15, 15, 30),
    (100, 200, 300), 
    (27, 34, 61)
])
def test_add(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(10, 0)
