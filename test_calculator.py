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

