import pytest
from calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 6),
    (5, 5, 20),
    (15, 15, 30),
    (100, 200, 300), 
    (27, 34, 61)
])

def test_add(a, b, expected):
    assert add(a, b) == expected

def test_subtract():
    from calculator import subtract
    assert subtract(10, 5) == 5

def test_multiply():
    from calculator import mutliply
    assert mutliply(4, 5) == 20

def test_divide():
    from calculator import divide
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)