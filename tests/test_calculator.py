import pytest
from core.calculator import Calculator

def test_addition():
    c = Calculator()
    assert c.calculate(10, "+", 5) == 15

def test_divide_by_zero():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.calculate(10, "/", 0)