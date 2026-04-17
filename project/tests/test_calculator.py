import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from calculator import addition, multiplication

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0

def test_addition_negative():
    assert addition(-5, -3) == -8

def test_multiplication_zero():
    assert multiplication(10, 0) == 0