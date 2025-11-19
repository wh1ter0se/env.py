import pytest
from src.utils import example


def test_example():
    assert example(True) == True
    assert example(False) == False
