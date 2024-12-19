# test_calc.py (使用 pytest)
import pytest
from calc import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_with_negative():
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0
